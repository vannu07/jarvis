#!/usr/bin/env python3
"""
Jarvis AI Assistant - Environment Setup Script
Created by: Varnit Kumar
Description: Interactive setup script to configure environment variables
"""

import os
import sys
from pathlib import Path

def create_env_file():
    """Create .env file with user input"""
    print("🤖 Jarvis AI Assistant - Environment Setup")
    print("=" * 50)
    print("This script will help you configure your environment variables.")
    print("Press Enter to use default values (shown in brackets).")
    print()
    
    env_content = []
    
    # Application Settings
    print("📱 APPLICATION SETTINGS")
    print("-" * 30)
    assistant_name = input("Assistant Name [jarvis]: ").strip() or "jarvis"
    app_name = input("App Name [Jarvis AI Assistant]: ").strip() or "Jarvis AI Assistant"
    user_name = input("Your Name [Varnit Kumar]: ").strip() or "Varnit Kumar"
    user_email = input("Your Email [varnitkumar@example.com]: ").strip() or "varnitkumar@example.com"
    
    env_content.extend([
        f"ASSISTANT_NAME={assistant_name}",
        f"APP_NAME={app_name}",
        f"USER_NAME={user_name}",
        f"USER_EMAIL={user_email}",
        ""
    ])
    
    # Voice Recognition Settings
    print("\n🎤 VOICE RECOGNITION SETTINGS")
    print("-" * 30)
    google_api_key = input("Google Speech API Key (optional): ").strip()
    speech_language = input("Speech Language [en-US]: ").strip() or "en-US"
    
    env_content.extend([
        f"GOOGLE_SPEECH_API_KEY={google_api_key}",
        f"GOOGLE_SPEECH_LANGUAGE={speech_language}",
        ""
    ])
    
    # Face Recognition Settings
    print("\n👤 FACE RECOGNITION SETTINGS")
    print("-" * 30)
    face_names = input("Face Recognition Names (comma-separated) [Unknown,Unknown,Varnit Kumar]: ").strip() or "Unknown,Unknown,Varnit Kumar"
    
    env_content.extend([
        f"FACE_RECOGNITION_NAMES={face_names}",
        ""
    ])
    
    # Hotword Detection Settings
    print("\n🔥 HOTWORD DETECTION SETTINGS")
    print("-" * 30)
    porcupine_key = input("Porcupine Access Key (optional): ").strip()
    hotwords = input("Hotwords (comma-separated) [jarvis,alexa]: ").strip() or "jarvis,alexa"
    
    env_content.extend([
        f"PORCUPINE_ACCESS_KEY={porcupine_key}",
        f"PORCUPINE_KEYWORDS={hotwords}",
        ""
    ])
    
    # WhatsApp Settings
    print("\n📱 WHATSAPP INTEGRATION SETTINGS")
    print("-" * 30)
    country_code = input("Default Country Code [+91]: ").strip() or "+91"
    
    env_content.extend([
        f"WHATSAPP_DEFAULT_COUNTRY_CODE={country_code}",
        ""
    ])
    
    # Web Server Settings
    print("\n🌐 WEB SERVER SETTINGS")
    print("-" * 30)
    web_host = input("Web Server Host [localhost]: ").strip() or "localhost"
    web_port = input("Web Server Port [8000]: ").strip() or "8000"
    
    env_content.extend([
        f"WEB_SERVER_HOST={web_host}",
        f"WEB_SERVER_PORT={web_port}",
        ""
    ])
    
    # Add default values for other settings
    env_content.extend([
        "# Database Settings",
        "DATABASE_PATH=jarvis.db",
        "",
        "# Speech Recognition Settings",
        "SPEECH_RECOGNITION_TIMEOUT=10",
        "SPEECH_RECOGNITION_PHRASE_TIMEOUT=8",
        "SPEECH_RECOGNITION_PAUSE_THRESHOLD=1",
        "",
        "# Text-to-Speech Settings",
        "TTS_VOICE_ID=2",
        "TTS_RATE=174",
        "TTS_VOLUME=1.0",
        "TTS_ENGINE=sapi5",
        "",
        "# Face Recognition Settings",
        "FACE_CASCADE_PATH=backend/auth/haarcascade_frontalface_default.xml",
        "FACE_TRAINER_PATH=backend/auth/trainer/trainer.yml",
        "FACE_SAMPLES_PATH=backend/auth/samples",
        "FACE_RECOGNITION_CONFIDENCE=100",
        "FACE_RECOGNITION_SCALE_FACTOR=1.2",
        "FACE_RECOGNITION_MIN_NEIGHBORS=5",
        "",
        "# Camera Settings",
        "CAMERA_INDEX=0",
        "CAMERA_WIDTH=640",
        "CAMERA_HEIGHT=480",
        "",
        "# Hotword Detection Settings",
        "PORCUPINE_SENSITIVITY=0.5",
        "",
        "# AI Chatbot Settings",
        "HUGCHAT_COOKIE_PATH=backend/cookie.json",
        "HUGCHAT_MODEL_NAME=huggingface/CodeLlama-7b-Instruct-hf",
        "",
        "# WhatsApp Settings",
        "WHATSAPP_MESSAGE_DELAY=5",
        "",
        "# Audio Settings",
        "AUDIO_START_SOUND_PATH=frontend/assets/audio/start_sound.mp3",
        "",
        "# Web Server Settings",
        "WEB_SERVER_MODE=None",
        "WEB_SERVER_BLOCK=true",
        "FRONTEND_PATH=frontend",
        "FRONTEND_INDEX_FILE=index.html",
        "",
        "# Feature Flags",
        "FACE_RECOGNITION_ENABLED=true",
        "HOTWORD_DETECTION_ENABLED=true",
        "VOICE_COMMANDS_ENABLED=true",
        "WHATSAPP_INTEGRATION_ENABLED=true",
        "YOUTUBE_INTEGRATION_ENABLED=true",
        "AI_CHATBOT_ENABLED=true",
        "SYSTEM_CONTROL_ENABLED=true",
        "WEB_INTERFACE_ENABLED=true",
        "",
        "# Logging Settings",
        "LOG_LEVEL=INFO",
        "LOG_FILE_PATH=logs/jarvis.log",
        "",
        "# Development Settings",
        "DEBUG_MODE=false",
        "DEVELOPMENT_MODE=false",
        ""
    ])
    
    # Write .env file
    env_file_path = Path(".env")
    with open(env_file_path, 'w') as f:
        f.write('\n'.join(env_content))
    
    print(f"\n✅ Environment file created: {env_file_path.absolute()}")
    print("📝 You can edit this file later to modify settings.")
    print("\n🚀 Next steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Train face recognition: cd backend/auth && python trainer.py")
    print("3. Run Jarvis: python run.py")

def main():
    """Main setup function"""
    try:
        create_env_file()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error during setup: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
