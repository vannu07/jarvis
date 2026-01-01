import eel
import pyttsx3
import speech_recognition as sr

from backend.config import (SPEECH_LANGUAGE, SPEECH_PAUSE_THRESHOLD,
                            SPEECH_PHRASE_TIMEOUT, SPEECH_TIMEOUT, TTS_ENGINE,
                            TTS_RATE, TTS_VOICE_ID)


def speak(text):
    text = str(text)
    engine = pyttsx3.init(TTS_ENGINE)
    voices = engine.getProperty("voices")
    # print(voices)
    engine.setProperty("voice", voices[TTS_VOICE_ID].id)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty("rate", TTS_RATE)
    eel.receiverText(text)


# Expose the Python function to JavaScript


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        eel.DisplayMessage("I'm listening...")
        r.pause_threshold = SPEECH_PAUSE_THRESHOLD
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, SPEECH_TIMEOUT, SPEECH_PHRASE_TIMEOUT)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language=SPEECH_LANGUAGE)
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)

        speak(query)
    except Exception as e:
        print(f"Error: {str(e)}\n")
        return None

    return query.lower()


@eel.expose
def takeAllCommands(message=None):
    if message is None:
        query = takecommand()  # If no message is passed, listen for voice input
        if not query:
            return  # Exit if no query is received
        print(query)
        eel.senderText(query)
    else:
        query = message  # If there's a message, use it
        print(f"Message received: {query}")
        eel.senderText(query)

    try:
        if query:
            if "open" in query:
                from backend.feature import openCommand

                openCommand(query)
            elif "send message" in query or "call" in query or "video call" in query:
                from backend.feature import findContact, whatsApp

                flag = ""
                Phone, name = findContact(query)
                if Phone != 0:
                    if "send message" in query:
                        flag = "message"
                        speak("What message to send?")
                        query = takecommand()  # Ask for the message text
                    elif "call" in query:
                        flag = "call"
                    else:
                        flag = "video call"
                    whatsApp(Phone, query, flag, name)
            elif "on youtube" in query:
                from backend.feature import PlayYoutube

                PlayYoutube(query)
            elif "weather" in query or "forecast" in query:
                from backend.feature import get_weather, get_weather_forecast
                import re

                # Extract city name using more robust parsing
                # First, look for "in" or "for" followed by city name
                match = re.search(r'\b(?:in|for)\s+(.+)', query, re.IGNORECASE)
                if match:
                    city = match.group(1).strip()
                    # Remove trailing command words if any
                    for word in ["weather", "forecast", "please"]:
                        city = re.sub(r'\b' + word + r'\b\s*$', '', city, flags=re.IGNORECASE).strip()
                else:
                    # Fallback: remove common command words
                    city = query
                    for word in ["weather", "forecast", "what's", "what is", "the", "show", "me", "get"]:
                        city = re.sub(r'\b' + word + r'\b', '', city, flags=re.IGNORECASE)
                    city = city.strip()
                
                if not city:
                    speak("Which city would you like to know the weather for?")
                    city_query = takecommand()
                    if city_query:
                        city = city_query.strip()
                
                if city:
                    if "forecast" in query:
                        get_weather_forecast(city)
                    else:
                        get_weather(city)
                else:
                    speak("Please specify a city name.")
            else:
                from backend.feature import chatBot

                chatBot(query)
        else:
            speak("No command was given.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, something went wrong.")

    eel.ShowHood()
