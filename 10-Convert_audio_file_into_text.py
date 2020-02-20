# Truzz Blogg - Youtube link: https://youtu.be/q-N6IcgCqCE
# Speech recognition in Python ::: How to convert an Audio File to Text

import speech_recognition as sr
import time

r = sr.Recognizer()

with sr.AudioFile('C:\\Users\\rickg\\OneDrive\\Documentos\\Audacity\\audio_20.wav') as source:
    # print("Say Something...")
    audio = r.listen(source)

    try:
        print("Reading audio file. Please, wait a moment...")
        text = r.recognize_google(audio, language='es-ES')
        time.sleep(1.5)
        print(text)
    except:
        print("I am sorry! I can not understand!")
