import os
import eel
import threading
import webbrowser

from backend.auth.recognize import AuthenticateFace
from backend.feature import speak, play_assistant_sound
from backend.command import take_command
from backend.config import (
    WEB_SERVER_HOST,
    WEB_SERVER_PORT,
    WEB_SERVER_MODE,
    WEB_SERVER_BLOCK,
    FRONTEND_PATH,
    FRONTEND_INDEX_FILE,
    USER_NAME,
)
from backend.feature.reminder import set_reminder

# Events for coordination and clean shutdown
auth_complete = threading.Event()
stop_event = threading.Event()


def command_handler(stop_event):
    """
    Runs in a separate thread to continuously listen for and handle voice commands.
    Stops when stop_event is set.
    """
    # Wait until authentication is finished
    auth_complete.wait()
    speak("I am online and ready for your commands.")

    while not stop_event.is_set():
        try:
            # take_command may return None; handle that safely
            raw = take_command()
            if not raw:
                continue
            command = raw.lower()
            print(f"Command received: {command}")

            # ----------------- COMMANDS -----------------
            if "remind me" in command:
                set_reminder(command)

            elif "goodbye" in command or "exit" in command:
                speak("Goodbye! Shutting down.")
                # Signal shutdown to the rest of the program
                stop_event.set()
                break

            # Add other commands here...
            # elif "open youtube" in command:
            #     speak("Opening YouTube")
            #     webbrowser.open("https://youtube.com")

        except Exception as e:
            print(f"Error in command loop: {e}")
            # keep listening


def init():
    """
    Frontend initialization and face authentication handler.
    This function mirrors the logic from your previous init block.
    """
    eel.hideLoader()
    speak(f"Welcome to Jarvis - Your AI Assistant by {USER_NAME}")
    speak("Ready for Face Authentication")

    flag = AuthenticateFace()
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
        # Do not set auth_complete so commands won't run without auth


def start():
    eel.init(FRONTEND_PATH)
    play_assistant_sound()

    # Open the frontend in the default browser (cross-platform)
    try:
        webbrowser.open(f'http://{WEB_SERVER_HOST}:{WEB_SERVER_PORT}/index.html', new=1)
    except Exception:
        # Fallback to the original os.system if needed on Windows
        try:
            os.system(f'start msedge.exe --app="http://{WEB_SERVER_HOST}:{WEB_SERVER_PORT}/index.html"')
        except Exception:
            pass

    # Start the command handler in a background NON-daemon thread so we can join it
    command_thread = threading.Thread(target=command_handler, args=(stop_event,), daemon=False)
    command_thread.start()

    # Start eel and ensure we perform cleanup on exit
    try:
        eel.start(
            FRONTEND_INDEX_FILE,
            mode=WEB_SERVER_MODE,
            host=WEB_SERVER_HOST,
            port=WEB_SERVER_PORT,
            block=WEB_SERVER_BLOCK,
        )
    except KeyboardInterrupt:
        print("Interrupted, shutting down...")
    finally:
        # Ask the command thread to stop and wait briefly for cleanup
        stop_event.set()
        command_thread.join(timeout=5)


if __name__ == '__main__':
    start()
