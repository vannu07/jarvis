import time
import threading
import pyttsx3
import speech_recognition as sr
import eel
from typing import Optional

from backend.feature import openCommand, findContact, whatsApp, PlayYoutube, chatBot

from backend.config import (
    TTS_VOICE_ID, TTS_RATE, TTS_VOLUME, TTS_ENGINE,
    SPEECH_LANGUAGE, SPEECH_TIMEOUT, SPEECH_PHRASE_TIMEOUT, SPEECH_PAUSE_THRESHOLD
)

_engine: Optional[pyttsx3.Engine] = None
_engine_lock = threading.Lock()

_recognizer: Optional[sr.Recognizer] = None
_rec_lock = threading.Lock()

_microphone: Optional[sr.Microphone] = None
_calibrated = False
_cached_energy_threshold: Optional[float] = None

_CALL_KEYS = ("send message", "video call", "call")
_YT_KEY = "on youtube"
_OPEN_KEY = "open"


def _get_engine() -> pyttsx3.Engine:
    global _engine
    if _engine is None:
        with _engine_lock:
            if _engine is None: 
                eng = pyttsx3.init(TTS_ENGINE)
                voices = eng.getProperty("voices")
                if 0 <= TTS_VOICE_ID < len(voices):
                    eng.setProperty("voice", voices[TTS_VOICE_ID].id)
                eng.setProperty("rate", TTS_RATE)
                eng.setProperty("volume", TTS_VOLUME)
                _engine = eng
    return _engine


def _get_recognizer() -> sr.Recognizer:
    global _recognizer
    if _recognizer is None:
        with _rec_lock:
            if _recognizer is None:
                r = sr.Recognizer()
                r.pause_threshold = SPEECH_PAUSE_THRESHOLD
                r.dynamic_energy_threshold = False
                _recognizer = r
    return _recognizer


def _get_microphone() -> sr.Microphone:
    global _microphone
    if _microphone is None:
        _microphone = sr.Microphone()  
    return _microphone


def _ensure_calibrated(r: sr.Recognizer, source: sr.AudioSource) -> None:
    """Calibrate ambient noise once and cache the energy threshold."""
    global _calibrated, _cached_energy_threshold
    if not _calibrated:
        r.adjust_for_ambient_noise(source, duration=0.4)
        _cached_energy_threshold = r.energy_threshold
        _calibrated = True
    elif _cached_energy_threshold is not None:
        r.energy_threshold = _cached_energy_threshold


def speak(text) -> None:
    """TTS + Eel UI; reuses engine; thread-safe."""
    s = str(text)
    eel.DisplayMessage(s)
    eel.receiverText(s)
    try:
        eng = _get_engine()
        with _engine_lock:
            eng.say(s)
            eng.runAndWait()
    except Exception as e:
        print(f"TTS error: {e}")


def takecommand() -> Optional[str]:
    """Capture voice -> lowercase string, or None on failure. Reuses mic/recognizer."""
    r = _get_recognizer()
    mic = _get_microphone()

    eel.DisplayMessage("I'm listening...")
    print("I'm listening...")

    try:
        with mic as source:
            _ensure_calibrated(r, source)
            audio = r.listen(
                source,
                timeout=SPEECH_TIMEOUT,
                phrase_time_limit=SPEECH_PHRASE_TIMEOUT
            )
    except Exception as e:
        print(f"Listen error: {e}")
        return None

    try:
        eel.DisplayMessage("Recognizing...")
        print("Recognizing...")
        query = r.recognize_google(audio, language=SPEECH_LANGUAGE)
        eel.DisplayMessage(query)
        print(f"User said: {query}\n")
        speak(query)
        normalized = query.strip().lower()
        return normalized or None
    except Exception as e:
        print(f"Recognition error: {e}")
        return None


def _handle_comm(query: str) -> None:
    """Route the normalized query to the correct feature handler."""
    if _OPEN_KEY in query:
        openCommand(query)
        return

    if any(k in query for k in _CALL_KEYS):
        Phone, name = findContact(query)
        if Phone != 0:
            if "send message" in query:
                speak("What message to send?")
                msg = takecommand()
                if msg:
                    whatsApp(Phone, msg, "message", name)
                else:
                    speak("I didn't catch the message.")
            elif "call" in query and "video call" not in query:
                whatsApp(Phone, query, "call", name)
            else:
                whatsApp(Phone, query, "video call", name)
        return

    if _YT_KEY in query:
        PlayYoutube(query)
        return
    chatBot(query)

@eel.expose
def takeAllCommands(message: Optional[str] = None) -> None:
    """Entry point for both text and voice; maintains original behavior."""
    if message is None:
        query = takecommand()
        if not query:
            speak("No command was given.")
            return
        eel.senderText(query)
    else:
        q = str(message).strip()
        print(f"Message received: {q}")
        eel.senderText(q)
        query = q.lower()

    try:
        if query:
            _handle_comm(query)
        else:
            speak("No command was given.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, something went wrong.")
    finally:
        eel.ShowHood()
