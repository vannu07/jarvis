"""
Configuration Module for Jarvis AI Assistant
Created by: Varnit Kumar
Description: Legacy configuration file - now uses config_manager for environment variables
"""

from backend.config_manager import config

# Legacy compatibility - maintain existing ASSISTANT_NAME for backward compatibility
ASSISTANT_NAME = config.assistant_name

# Export commonly used configuration values
APP_NAME = config.app_name
DEBUG_MODE = config.debug_mode
DATABASE_PATH = config.database_path

# Voice Recognition Settings
SPEECH_LANGUAGE = config.speech_language
SPEECH_TIMEOUT = config.speech_timeout
SPEECH_PHRASE_TIMEOUT = config.speech_phrase_timeout
SPEECH_PAUSE_THRESHOLD = config.speech_pause_threshold

# Text-to-Speech Settings
TTS_VOICE_ID = config.tts_voice_id
TTS_RATE = config.tts_rate
TTS_VOLUME = config.tts_volume
TTS_ENGINE = config.tts_engine

# Face Recognition Settings
FACE_CASCADE_PATH = config.face_cascade_path
FACE_TRAINER_PATH = config.face_trainer_path
FACE_SAMPLES_PATH = config.face_samples_path
FACE_RECOGNITION_CONFIDENCE = config.face_recognition_confidence
FACE_RECOGNITION_NAMES = config.face_recognition_names

# Camera Settings
CAMERA_INDEX = config.camera_index
CAMERA_WIDTH = config.camera_width
CAMERA_HEIGHT = config.camera_height

# Hotword Detection Settings
PORCUPINE_ACCESS_KEY = config.porcupine_access_key
PORCUPINE_KEYWORDS = config.porcupine_keywords
PORCUPINE_SENSITIVITY = config.porcupine_sensitivity

# AI Chatbot Settings
HUGCHAT_COOKIE_PATH = config.hugchat_cookie_path
HUGCHAT_MODEL_NAME = config.hugchat_model_name

# WhatsApp Settings
WHATSAPP_COUNTRY_CODE = config.whatsapp_country_code
WHATSAPP_MESSAGE_DELAY = config.whatsapp_message_delay

# Audio Settings
AUDIO_START_SOUND_PATH = config.audio_start_sound_path

# Web Server Settings
WEB_SERVER_HOST = config.web_server_host
WEB_SERVER_PORT = config.web_server_port
WEB_SERVER_MODE = config.web_server_mode
WEB_SERVER_BLOCK = config.web_server_block

# Frontend Settings
FRONTEND_PATH = config.frontend_path
FRONTEND_INDEX_FILE = config.frontend_index_file

# User Settings
USER_NAME = config.user_name
USER_EMAIL = config.user_email

# Weather Settings
OPENWEATHERMAP_API_KEY = config.openweathermap_api_key

# Feature Flags
FACE_RECOGNITION_ENABLED = config.face_recognition_enabled
HOTWORD_DETECTION_ENABLED = config.hotword_detection_enabled
VOICE_COMMANDS_ENABLED = config.voice_commands_enabled
WHATSAPP_INTEGRATION_ENABLED = config.whatsapp_integration_enabled
YOUTUBE_INTEGRATION_ENABLED = config.youtube_integration_enabled
AI_CHATBOT_ENABLED = config.ai_chatbot_enabled
SYSTEM_CONTROL_ENABLED = config.system_control_enabled
WEB_INTERFACE_ENABLED = config.web_interface_enabled
