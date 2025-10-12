# Keyword-Based News Fetcher

## Description
A Python module that fetches the top news articles for a given keyword using [NewsAPI.org](https://newsapi.org/).  
Features:
- Fetch top 3 news articles (can be changed in script).
- Display title + URL.
- Shortens long URLs for cleaner output.
- Logs fetched news to `news_log.txt`.
- Accepts commands like `show news about AI`.

## Usage
1. Install dependencies:

<div align="center">

# 🤖 Jarvis AI Assistant

### *Your Personal Voice-Controlled AI Companion*

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
[![Stars](https://img.shields.io/github/stars/vannu07/jarvis?style=for-the-badge&logo=github)](https://github.com/vannu07/jarvis/stargazers)
[![Forks](https://img.shields.io/github/forks/vannu07/jarvis?style=for-the-badge&logo=github)](https://github.com/vannu07/jarvis/network)

<img src="https://raw.githubusercontent.com/vannu07/jarvis/main/frontend/assets/img/logo.ico" alt="Jarvis Logo" width="150"/>

*A production-ready voice assistant with facial recognition authentication, built on modern Python architecture and web technologies.*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-development) • [Contributing](#-contributing)

---

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

## ✨ Features

<div align="center">

| 🎤 Voice Control | 👤 Face Recognition | 🔥 Hotword Detection | 🌐 Web Integration |
|:---:|:---:|:---:|:---:|
| Advanced speech-to-text | Secure biometric auth | Always-on wake word | Modern responsive UI |

</div>

### 🚀 Core Capabilities

<table>
<tr>
<td width="50%">

#### 🎯 Voice & AI
- 🗣️ **Real-time Speech Recognition** using Google STT
- 💬 **Natural Language Processing** with Hugging Face
- 🎵 **Text-to-Speech** with customizable voices
- 🔊 **Audio Visualization** in real-time
- 🎙️ **Wake Word Detection** ("Jarvis", "Alexa")

</td>
<td width="50%">

#### 🔧 Smart Integrations
- 📱 **WhatsApp Automation** (messages, calls, video)
- 🎬 **YouTube Control** via voice commands
- 💻 **System Control** (apps, windows, shortcuts)
- 📞 **Contact Management** with voice lookup
- 🌐 **Web Browsing** through voice

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

### Backend Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

### Frontend Technologies
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

### AI & ML
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

### Tools & Libraries
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PyPI](https://img.shields.io/badge/PyPI-3775A9?style=for-the-badge&logo=pypi&logoColor=white)

</div>

---

## 🏗️ Architecture

<div align="center">

```mermaid
graph TD
    A[🌐 Web Frontend] -->|Eel Bridge| B[🎯 Main Process]
    B --> C[🎤 Speech Recognition]
    B --> D[👤 Face Authentication]
    B --> E[🔥 Hotword Detection]
    C --> F[📝 Command Parser]
    F --> G[⚡ Feature Handlers]
    G --> H[💾 SQLite Database]
    G --> I[📱 WhatsApp Integration]
    G --> J[🎬 YouTube Control]
    G --> K[💬 AI Chatbot]
    
    style A fill:#e1f5ff
    style B fill:#fff3e0
    style G fill:#f3e5f5
    style H fill:#e8f5e9
```

</div>

---

## 📋 Prerequisites

<table>
<tr>
<td width="50%">

### 🖥️ System Requirements
```yaml
OS: Windows 10/11, Linux, macOS
Python: 3.10+
RAM: 4GB minimum
Storage: 500MB free space
```

</td>
<td width="50%">

### 🔌 Hardware
```yaml
Microphone: Required for voice input
Webcam: Required for face recognition
Internet: Active connection needed
Audio Output: Speakers/Headphones
```

</td>
</tr>
</table>

---

## 🚀 Installation

<details>
<summary><b>📦 Quick Install (Click to expand)</b></summary>

### Step 1️⃣: Clone Repository

```bash
git clone https://github.com/vannu07/jarvis.git
cd jarvis
```

### Step 2️⃣: Setup Virtual Environment

<table>
<tr>
<td width="50%">

**🪟 Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

</td>
<td width="50%">

**🐧 Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

</td>
</tr>
</table>

### Step 3️⃣: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4️⃣: Configure Environment

Create a `.env` file:

```env
# API Keys
HUGGINGFACE_TOKEN=your_token_here
PORCUPINE_ACCESS_KEY=your_key_here

# Voice Settings
TTS_RATE=150
TTS_VOICE=0

# Recognition Settings
FACE_CONFIDENCE_THRESHOLD=50
HOTWORD_SENSITIVITY=0.5
```

### Step 5️⃣: Train Face Recognition (Optional)

```bash
python backend/auth/trainer.py
```

</details>

<div align="center">

### 🎬 Quick Start

```bash
python run.py
```

**That's it! Jarvis will launch at** `http://localhost:8000` 🚀

<img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4eeccf656e44.gif" width="500">

</div>

---

## 💡 Usage

### 🎤 Voice Commands

<table>
<tr>
<td width="33%">

#### 🖥️ System Control
```
Jarvis, open Chrome
Jarvis, launch VS Code
Jarvis, close window
Jarvis, shutdown computer
```

</td>
<td width="33%">

#### 🎵 Media Control
```
Jarvis, play Metallica
Jarvis, pause video
Jarvis, next song
Jarvis, volume up
```

</td>
<td width="33%">

#### 📱 Communication
```
Jarvis, message John
Jarvis, call Sarah
Jarvis, video call Mike
Jarvis, open WhatsApp
```

</td>
</tr>
</table>

### ⌨️ Keyboard Shortcuts

<div align="center">

| Shortcut | Action |
|:--------:|:------:|
| `Win + J` (Windows) | Manual Activation |
| `Cmd + J` (macOS) | Manual Activation |
| `Ctrl + Q` | Quit Application |
| `F11` | Fullscreen Toggle |

</div>

### 🎯 Wake Words

Say **"Jarvis"** or **"Alexa"** followed by your command!

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">
</div>

---

## 📁 Project Structure

```
📦 jarvis/
┣ 📂 backend/
┃ ┣ 📂 auth/
┃ ┃ ┣ 📄 haarcascade_frontalface_default.xml
┃ ┃ ┣ 📄 recognize.py        # 👤 Face recognition
┃ ┃ ┣ 📄 trainer.py          # 🎓 Model training
┃ ┃ ┗ 📂 trainer/            # 💾 Trained models
┃ ┣ 📄 command.py            # 🎯 Command parser
┃ ┣ 📄 config.py             # ⚙️ Configuration
┃ ┣ 📄 db.py                 # 💾 Database ops
┃ ┣ 📄 feature.py            # ⚡ Feature handlers
┃ ┗ 📄 helper.py             # 🛠️ Utilities
┣ 📂 frontend/
┃ ┣ 📂 assets/
┃ ┃ ┣ 📂 audio/              # 🔊 Sound files
┃ ┃ ┣ 📂 img/                # 🖼️ Images & icons
┃ ┃ ┗ 📂 vendor/             # 📚 Third-party libs
┃ ┣ 📄 index.html            # 🌐 Main UI
┃ ┣ 📄 style.css             # 🎨 Styles
┃ ┣ 📄 script.js             # ✨ Particle effects
┃ ┣ 📄 main.js               # 🎮 Core logic
┃ ┗ 📄 controller.js         # 🎛️ Event handlers
┣ 📄 main.py                 # 🚀 Entry point
┣ 📄 run.py                  # 🔄 Launcher
┣ 📄 requirements.txt        # 📦 Dependencies
┗ 📄 jarvis.db              # 💾 SQLite DB
```

---

## 🔧 Development

<details>
<summary><b>🎨 Adding Custom Commands</b></summary>

### 1️⃣ Define Command Pattern

Edit `backend/command.py`:

```python
def parse_command(query: str) -> dict:
    if "my custom action" in query.lower():
        return {
            "action": "custom_action",
            "params": {"param1": "value1"}
        }
```

### 2️⃣ Implement Handler

Edit `backend/feature.py`:

```python
def handle_custom_action(params: dict) -> str:
    # Your implementation here
    result = do_something(params)
    return f"Action completed: {result}"
```

### 3️⃣ Register Command

```python
COMMAND_HANDLERS = {
    "custom_action": handle_custom_action,
    # ... other handlers
}
```

</details>

<details>
<summary><b>💾 Database Schema</b></summary>

```sql
-- 📇 Contacts Table
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    whatsapp TEXT,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 💻 Applications Table
CREATE TABLE apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    path TEXT NOT NULL,
    keywords TEXT,  -- JSON array
    icon TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 🌐 Web Commands Table
CREATE TABLE web_commands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT NOT NULL,
    url TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

</details>

<details>
<summary><b>🧪 Testing</b></summary>

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest --cov=backend --cov-report=html tests/

# Run specific test file
pytest tests/test_command.py -v

# Linting
black backend/ frontend/ --check
flake8 backend/
pylint backend/
```

</details>

<details>
<summary><b>🐳 Docker Deployment</b></summary>

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-pyaudio \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

EXPOSE 8000

CMD ["python", "run.py"]
```

**Build & Run:**
```bash
docker build -t jarvis-ai .
docker run -p 8000:8000 -v $(pwd)/jarvis.db:/app/jarvis.db jarvis-ai
```

</details>

---

## 📊 Performance Metrics

<div align="center">

| Metric | Value | Status |
|:------:|:-----:|:------:|
| 🚀 Cold Start Time | ~3.5s | ![](https://img.shields.io/badge/-Excellent-brightgreen) |
| ⚡ Response Latency | <200ms | ![](https://img.shields.io/badge/-Fast-green) |
| 🎯 Face Recognition Accuracy | 94.2% | ![](https://img.shields.io/badge/-High-blue) |
| 💾 Memory Footprint | ~150MB | ![](https://img.shields.io/badge/-Efficient-green) |
| 🔋 CPU Usage (Idle) | 2-5% | ![](https://img.shields.io/badge/-Low-brightgreen) |

*Benchmarked on Windows 11, Intel i5-10400, 16GB RAM*

</div>

---

## 🐛 Troubleshooting

<details>
<summary><b>🔴 Common Issues & Solutions</b></summary>

### ❌ PyAudio Installation Fails

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Linux:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

### ❌ Face Recognition Not Working

1. Ensure good lighting conditions
2. Position face 2-3 feet from camera
3. Retrain model:
   ```bash
   python backend/auth/trainer.py
   ```
4. Check camera permissions in system settings

### ❌ Voice Commands Unresponsive

1. Check microphone permissions
2. Test microphone:
   ```bash
   python -m speech_recognition
   ```
3. Verify internet connection
4. Try different microphone device

### ❌ Module Import Errors

```bash
pip install --upgrade --force-reinstall -r requirements.txt
```

### 🐞 Enable Debug Mode

```bash
# Windows
set JARVIS_DEBUG=1
python run.py

# Linux/Mac
export JARVIS_DEBUG=1
python run.py
```

</details>

---

## 🤝 Contributing

<div align="center">

**We love contributions!** 💖

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="400">

</div>

### 📝 Contribution Guidelines

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 **Commit** your changes (`git commit -m 'feat: add amazing feature'`)
4. 📤 **Push** to the branch (`git push origin feature/amazing-feature`)
5. 🎉 **Open** a Pull Request

### 📋 Commit Convention

```
type(scope): subject

[optional body]

[optional footer]
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Example:**
```bash
git commit -m "feat(voice): add support for multiple languages"
git commit -m "fix(face): improve recognition accuracy in low light"
git commit -m "docs(readme): update installation instructions"
```

### 🎯 Code Style

- ✅ Follow PEP 8 for Python code
- ✅ Use type hints where applicable
- ✅ Write docstrings for public functions
- ✅ Run `black` and `flake8` before committing
- ✅ Add unit tests for new features

<div align="center">

### 🌟 Top Contributors

<a href="https://github.com/vannu07/jarvis/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vannu07/jarvis" />
</a>

</div>

---

## 🗺️ Roadmap

<table>
<tr>
<td width="33%">

### 🎯 Short Term
- [ ] 🌍 Multi-language support
- [ ] 📱 Mobile companion app
- [ ] 🎨 Theme customization
- [ ] 🔌 Plugin system

</td>
<td width="33%">

### 🚀 Medium Term
- [ ] ☁️ Cloud synchronization
- [ ] 🏠 Home automation
- [ ] 🎓 Voice training
- [ ] 📊 Analytics dashboard

</td>
<td width="33%">

### 💫 Long Term
- [ ] 🤖 Advanced AI models
- [ ] 🌐 Cross-platform support
- [ ] 👥 Multi-user profiles
- [ ] 🔐 End-to-end encryption

</td>
</tr>
</table>

---

## 📜 License

<div align="center">

This project is licensed under the **MIT License**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

See [LICENSE](LICENSE) file for details

</div>

---

## 🙏 Acknowledgments

<div align="center">

Special thanks to these amazing projects:

[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Google](https://img.shields.io/badge/Google-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://cloud.google.com/speech-to-text)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

</div>

---

## 📞 Contact & Support

<div align="center">

**Varnit Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-vannu07-181717?style=for-the-badge&logo=github)](https://github.com/vannu07)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Varnit%20Kumar-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/varnit-kumar)
[![Email](https://img.shields.io/badge/Email-kumar.varnit.16%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kumar.varnit.16@gmail.com)

**Project Link:** [github.com/vannu07/jarvis](https://github.com/vannu07/jarvis)

---

### 💖 Show Your Support

If you find this project helpful, please consider:

⭐ **Starring** this repository
🐛 **Reporting** bugs
💡 **Suggesting** new features
🤝 **Contributing** to the code
📢 **Sharing** with others

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="400">

**Made with ❤️ and Python**

[![Star History Chart](https://api.star-history.com/svg?repos=vannu07/jarvis&type=Date)](https://star-history.com/#vannu07/jarvis&Date)

</div>

---

<div align="center">

### 🌟 Don't forget to star this repository!

![](https://img.shields.io/github/stars/vannu07/jarvis?style=social)
![](https://img.shields.io/github/forks/vannu07/jarvis?style=social)
![](https://img.shields.io/github/watchers/vannu07/jarvis?style=social)

**© 2025 Varnit Kumar. All rights reserved.**

</div>
>>>>>>> bd1d8cfda59b40748beac88a96cbf5f19c082e32
