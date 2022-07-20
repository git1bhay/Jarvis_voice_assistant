from ast import operator
from asyncio import Task
from ctypes.wintypes import HGDIOBJ
from email.mime import audio
from multiprocessing.context import SpawnContext
from re import search
import sys
import operator
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import PyPDF4
import os
import requests
import pyautogui
import wolframalpha
from bs4 import BeautifulSoup
import wikipedia
import pyjokes
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
from QTGUI import Ui_gui1
import AI


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[1].id)
# text to speech


def Speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        Speak("Good Morning")

    elif hour > 12 and hour < 18:
        Speak("Good Afternoon")

    else:
        Speak("Good Evening")

    Speak("I am jarvis sir. please tell me how can i help you ")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExe()
    # To convert voice into text

    def takecommand(self):
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            command.pause_threshold = 1
            command.energy_threshold = 3500
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio, language='en-in')
                print(f"You said : {query}\n")

            except Exception as Error:
                Speak("Say that again please.......")
                return "none"

            return query.lower()
    #Speak("hello sir i am jarvis")

    def TaskExe(self):

        def celcius():
            search = "temperature in jabalpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            Speak(f"The temperature Outside is {temperature} celcius")

        def pdf_reader():
        
            book = open('h.pdf',"rb")
            pdfReader = PyPDF4.PdfFileReader(book)  # pip install PyPDF2
            pages = pdfReader.numPages
            Speak(f"Total numbers of pages in this book {pages}")
            Speak("sir please enter the page number i have to read")
            pg = int(input("Please enter the page number: "))
            page = pdfReader.getPage(pg)
            text = page.extractText()
            Speak(text)

        def Whatsapp():
            Speak("Tell Me The Name Of the Person!")
            Speak("Tell Me The Message!")
            msg = self.takecommand()
            Speak("Tell Me The Time Sir!")
            Speak("Time In Hour!")
            hour = int(self.takecommand())
            Speak("Time In Minutes!")
            min = int(self.takecommand())
            pywhatkit.sendwhatmsg("+918103334932", msg, hour, min, 20)
            Speak("Ok Sir, Sending Whatsapp Message!")

        wish()

        while True:

            self.query = self.takecommand()

            if 'who are you' in self.query:
                Speak("Hello sir,I Am Jarvis. ")
                Speak("You Personal Ai Assistant! ")
                Speak("How May I Help You?")

            elif 'google search' in self.query:

                query = self.query.replace('google search', '')
                Speak('searching on google')
                webbrowser.open("https://www.google.com/search?q="+query+"&rlz=1C1CHZN_enIN949IN949&oq="+query +
                                "&aqs=chrome..69i57j0i131i433j0i433j0i131i433l3j0i433j0i131i433j0i433j0.2513j0j15&sourceid=chrome&ie=UTF-8")

            elif 'where is' in self.query:
                query = self.query . replace('where is', '')
                location = query
                Speak('serching' ""+location+"" 'on maps')
                webbrowser.open("https://www.google.co.in/maps/place/" + location + '')
                Speak("Serching" + location)

            # switch the window
            elif "switch the window" in self.query or "switch window" in self.query:
                Speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")

            elif 'read book' in self.query or 'read pdf' in self.query:
                pdf_reader()
                    

            elif 'current time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                Speak(strTime)
                Speak(f"Sir, the time is {strTime}")

            elif 'what is' in self.query or "who is" in self.query:
                client = wolframalpha.Client("35T67T-PJR6LQ659T")
                rec = client.query(self.query)
                try:
                    print(next(rec.results).text)
                    Speak(next(rec.results).text)
                except StopIteration:
                    print("No results")

            elif "send message" in self.query:
                Whatsapp()

            elif 'website' in self.query:
                Speak("Ok Sir Launching.....")
                query = self.query.replace("website", "")
                web1 = self.query.replace("open", "")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                Speak("Launched!")

            elif 'Launch' in self.query:
                Speak("Tell Me The name of  the Website!")
                name = self.takecommand()
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                Speak("Done Sir!")

            elif 'facebook' in self.query:
                Speak("Ok Sir!")
                webbrowser.open("https://www.facebook.com")
                Speak("Ok Sir....")
            
            elif 'open java point' in self.query:
                Speak("Ok Sir!")
                webbrowser.open("https://www.javatpoint.com")
                Speak("Ok Sir....")

            elif 'youtube search' in self.query:
                Speak("Ok Sir, This is What I found for Search!")
                query = self.query.replace("jarvis", "")
                query = self.query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(web)
                Speak("Done Sir")

            elif 'open stack overflow' in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif 'play music' in self.query:
                music = 'E:\\Music'
                songs = os.listdir(music)
                os.startfile(os.path.join(music, songs[0]))

            elif 'wikipedia' in self.query:
                Speak("Searching wikipedia.....")
                query = query.replace("wikipedia", "")
                wiki = wikipedia.summary(query, 2)
                print(wiki)
                Speak(f"According to wikipedia : {wiki}")

            elif "temperature" in self.query:
                celcius()

            elif 'open cmd' in self.query:
                os.system('start cmd')

            elif 'open notepad' in self.query:
                npath = 'C:\\Windows\\system32\\notepad.exe'
                os.startfile(npath)

            elif 'close notepad' in self.query:
                Speak("OK sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif 'open Adobe' in self.query:
                npath = 'C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe'
                os.startfile(npath)

            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                Speak(joke)

            elif 'how are you' in self.query:
                Speak("I Am Fine Sir!")
                Speak("What About You?")

            elif 'what is my name' in self.query:
                Speak("Your name is Abhay soni")

            elif 'what is your name' in self.query:
                Speak("My good name Jarvis Assistant, my good game,helping you")

            #######################################################################################################################
            #######################################################################################################################

            elif "do some calculationns" in self.query or "can you calculate" in self.query:
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        Speak("Say What you want to calculate, example : 3 plus 3")
                        print("Listening......")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)

                    def get_operator_fn(op):
                        return {
                            '+': operator.add,  # plus
                            '-': operator.sub,  # minus
                            'x': operator.mul,  # multiplied by
                            'divided': operator.__truediv__,  # divided
                        }[op]

                    def eval_binary_expr(op1, oper, op2):  # 5 plus 8
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    Speak("your result is")
                    Speak(eval_binary_expr(*(my_string.split())))

                except Exception as error:
                    Speak("try again")
                    return "none"

                ##################################################################################################################

            elif 'you need a break' in self.query:
                Speak("Ok Sir,You Call Me Anytime !")
                break


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_gui1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie(
            "C:\\Users\\DELL\\AppData\\Roaming\\Python\\Python39\\Scripts\\Jarvis_Gui (2).gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie(
            "C:\\Users\DELL\\AppData\\Roaming\\Python\Python39\\Scripts\\Iron_Template_1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
AI = Main()
AI.show()
exit(app.exec_())


'''query = takecommand()

if 'hello ' in query:
    Speak("hello sir")

else:
    Speak("no command found")'''
