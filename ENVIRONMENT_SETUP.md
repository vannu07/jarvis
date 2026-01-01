# 🔐 Environment Configuration Guide

## Overview
This guide explains how to configure your Jarvis AI Assistant using environment variables for secure credential management.

## 📁 Files Created

### 1. `env_template.txt`
A comprehensive template containing all possible environment variables with explanations and default values.

### 2. `backend/config_manager.py`
A robust configuration management system that:
- Loads environment variables from `.env` file
- Provides type-safe access to configuration values
- Includes logging setup
- Offers backward compatibility

### 3. `setup_env.py`
An interactive setup script that guides you through configuring your environment.

## 🚀 Quick Setup

### Option 1: Interactive Setup (Recommended)
```bash
python setup_env.py
```
This will guide you through configuring all necessary settings.

### Option 2: Manual Setup
1. Copy `env_template.txt` to `.env`
2. Edit `.env` with your actual credentials
3. Replace placeholder values with real API keys

## 🔑 Required Credentials

### Essential (Must Configure)
- **USER_NAME**: Your name (default: "Varnit Kumar")
- **USER_EMAIL**: Your email address

### Optional (For Enhanced Features)
- **GOOGLE_SPEECH_API_KEY**: For improved speech recognition
- **PORCUPINE_ACCESS_KEY**: For hotword detection
- **HUGCHAT_COOKIE_PATH**: For AI chatbot functionality
- **OPENWEATHERMAP_API_KEY**: For weather forecast features

## 📋 Configuration Categories

### 🎤 Voice Recognition
```env
GOOGLE_SPEECH_API_KEY=your_api_key_here
GOOGLE_SPEECH_LANGUAGE=en-US
SPEECH_RECOGNITION_TIMEOUT=10
SPEECH_RECOGNITION_PHRASE_TIMEOUT=8
SPEECH_RECOGNITION_PAUSE_THRESHOLD=1
```

### 🗣️ Text-to-Speech
```env
TTS_VOICE_ID=2
TTS_RATE=174
TTS_VOLUME=1.0
TTS_ENGINE=sapi5
```

### 👤 Face Recognition
```env
FACE_CASCADE_PATH=backend/auth/haarcascade_frontalface_default.xml
FACE_TRAINER_PATH=backend/auth/trainer/trainer.yml
FACE_SAMPLES_PATH=backend/auth/samples
FACE_RECOGNITION_CONFIDENCE=100
FACE_RECOGNITION_NAMES=Unknown,Unknown,Varnit Kumar
```

### 🔥 Hotword Detection
```env
PORCUPINE_ACCESS_KEY=your_porcupine_key_here
PORCUPINE_KEYWORDS=jarvis,alexa
PORCUPINE_SENSITIVITY=0.5
```

### 💬 AI Chatbot
```env
HUGCHAT_COOKIE_PATH=backend/cookie.json
HUGCHAT_MODEL_NAME=huggingface/CodeLlama-7b-Instruct-hf
```

### 📱 WhatsApp Integration
```env
WHATSAPP_DEFAULT_COUNTRY_CODE=+91
WHATSAPP_MESSAGE_DELAY=5
```

### 🌤️ Weather API
```env
OPENWEATHERMAP_API_KEY=your_openweathermap_key_here
```
Get your free API key at: https://openweathermap.org/api

### 🌐 Web Server
```env
WEB_SERVER_HOST=localhost
WEB_SERVER_PORT=8000
WEB_SERVER_MODE=None
WEB_SERVER_BLOCK=true
```

## 🛠️ Usage in Code

### Using Configuration Manager
```python
from backend.config_manager import config

# Get string values
assistant_name = config.assistant_name
user_name = config.user_name

# Get boolean values
debug_mode = config.debug_mode
face_recognition_enabled = config.face_recognition_enabled

# Get integer values
camera_width = config.camera_width
speech_timeout = config.speech_timeout

# Get list values
face_names = config.face_recognition_names
hotwords = config.porcupine_keywords
```

### Using Legacy Config (Backward Compatibility)
```python
from backend.config import ASSISTANT_NAME, USER_NAME, DEBUG_MODE

# These now use the configuration manager internally
print(f"Assistant: {ASSISTANT_NAME}")
print(f"User: {USER_NAME}")
print(f"Debug: {DEBUG_MODE}")
```

## 🔒 Security Best Practices

### 1. Never Commit .env Files
Ensure `.env` is in your `.gitignore`:
```gitignore
.env
*.env
.env.local
.env.production
```

### 2. Use Strong API Keys
- Generate unique API keys for each service
- Rotate keys regularly
- Use environment-specific keys (dev/prod)

### 3. Limit API Key Permissions
- Only grant necessary permissions
- Use read-only keys where possible
- Monitor API usage

### 4. Secure Storage
- Store production keys in secure vaults
- Use different keys for different environments
- Never hardcode credentials in source code

## 🐛 Troubleshooting

### Common Issues

**Configuration not loading:**
- Ensure `.env` file exists in project root
- Check file permissions
- Verify syntax (no spaces around `=`)

**API keys not working:**
- Verify key format and validity
- Check API quotas and limits
- Ensure proper permissions

**Face recognition failing:**
- Verify file paths in configuration
- Check camera permissions
- Ensure training data exists

### Debug Mode
Enable debug mode for detailed logging:
```env
DEBUG_MODE=true
LOG_LEVEL=DEBUG
VERBOSE_LOGGING=true
```

## 📊 Environment Variables Reference

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `ASSISTANT_NAME` | string | jarvis | Name of the assistant |
| `USER_NAME` | string | Varnit Kumar | Your name |
| `USER_EMAIL` | string | varnitkumar@example.com | Your email |
| `GOOGLE_SPEECH_API_KEY` | string | "" | Google Speech API key |
| `PORCUPINE_ACCESS_KEY` | string | "" | Porcupine hotword detection key |
| `OPENWEATHERMAP_API_KEY` | string | "" | OpenWeatherMap API key |
| `FACE_RECOGNITION_NAMES` | list | Unknown,Unknown,Varnit Kumar | Recognized face names |
| `WHATSAPP_COUNTRY_CODE` | string | +91 | Default country code |
| `WEB_SERVER_PORT` | int | 8000 | Web server port |
| `DEBUG_MODE` | bool | false | Enable debug mode |

## 🔄 Migration from Hardcoded Values

If you have existing hardcoded values, follow these steps:

1. **Identify hardcoded values** in your code
2. **Add corresponding environment variables** to `.env`
3. **Update code** to use configuration manager
4. **Test thoroughly** to ensure functionality

## 📝 Example Configuration

Here's a complete example `.env` file:

```env
# Application Settings
ASSISTANT_NAME=jarvis
USER_NAME=Varnit Kumar
USER_EMAIL=varnitkumar@example.com

# Voice Recognition
GOOGLE_SPEECH_API_KEY=your_google_api_key_here
GOOGLE_SPEECH_LANGUAGE=en-US

# Face Recognition
FACE_RECOGNITION_NAMES=Unknown,Unknown,Varnit Kumar

# Hotword Detection
PORCUPINE_ACCESS_KEY=your_porcupine_key_here
PORCUPINE_KEYWORDS=jarvis,alexa

# WhatsApp
WHATSAPP_DEFAULT_COUNTRY_CODE=+91

# Weather API
OPENWEATHERMAP_API_KEY=your_openweathermap_key_here

# Web Server
WEB_SERVER_HOST=localhost
WEB_SERVER_PORT=8000

# Feature Flags
FACE_RECOGNITION_ENABLED=true
HOTWORD_DETECTION_ENABLED=true
VOICE_COMMANDS_ENABLED=true
WHATSAPP_INTEGRATION_ENABLED=true
AI_CHATBOT_ENABLED=true
```

## 🎯 Next Steps

1. **Run setup script**: `python setup_env.py`
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Train face recognition**: `cd backend/auth && python trainer.py`
4. **Test configuration**: `python -c "from backend.config_manager import config; print('Config loaded successfully!')"`
5. **Run Jarvis**: `python run.py`

## 📞 Support

If you encounter issues with configuration:
1. Check the logs in `logs/jarvis.log`
2. Enable debug mode for detailed information
3. Verify all file paths and permissions
4. Ensure all required dependencies are installed

---

**Created by Varnit Kumar** - Your AI Assistant Configuration Expert! 🤖
