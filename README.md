# 📚 eLearning Auto Scroller

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Selenium](https://img.shields.io/badge/selenium-4.15.2-green)](https://www.selenium.dev/)
[![Ethical Use](https://img.shields.io/badge/Use-Ethical%20Only-green)](https://github.com/primoco/elearning-auto-scroller#legal--ethical-disclaimer)
[![Purpose](https://img.shields.io/badge/Purpose-Testing%20%26%20QA-blue)](https://github.com/primoco/elearning-auto-scroller#legitimate-use-cases)

**Automation tool for testing and navigating Moodle-based e-learning platforms.**

An open-source Python framework for automated testing of SCORM content delivery, accessibility support, and quality assurance of e-learning platforms.

---

## 🎯 Legitimate Use Cases

### For Developers & QA Teams
- ✅ **Test SCORM package deployment** on Moodle installations
- ✅ **Automated regression testing** for platform updates
- ✅ **Verify lesson navigation flow** and tracking functionality
- ✅ **Validate course completion** mechanisms
- ✅ **Cross-platform compatibility testing** (different browsers/devices)

### For Students (Ethical Use Only)
- ✅ **Review content** from courses already completed or certified
- ✅ **Navigate courses** for which you already have demonstrated competency
- ✅ **Accessibility tool** for students with motor disabilities
- ✅ **Preview course structure** before formal enrollment decisions
- ✅ **Refresh knowledge** from previously mastered material

### For Educational Institutions
- ✅ **Quality assurance testing** of course materials
- ✅ **Verify platform compliance** and SCORM standards
- ✅ **Test user experience flow** and identify UX issues
- ✅ **Benchmark course completion times** and engagement metrics
- ✅ **Accessibility audits** for inclusive learning

### ⚠️ NOT Intended For
- ❌ Cheating or academic dishonesty
- ❌ Circumventing mandatory learning requirements
- ❌ Violating university Terms of Service
- ❌ Fraudulent certificate acquisition
- ❌ Completing courses without acquiring knowledge

---

## ✨ Features

### Core Functionality
- 🚀 **Automated Navigation**: Systematically navigates through SCORM/iSpring presentations
- 🎯 **Smart Detection**: Automatically identifies and processes course lessons
- ⏯️ **Resume Support**: Continue from any specific lesson if interrupted
- 🔄 **Multi-Course**: Easily switch between different courses
- 📊 **Progress Tracking**: Real-time display of navigation progress

### Platform Support
- 🌐 **Moodle Compatible**: Works with standard Moodle installations
- 🎓 **Multi-Institution**: Tested on various university platforms
- 🌍 **Multi-Language**: Supports multiple lesson naming conventions
- ⚙️ **Configurable**: JSON-based configuration for different platforms

### Deployment Options
- 🐍 **Native Python**: Run directly with Python 3.8+
- 🐳 **Docker Support**: Containerized deployment for consistency
- 🔧 **Easy Configuration**: Simple JSON configuration file

---

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Supported Platforms](#supported-platforms)
- [For Educational Institutions](#for-educational-institutions)
- [Legal & Ethical Disclaimer](#legal--ethical-disclaimer)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Installation

### Method 1: Python (Native)

**Requirements:**
- Python 3.8+
- Chrome or Chromium browser

**Steps:**

1. **Clone the repository:**
```bash
git clone https://github.com/primoco/elearning-auto-scroller.git
cd elearning-auto-scroller
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure:**
```bash
cp config.example.json config.json
nano config.json
```

Edit `config.json` with your settings:
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

4. **Run:**
```bash
python3 src/moodle_auto.py
```

---

### Method 2: Docker

**Requirements:**
- Docker
- Docker Compose

**Steps:**

1. **Clone the repository:**
```bash
git clone https://github.com/primoco/elearning-auto-scroller.git
cd elearning-auto-scroller
```

2. **Configure docker-compose.yml:**
```yaml
environment:
  - MOODLE_URL=https://elearning.youruniversity.it
  - MOODLE_USERNAME=your_username
  - MOODLE_PASSWORD=your_password
  - COURSE_ID=395
```

3. **Build and run:**
```bash
docker-compose -f docker/docker-compose.yml up --build
```

---

## 📖 Usage

### Basic Usage

**For Testing/QA:**
```bash
python3 src/moodle_auto.py
```

The tool will:
1. Connect to the specified Moodle platform
2. Navigate to the course
3. Systematically process each SCORM lesson
4. Display real-time progress

**Example output:**
```
============================================================
🔐 LOGIN
============================================================
✓ Login effettuato con successo!

============================================================
📚 ANALISI CORSO
============================================================
✓ Trovate 96 lezioni SCORM da completare

============================================================
⚙️ INIZIO NAVIGAZIONE AUTOMATICA
============================================================

[1/96] Lezione 01 Pacchetto SCORM
  📖 Slide 11/11... 
  ✓ Completata! (11/11 slide)
...
```

### Resume from Specific Lesson

For continued testing sessions:

**Option 1: Configure in JSON**
```json
{
  "start_from_lesson": 42
}
```

**Option 2: Interactive prompt**
```
> Vuoi partire dall'inizio o da una lezione specifica? (i=inizio / numero lezione): 42
✓ Partirò dalla lezione 42
```

### Multiple Test Configurations

Create separate config files for different test scenarios:
```bash
python3 src/moodle_auto.py --config test_config_1.json
python3 src/moodle_auto.py --config test_config_2.json
```

---

## ⚙️ Configuration

### Standard Moodle Configuration

```json
{
  "platform_type": "moodle",
  "moodle_url": "https://elearning.university.it",
  "course_id": "395",
  "username": "test_account",
  "password": "test_password",
  "start_from_lesson": 0,
  "lesson_keyword": "lezione",
  "slide_delay": 0.25,
  "lesson_delay": 2
}
```

### Configuration Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `platform_type` | Platform type (`moodle` or `custom`) | `moodle` |
| `moodle_url` | Base URL of Moodle instance | Required |
| `course_id` | Course identifier | Required |
| `username` | Account username | Required |
| `password` | Account password | Required |
| `start_from_lesson` | Lesson number to start from (0 = beginning) | `0` |
| `lesson_keyword` | Keyword to identify lessons | `lezione` |
| `slide_delay` | Delay between slides (seconds) | `0.25` |
| `lesson_delay` | Delay between lessons (seconds) | `2` |

---

## 🌍 Supported Platforms

This tool has been tested with:

✅ **Standard Moodle Installations**
- Various Italian universities
- International Moodle instances
- Self-hosted Moodle servers

✅ **SCORM Content Types**
- iSpring presentations
- Articulate Storyline
- Adobe Captivate
- Generic SCORM 1.2 and 2004

⚠️ **May require configuration:**
- Custom Moodle themes
- Non-standard authentication
- Heavily customized platforms

---

## 🏫 For Educational Institutions

### Quality Assurance Partnership

We encourage institutional use for:
- **Platform Testing**: Validate SCORM delivery
- **Accessibility Audits**: Ensure inclusive design
- **UX Research**: Identify navigation issues
- **Performance Benchmarking**: Measure system efficiency

### Collaboration Opportunities

We welcome partnerships with universities to:
- Improve e-learning platform quality
- Develop accessibility features
- Create testing standards
- Share best practices

**For institutional inquiries:** Open an issue with the tag `institutional-use`

### Preventing Misuse

We actively cooperate with institutions to prevent abuse:
- Report suspected misuse via GitHub issues
- We can add institution-specific safeguards
- Open to implementing usage verification systems
- Committed to ethical educational technology

---

## ⚠️ Legal & Ethical Disclaimer

**IMPORTANT - READ CAREFULLY BEFORE USE**

This tool is designed exclusively for:
- ✅ Platform testing and quality assurance
- ✅ Accessibility support for users with disabilities
- ✅ Reviewing content from already-completed or certified courses
- ✅ Educational technology development and research

### You MUST:
- ✅ Only use on **your own account**
- ✅ Have **legitimate educational, testing, or accessibility purposes**
- ✅ **Comply** with your institution's acceptable use policies
- ✅ **Already possess** the knowledge/certifications for content being reviewed
- ✅ Use for accessibility needs when applicable
- ✅ Respect intellectual property and content rights

### You MUST NOT:
- ❌ Use to **cheat** or violate academic integrity policies
- ❌ Obtain certificates **without acquiring the required knowledge**
- ❌ **Circumvent legitimate learning** requirements
- ❌ **Violate platform** Terms of Service
- ❌ Use for **fraudulent purposes**
- ❌ **Harm your educational institution's** reputation or systems

### Acknowledgment

**By using this tool, you acknowledge that:**

1. You are **solely responsible** for your use of this software
2. You will **not use it for academic dishonesty** or policy violations
3. You **understand the potential consequences** of misuse (including but not limited to: academic penalties, expulsion, legal action)
4. The **authors and contributors are not liable** for any misuse
5. This tool is provided **"as is" without warranty** of any kind

### For Institutions

If you believe this tool is being misused at your institution, please:
- Open a GitHub issue with details
- We will cooperate fully with legitimate concerns
- We can implement institution-specific safeguards
- We are committed to preventing abuse

---

## ❓ FAQ

### General Questions

**Q: What is this tool for?**  
A: It's primarily a testing and QA tool for Moodle platforms, also useful for accessibility needs and reviewing previously mastered content.

**Q: Can I use this to complete courses I haven't studied?**  
A: **No.** This violates academic integrity policies and the tool's intended purpose. Use only for testing, accessibility, or reviewing content you've already mastered.

**Q: Is this legal?**  
A: When used for legitimate purposes (testing, QA, accessibility, review), yes. When used for cheating or policy violations, no.

**Q: Will I get in trouble for using this?**  
A: If used ethically and within policy guidelines, no. If used for academic dishonesty, you risk serious consequences including expulsion.

### Technical Questions

**Q: Which platforms does it support?**  
A: Standard Moodle installations with SCORM content. Custom platforms may require configuration.

**Q: Do I need programming knowledge?**  
A: Basic familiarity with command line is helpful but not required. Follow the installation guide step-by-step.

**Q: Can I contribute to the project?**  
A: Absolutely! See the [Contributing](#contributing) section.

**Q: Does it work headless/in background?**  
A: Currently requires visible browser. Headless mode is a planned feature.

### Ethical Questions

**Q: Why make this public if it can be misused?**  
A: Legitimate use cases (QA testing, accessibility, development) exist and are valuable. Responsible users shouldn't be restricted because of potential misuse. We actively discourage and prevent abuse.

**Q: Do you condone cheating?**  
A: **Absolutely not.** We strongly oppose academic dishonesty and cooperate with institutions to prevent misuse.

**Q: How do you prevent misuse?**  
A: Through clear documentation, ethical guidelines, cooperation with institutions, and community reporting mechanisms.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**: Open detailed issue reports
2. **Suggest Features**: Share ideas for legitimate improvements
3. **Add Platform Support**: Help support more e-learning platforms
4. **Improve Documentation**: Fix typos, add examples, translate
5. **Code Contributions**: Submit pull requests

### Contribution Guidelines

**We welcome contributions that:**
- ✅ Improve testing and QA capabilities
- ✅ Enhance accessibility features
- ✅ Add legitimate platform support
- ✅ Improve documentation
- ✅ Add safeguards against misuse

**We do not accept contributions that:**
- ❌ Facilitate academic dishonesty
- ❌ Bypass legitimate security measures
- ❌ Violate platform Terms of Service
- ❌ Remove ethical safeguards

### How to Contribute Code

```bash
# Fork the repository
git clone https://github.com/primoco/elearning-auto-scroller.git
cd elearning-auto-scroller

# Create a feature branch
git checkout -b feature/my-contribution

# Make your changes and commit
git commit -am "Add: description of contribution"

# Push and create Pull Request
git push origin feature/my-contribution
```

---

## 📝 License

This project is licensed under the **MIT License** with additional ethical use requirements - see the [LICENSE](LICENSE) file for details.

### Summary

- ✅ Free to use for legitimate purposes
- ✅ Open source and modifiable
- ✅ Commercial use allowed for ethical applications
- ⚠️ Subject to ethical use requirements outlined in this README
- ⚠️ No warranty provided

---

## 🙏 Acknowledgments

- Built with [Selenium WebDriver](https://www.selenium.dev/)
- Inspired by the need for better e-learning platform testing tools
- Thanks to all ethical contributors and testers
- Special thanks to the open-source community

---

## 📧 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/primoco/elearning-auto-scroller/issues)
- **Discussions**: [GitHub Discussions](https://github.com/primoco/elearning-auto-scroller/discussions)
- **Institutional Inquiries**: Open issue with tag `institutional-use`
- **Security Concerns**: See [SECURITY.md](SECURITY.md) (if applicable)

---

## 📊 Project Status

![GitHub stars](https://img.shields.io/github/stars/primoco/elearning-auto-scroller?style=social)
![GitHub forks](https://img.shields.io/github/forks/primoco/elearning-auto-scroller?style=social)
![GitHub issues](https://img.shields.io/github/issues/primoco/elearning-auto-scroller)
![GitHub pull requests](https://img.shields.io/github/issues-pr/primoco/elearning-auto-scroller)

---

**⭐ If you find this tool useful for testing or accessibility, consider giving it a star on GitHub!**

**🤝 Committed to ethical educational technology development.**
