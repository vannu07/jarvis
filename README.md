<div align="center">

# Jarvis AI Assistant

### *Your Personal Voice-Controlled AI Companion*

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)
[![Stars](https://img.shields.io/github/stars/vannu07/jarvis?style=for-the-badge&logo=github)](https://github.com/vannu07/jarvis/stargazers)
[![Forks](https://img.shields.io/github/forks/vannu07/jarvis?style=for-the-badge&logo=github)](https://github.com/vannu07/jarvis/network)
[![CodeQL](https://github.com/vannu07/jarvis/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/vannu07/jarvis/actions/workflows/codeql-analysis.yml)

<img src="https://raw.githubusercontent.com/vannu07/jarvis/main/frontend/assets/img/logo.ico" alt="Jarvis Logo" width="150"/>

*A production-ready voice assistant with facial recognition authentication, built on modern Python architecture and web technologies.*

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#development) • [Contributing](#contributing)

---

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

## Overview

Jarvis is an intelligent voice assistant that combines speech recognition, natural language processing, and computer vision to provide a seamless user experience. The system features biometric authentication, hotword detection, and extensive integration with popular platforms.

<div align="center">

## Key Features

| Voice Control | Face Recognition | Hotword Detection | Web Integration |
|:---:|:---:|:---:|:---:|
| Advanced speech-to-text | Secure biometric auth | Always-on wake word | Modern responsive UI |

</div>

### Core Capabilities

<table>
<tr>
<td width="50%">

**Voice & AI**
- Real-time Speech Recognition using Google STT
- Natural Language Processing with Hugging Face
- Text-to-Speech with customizable voices
- Audio Visualization in real-time
- Wake Word Detection ("Jarvis", "Alexa")

</td>
<td width="50%">

**Smart Integrations**
- WhatsApp Automation (messages, calls, video)
- YouTube Control via voice commands
- System Control (apps, windows, shortcuts)
- Contact Management with voice lookup
- Web Browsing through voice
- Weather Forecasts via OpenWeatherMap API

</td>
</tr>
</table>

---

<div align="center">

## Technology Stack

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

</div>

---

<div align="center">

## System Architecture

```mermaid
graph TD
    A[Web Frontend] -->|Eel Bridge| B[Main Process]
    B --> C[Speech Recognition]
    B --> D[Face Authentication]
    B --> E[Hotword Detection]
    C --> F[Command Parser]
    F --> G[Feature Handlers]
    G --> H[SQLite Database]
    G --> I[WhatsApp Integration]
    G --> J[YouTube Control]
    G --> K[AI Chatbot]

    %% Consistent style for all nodes
    style A fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style B fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style C fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style D fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style E fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style F fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style G fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style H fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style I fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style J fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121
    style K fill:#ede7f6,stroke:#4a148c,stroke-width:1px,color:#212121

```

</div>

---

## Prerequisites

<table>
<tr>
<td width="50%">

### System Requirements
```yaml
OS: Windows 10/11, Linux, macOS
Python: 3.10+
RAM: 4GB minimum
Storage: 500MB free space
```

</td>
<td width="50%">

### Hardware
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

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/vannu07/jarvis.git
cd jarvis
```

### Step 2: Setup Virtual Environment

<table>
<tr>
<td width="50%">

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

</td>
<td width="50%">

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

</td>
</tr>
</table>

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment

Create a `.env` file:

```env
# API Keys
HUGGINGFACE_TOKEN=your_token_here
PORCUPINE_ACCESS_KEY=your_key_here
NEWSAPI_KEY=your_newsapi_key
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key

# Voice Settings
TTS_RATE=150
TTS_VOICE=0

# Recognition Settings
FACE_CONFIDENCE_THRESHOLD=50
HOTWORD_SENSITIVITY=0.5
```

### Step 5: Train Face Recognition (Optional)

```bash
python backend/auth/trainer.py
```

<div align="center">

### Quick Start

```bash
python run.py
```

**Jarvis will launch at** `http://localhost:8000`

</div>

---

## Usage

### Voice Commands

<table>
<tr>
<td width="33%">

#### System Control
```
Jarvis, open Chrome
Jarvis, launch VS Code
Jarvis, close window
Jarvis, shutdown computer
```

</td>
<td width="33%">

#### Media Control
```
Jarvis, play Metallica
Jarvis, pause video
Jarvis, next song
Jarvis, volume up
```

</td>
<td width="33%">

#### Communication
```
Jarvis, message John
Jarvis, call Sarah
Jarvis, video call Mike
Jarvis, open WhatsApp
```

</td>
</tr>
<tr>
<td width="33%">

#### Weather & Information
```
Jarvis, weather in London
Jarvis, forecast for Tokyo
Jarvis, weather in New York
Jarvis, forecast Paris
```

</td>
<td width="66%" colspan="2">

#### AI Assistant
```
Jarvis, what is the capital of France?
Jarvis, tell me a joke
Jarvis, help me with Python
```

</td>
</tr>
</table>

### Keyboard Shortcuts

<div align="center">

| Shortcut | Action |
|:--------:|:------:|
| `Win + J` (Windows) | Manual Activation |
| `Cmd + J` (macOS) | Manual Activation |
| `Ctrl + Q` | Quit Application |
| `F11` | Fullscreen Toggle |

</div>

### Wake Words

Say **"Jarvis"** or **"Alexa"** followed by your command

---

## Weather Feature

Jarvis integrates with OpenWeatherMap API to provide real-time weather updates and forecasts.

### Setup OpenWeatherMap API

1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
2. Add your API key to the `.env` file:
   ```env
   OPENWEATHERMAP_API_KEY=your_api_key_here
   ```

### Weather Commands

**Current Weather:**
```bash
Jarvis, weather in London
Jarvis, what's the weather in Tokyo
Jarvis, weather for New York
```

**Weather Forecast (3-5 days):**
```bash
Jarvis, forecast for Paris
Jarvis, forecast in Mumbai
Jarvis, weather forecast for Berlin
```

### Features

- ✅ Current temperature, feels-like temperature, and conditions
- ✅ Humidity, wind speed, and atmospheric pressure
- ✅ 3-5 day weather forecast with daily min/max temperatures
- ✅ Graceful handling of invalid city names
- ✅ Clean console output with detailed information
- ✅ Voice responses for hands-free operation

### Standalone Usage

You can also use the weather module independently:

```bash
python weather_fetcher.py
```

Then use commands like:
- `weather London` - Get current weather
- `forecast Tokyo` - Get 5-day forecast
- `exit` - Quit the application

### Testing

Run the weather module tests:

```bash
python -m testing.weather_test
```

---

## Project Structure

```
jarvis/
├── backend/
│   ├── auth/
│   │   ├── haarcascade_frontalface_default.xml
│   │   ├── recognize.py        # Face recognition
│   │   ├── trainer.py          # Model training
│   │   └── trainer/            # Trained models
│   ├── command.py              # Command parser
│   ├── config.py               # Configuration
│   ├── db.py                   # Database ops
│   ├── feature.py              # Feature handlers
│   └── helper.py               # Utilities
├── frontend/
│   ├── assets/
│   │   ├── audio/              # Sound files
│   │   ├── img/                # Images & icons
│   │   └── vendor/             # Third-party libs
│   ├── index.html              # Main UI
│   ├── style.css               # Styles
│   ├── script.js               # Particle effects
│   ├── main.js                 # Core logic
│   └── controller.js           # Event handlers
├── main.py                     # Entry point
├── run.py                      # Launcher
├── weather_fetcher.py          # Weather module
├── requirements.txt            # Dependencies
├── testing/
│   ├── weather_test.py         # Weather tests
│   └── text_test.py            # Command parser tests
└── jarvis.db                  # SQLite DB
```

---

## Development

### Adding Custom Commands

**1. Define Command Pattern**

Edit `backend/command.py`:

```python
def parse_command(query: str) -> dict:
    if "my custom action" in query.lower():
        return {
            "action": "custom_action",
            "params": {"param1": "value1"}
        }
```

**2. Implement Handler**

Edit `backend/feature.py`:

```python
def handle_custom_action(params: dict) -> str:
    result = do_something(params)
    return f"Action completed: {result}"
```

**3. Register Command**

```python
COMMAND_HANDLERS = {
    "custom_action": handle_custom_action,
    # ... other handlers
}
```

### Database Schema

```sql
-- Contacts Table
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    whatsapp TEXT,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Applications Table
CREATE TABLE apps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    path TEXT NOT NULL,
    keywords TEXT,
    icon TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Web Commands Table
CREATE TABLE web_commands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    command TEXT NOT NULL,
    url TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Testing

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

### Docker Deployment

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

---

<div align="center">

## Performance Metrics

| Metric | Value | Status |
|:------:|:-----:|:------:|
| Cold Start Time | ~3.5s | ![](https://img.shields.io/badge/-Excellent-brightgreen) |
| Response Latency | <200ms | ![](https://img.shields.io/badge/-Fast-green) |
| Face Recognition Accuracy | 94.2% | ![](https://img.shields.io/badge/-High-blue) |
| Memory Footprint | ~150MB | ![](https://img.shields.io/badge/-Efficient-green) |
| CPU Usage (Idle) | 2-5% | ![](https://img.shields.io/badge/-Low-brightgreen) |

*Benchmarked on Windows 11, Intel i5-10400, 16GB RAM*

</div>

---

## Troubleshooting

### PyAudio Installation Fails

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

### Face Recognition Not Working

1. Ensure good lighting conditions
2. Position face 2-3 feet from camera
3. Retrain model:
   ```bash
   python backend/auth/trainer.py
   ```
4. Check camera permissions in system settings

### Voice Commands Unresponsive

1. Check microphone permissions
2. Test microphone:
   ```bash
   python -m speech_recognition
   ```
3. Verify internet connection
4. Try different microphone device

### Module Import Errors

```bash
pip install --upgrade --force-reinstall -r requirements.txt
```

### Enable Debug Mode

```bash
# Windows
set JARVIS_DEBUG=1
python run.py

# Linux/Mac
export JARVIS_DEBUG=1
python run.py
```

---

<div align="center">

## Contributing

**We welcome contributions from the community**

</div>

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Commit Convention

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

### Code Style

- Follow PEP 8 for Python code
- Use type hints where applicable
- Write docstrings for public functions
- Run `black` and `flake8` before committing
- Add unit tests for new features

<div align="center">

### Top Contributors

<a href="https://github.com/vannu07/jarvis/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vannu07/jarvis" />
</a>

</div>

---

## Roadmap

<table>
<tr>
<td width="33%">

### Short Term
- [ ] Multi-language support
- [ ] Mobile companion app
- [ ] Theme customization
- [ ] Plugin system

</td>
<td width="33%">

### Medium Term
- [ ] Cloud synchronization
- [ ] Home automation
- [ ] Voice training
- [ ] Analytics dashboard

</td>
<td width="33%">

### Long Term
- [ ] Advanced AI models
- [ ] Cross-platform support
- [ ] Multi-user profiles
- [ ] End-to-end encryption

</td>
</tr>
</table>

---

<div align="center">

## License

This project is licensed under the **MIT License**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

See [LICENSE](LICENSE) file for details

</div>

---

<div align="center">

## Acknowledgments

Special thanks to these amazing projects:

[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Google](https://img.shields.io/badge/Google-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://cloud.google.com/speech-to-text)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

</div>

---

<div align="center">

## Support

**Project Link:** [github.com/vannu07/jarvis](https://github.com/vannu07/jarvis)

For issues, questions, or feature requests, please open an issue on GitHub

---

### Show Your Support

If you find this project helpful, please consider starring the repository

[![Star History Chart](https://api.star-history.com/svg?repos=vannu07/jarvis&type=Date)](https://star-history.com/#vannu07/jarvis&Date)

**Made with Python**

![](https://img.shields.io/github/stars/vannu07/jarvis?style=social)
![](https://img.shields.io/github/forks/vannu07/jarvis?style=social)
![](https://img.shields.io/github/watchers/vannu07/jarvis?style=social)

**Copyright 2025**

</div>
