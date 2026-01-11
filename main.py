import os
import threading
import webbrowser

import eel

from backend.auth.recognize import AuthenticateFace
from backend.command import take_command
from backend.config import (FRONTEND_INDEX_FILE, FRONTEND_PATH, USER_NAME,
                            WEB_SERVER_BLOCK, WEB_SERVER_HOST, WEB_SERVER_MODE,
                            WEB_SERVER_PORT)
from backend.feature import play_assistant_sound, speak
from backend.feature.reminder import set_reminder
from backend.feedback import StatusIndicator, Timer

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
    StatusIndicator.success("I am online and ready for your commands")
    speak("I am online and ready for your commands.")

    while not stop_event.is_set():
        try:
            # take_command may return None; handle that safely
            raw = take_command()
            if not raw:
                continue
            command = raw.lower()
            StatusIndicator.command(f"Command received: {command}")
            print(f"Command received: {command}")

            # ----------------- COMMANDS -----------------
            if "remind me" in command:
                with Timer(f"Setting reminder: {command}"):
                    set_reminder(command)

            elif "goodbye" in command or "exit" in command:
                StatusIndicator.info("Shutting down...")
                speak("Goodbye! Shutting down.")
                # Signal shutdown to the rest of the program
                stop_event.set()
                break

            # Add other commands here...
            # elif "open youtube" in command:
            #     speak("Opening YouTube")
            #     webbrowser.open("https://youtube.com")

        except Exception as e:
            StatusIndicator.error(f"Error in command loop: {e}")
            print(f"Error in command loop: {e}")
            # keep listening


def init():
    """
    Frontend initialization and face authentication handler.
    This function mirrors the logic from your previous init block.
    """
    eel.hideLoader()
    StatusIndicator.info(f"Welcome to Jarvis - Your AI Assistant by {USER_NAME}")
    speak(f"Welcome to Jarvis - Your AI Assistant by {USER_NAME}")
    StatusIndicator.processing("Ready for Face Authentication")
    speak("Ready for Face Authentication")

    with Timer("Face authentication"):
        flag = AuthenticateFace()
    
    if flag == 1:
        StatusIndicator.success("Face recognized successfully")
        speak("Face recognized successfully")
        eel.hideFaceAuth()
        eel.hideFaceAuthSuccess()
        StatusIndicator.success(f"Welcome back, {USER_NAME}!")
        speak(f"Welcome back, {USER_NAME}!")
        eel.hideStart()
        play_assistant_sound()
        # Signal that authentication is complete so the command loop can start
        auth_complete.set()
    else:
        StatusIndicator.error("Face not recognized. Please try again")
        speak("Face not recognized. Please try again")
        # Do not set auth_complete so commands won't run without auth


def start():
    StatusIndicator.info("Initializing Jarvis AI Assistant...")
    eel.init(FRONTEND_PATH)
    play_assistant_sound()

    # Open the frontend in the default browser (cross-platform)
    try:
        StatusIndicator.processing("Opening web interface...")
        webbrowser.open(f"http://{WEB_SERVER_HOST}:{WEB_SERVER_PORT}/index.html", new=1)
        StatusIndicator.success(f"Web interface available at http://{WEB_SERVER_HOST}:{WEB_SERVER_PORT}")
    except Exception:
        # Fallback to the original os.system if needed on Windows
        try:
            os.system(
                f'start msedge.exe --app="http://{WEB_SERVER_HOST}:{WEB_SERVER_PORT}/index.html"'
            )
        except Exception:
            pass

    # Start the command handler in a background NON-daemon thread so we can join it
    StatusIndicator.processing("Starting command handler...")
    command_thread = threading.Thread(
        target=command_handler, args=(stop_event,), daemon=False
    )
    command_thread.start()
    StatusIndicator.success("Command handler started")

    # Start eel and ensure we perform cleanup on exit
    try:
        StatusIndicator.success("Jarvis is now running!")
        eel.start(
            FRONTEND_INDEX_FILE,
            mode=WEB_SERVER_MODE,
            host=WEB_SERVER_HOST,
            port=WEB_SERVER_PORT,
            block=WEB_SERVER_BLOCK,
        )
    except KeyboardInterrupt:
        StatusIndicator.warning("Interrupted, shutting down...")
        print("Interrupted, shutting down...")
    finally:
        # Ask the command thread to stop and wait briefly for cleanup
        stop_event.set()
        command_thread.join(timeout=5)
        StatusIndicator.info("Jarvis has shut down")


if __name__ == "__main__":
    start()
