#!/usr/bin/env python3
"""
eLearning Auto Scroller
Automatically complete SCORM lessons on Moodle-based platforms
GitHub: https://github.com/primoco/elearning-auto-scroller
License: MIT
"""

import json
import os
import sys
import time
import argparse
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Config:
    """Configuration manager"""
    
    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration from JSON file or environment variables"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        
        # Fallback to environment variables (for Docker)
        return {
            "platform_type": os.getenv("PLATFORM_TYPE", "moodle"),
            "moodle_url": os.getenv("MOODLE_URL", ""),
            "course_id": os.getenv("COURSE_ID", ""),
            "username": os.getenv("MOODLE_USERNAME", ""),
            "password": os.getenv("MOODLE_PASSWORD", ""),
            "start_from_lesson": int(os.getenv("START_FROM_LESSON", "0")),
            "lesson_keyword": os.getenv("LESSON_KEYWORD", "lezione"),
            "slide_delay": float(os.getenv("SLIDE_DELAY", "0.25")),
            "lesson_delay": int(os.getenv("LESSON_DELAY", "2"))
        }
    
    def get(self, key, default=None):
        return self.config.get(key, default)


class MoodleAutomation:
    """Main automation class for Moodle platforms"""
    
    def __init__(self, config):
        self.config = config
        self.driver = None
    
    def setup_browser(self):
        """Initialize Chrome browser"""
        print("🚀 Avvio browser Chrome...")
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(service=service, options=options)
        return self.driver
    
    def login(self, username, password):
        """Login to Moodle platform"""
        print(f"\n{'='*60}")
        print(f"🔐 LOGIN")
        print(f"{'='*60}")
        
        moodle_url = self.config.get('moodle_url')
        login_url = f"{moodle_url}/login/index.php"
        
        self.driver.get(login_url)
        
        try:
            wait = WebDriverWait(self.driver, 10)
            
            username_field = wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.send_keys(username)
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(password)
            
            login_button = self.driver.find_element(By.ID, "loginbtn")
            login_button.click()
            
            time.sleep(3)
            print("✓ Login effettuato con successo!")
            return True
            
        except Exception as e:
            print(f"✗ Errore durante il login: {e}")
            return False
    
    def get_scorm_lessons(self, course_id):
        """Get all SCORM lessons from course"""
        print(f"\n{'='*60}")
        print(f"📚 ANALISI CORSO")
        print(f"{'='*60}")
        
        moodle_url = self.config.get('moodle_url')
        course_url = f"{moodle_url}/course/view.php?id={course_id}"
        
        self.driver.get(course_url)
        time.sleep(3)
        
        scorm_links = []
        links = self.driver.find_elements(By.CSS_SELECTOR, "a.aalink")
        
        lesson_keyword = self.config.get('lesson_keyword', 'lezione').lower()
        
        for link in links:
            href = link.get_attribute('href')
            text = link.text.strip()
            
            if 'mod/scorm/view.php' in href and lesson_keyword in text.lower():
                scorm_links.append({
                    'title': text,
                    'url': href
                })
        
        print(f"✓ Trovate {len(scorm_links)} lezioni SCORM da completare\n")
        return scorm_links
    
    def click_enter_button(self):
        """Click 'Entra' button on SCORM intermediate page"""
        try:
            wait = WebDriverWait(self.driver, 10)
            enter_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][value='Entra']"))
            )
            enter_button.click()
            time.sleep(4)
            return True
        except:
            # Try alternative button texts
            try:
                enter_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Enter']")
                enter_button.click()
                time.sleep(4)
                return True
            except:
                return True  # Maybe no intermediate page
    
    def complete_lesson(self, lesson_title):
        """Complete a single iSpring SCORM lesson"""
        print(f"  📖 Completamento in corso...", end='', flush=True)
        
        try:
            wait = WebDriverWait(self.driver, 15)
            
            # Find iframe
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
            
            if len(iframes) == 0:
                print("\n  ✗ Nessun iframe trovato!")
                return False
            
            # Enter iframe
            self.driver.switch_to.frame(iframes[-1])
            
            # Find Next button and slide counter
            try:
                next_button = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".next.button"))
                )
                slides_label = self.driver.find_element(By.CSS_SELECTOR, ".slides_label")
            except:
                print("\n  ⚠ Player non trovato, lezione già completata?")
                self.driver.switch_to.default_content()
                return True
            
            # Click Next until end
            max_clicks = 300
            clicks = 0
            last_slide = None
            slide_delay = self.config.get('slide_delay', 0.25)
            
            while clicks < max_clicks:
                try:
                    current_slide_text = slides_label.text
                    
                    if current_slide_text == last_slide:
                        time.sleep(0.5)
                        if slides_label.text == last_slide:
                            break
                    
                    last_slide = current_slide_text
                    
                    if "/" in current_slide_text:
                        parts = current_slide_text.split("/")
                        current = int(parts[0].strip())
                        total = int(parts[1].strip())
                        
                        print(f"\r  📖 Slide {current}/{total}... ", end='', flush=True)
                        
                        if current >= total:
                            print(f"\r  ✓ Completata! ({total}/{total} slide)          ")
                            break
                    
                    if 'disabled' in next_button.get_attribute('class'):
                        print(f"\r  ✓ Completata!                          ")
                        break
                    
                    next_button.click()
                    time.sleep(slide_delay)
                    
                    clicks += 1
                    
                    slides_label = self.driver.find_element(By.CSS_SELECTOR, ".slides_label")
                    next_button = self.driver.find_element(By.CSS_SELECTOR, ".next.button")
                    
                except Exception:
                    print(f"\r  ✓ Completata!                          ")
                    break
            
            self.driver.switch_to.default_content()
            time.sleep(2)
            return True
            
        except Exception as e:
            print(f"\n  ✗ Errore: {e}")
            self.driver.switch_to.default_content()
            return False
    
    def run(self):
        """Main execution flow"""
        print("\n" + "="*60)
        print(" 📚 eLEARNING AUTO SCROLLER")
        print("="*60)
        
        # Get credentials
        username = self.config.get('username')
        password = self.config.get('password')
        course_id = self.config.get('course_id')
        start_from = self.config.get('start_from_lesson', 0)
        
        if not all([username, password, course_id]):
            print("\n✗ Errore: configurazione incompleta!")
            print("Compila config.json con username, password e course_id")
            return
        
        # Interactive start_from prompt if not configured
        if start_from == 0:
            risposta = input("\nVuoi partire dall'inizio o da una lezione specifica? (i=inizio / numero lezione): ")
            if risposta.lower() != 'i':
                try:
                    start_from = int(risposta)
                    print(f"✓ Partirò dalla lezione {start_from}")
                except:
                    print("✓ Partirò dall'inizio")
                    start_from = 0
        
        # Confirm before starting
        print(f"\nCorso ID: {course_id}")
        print(f"URL: {self.config.get('moodle_url')}/course/view.php?id={course_id}")
        
        risposta = input("\nVuoi procedere? (s/n): ")
        if risposta.lower() != 's':
            print("Operazione annullata.")
            return
        
        # Setup browser
        self.setup_browser()
        
        try:
            # Login
            if not self.login(username, password):
                print("Login fallito!")
                return
            
            # Get lessons
            lessons = self.get_scorm_lessons(course_id)
            
            if len(lessons) == 0:
                print("Nessuna lezione trovata!")
                return
            
            # Filter lessons based on start_from
            if start_from > 0:
                if start_from > len(lessons):
                    print(f"Errore: il corso ha solo {len(lessons)} lezioni!")
                    return
                lessons = lessons[start_from - 1:]
                print(f"\n✓ Saltate le prime {start_from - 1} lezioni")
            
            # Process lessons
            print(f"{'='*60}")
            print(f"⚙️  INIZIO COMPLETAMENTO AUTOMATICO")
            print(f"{'='*60}\n")
            
            completed = 0
            failed = 0
            lesson_delay = self.config.get('lesson_delay', 2)
            
            for i, lesson in enumerate(lessons, start_from if start_from > 0 else 1):
                total = start_from + len(lessons) - 1 if start_from > 0 else len(lessons)
                print(f"\n[{i}/{total}] {lesson['title']}")
                
                self.driver.get(lesson['url'])
                time.sleep(2)
                
                if not self.click_enter_button():
                    print("  ✗ Impossibile entrare nella lezione")
                    failed += 1
                    continue
                
                if self.complete_lesson(lesson['title']):
                    completed += 1
                else:
                    failed += 1
                
                time.sleep(lesson_delay)
            
            # Summary
            print(f"\n{'='*60}")
            print(f"✅ COMPLETAMENTO TERMINATO")
            print(f"{'='*60}")
            print(f"✓ Lezioni completate: {completed}/{len(lessons)}")
            if failed > 0:
                print(f"✗ Lezioni fallite: {failed}")
            print(f"\nControlla il corso su Moodle per verificare.")
            
            input("\nPremi INVIO per chiudere...")
            
        except KeyboardInterrupt:
            print("\n\n⚠ Interruzione manuale!")
            print(f"Lezioni completate: {completed}")
            input("\nPremi INVIO per chiudere...")
        
        except Exception as e:
            print(f"\n✗ Errore critico: {e}")
            input("\nPremi INVIO per chiudere...")
        
        finally:
            if self.driver:
                self.driver.quit()
            print("\n👋 Browser chiuso. Script terminato.")


def main():
    """Entry point"""
    parser = argparse.ArgumentParser(description='eLearning Auto Scroller')
    parser.add_argument('--config', default='config.json', help='Path to config file')
    args = parser.parse_args()
    
    # Load config
    config = Config(args.config)
    
    # Run automation
    automation = MoodleAutomation(config)
    automation.run()


if __name__ == "__main__":
    main()
