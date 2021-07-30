# This is Jarvis-5th.py File with Male Voice.
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

def take_command():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en')
        print("You Said -", query)

    except Exception as e:
        print("I Couldn't Understand, Please Repeat")
        speak("i couldn't understand, Please Repeat")
        return "None"
    return query

if __name__ == '__main__':
    while True:
        query: str = take_command().lower()

        # General Commands (Casual)

        if 'what can you do' in query:
            print("     _____                       ")
            print("    /     \ - Anything for you! ")
            print("   |  * *  |                     ")
            print("    \_---_/                      ")
            print("      | |                        ")
            speak("I am your personal assistant , i can do anything for you ")
            speak("These are Some Things you can Command Me:")
            print("These are Some Things you can Command Me:")
            print("Wikipedia - for Descriptions of People and Other Things")
            print("Open + Name of the App / Website - for Opening Apps and Websites")
            print("Where Is + Name of the Place - For Finding Location of Places")
            print("What Is + The Word You Want to Search - To Search on Web")
            print(
                  "What Is The Definition/Synonym/Antonym Of + The Word - To Find The "
                  "Definition/Antonym/Synonym Of "
                  "any Word")
            print("Pause - To Stop Me Temporarily")
            print("Close - To Exit me")
            os.system("python Jarvis-6th.py")
        elif 'what is your name' in query:
            print("     _____                       ")
            print("    /     \ - I Am your Personal Assistant,you can call me Jarvis ")
            print("   |  * *  |                     ")
            print("    \_---_/                      ")
            print("      | |                        ")
            speak("i am your personal assistant, you can call me Jarvis, and it's not hard to speak !,ha ha")
            os.system("python Jarvis-6th.py")
        elif 'talk to me in' in query:
            print("     _____                       ")
            print("    /     \ - Sorry, but i am not multillingual ")
            print("   |  * *  |                     ")
            print("    \_---_/                      ")
            print("      | |                        ")
            speak("sorry, but i am not able talk in other languages, but my team is working hard to achieve it")
            os.system("python Jarvis-6th.py")
        elif 'how do you do' in query:
            print("     _____                       ")
            print("    /     \  - Well, I Am Fine   ")
            print("   |  * *  |                     ")
            print("    \_---_/                      ")
            print("      | |                        ")
            speak("well i am fine, how about you !")
            os.system("python Jarvis-6th.py")
        elif 'do you know siri' in query:
            speak("yes i know her, she is a good frend of mine, and she is made by Apple at silicon valley")
            os.system("python Jarvis-6th.py")
        elif 'do you know google assistant' in query:
            speak("yes i know him, he had a bad habit of crashing but now he is fine because of the great company developing it better every day just like me")
            os.system("python Jarvis-6th.py")

        # General Commands (Useful)

        elif 'call' in query:
            speak("sorry, but i may not be able to do that at the moment, but you can call by using google duo")
            command = "C:/Program Files (x86)/Microsoft Office/root/Office16/MSACCESS.EXE"
            subprocess.Popen(command)
            subprocess.Popen(command)
            speak("Please try and find the person you want to call")
            os.system("python Jarvis-6th.py")
        elif 'play music' in query:
            speak("sorry, i may not be able to do that at the moment, but you can enjoy the music by the "
                          "spotify app")
            os.system("python Jarvis-6th.py")
        elif 'wikipedia' in query:
            print("Searching")
            speak('Searching in Wikipedia...., please wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak("According to Wikipedia")
            speak(results)
            os.system("python Jarvis-6th.py")
        elif 'take a screenshot' in query:
            speak("Taking")
            image = pyautogui.screenshot()
            speak("please enter the name of the screenshot you want to save")
            image_name = input('Name of the shot:-')
            path = "E:/Screenshots by Jarvis/" + image_name + ".png"
            image.save(path)
            speak("screenshot taken, check your screenshot folder")
            os.system("python Jarvis-6th.py")
        elif 'where is' in query:
            playsound("on.mp3")
            print("Please Wait, I will Show you")
            speak('please wait, i can show you the place')
            place = query = query.replace("where is", "")
            url = "https://www.google.com/maps/place/" + str(place)
            webbrowser.open(url)
            results = wikipedia.summary(place, sentences=3)
            speak(results)
            os.system("python Jarvis-6th.py")
        elif 'what are you doing' in query:
            print("     _____                       ")
            print("    /     \ - Helping You!      ")
            print("   |  * *  |                     ")
            print("    \_---_/                      ")
            print("      | |                        ")
            speak("Just helping you, and my team is making me better and better eveyday at this task")
            os.system("python Jarvis-6th.py")
        elif "show the calendar" in query:
            root = Tk()
            root.title('Calender')
            root.geometry("600x400")
            cal = Calendar(root, selectmode = "day", year = 2020, month =11, day =14)
            cal.pack()
            mylabel = Label(root, text="")
            mylabel.pack()
            def grab_date():
                mylabel.config(text = "Today's date is" + cal.get_date())
            mybutton = Button(root, text ="Select Date", command = grab_date())
            mybutton.pack()
            root.mainloop()
            os.system("python Jarvis-6th.py")
        elif "what's today's date" in query:
            Current_Date = datetime.datetime.today()
            date = 'Today is', Current_Date
            print(date)
            speak(date)
            os.system("python Jarvis-6th.py")
        elif 'what is the time' in query:
            starTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir, the time is")
            print(starTime)
            speak(starTime)
            os.system("python Jarvis-6th.py")
        elif 'what is the definition of' in query:
            print("Got It")
            speak("finding, Please wait")
            define = query = query.replace("what is the definition of", "")
            print(dictionary.meaning(define, ))
            speak(dictionary.meaning(define))
            os.system("python Jarvis-6th.py")
        elif 'what is the synonym of' in query:
            print("Got It")
            speak("finding, Please wait")
            word = query = query.replace("what is the synonym of", "")
            print(dictionary.synonym(word, ))
            speak(dictionary.synonym(word))
            os.system("python Jarvis-6th.py")
        elif 'what is the antonym of' in query:
            print("Got It")
            speak("finding, Please wait")
            word = query = query.replace("what is the antonym of", "")
            print(dictionary.antonym(word, ))
            speak(dictionary.antonym(word))
            os.system("python Jarvis-6th.py")
        elif 'what is ' in query:
            print("Opening")
            speak("Please wait, i will search for you")
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia:")
            speak(results)
            speak("here are some links, please check them")
            query = query.replace("what is", "")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)
                query = query.replace(' ', '+')
                browser = webdriver.Chrome('chromedriver')
            for i in range(1):
                matched_elements = browser.get("https://www.google.com/search?q=" +
                                                   query + "&start=" + str(i))
            os.system("python Jarvis-6th.py")
                            
        elif 'browse the web for' in query:
            print("Opening")
            speak("Please wait, i will search for you")
            query = query.replace("browse the web for", "")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            query = query.replace(' ', '+')
            browser = webdriver.Chrome('chromedriver')
            for i in range(1):
                matched_elements = browser.get("https://www.google.com/search?q=" +
                                                query + "&start=" + str(i))
            os.system("python Jarvis-6th.py")
        elif 'search the web for' in query:
            print("Opening")
            speak("Please wait, i will search for you")
            query = query.replace("search the web for", "")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            query = query.replace(' ', '+')
            browser = webdriver.Chrome('chromedriver')
            for i in range(1):
                matched_elements = browser.get("https://www.google.com/search?q=" +
                                                query + "&start=" + str(i))
            os.system("python Jarvis-6th.py")
        elif 'why is ' in query:
            print("Opening")
            speak("Please wait, i will search for you")
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)
            query = query.replace(' ', '+')
            browser = webdriver.Chrome('chromedriver')
            for i in range(1):
                 matched_elements = browser.get("https://www.google.com/search?q=" +
                                                 query + "&start=" + str(i))
            os.system("python Jarvis-6th.py")

        # Opening Websites

        elif 'open youtube' in query:
            print("Opening....")
            speak("Opening, Please wait")
            webbrowser.open("https://www.youtube.com/")
            os.system("python Jarvis-6th.py")
        elif 'open edu sprint' in query:
            print("Opening....")
            speak("Opening, Please wait")
            webbrowser.open("http://thakur.edusprint.in/thakur/Portal/Default/IndexLite?_ca=1943187191")
        elif 'open stack overflow' in query:
            print("Opening....")
            speak("Opening, Please wait")
            webbrowser.open("https://stackoverflow.com/")
            os.system("python Jarvis-6th.py")
        elif 'open hot-star' in query:
            print("Opening....")
            speak("Opening")
            webbrowser.open("https://www.hotstar.com/in")
            os.system("python Jarvis-6th.py")
        elif 'open my coding website' in query:
            print("Opening....")
            speak("Opening")
            webbrowser.open("https://repl.it/")
            os.system("python Jarvis-6th.py")
        elif 'open python website' in query:
            print("Opening....")
            speak("Opening, Please wait")
            webbrowser.open("https://www.python.org/")
            os.system("python Jarvis-6th.py")
        elif 'open google drive' in query:
            print("Opening....")
            speak("Opening, Please wait")
            webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
            os.system("python Jarvis-6th.py")
        elif 'open google slides' in query:
            print("Opening....")
            speak("Opening, Please wait")
            webbrowser.open("https://docs.google.com/presentation/u/0/")
            os.system("python Jarvis-6th.py")
        elif 'open google docs' in query:
            print("Opening....")
            speak("Opening, Please wait")
            webbrowser.open("https://docs.google.com/document/u/0/")
            os.system("python Jarvis-6th.py")
        elif 'open google sheets' in query:
            print("Opening....")
            speak("Opening, Please wait")
            webbrowser.open("https://docs.google.com/spreadsheets/u/0/")
            os.system("python Jarvis-6th.py")
        elif 'open google earth' in query:
            print("Opening")
            speak("Opening, Please wait")
            webbrowser.open("https://earth.google.com/web/?authuser=0")
            os.system("python Jarvis-6th.py")
        elif 'open google play ' in query:
            print("Opening")
            speak("Opening, Please wait")
            webbrowser.open("https://play.google.com/?hl=en&authuser=0")
            os.system("python Jarvis-6th.py")
        elif 'open g mail' in query:
            print("Opening")
            speak("Opening, Please wait")
            webbrowser.open("https://mail.google.com/mail/?authuser=0")
            os.system("python Jarvis-6th.py")
        elif 'open google scholar' in query:
            print("Opening....")
            speak("Opening")
            webbrowser.open("https://scholar.google.com/")
            os.system("python Jarvis-6th.py")
        elif 'open google maps' in query:
            print("Opening")
            speak("Opening, Please wait")
            webbrowser.open("https://maps.google.co.in/maps?hl=en&tab=rl&authuser=0")
            os.system("python Jarvis-6th.py")
        elif 'open google news' in query:
            print("Opening")
            speak("Opening, Please wait")
            webbrowser.open("https://news.google.com/?tab=rn&authuser=0")
            os.system("python Jarvis-6th.py")
        elif 'open google duo' in query:
            print("Opening")
            speak("Opening, Please wait")
            webbrowser.open("https://duo.google.com/?usp=duo_ald")
            os.system("python Jarvis-6th.py")
        elif 'open google' in query:
            print("Opening....")
            speak("Opening, Please wait")
            webbrowser.open("https://www.google.com/")
            os.system("python Jarvis-6th.py")

        # Opening Apps

        elif 'open virtualbox' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files/Oracle/VirtualBox/VirtualBox.exe"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open powerpoint' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open excel' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open word' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open acces' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files (x86)/Microsoft Office/root/Office16/MSACCESS.EXE"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open outlook ' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files (x86)/Microsoft Office/root/Office16/OUTLOOK.EXE"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open webex' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files (x86)/Webex/Webex/Applications/ptoneclk.exe"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open zoom' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Users/rishi/AppData/Roaming/Zoom/bin/Zoom.exe"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open intelli j idea' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files/JetBrains/IntelliJ IDEA Community Edition 2020.2/bin/idea64.exe"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open telegram' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "A:/Telegram Desktop/Telegram.exe"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open whatsapp' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Users/rishi/AppData/Local/WhatsApp/WhatsApp.exe"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open microsoft edge ' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open mac fee' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files/Common Files/McAfee/Platform/McUICnt.exe"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open vs code' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Users/rishi/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open apple mail' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/Program Files (x86)/Common Files/Apple/Internet Services/iCloudWeb.exe mail"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")
        elif 'open turbo c ' in query:
            print("Opening....")
            speak("Opening, Please wait")
            command = "C:/TURBOC3/Turbo C++/"
            subprocess.Popen(command)
            os.system("python Jarvis-6th.py")

        # System Commands and Jarvis main commands

        elif 'disable Wi-Fi' in query:
            os.system("netsh interface set interface 'Wifi' disabled")
            speak("wi-fi disabled")
            os.system("python Jarvis-6th.py")
        elif 'read the screen' in query:
            image = pyautogui.screenshot()
            path = "E:/Screenshots by Jarvis/screen.png"
            image.save(path)
            image2 = Image.open('E:/Screenshots by Jarvis/screen.png')
            text = pytesseract.image_to_string(image2)
            print(text)
            speak(text)
            os.system("python Jarvis-6th.py")
        elif 'enable wi-fi' in query:
            os.system("netsh interface set interface 'Wifi' enabled")
            speak("wi-fi enabled")
            os.system("python Jarvis-6th.py")
        elif 'bluetooth devices' in query:
            nearby_devices = bluetooth.discover_devices(lookup_names=True)
            print("found %d devices" % len(nearby_devices))
            for name, addr in nearby_devices:
            print(" %s - %s" % (addr, name))
            os.system("python Jarvis-6th.py")
        elif 'exit' in query:
            print("     _____            ")
            print("    /     \  -> Bye !")
            print("   |  * *  |          ")
            print("    \_---_/           ")
            print("      | |             ")
            speak("I am closing myself, please restart me to speak to me again")
            playsound("off.mp3")
            sys.exit()
        elif 'close' in query:
            print("     _____            ")
            print("    /     \  -> Bye !")
            print("   |  * *  |          ")
            print("    \_---_/           ")
            print("      | |             ")
            speak("I am closing , nice talking with you")
            playsound("off.mp3")
            sys.exit()
        elif 'bye' in query:
            print("     _____            ")
            print("    /     \   -> Bye !")
            print("   |  * *  |          ")
            print("    \_---_/           ")
            print("      | |             ")
            speak("bye , take care")
            playsound("off.mp3")
            sys.exit()
        elif 'stop' in query:
            print("Stopped")
            speak("I am Paused, press any key to speak to me again")
            playsound("jarvis_beep.mp3")
            os.system("python Jarvis_with_wake.py")
        elif 'pause' in query:
            print("Stopped")
            speak("I am Paused, press any key to speak to me again")
            playsound("jarvis_beep.mp3")
            os.system('cls')
            os.system("python Jarvis_with_wake.py")
        elif 'hey jarvis' in query:
            print("     _____                    ")
            print("    /     \  -> Here for Help!")
            print("   |  * *  |                  ")
            print("    \_---_/                   ")
            print("      | |                     ")
            speak("here i am!")
            os.system("python Jarvis-6th.py")
        elif 'are you there' in query:
            print("     _____                    ")
            print("    /     \ -> Here for you!")
            print("   |  * *  |                  ")
            print("    \_---_/                   ")
            print("      | |                     ")
            speak("at your service sir")
            os.system("python Jarvis-6th.py")
        elif 'hello' in query:
            print("Hi")
            speak("hai")
        elif 'hai' in query:
            print("Hello")
            speak("Hello")
        elif 'hi' in query:
            print("Hello")
            speak("Hello")