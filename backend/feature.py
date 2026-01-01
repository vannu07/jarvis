# import playsound
# import eel


# @eel.expose
# def playAssistantSound():
#     music_dir = "frontend\\assets\\audio\\start_sound.mp3"
#     playsound(music_dir)

import os
import sqlite3
import struct
import subprocess
import time
import webbrowser
from shlex import quote

import eel
import pvporcupine
import pyaudio
import pyautogui
import pygame
import pywhatkit as kit
from hugchat import hugchat

from backend.command import speak, takecommand
from backend.config import (ASSISTANT_NAME, AUDIO_START_SOUND_PATH,
                            DATABASE_PATH, HUGCHAT_COOKIE_PATH,
                            PORCUPINE_ACCESS_KEY, PORCUPINE_KEYWORDS,
                            PORCUPINE_SENSITIVITY, WHATSAPP_COUNTRY_CODE,
                            WHATSAPP_MESSAGE_DELAY)
from backend.helper import extract_yt_term, remove_words
from backend.nlp.command_parser import parse_command

# -----------------------------
# Database & audio setup
# -----------------------------
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
pygame.mixer.init()


# -----------------------------
# Play assistant start sound
# -----------------------------
@eel.expose
def play_assistant_sound():
    sound_file = AUDIO_START_SOUND_PATH
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


# -----------------------------
# Intent handling (Parser Integration)
# -----------------------------
def handle_user_text(user_text):
    """Convert recognized text into intent and trigger action."""
    intent = parse_command(user_text)

    if not intent:
        speak("Sorry, I did not understand that.")
        return

    if intent == "get_time":
        from datetime import datetime

        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")

    elif intent == "open_youtube":
        PlayYoutube(user_text)

    elif intent in ["open_whatsapp", "open_calculator"]:
        openCommand(user_text)

    else:
        speak("Intent recognized but no action defined.")


# -----------------------------
# Core Command Functions
# -----------------------------
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()

    app_name = query.strip()
    if not app_name:
        return

    try:
        # Try system apps
        cursor.execute("SELECT path FROM sys_command WHERE name IN (?)", (app_name,))
        results = cursor.fetchall()

        if results:
            speak("Opening " + query)
            os.startfile(results[0][0])
            return

        # Try web URLs
        cursor.execute("SELECT url FROM web_command WHERE name IN (?)", (app_name,))
        results = cursor.fetchall()

        if results:
            speak("Opening " + query)
            webbrowser.open(results[0][0])
            return

        # Try OS-level open
        speak("Opening " + query)
        os.system("start " + query)

    except Exception as e:
        print("Error in openCommand:", e)
        speak("Something went wrong while opening.")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)


# -----------------------------
# Hotword detection + parser link
# -----------------------------
def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        porcupine = pvporcupine.create(
            access_key=PORCUPINE_ACCESS_KEY,
            keywords=PORCUPINE_KEYWORDS,
            sensitivities=[PORCUPINE_SENSITIVITY] * len(PORCUPINE_KEYWORDS),
        )
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length,
        )

        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            keyword_index = porcupine.process(keyword)

            if keyword_index >= 0:
                print("Hotword detected!")

                # Simulate shortcut (Win + J)
                pyautogui.keyDown("win")
                pyautogui.press("j")
                time.sleep(2)
                pyautogui.keyUp("win")

                # Capture and process user speech
                recognized_text = takecommand()
                if recognized_text:
                    print("You said:", recognized_text)
                    handle_user_text(recognized_text)

    except Exception as e:
        print("Error in hotword:", e)
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


# -----------------------------
# WhatsApp contact + messaging
# -----------------------------
def findContact(query):
    words_to_remove = [
        ASSISTANT_NAME,
        "make",
        "a",
        "to",
        "phone",
        "call",
        "send",
        "message",
        "wahtsapp",
        "video",
    ]
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute(
            "SELECT Phone FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",
            ("%" + query + "%", query + "%"),
        )
        results = cursor.fetchall()
        if not results:
            speak("Contact not found.")
            return 0, 0

        mobile_number = str(results[0][0])
        if not mobile_number.startswith(WHATSAPP_COUNTRY_CODE):
            mobile_number = WHATSAPP_COUNTRY_CODE + mobile_number

        return mobile_number, query
    except Exception as e:
        print("Error in findContact:", e)
        speak("Could not find the contact.")
        return 0, 0


def whatsApp(Phone, message, flag, name):
    if flag == "message":
        target_tab = 12
        jarvis_message = "Message sent successfully to " + name
    elif flag == "call":
        target_tab = 7
        message = ""
        jarvis_message = "Calling " + name
    else:
        target_tab = 6
        message = ""
        jarvis_message = "Starting video call with " + name

    encoded_message = quote(message)
    whatsapp_url = f"whatsapp://send?phone={Phone}&text={encoded_message}"
    full_command = f'start "" "{whatsapp_url}"'

    subprocess.run(full_command, shell=True)
    time.sleep(WHATSAPP_MESSAGE_DELAY)
    subprocess.run(full_command, shell=True)

    pyautogui.hotkey("ctrl", "f")
    for _ in range(target_tab - 1):
        pyautogui.hotkey("tab")
    pyautogui.hotkey("enter")

    speak(jarvis_message)


# -----------------------------
# Chatbot fallback
# -----------------------------
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path=HUGCHAT_COOKIE_PATH)
    chat_id = chatbot.new_conversation()
    chatbot.change_conversation(chat_id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
