# import playsound
# import eel


# @eel.expose
# def playAssistantSound():
#     music_dir = "frontend\\assets\\audio\\start_sound.mp3"
#     playsound(music_dir)


import os
from shlex import quote
import struct
import subprocess
import time
import webbrowser
import eel
from hugchat import hugchat
import pvporcupine
import pyaudio
import pyautogui
import pywhatkit as kit
import pygame
from backend.command import speak
from backend.config import (
    ASSISTANT_NAME,
    DATABASE_PATH,
    AUDIO_START_SOUND_PATH,
    PORCUPINE_ACCESS_KEY,
    PORCUPINE_KEYWORDS,
    PORCUPINE_SENSITIVITY,
    HUGCHAT_COOKIE_PATH,
    WHATSAPP_COUNTRY_CODE,
    WHATSAPP_MESSAGE_DELAY,
)
import sqlite3

from backend.helper import extract_yt_term, remove_words

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()
# Initialize pygame mixer
pygame.mixer.init()


# Define the function to play sound
@eel.expose
def play_assistant_sound():
    sound_file = AUDIO_START_SOUND_PATH
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                "SELECT path FROM sys_command WHERE name IN (?)", (app_name,)
            )
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute(
                    "SELECT url FROM web_command WHERE name IN (?)", (app_name,)
                )
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening " + query)
                    try:
                        os.system("start " + query)
                    except Exception:
                        speak("not found")
        except Exception:
            speak("some thing went wrong")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on YouTube")
    kit.playonyt(search_term)


def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:

        # pre trained keywords
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

        # loop for streaming
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            # processing keyword comes from mic
            keyword_index = porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index >= 0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui

                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except Exception:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


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
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith(WHATSAPP_COUNTRY_CODE):
            mobile_number_str = WHATSAPP_COUNTRY_CODE + mobile_number_str

        return mobile_number_str, query
    except Exception:
        speak("not exist in contacts")
        return 0, 0


def whatsApp(Phone, message, flag, name):

    if flag == "message":
        target_tab = 12
        jarvis_message = "message send successfully to " + name

    elif flag == "call":
        target_tab = 7
        message = ""
        jarvis_message = "calling to " + name

    else:
        target_tab = 6
        message = ""
        jarvis_message = "staring video call with " + name

    # Encode the message for URL
    encoded_message = quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={Phone}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(WHATSAPP_MESSAGE_DELAY)
    subprocess.run(full_command, shell=True)

    pyautogui.hotkey("ctrl", "f")

    for i in range(1, target_tab):
        pyautogui.hotkey("tab")

    pyautogui.hotkey("enter")
    speak(jarvis_message)


def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path=HUGCHAT_COOKIE_PATH)
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response
