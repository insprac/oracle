from dotenv import load_dotenv

load_dotenv()

import speech_recognition as sr
import tts
from chat import chat

recognizer = sr.Recognizer()
mic = sr.Microphone()

def print_message(role, message):
    print("")
    print(role + ":")
    print(message)

while True:
    with mic as source:
        audio = recognizer.listen(source)
        message = recognizer.recognize_whisper(audio).strip()

        print_message("You", message)
        response = chat(message)
        print_message("Assistant", response)
        tts.synthesize(response)
