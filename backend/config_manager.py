"""
Configuration Management Module for Jarvis AI Assistant
Created by: Varnit Kumar
Description: Handles loading and management of environment variables and configuration
"""

import os
import logging
from typing import Optional
from pathlib import Path


class Config:
    """Configuration management class for Jarvis AI Assistant"""

    def __init__(self, env_file: str = ".env"):
        """
        Initialize configuration manager

        Args:
            env_file (str): Path to environment file
        """
        self.env_file = env_file
        self._load_env_file()
        self._setup_logging()

    def _load_env_file(self):
        """Load environment variables from .env file"""
        env_path = Path(self.env_file)
        if env_path.exists():
            with open(env_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        os.environ[key.strip()] = value.strip()

    def _setup_logging(self):
        """Setup logging configuration"""
        log_level = self.get("LOG_LEVEL", "INFO")
        log_file = self.get("LOG_FILE_PATH", "logs/jarvis.log")

        # Create logs directory if it doesn't exist
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            level=getattr(logging, log_level.upper()),
            format=self.get(
                "LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            ),
            handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
        )

    def get(self, key: str, default: Optional[str] = None) -> str:
        """
        Get environment variable value

        Args:
            key (str): Environment variable key
            default (Optional[str]): Default value if key not found

        Returns:
            str: Environment variable value or default
        """
        return os.environ.get(key, default)

    def get_bool(self, key: str, default: bool = False) -> bool:
        """
        Get boolean environment variable

        Args:
            key (str): Environment variable key
            default (bool): Default value if key not found

        Returns:
            bool: Boolean value
        """
        value = self.get(key, str(default)).lower()
        return value in ("true", "1", "yes", "on")

    def get_int(self, key: str, default: int = 0) -> int:
        """
        Get integer environment variable

        Args:
            key (str): Environment variable key
            default (int): Default value if key not found

        Returns:
            int: Integer value
        """
        try:
            return int(self.get(key, str(default)))
        except ValueError:
            return default

    def get_float(self, key: str, default: float = 0.0) -> float:
        """
        Get float environment variable

        Args:
            key (str): Environment variable key
            default (float): Default value if key not found

        Returns:
            float: Float value
        """
        try:
            return float(self.get(key, str(default)))
        except ValueError:
            return default

    def get_list(
        self, key: str, default: Optional[list] = None, separator: str = ","
    ) -> list:
        """
        Get list from environment variable

        Args:
            key (str): Environment variable key
            default (Optional[list]): Default value if key not found
            separator (str): Separator for splitting values

        Returns:
            list: List of values
        """
        if default is None:
            default = []

        value = self.get(key)
        if value:
            return [item.strip() for item in value.split(separator) if item.strip()]
        return default

    # Application Settings
    @property
    def assistant_name(self) -> str:
        return self.get("ASSISTANT_NAME", "jarvis")

    @property
    def app_name(self) -> str:
        return self.get("APP_NAME", "Jarvis AI Assistant")

    @property
    def debug_mode(self) -> bool:
        return self.get_bool("DEBUG_MODE", False)

    # Database Settings
    @property
    def database_path(self) -> str:
        return self.get("DATABASE_PATH", "jarvis.db")

    # Voice Recognition Settings
    @property
    def google_speech_api_key(self) -> str:
        return self.get("GOOGLE_SPEECH_API_KEY", "")

    @property
    def speech_language(self) -> str:
        return self.get("GOOGLE_SPEECH_LANGUAGE", "en-US")

    @property
    def speech_timeout(self) -> int:
        return self.get_int("SPEECH_RECOGNITION_TIMEOUT", 10)

    @property
    def speech_phrase_timeout(self) -> int:
        return self.get_int("SPEECH_RECOGNITION_PHRASE_TIMEOUT", 8)

    @property
    def speech_pause_threshold(self) -> int:
        return self.get_int("SPEECH_RECOGNITION_PAUSE_THRESHOLD", 1)

    # Text-to-Speech Settings
    @property
    def tts_voice_id(self) -> int:
        return self.get_int("TTS_VOICE_ID", 2)

    @property
    def tts_rate(self) -> int:
        return self.get_int("TTS_RATE", 174)

    @property
    def tts_volume(self) -> float:
        return self.get_float("TTS_VOLUME", 1.0)

    @property
    def tts_engine(self) -> str:
        return self.get("TTS_ENGINE", "sapi5")

    # Face Recognition Settings
    @property
    def face_cascade_path(self) -> str:
        return self.get(
            "FACE_CASCADE_PATH", "backend/auth/haarcascade_frontalface_default.xml"
        )

    @property
    def face_trainer_path(self) -> str:
        return self.get("FACE_TRAINER_PATH", "backend/auth/trainer/trainer.yml")

    @property
    def face_samples_path(self) -> str:
        return self.get("FACE_SAMPLES_PATH", "backend/auth/samples")

    @property
    def face_recognition_confidence(self) -> int:
        return self.get_int("FACE_RECOGNITION_CONFIDENCE", 100)

    @property
    def face_recognition_names(self) -> list:
        return self.get_list(
            "FACE_RECOGNITION_NAMES", ["Unknown", "Unknown", "Varnit Kumar"]
        )

    @property
    def camera_index(self) -> int:
        return self.get_int("CAMERA_INDEX", 0)

    @property
    def camera_width(self) -> int:
        return self.get_int("CAMERA_WIDTH", 640)

    @property
    def camera_height(self) -> int:
        return self.get_int("CAMERA_HEIGHT", 480)

    # Hotword Detection Settings
    @property
    def porcupine_access_key(self) -> str:
        return self.get("PORCUPINE_ACCESS_KEY", "")

    @property
    def porcupine_keywords(self) -> list:
        return self.get_list("PORCUPINE_KEYWORDS", ["jarvis", "alexa"])

    @property
    def porcupine_sensitivity(self) -> float:
        return self.get_float("PORCUPINE_SENSITIVITY", 0.5)

    # AI Chatbot Settings
    @property
    def hugchat_cookie_path(self) -> str:
        return self.get("HUGCHAT_COOKIE_PATH", "backend/cookie.json")

    @property
    def hugchat_model_name(self) -> str:
        return self.get("HUGCHAT_MODEL_NAME", "huggingface/CodeLlama-7b-Instruct-hf")

    # WhatsApp Settings
    @property
    def whatsapp_country_code(self) -> str:
        return self.get("WHATSAPP_DEFAULT_COUNTRY_CODE", "+91")

    @property
    def whatsapp_message_delay(self) -> int:
        return self.get_int("WHATSAPP_MESSAGE_DELAY", 5)

    # Audio Settings
    @property
    def audio_start_sound_path(self) -> str:
        return self.get(
            "AUDIO_START_SOUND_PATH", "frontend/assets/audio/start_sound.mp3"
        )

    # Web Server Settings
    @property
    def web_server_host(self) -> str:
        return self.get("WEB_SERVER_HOST", "localhost")

    @property
    def web_server_port(self) -> int:
        return self.get_int("WEB_SERVER_PORT", 8000)

    @property
    def web_server_mode(self) -> str:
        return self.get("WEB_SERVER_MODE", "None")

    @property
    def web_server_block(self) -> bool:
        return self.get_bool("WEB_SERVER_BLOCK", True)

    # User Settings
    @property
    def user_name(self) -> str:
        return self.get("USER_NAME", "Varnit Kumar")

    @property
    def user_email(self) -> str:
        return self.get("USER_EMAIL", "varnitkumar@example.com")

    # Feature Flags
    @property
    def face_recognition_enabled(self) -> bool:
        return self.get_bool("FACE_RECOGNITION_ENABLED", True)

    @property
    def hotword_detection_enabled(self) -> bool:
        return self.get_bool("HOTWORD_DETECTION_ENABLED", True)

    @property
    def voice_commands_enabled(self) -> bool:
        return self.get_bool("VOICE_COMMANDS_ENABLED", True)

    @property
    def whatsapp_integration_enabled(self) -> bool:
        return self.get_bool("WHATSAPP_INTEGRATION_ENABLED", True)

    @property
    def youtube_integration_enabled(self) -> bool:
        return self.get_bool("YOUTUBE_INTEGRATION_ENABLED", True)

    @property
    def ai_chatbot_enabled(self) -> bool:
        return self.get_bool("AI_CHATBOT_ENABLED", True)

    @property
    def system_control_enabled(self) -> bool:
        return self.get_bool("SYSTEM_CONTROL_ENABLED", True)

    @property
    def web_interface_enabled(self) -> bool:
        return self.get_bool("WEB_INTERFACE_ENABLED", True)


# Global configuration instance
config = Config()


# Convenience functions for backward compatibility
def get_config(key: str, default: Optional[str] = None) -> str:
    """Get configuration value"""
    return config.get(key, default)


def get_config_bool(key: str, default: bool = False) -> bool:
    """Get boolean configuration value"""
    return config.get_bool(key, default)


def get_config_int(key: str, default: int = 0) -> int:
    """Get integer configuration value"""
    return config.get_int(key, default)


def get_config_float(key: str, default: float = 0.0) -> float:
    """Get float configuration value"""
    return config.get_float(key, default)


def get_config_list(
    key: str, default: Optional[list] = None, separator: str = ","
) -> list:
    """Get list configuration value"""
    return config.get_list(key, default, separator)
