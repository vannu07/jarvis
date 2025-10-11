# 🤖 Jarvis - AI Voice Assistant

<div align="center">

![Jarvis Logo](frontend/assets/img/logo.ico)

**An intelligent voice-controlled AI assistant with face recognition, built with Python and modern web technologies**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/VarnitKumar/Jarvis)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)](CONTRIBUTING.md)
[![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-Friendly-orange.svg)](https://hacktoberfest.com)
[![Good First Issues](https://img.shields.io/github/issues/VarnitKumar/Jarvis/good%20first%20issue.svg)](https://github.com/VarnitKumar/Jarvis/labels/good%20first%20issue)
[![Help Wanted](https://img.shields.io/github/issues/VarnitKumar/Jarvis/help%20wanted.svg)](https://github.com/VarnitKumar/Jarvis/labels/help%20wanted)

*Created by [Varnit Kumar](https://github.com/vannu07)*

</div>

---

## 🎃 Hacktoberfest 2024

<div align="center">

![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-2024-orange?style=for-the-badge&logo=octocat)

**🎉 Welcome Hacktoberfest Contributors! 🎉**

This repository is **Hacktoberfest-friendly** and welcomes contributions from developers of all skill levels!

### 🎯 Quick Start for Contributors

1. **Star** ⭐ this repository
2. **Fork** 🍴 the repository
3. **Look for issues** with `hacktoberfest` or `good first issue` labels
4. **Make your contribution** 🚀
5. **Submit a PR** 📝

### 🏷️ Contribution Labels

- `hacktoberfest` - All Hacktoberfest contributions
- `good first issue` - Perfect for beginners
- `help wanted` - Community help needed
- `documentation` - Documentation improvements
- `bug` - Bug fixes
- `enhancement` - New features

### 💡 Contribution Ideas

- 🎤 **Voice Features**: Add new voice commands
- 🎨 **UI/UX**: Improve interface and animations
- 📱 **Mobile**: Enhance mobile responsiveness
- 🔧 **Integrations**: Add new service integrations
- 📚 **Documentation**: Improve docs and examples
- 🧪 **Testing**: Add unit tests and coverage
- 🌐 **Web Features**: Add new web functionality

### 🎁 What You Get

- ✅ PRs counted towards Hacktoberfest goals
- 🏆 Recognition in contributors list
- 📜 Mention in release notes
- 🎉 Potential Hacktoberfest swag

**Ready to contribute?** Check out our [Contributing Guidelines](CONTRIBUTING.md) for detailed instructions!

</div>

---

## 🌟 Features

### 🎯 Core Capabilities
- **🎤 Voice Recognition**: Advanced speech-to-text using Google Speech Recognition
- **🗣️ Text-to-Speech**: Natural voice responses with customizable voices
- **👤 Face Authentication**: Secure login using OpenCV face recognition
- **🔥 Hotword Detection**: Always-listening "Jarvis" wake word detection
- **🌐 Web Integration**: Seamless web application with modern UI

### 🚀 Smart Functions
- **📱 WhatsApp Integration**: Send messages, make calls, and video calls
- **🎵 YouTube Control**: Play videos directly from voice commands
- **💬 AI Chatbot**: Intelligent conversations using Hugging Face ChatBot
- **🖥️ System Control**: Open applications and websites via voice
- **📞 Contact Management**: Voice-activated contact lookup and calling

### 🎨 User Interface
- **✨ Modern Design**: Beautiful, responsive web interface
- **🎭 Animated Elements**: Smooth animations and visual feedback
- **🎵 Audio Visualizer**: Real-time audio waveform visualization
- **📱 Mobile Friendly**: Responsive design for all devices

---

## 🛠️ Tech Stack

### Backend Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Eel](https://img.shields.io/badge/Eel-FF6B6B?style=for-the-badge&logo=python&logoColor=white)

### Frontend Technologies
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

### AI & Machine Learning
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF6B6B?style=for-the-badge&logo=huggingface&logoColor=white)
![Google Speech](https://img.shields.io/badge/Google%20Speech-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Porcupine](https://img.shields.io/badge/Porcupine-FF6B6B?style=for-the-badge&logo=python&logoColor=white)

### Audio & Media
![PyAudio](https://img.shields.io/badge/PyAudio-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-FF6B6B?style=for-the-badge&logo=python&logoColor=white)

---

## 📋 Prerequisites

Before running Jarvis, ensure you have the following installed:

- **Python 3.10+** 🐍
- **Windows 10/11** (for optimal compatibility)
- **Microphone** 🎤
- **Webcam** 📹 (for face recognition)
- **Internet Connection** 🌐

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/VarnitKumar/Jarvis.git
cd Jarvis
```

### 2. Create Virtual Environment
```bash
python -m venv envJarvis
envJarvis\Scripts\activate  # Windows
# source envJarvis/bin/activate  # Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
The SQLite database (`jarvis.db`) will be created automatically on first run.

### 5. Face Recognition Training
```bash
cd backend/auth
python trainer.py
```

---

## 🎮 Usage

### Starting Jarvis
```bash
python run.py
```

### Voice Commands Examples
- **"Jarvis, open Chrome"** - Opens web browser
- **"Jarvis, play [song name] on YouTube"** - Plays YouTube videos
- **"Jarvis, send message to [contact name]"** - Sends WhatsApp message
- **"Jarvis, call [contact name]"** - Makes WhatsApp call
- **"Jarvis, what's the weather?"** - AI conversation

### Hotword Activation
- Say **"Jarvis"** or **"Alexa"** to activate
- Press **Win + J** for manual activation

---

## 📁 Project Structure

```
Jarvis/
├── 📁 backend/
│   ├── 📁 auth/                 # Face recognition system
│   │   ├── haarcascade_frontalface_default.xml
│   │   ├── recoganize.py       # Face authentication
│   │   ├── trainer.py          # Face training module
│   │   └── 📁 trainer/         # Trained models
│   ├── command.py              # Voice command processing
│   ├── config.py               # Configuration settings
│   ├── db.py                   # Database operations
│   ├── feature.py              # Core features & integrations
│   └── helper.py               # Utility functions
├── 📁 frontend/
│   ├── 📁 assets/
│   │   ├── 📁 audio/           # Sound files
│   │   ├── 📁 img/             # Images & icons
│   │   └── 📁 vendore/         # Third-party libraries
│   ├── index.html              # Main web interface
│   ├── style.css               # Styling
│   ├── script.js               # Particle effects
│   ├── main.js                 # Main JavaScript logic
│   └── controller.js           # UI controllers
├── main.py                     # Application entry point
├── run.py                      # Multi-process launcher
└── jarvis.db                   # SQLite database
```

---

## ⚙️ Configuration

### Voice Settings
Edit `backend/command.py` to customize:
- Speech rate and voice selection
- Language settings
- Audio input sensitivity

### Face Recognition
Configure in `backend/auth/`:
- Training data collection
- Recognition accuracy thresholds
- Camera settings

### Database
Modify `backend/db.py` for:
- Contact management
- Application shortcuts
- Web command mappings

---

## 🔧 Customization

### Adding New Voice Commands
1. Edit `backend/command.py`
2. Add new command logic in `backend/feature.py`
3. Update the command processing function

### Modifying UI
1. Edit `frontend/index.html` for layout changes
2. Modify `frontend/style.css` for styling
3. Update `frontend/main.js` for behavior changes

### Database Extensions
1. Add new tables in `backend/db.py`
2. Create corresponding functions in `backend/feature.py`
3. Update the command processing logic

---

## 🐛 Troubleshooting

### Common Issues

**Microphone not working:**
- Check microphone permissions
- Ensure microphone is not muted
- Try different audio input devices

**Face recognition failing:**
- Ensure good lighting conditions
- Retrain face recognition model
- Check camera permissions

**Voice commands not recognized:**
- Speak clearly and at normal volume
- Check internet connection (for Google Speech API)
- Verify microphone quality

**Application crashes:**
- Check Python version compatibility
- Verify all dependencies are installed
- Review error logs in console

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### 🎃 Hacktoberfest Contributors

**Special welcome to Hacktoberfest contributors!** 🎉

- Check out our [Hacktoberfest section](#-hacktoberfest-2025) above
- Look for issues with `hacktoberfest` or `good first issue` labels
- Follow our [detailed contributing guidelines](CONTRIBUTING.md)
- Join our community discussions

### Contribution Guidelines
- Follow PEP 8 Python style guidelines
- Add comments for complex code sections
- Test your changes thoroughly
- Update documentation as needed
- Use meaningful commit messages
- Ensure your PRs are properly labeled

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Varnit Kumar**
- GitHub: [@vannu07](https://github.com/vannu07)
- LinkedIn: [Varnit Kumar](https://linkedin.com/in/varnit-kumar)
- Email: [mail](kumar.varnit.16@gmail.com)

---

## 🙏 Acknowledgments

- **OpenCV** for computer vision capabilities
- **Google Speech Recognition** for voice processing
- **Hugging Face** for AI chatbot integration
- **Bootstrap** for responsive UI components
- **Eel** for Python-JavaScript communication
- **PyAudio** for audio processing
- **Porcupine** for hotword detection

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/VarnitKumar/Jarvis?style=social)
![GitHub forks](https://img.shields.io/github/forks/VarnitKumar/Jarvis?style=social)
![GitHub issues](https://img.shields.io/github/issues/VarnitKumar/Jarvis)
![GitHub pull requests](https://img.shields.io/github/issues-pr/VarnitKumar/Jarvis)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ by [Varnit Kumar](https://github.com/vannu07)

</div>
