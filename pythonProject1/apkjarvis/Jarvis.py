#from  kivy.app import MDApp
#from kivy.uix.screenmanager import screen
#from kivy.lang import Builder
import operator
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic import loadUiType
from JarvisUI import Ui_JarvisUI

import PyPDF2
import pyautogui
import pyttsx3
import requests
import bs4
from bs4 import BeautifulSoup
import speech_recognition as sr
import datetime
import os
import cv2
import pywikihow
from pywikihow import search_wikihow
import random

from instaloader import instaloader
from requests import get


import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
import time
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"good morning Mj, its {strTime} am")

    elif hour > 12 and hour < 18:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"good afternoon Mj, it's {strTime} pm")
    else:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"good evening Mj, it's {strTime} pm")

    speak("I am jarvis. please tell me how can I assist you ")


#def sendEmail(to, content):
 #   from xmlrpc import server
 #   server.ehlo()
 #   server.starttls()
 #   server.login('emailid@gmail.com', 'Password')
 #   server.send('emailid@gmail.com', to, content)
 #   server.close()


def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=5c7efe1feacf4425801b012e3497b431"

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is:{head[i]}")


def pdf_reader():
    book = open('OOPS.pdf', 'rb')
    reader = PyPDF2.PdfFileReader(book)
    pages = reader.numPages
    print(reader.documentInfo)
    speak(f"Total number of pages in this book {pages} ")
    speak("MJ please enter the pages number i have to read")
    pg = int(input("please enter the page number: "))
    page = reader.getPage(pg)
    texts = page.extractText()
    speak(texts)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold = 2
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"{self.query}")

        except Exception as e:
            # speak("Say that again please...")
            return "none"
        self.query = self.query.lower()
        return self.query


    def TaskExecution(self):
        wish()

        while True:

            self.query = self.takeCommand().lower()

            if "open notepad" in self.query:
                npath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)

            elif "close notepad" in self.query:
                speak("okay mj, closing notepad")
                os.system("taskkill/f /im notepad.exe")

            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "close adobe reader" in self.query:
                speak("okay mj, closing adobe reader")
                os.system("taskkill/f /im AcroRd32.exe")


            elif "open excel" in self.query:
                epath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(epath)

            elif "close excel" in self.query:
                speak("okay mj, closing adobe reader")
                os.system("taskkill/f /im EXCEL.EXE")

            elif "open word" in self.query:
                wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(wpath)

            elif "close  word" in self.query:
                speak("okay mj, closing adobe reader")
                os.system("taskkill/f /im WINWORD.EXE")

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "close  command prompt" in self.query:
                speak("okay mj, closing command prompt")
                os.system("taskkill/f /im cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                music_dir = "E:\\Songs"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching on wikipedia")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=5)
                speak("according to wikipedia")
                speak(results)
            # print(results)

            elif "the time" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Mj, the time is {strTime}")

            elif "open youtube" in self.query:
                speak("mj, what should I search on youtube")
                dm = self.takeCommand().lower()
                webbrowser.open(f"https://www.youtube.com/results?search_query={dm}")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("mj, what should I search on google")
                cm = self.takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif "send message " in self.query:
                speak("mj, what message I am send")
                wm = self.takeCommand().lower()
                pywhatkit.sendwhatmsg("+919382454167", f"{wm}", 8, 25)

            # elif "email to atul" in self.query:
            #    try:
            #        speak("what should I say?")
            #        content = takeCommand().lower()
            #         to = "sendto@gmail.com"
            #         sendEmail(to, content)
            #         speak("Email has been sent to Atul")
            #     except Exception as e:
            #         print(e)
            #     speak("sorry, I am not able to send this mail to atul")

            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 23:
                    music_dir = 'E:\\Songs'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif " tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif " shut down the system" in self.query:
                os.system("shutdown/s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powerprof.dll,SetSuspend 0,1,0")


            elif "you can sleep" in self.query:
                speak("thanks for using me mj, have a good day")
                break

            elif "activate how to do mode" in self.query:
                speak("how to do mode is activated")
                while True:
                    speak("please tell me what you want to know")
                    how = self.takeCommand()
                    try:
                        if "exit" in how or "close" in how:
                            speak("okay MJ, How to do mode is closed")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("Sorry Mj, I am not able to find")



            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me today's news" in self.query:
                speak("wait Mj, fetching the latest news")
                news()

            elif "temperature" in self.query:
                search = "temperature in Mohali"
                url = f"https://www.google.com/search?q={search}"
                m = requests.get(url)
                data = BeautifulSoup(m.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current  {search} is {temp}")


            elif "email to atul" in self.query:
                speak("sir what should i say")
                self.query = self.takeCommand().lower()
                if "send a file " in self.query:
                    email = 'mjpython09@gamil.com'
                    speak("MJ, Please enter your password")
                    password = input(str("please enter your password: "))
                    send_to_email = 'atulthakur2802@gmail.com'
                    speak("okay mj, what is the subject for this email")
                    self.query = self.takeCommand().lower()
                    subject = self.query
                    speak("and Mj, what is the message for this email")
                    self.query2 = self.takeCommand().lower()
                    message = self.query2
                    speak("Mj please enter the correct path file into the shell")
                    file_location = input("please enter the path here: ")
                    speak("please wait , I am sending email now")
                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-steam')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                    msg.attach(part)
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("Mj, email has been sent to atul")
                else:
                    email = 'mjpython09@gmail.com'
                    speak("MJ, Please enter your password")
                    password = input(str("please enter your password: "))
                    send_to_email = 'atulthakur2802@gmail.com'
                    message = self.query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("Mj, email has been sent to Atul")

            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait mj, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"Mj i am not sure , but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry mj, Due to network issue i am not able to find where we are")
                    pass

            elif "instagram profile" in self.query or "profile in instagram" in self.query:
                speak("mj please enter the user name")
                name = input("enter user name here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"mj here is the profile of user {name}")
                time.sleep(5)
                speak("Mj would you like to download profile picture of this account")
                condition = self.takeCommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done mj, profile picture is saved in our folder, now i am ready for next command")
                else:
                    pass



            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("mj , please tell me the name for this screenshot file")
                name = self.takeCommand().lower()
                speak("mj please hold  the screen for few seconds, i am taking screen short")
                time.sleep(5)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done mj, the screenshot is saved in our pc, , now i am ready for next command")

            elif "read book" in self.query:
                pdf_reader()



            elif "do some calculation" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("listening....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided': operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                speak("result is")
                speak(eval_binary_expr(*(my_string.split())))

            elif "hide all files" in self.query or "hide this folder" in self.query or " visible for everyone" in self.query:
                speak("Mj please tell me want hide this folder or make it visible for everyone ")
                condition = self.takeCommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("Mj all file in folder are now hidden.")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("Mj all file in folder are now visible to everyone.")

                elif "leave it" in condition or "leave for now" in condition:
                    speak("ok Mj")

            speak("mj, do you have any other work")


statExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/Downloads/MJ.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/Downloads/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        statExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = now.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
Jarvis = Main()
Jarvis.show()
exit(app.exec_())

