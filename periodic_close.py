# This is periodic_close.py File with Male Voice.
import datetime
import os
import sys
import subprocess
import pyautogui
import webbrowser
import pyttsx3
import bluetooth
import speech_recognition as sr
import wikipedia
import pytesseract
import time
from tkcalendar import *
from tkinter import *
from win10toast import ToastNotifier
from PIL import Image
from selenium import webdriver
from PyDictionary import PyDictionary
from googlesearch import search
from playsound import playsound

dictionary = PyDictionary()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 193)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def options():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        r.pause_threshold = 2
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        option_answer= r.recognize_google(audio, language='en')

    except Exception as e:
        pass
        return "None"
    return option_answer


if __name__ == '__main__':
    speak("do you want to continue using me ?")
    option_answer: str = options().lower
    if "yes" in option_answer:
        speak("okay")
        speak("if you wanto close me just say close")
        os.system("python Jarvis_continous.py")
    elif 'no' in option_answer:
        speak('okay, bye !')
        speak("if you want to speak with me again, please restart me")
        sys.exit()
    else: 
        speak(" i won't close until you close me. if you want me to shut down please say close in about 8 to 10 seconds")
        os.system("python Jarvis_continous.py")
        
        