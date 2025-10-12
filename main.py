import os
import eel
from backend.auth import recoganize
from backend.auth.recoganize import AuthenticateFace
from backend.feature import *
from backend.command import *
from backend.config import (
    WEB_SERVER_HOST,
    WEB_SERVER_PORT,
    WEB_SERVER_MODE,
    WEB_SERVER_BLOCK,
    USER_NAME,
    FRONTEND_PATH,
    FRONTEND_INDEX_FILE,
)


def start():

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
            speak(f"Welcome to Your AI Assistant by {USER_NAME}")
            eel.hideStart()
            play_assistant_sound()
        else:
            speak("Face not recognized. Please try again")

    os.system('start msedge.exe --app="http://127.0.0.1:8000/index.html"')

    eel.start(
        FRONTEND_INDEX_FILE,
        mode=WEB_SERVER_MODE,
        host=WEB_SERVER_HOST,
        block=WEB_SERVER_BLOCK,
    )
