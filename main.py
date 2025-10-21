import os
import eel
import threading
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import * # Assuming a take_command() function exists here
from backend.config import (
    WEB_SERVER_HOST,
    WEB_SERVER_PORT,
    WEB_SERVER_MODE,
    WEB_SERVER_BLOCK,
    USER_NAME,
    FRONTEND_PATH,
    FRONTEND_INDEX_FILE,
)
# Import our new reminder function
from backend.feature.reminder import set_reminder

# A flag to signal when authentication is complete
auth_complete = threading.Event()

def command_handler():
    """
    Runs in a separate thread to continuously listen for and handle voice commands.
    """
    # Wait until the authentication process is finished
    auth_complete.wait()
    speak("I am online and ready for your commands.")
    
    while True:
        try:
            # This function should capture voice input and return it as text
            command = take_command().lower()
            if not command:
                continue

            print(f"Command received: {command}")

            # ----------------- COMMANDS -----------------
            if "remind me" in command:
                set_reminder(command)
            
            elif "goodbye" in command or "exit" in command:
                speak("Goodbye! Shutting down.")
                # This will stop the command loop
                break
            
            # Add other commands here...
            # elif "open youtube" in command:
            #     speak("Opening YouTube")
            #     # import webbrowser
            #     # webbrowser.open("youtube.com")

        except Exception as e:
            print(f"Error in command loop: {e}")
            # Loop continues listening

def start():
    """
    Initializes the frontend, authentication, and starts the command handler.
    """
    eel.init(FRONTEND_PATH)

    play_assistant_sound()

    @eel.expose
    def init():
        eel.hideLoader()
        speak(f"Welcome to Jarvis - Your AI Assistant by {USER_NAME}")
        speak("Ready for Face Authentication")
        
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            speak("Face recognized successfully")
            eel.hideFaceAuth()
            eel.hideFaceAuthSuccess()
            speak(f"Welcome back, {USER_NAME}!")
            eel.hideStart()
            play_assistant_sound()
            # Signal that authentication is complete so the command loop can start
            auth_complete.set()
        else:
            speak("Face not recognized. Please try again")
            # In a real app, you might want to handle this case differently,
            # maybe by retrying or exiting.
            # For now, we will NOT set the event to prevent commanding without auth.

    os.system(f'start msedge.exe --app="http://{WEB_SERVER_HOST}:{WEB_SERVER_PORT}/index.html"')

    # Start the command handler in a background thread
    command_thread = threading.Thread(target=command_handler, daemon=True)
    command_thread.start()

    eel.start(
        FRONTEND_INDEX_FILE,
        mode=WEB_SERVER_MODE,
        host=WEB_SERVER_HOST,
        port=WEB_SERVER_PORT,
        block=WEB_SERVER_BLOCK,
    )

if __name__ == '__main__':
    start()
