import requests
import speech_recognition as sr     # import the library
import subprocess
import numpy as np
from scipy.io.wavfile import read, write
import io
import aubio
r = sr.Recognizer()  # initialize recognizer
with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.wwwwwwwwwwww
    print("Speak Anything :")
    audio = r.listen(source)  # listen to the source

    print("###")
    try:
        message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
        print("You said : {}".format(message))
       
    except:
        print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly