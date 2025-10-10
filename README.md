# 📚 eLearning Auto Scroller

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Selenium](https://img.shields.io/badge/selenium-4.15.2-green)](https://www.selenium.dev/)

**Automatically complete eLearning SCORM lessons on Moodle-based platforms.**

A Python automation tool that navigates through eLearning courses and automatically scrolls through iSpring/SCORM presentations, saving you hours of manual clicking.

---

## ✨ Features

- 🚀 **Fast Completion**: Automatically clicks through all slides in SCORM lessons
- 🎯 **Smart Detection**: Automatically finds and processes all lessons in a course
- ⏯️ **Resume Support**: Start from any lesson number if interrupted
- 🔄 **Multi-Course**: Easily switch between different courses
- 🐳 **Docker Support**: Run anywhere with Docker (no local setup needed)
- 🌍 **Moodle Compatible**: Works with most Moodle-based platforms
- ⚙️ **Customizable**: Support for non-standard platforms via config

---

## 📋 Table of Contents

- [Installation](#installation)
  - [Quick Start (Python)](#quick-start-python)
  - [Docker Installation](#docker-installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Resume from Specific Lesson](#resume-from-specific-lesson)
  - [Multiple Courses](#multiple-courses)
- [Configuration](#configuration)
- [Supported Platforms](#supported-platforms)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Installation

### Quick Start (Python)

**Requirements:**
- Python 3.8+
- Chrome or Chromium browser

**1. Clone the repository:**
```bash
git clone https://github.com/primoco/elearning-auto-scroller.git
cd elearning-auto-scroller
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Configure your credentials:**
```bash
cp config.example.json config.json
nano config.json
```

Edit `config.json`:
```json
{
  "platform_type": "moodle",
  "moodle_url": "https://elearning.youruniversity.it",
  "course_id": "395",
  "username": "your_username",
  "password": "your_password",
  "start_from_lesson": 0
}
```

**4. Run:**
```bash
python3 src/moodle_auto.py
```

---

### Docker Installation

**1. Clone the repository:**
```bash
git clone https://github.com/primoco/elearning-auto-scroller.git
cd elearning-auto-scroller
```

**2. Edit docker-compose.yml with your credentials:**
```yaml
environment:
  - MOODLE_USERNAME=your_username
  - MOODLE_PASSWORD=your_password
  - COURSE_ID=395
```

**3. Build and run:**
```bash
docker-compose up --build
```

---

## 📖 Usage

### Basic Usage

Run the script to complete all lessons in a course:

```bash
python3 src/moodle_auto.py
```

The script will:
1. Login to your eLearning platform
2. Navigate to the specified course
3. Find all SCORM lessons
4. Complete each lesson by clicking through all slides
5. Show progress in real-time

**Example output:**
```
============================================================
LOGIN SU MOODLE
============================================================
✓ Login effettuato con successo!

============================================================
ANALISI CORSO
============================================================
✓ Trovate 96 lezioni SCORM da completare

============================================================
INIZIO COMPLETAMENTO AUTOMATICO
============================================================

[1/96] Lezione 01 Pacchetto SCORM
  📖 Slide 11/11... 
  ✓ Completata! (11/11 slide)

[2/96] Lezione 02 Pacchetto SCORM
  📖 Slide 8/8... 
  ✓ Completata! (8/8 slide)
...
```

### Resume from Specific Lesson

If interrupted, you can resume from a specific lesson:

**Option 1: Edit config.json**
```json
{
  "start_from_lesson": 42
}
```

**Option 2: Interactive prompt**
```bash
python3 src/moodle_auto.py
> Vuoi partire dall'inizio o da una lezione specifica? (i=inizio / numero lezione): 42
✓ Partirò dalla lezione 42
```

### Multiple Courses

To switch between courses, just change the `course_id`:

```json
{
  "course_id": "420"
}
```

Or create multiple config files:
```bash
python3 src/moodle_auto.py --config corso_diritto.json
python3 src/moodle_auto.py --config corso_economia.json
```

---

## ⚙️ Configuration

### Standard Moodle Configuration

Most Moodle platforms work with minimal configuration:

```json
{
  "platform_type": "moodle",
  "moodle_url": "https://elearning.university.it",
  "course_id": "395",
  "username": "student123",
  "password": "your_password",
  "start_from_lesson": 0,
  "lesson_keyword": "lezione"
}
```

### Custom Platform Configuration

For non-standard platforms:

```json
{
  "platform_type": "custom",
  "login_url": "https://custom.platform/auth/login",
  "course_url_template": "https://custom.platform/course/{course_id}",
  "username_field": "user",
  "password_field": "pass",
  "login_button_id": "submit",
  "lesson_link_selector": "a.lesson-link",
  "enter_button_text": "Start",
  "next_button_selector": ".next-slide"
}
```

---

## 🌍 Supported Platforms

This tool has been tested and works with:

✅ **Standard Moodle Installations:**
- Columbus Academy
- eCampus
- Unicusano
- IUL (Italian University Line)
- Most university Moodle instances

✅ **SCORM Players:**
- iSpring
- Articulate Storyline
- Adobe Captivate

⚠️ **May require custom configuration:**
- Blackboard
- Canvas LMS
- Custom university platforms

---

## ⚠️ Disclaimer

**IMPORTANT - READ CAREFULLY:**

This tool is provided for **educational and research purposes only**.

- ✅ Use only on your **own account**
- ✅ Use only for **legitimate educational purposes**
- ✅ Respect your institution's **Terms of Service**
- ✅ Check if automation is **allowed** by your university
- ❌ Do NOT use to violate academic integrity policies
- ❌ Do NOT use for cheating or fraud
- ❌ Do NOT share accounts or credentials

**The authors are not responsible for:**
- Violations of university policies
- Academic consequences
- Account suspensions or bans
- Any misuse of this tool

**Use at your own risk.** This tool simulates human interaction with the platform. Some institutions may consider automated course completion a violation of their policies.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue describing the problem
2. **Suggest Features**: Share your ideas for improvements
3. **Add Platform Support**: Help add configurations for new platforms
4. **Improve Documentation**: Fix typos, add examples, translate

**To contribute code:**

```bash
# Fork the repo
git clone https://github.com/primoco/elearning-auto-scroller.git
cd elearning-auto-scroller

# Create a branch
git checkout -b feature/my-feature

# Make changes and commit
git commit -am "Add amazing feature"

# Push and create PR
git push origin feature/my-feature
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Selenium](https://www.selenium.dev/)
- Inspired by the need to save time on repetitive eLearning tasks
- Thanks to all contributors

---

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/primoco/elearning-auto-scroller/issues)
- **Discussions**: [GitHub Discussions](https://github.com/primoco/elearning-auto-scroller/discussions)

---

**⭐ If this tool saved you time, consider giving it a star on GitHub!**
