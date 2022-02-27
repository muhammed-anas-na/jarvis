from logging import exception
from sys import exec_prefix
from cv2 import EVENT_FLAG_SHIFTKEY, THRESH_MASK, SparsePyrLKOpticalFlow, imshow, rectify3Collinear
from jinja2.tests import test_integer
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
from geopy.geocoders import Nominatim
import random
import whatsapp
import email_sender
import pyautogui
from datetime import date
import speedtest
import platform
import subprocess
from instabot import Bot
import pdfplumber
from PyPDF2 import PdfFileReader
from keyboard import press, press_and_release
import time
from cv2 import extractChannel
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

my_name = Your Name
password = password

# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
person = 0


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 0 and hour < 12:
        greeting_morning = [
            ["Hello there"],
            ["Good Morining sir"],
        ]
        import random
        random_number = random.randint(0, len(greeting_morning))
        speak(greeting_morning[random_number])

        StrTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("The time is " + StrTime)
        speak(f"It's {StrTime} morning")

    elif(hour >= 12 and hour < 18):
        speak(f"Good afternooon")

        StrTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("The time is " + StrTime)
        speak(f"It's {StrTime} afternoon")
    else:
        speak(f"Good evening {my_name}")
        StrTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("The time is " + StrTime)
        speak(f"It's {StrTime} evening")

    speak("How can I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listerning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recoganizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said :" + query)

    except Exception as e:

        # print(e)
        print("Say that again")
        speak("What do you mean")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # LOGIC EXECUTING TASK
        if 'wikipedia' in query:
            try:

                query = query.replace("wikipedia", "")
                query = query.replace("Search", "")
                query = query.replace("Jarvis", "")
                query = query.replace("can", "")
                query = query.replace("you", "")
                query = query.replace('-', "")
                speak(f"Searching {query} in  Wikipedia")
                print(query)
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak("According to wikipedia")
                speak(results)
            except:
                speak(f"Sorry sir I could not find {query} in wikipedia")

        elif 'chrome' in query:  # chrome should be open in you screen to execture this commands
            if 'new tab' in query:
                speak("Opening new tab in chrome")
                press_and_release('ctrl+t')
            elif 'new window' in query:
                speak("New window in chrome")
                press_and_release('ctrl+n')
            elif 'open closed tabs' in query:
                speak("Opening recently closed tabs")
                press_and_release('ctrl + shift + t')
            elif 'switch tab' in query or 'change tab' in query:
                speak("Which tab should i switch?")
                tab_no = takeCommand()
                if '1' in tab_no or 'one' in tab_no:
                    press_and_release('ctrl + 1')
                elif '2' in tab_no or 'two' in tab_no:
                    press_and_release('ctrl + 2')
                elif '3' in tab_no or 'three' in tab_no:
                    press_and_release('ctrl + 3')
                elif '4' in tab_no or 'four' in tab_no:
                    press_and_release('ctrl + 4')
                elif '5' in tab_no or 'five' in tab_no:
                    press_and_release('ctrl + 5')
                elif '6' in tab_no or 'six' in tab_no:
                    press_and_release('ctrl + 6')
                else:
                    speak("No tab found")
            elif 'close this tab' in query:
                speak("Closing this tab")
                press_and_release('ctrl + w')
            elif 'close this window' in query:
                speak("Closing this window")
                press_and_release('ctrl + shift + w')
            elif 'minimize' in query or 'minimise' in query:
                speak("Minimizing chrome")
                press_and_release('alt + space')
                press('n')
            elif 'maximise' in query or 'maximize' in query:
                speak("Maximizing chrome")
                press_and_release('alt + space')
                press('x')
            elif 'quit' in query or 'exit' in query or 'kill' in query:
                speak("Quitting chrome")
                press_and_release('alt + f4')
            elif 'menu' in query:
                speak("Menu")
                press_and_release('alt + f')
            elif 'bookmark' in query or 'book mark' in query:
                speak("Opening bookmark tab")
                press_and_release('ctrl + shift + b')
            elif 'bookmark manager' in query or 'book mark manager' in query:
                speak("Opening bookmart manager")
                press_and_release('ctrl + shift + o')
            elif 'history' in query:
                speak("Opening history")
                press_and_release('ctrl + h')
            elif 'download' in query:
                speak("Opening downloads")
                press_and_release('ctrl + j')
            elif 'task manager' in query:
                speak("Chrome task manager")
                press_and_release('shift + esc')
            elif 'developers tool' in query:
                speak("Opening developers tool")
                press_and_release('ctrl+shift+j')
            elif 'clear data' in query:
                speak("Clear data here")
                press_and_release("ctrl + shift + delete")
            elif 'print' in query:
                speak("Print this page here")
                press_and_release('ctrl + p')
            elif 'reload' in query:
                speak("Reloading please wait")
                press_and_release('ctrl + r')
            elif 'fullscreen' in query or 'full screen' in query:
                speak("opening full screen")
                press_and_release('f11')
            elif 'source code' in query:
                speak("Opening source code")
                press_and_release('ctr; + u')

        elif 'close' in query:
            query = query.replace("close", "")
            print(query)
            if 'vs code' in query:
                speak("Closing vs code")
                os.system('TASKKILL /F /IM code.exe')
            elif 'cmd' in query or 'command prompt' in query:
                speak("Closing command prompt")

                os.system('TASKKILL /F /IM cmd.exe')
            elif 'chrome' in query:
                speak("Closing chrome")
                os.system('TASKKILL /F /IM chrome.exe')
            elif 'facebook' in query:
                speak("Closing facebook")
                os.system('TASKKILL /F /IM chrome.exe')
            elif 'whatssapp' in query:
                speak("Closing whatssapp")
                os.system('TASKKILL /F /IM chrome.exe')
            elif 'google' in query:
                speak("Closing google")
                os.system('TASKKILL /F /IM chrome.exe')
            elif 'youtube' in query:
                speak("Closing youtube")
                os.system('TASKKILL /F /IM chrome.exe')
            elif 'instagram' in query:
                speak("Closing instagram")
                os.system('TASKKILL /F /IM chrome.exe')
            elif 'music' in query:
                os.system('TASKKILL /F /IM vlc.exe')
        elif 'open chrome' in query:
            speak("Opening chrome please wait")
            os.startfile(
                'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

        elif 'thank you' in query:
            import random
            replays = [
                ["You're welcome"],
                ["No problem"],
                ["Don't mention it"],
                ["My pleasure"],
                ["It was the least I could do."]
            ]

            random_number = random.randint(0, len(replays))
            speak(replays[random_number])
        elif 'open youtube' in query:
            speak("Opening youtube. Please wait")
            webbrowser.open('https://www.youtube.com')
        elif 'open google earth' in query:
            speak("Opening google earth")
            webbrowser.open('https://earth.google.com/web/')
        elif 'open google' in query:
            speak("Opening Google. Please wait")
            url = "https://www.google.com"
            webbrowser.open(url)
        elif 'open leetcode' in query:
            speak("Opening leetcode. Please wait")
            webbrowser.open('https://www.leetcode.com')
        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow. Please wait")
            webbrowser.open('https://www.stackoverflow.com')
        elif 'the time' in query:
            StrTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("The time is " + StrTime)
            speak("The time is " + StrTime)
        elif 'vs code' in query:
            speak("Opening vscode")
            url = "C:\\Users\\Admin\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(url)
        elif 'camera' in query:
            speak("Opening webcam. Please wait")

            webcam = cv2.VideoCapture(0)
            speak("Press Q to exit")
            while True:
                sucess_frame_rate, frame = webcam.read()
                imshow('webcam', frame)

                key = cv2.waitKey(1)
                if key == 81 or key == 113:
                    break
                command = takeCommand()

                if 'close' in command:
                    speak("Closing camera")
                    break
            webcam.release()
        elif 'shutdown' in query or 'shut down' in query or 'kill' in query:
            speak("Ok Sir, You can call me anytime!")
            speak("Just say wake up jarvis")
            os.startfile("C:\\Users\\Admin\\Music\\jarvis\\wake_up.py")
            break
        elif 'weather' and 'around' in query:
            speak("Searching weather details near you. Please wait Sir")
            import weather_details
            details = weather_details.weather(Your place)
            speak(f"Details of the place {details[0]}")
            speak(f"It's {details[1]} ")
            speak(f"The weather at pattimattom looks like {details[2]}")
            speak(f"It looks like it's {details[3]} °Celcius")
        elif 'cmd' in query or 'command prompt' in query:
            os.startfile(
                "C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt")
        elif 'check ' and 'instagram message' in query:
            path = "chromedriver"
            driver = webdriver.Chrome(path)
            try:
                driver.get('https://www.instagram.com/')
                speak("Opening instagram please wait")
                time.sleep(6)
                user_bar = driver.find_element_by_name('username')
                user_bar.clear()
                user_bar.send_keys(Your Instagram Username)
                pass_bar = driver.find_element_by_name('password')
                pass_bar.clear()
                pass_bar.send_keys(Your Instagam password)

                pass_bar.send_keys(Keys.RETURN)
                speak("Loggin into your account please wait")
                time.sleep(5)
                messages = driver.find_element_by_class_name('bqXJH')
                print(messages.text)

                if messages.text == 0:
                    speak("You are all catched up sir")
                else:
                    print("you have new message")
                    speak(f"You have messges from {messages.text} account")
                    speak("Do you want me to open it sir ?")
                    command = takeCommand()
                    if 'yes' in command:
                        driver.get('https://www.instagram.com/direct/inbox/')
                        print("Done")
                    else:
                        driver.quit()
            except:
                speak("Sorry sir i couldn't reach your account")

        # command : whatsapp message to friend Name
        elif 'whatsapp message' in query:
            query = query.replace("jarvis", "")
            query = query.replace("please", "")
            query = query.replace("send", "")
            query = query.replace("whatsapp", "")
            query = query.replace("message", "")
            query = query.replace("to", "")
            query = query.replace(" ", "")
            print(query)
            name = query
            if 'Friend Name 01' in name:
                number = "Friend Number"
                speak(f"What is the message for {name}")
                message = takeCommand()
                speak(
                    f"Sir please wait opening whatssapp and sending message to {name}")
                whatsapp.whatsapp(number, message)
            elif 'Friend Name 02' in name:
                number = "Friend Number"
                speak(f"What is the message for {name}")
                message = takeCommand()
                speak(
                    f"Sir please wait opening whatssapp and sending message to {name}")
                whatsapp.whatsapp(number, message)
            else:
                speak(f"Sorry sir I couldn't find {name} in your contact list")
        elif 'weather' in query:
            print("Please mention the place. example: weather at delhi")
            speak("Please mention the place. example: weather at delhi")
            place = takeCommand()
            place = place.replace("weather", "")
            place = place.replace("at", "")
            place = place.replace(" ", "")
            print(f"Searching weather details of {place}")
            speak("Searching weather details of " + place)
            import weather_details
            place = place + " weather"
            details = weather_details.weather(place)
            speak(f"Details of the place {details[0]}")
            speak(f"It's {details[1]} ")
            speak(f"The weather at {place} looks like {details[2]}")
            speak(f"It looks like it's {details[3]} °Celcius")
        elif 'where am i' in query:

            loc = Nominatim(user_agent="GetLoc")
            getLoc = loc.geocode("Your place")
            print(getLoc.address)
            speak(getLoc.address)
        elif 'activate how to do mode' in query:
            from pywikihow import search_wikihow
            speak("How to do mode is activated")
            while True:
                speak("please tell me what to do?")
                how = takeCommand()
                try:
                    if 'close' in how or 'exit' in how:
                        speak("Ok sir, How to do mode is closed")
                        break
                    else:
                        max_result = 1
                        how_to = search_wikihow(how, max_result)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except exception as e:
                    speak("Sorry sir, I am not able to find this")
        elif 'music' in query:
            speak("OK sir")
            music_dir = "C:\\Users\\Admin\\Pictures\\Music"
            songs = os.listdir(music_dir)
            random_number = random.randint(0, 4)
            print("Playing {songs[random_number]}")
            player = os.startfile(os.path.join(
                music_dir, songs[random_number]))
        # command : Instagram message to friend Name
        elif 'instagram message' in query:
            bot = Bot()
            query = query.replace("jarvis", "")
            query = query.replace("send", "")
            query = query.replace("instagram message", "")
            query = query.replace("to", "")
            query = query.replace(" ", "")
            print(query)
            speak("Logging into your account please wait")
            if 'Friend Name 01' in query:
                speak("This may take time depending on your internet speed")
                bot.login(username="Your UserName",
                          password= "Your Password")
                urer_ids = ["Friend 01 Instagram Id"]
                speak("What should I say?")
                text = takeCommand()
                bot.send_messages(text, urer_ids)
                speak(f"Message send to {query}")
            elif 'Friend Name 02' in query:
                speak("This may take time depending on your internet speed")
                bot.login(username="Your UserName",
                          password="Your Password")
                urer_ids = ["Friend 02 Instagram Id"]
                speak("What should I say?")
                text = takeCommand()
                bot.send_messages(text, urer_ids)
                speak(f"Message send to {query}")
            else:
                speak(f"sorry sir I couldn't find {query}")
        # Command : send email to friend Name
        elif 'email' in query:
            name = query.replace("jarvis", "")
            name = name.replace("send email", "")
            name = name.replace("to", "")
            name = name.replace("please", "")
            name = name.replace(" ", "")

            speak("What is the subject sir?")
            subject = takeCommand()
            speak("What should i say?")
            content = takeCommand()

            print(name)
            print(subject)
            print(content)
            if 'Friend Name 01' in name:
                email = "example@gmail.com"
                email_sender.sendmail(subject, content, email)
                speak("Email send to Friend 01")
            elif 'Friend Name 02' in query:
                email = "example1@gmail.com"
                email_sender.sendmail(subject, content, email)
                speak("Email send to Friend 02")
            else:
                speak(f"Sorry sir could not find {name} in your contact list")
        elif 'ip address' in query:
            # Python Program to Get IP Address
            import socket
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your Computer IP Address is:" + IPAddr)
            speak(f"Your computers ip adress is {IPAddr}")
        elif 'volume up' in query:
            pyautogui.press('volumeup')
        elif 'volume down' in query:
            pyautogui.press('volumedown')
        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press('volumemute')
        #Command : Search python in youtube
        elif 'youtube' in query:
            query = query.replace("jarvis", "")
            query = query.replace("search", "")
            query = query.replace("in", "")
            query = query.replace("youtube", "")
            query = query.replace("on", "")
            query = query.replace(" ", "")
            print(query)
            speak(f"Searching {query} in youtube")
            url = "https://www.youtube.com/results?search_query="+query
            webbrowser.open(url)

        elif 'nasa news' in query:
            import nasa

            today = date.today()
            print(today)
            data = nasa.nasaNews(today)
            speak("Here is what i found from nasa")
            print(data['title'])
            print(data['explanation'])
            speak(f"Title of today's new is{data['title']}")
            speak(data['explanation'])
        # Command : search python in google
        elif 'google' in query:
            query = query.replace("search", "")
            query = query.replace("on", "")
            query = query.replace("google", "")
            query = query.replace(" ", "+")
            speak("Searching on google please wait")
            url = f"https://www.google.com/search?q={query}&rlz=1C1VDKB_enIN979IN979&sxsrf=AOaemvK6YmRBaHpic6DfVtXGS1g6yZnYJw%3A1639760209662&ei=UcG8YYPmJ4KTseMPl7K3qAQ&ved=0ahUKEwjD0sDmpuv0AhWCSWwGHRfZDUUQ4dUDCA4&uact=5&oq=google+hi&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAELEDEJECMggIABCxAxCRAjILCAAQsQMQgwEQkQIyEAgAEIAEEIcCELEDEIMBEBQyBQgAEIAEMgUIABCABDIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjELADECc6BwgAEEcQsAM6CgguEMgDELADEEM6BAgjECc6BQgAEJECOgsIABCABBCxAxCDAToKCAAQgAQQhwIQFEoECEEYAEoECEYYAFCTBVicCWD6C2gBcAJ4AIAB5QGIAYoEkgEFMC4yLjGYAQCgAQHIAQzAAQE&sclient=gws-wiz"
            webbrowser.open(url)
        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            speak("Checking your download speed")
            download_speed = st.download()
            print(f"Your download speed is {download_speed}")
            speak(f"Your download speed is {download_speed}")
            speak("Checking your upload speed")
            upload_speed = st.upload()
            print(f"and your upload speed is {upload_speed}")
            speak(f"and your upload speed is {upload_speed}")
        elif 'system info' in query:
            my_system = platform.uname()
            print(f"System: {my_system.system}")
            print(f"Node Name: {my_system.node}")
            print(f"Release: {my_system.release}")
            print(f"Version: {my_system.version}")
            print(f"Machine:{my_system.machine}")
            print(f"Processor: {my_system.processor}")
            # Speak
            speak(f"System: {my_system.system}")
            speak(f"Node Name: {my_system.node}")
            speak(f"Release: {my_system.release}")
            speak(f"Version: {my_system.version}")
            speak(f"Machine:{my_system.machine}")
            speak(f"Processor: {my_system.processor}")
        elif 'screenshot' in query or 'screen shot' in query:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(
                r'C:\Users\Admin\Pictures\Saved Pictures/image.jpg')
            speak("Screen shot save in saved pictures")
        elif 'signin' in query or 'sign in' in query:
            speak("Welcome sir")
            person = person+1
        elif 'logout' in query or 'log out' in query:
            speak("Logged out sir")
            person = person-1
        elif "room" in query:
            speak(f"There are {person} persons signed in")
        elif 'describe' in query:
            speak("Hello I am Jarvis. I am your personal assistance.")
        elif 'pdf' and 'detail' in query:
            speak("Finding details please wait")

            def extract_information(pdf_path):
                with open(pdf_path, 'rb') as f:
                    pdf = PdfFileReader(f)
                    information = pdf.getDocumentInfo()
                    number_of_pages = pdf.getNumPages()

                txt = f"""
                Information about {pdf_path}: 

                Author: {information.author}
                Creator: {information.creator}
                Producer: {information.producer}
                Subject: {information.subject}
                Title: {information.title}
                Number of pages: {number_of_pages}
                """

                print(txt)

                speak(txt)
                return information

            if __name__ == '__main__':
                path = '0 to 1.pdf'
                extract_information(path)
        elif 'my name' in query:
            speak("Your name is ______")
        elif 'read' in query:
            query = query.replace("jarvis", "")
            query = query.replace("read", "")

            if '021' in query or 'zero to one' in query:
                pdf = PdfFileReader('0 to 1.pdf')
                pages = pdf.getNumPages()
                print(pages)
                with pdfplumber.open(r'0 to 1.pdf') as pdf:
                    speak("Reading zero to one")

                    for i in range(pages):
                        first_page = pdf.pages[i]
                        print(first_page.extract_text())
                        speak(first_page.extract_text())
            else:
                speak(
                    "Sorry sir I couln't find {query} in your library. Please download it sir")
        elif 'how are you' in query:
            speak("I am fine sir")
            speak("How about you ?")
            command = takeCommand()
            if 'not fine' in command or 'bad' in command or 'not good' in command or 'bad day' in command:
                speak("Sorry to hear about you sir")
                speak("should i play some music sir?")
                command = takeCommand()
                if 'yes' in command or 'play' in command or 'ok' in command:
                    music_dir = "C:\\Users\\Admin\\Pictures\\Music"
                    songs = os.listdir(music_dir)
                    random_number = random.randint(0, 4)
                    print("Playing {songs[random_number]}")
                    player = os.startfile(os.path.join(
                        music_dir, songs[random_number]))
                else:
                    speak("Ok sir")
            else:
                speak("Happy to hear that sir")
        elif 'jokes' in query or 'joke' in query:
            jokes = [
                "What is the most shocking city in the world",
                "Why don't some couples go to gym?",
                "Why are cricket stadium so cool?",
                "What movie should you watch on a dineer date ?  ",
                "Where do cauliflower hangout? ",
                "What did the cow say when it wanted to watch a film? ",
                "What did one shark say to the other while eating a clownfish ? ",
                "Did you hear about the new anti-gravity book ",
                "Chintu to his mother : 'Amma, can I watch more TV' ",
                "Did you know that all clouds have dandruff?",
                "Why did the banker switch carrer ?",
                "The right eye said to the left eye",
                'Whats invisible and smells like carrots?',
                "Can a kangaroo jump higher than the house ?"
            ]

            answer = [
                "Electricity ⚡",
                "Because some relationships don't workout 💪🏻",
                "Because eveery seat has fan on it 🎊",
                "Kabhi Sushi Kabhie Rum",
                "The Gobi Desert!",
                " Let's go to the moovies!",
                "This tastes funny",
                "Apparently you can't put it down 📙",
                "Amma : Only if you don't turn it on",
                "That's where snowflakes come from",
                "She lost interest"
                "between you and me something smells 👃🏻",
                "Bunny farts 🐰 ",
                "Of course! Houses can't jump 🏡",
            ]
            import random
            random_number = random.randint(0, len(jokes))
            print(random_number)
            print(jokes[random_number])
            speak(jokes[random_number])
            print(answer[random_number])
            speak(answer[random_number])
        elif 'tongue twister' in query:
            twisters = [
                "Shy shelly says she shall sew sheets",
                "I thought a thought. But the thought I thought wasn't the thought I thought I thought. If the thought I thought has been the thought I thought, I wouldn't have thought so much",
                "Betty Botter bought a bit of butter But ,she said,this butter's bitter. It will make my batter better. So she bought a bit of butter. Better than her bitter butter. And made ner bitter batter better",
                "Kishan saw a kitten eating a chicken in the kitchen",
                "Shyam's shop stocks short spotted socks",
                "Pink's papa picked a pink papaya to pickle",

            ]

            random_number = random.randint(0, len(twisters))
            print(random_number)
            print(twisters[random_number])
            speak(twisters[random_number])
        elif 'play a game' in query:
            speak("Alright which one you like to try")
            print("1 : Bottle shoot")
            print("2 : Slap fest")
            print("3 : Rocket man")
            speak("Bottle shoot")
            speak("Slap fest")
            speak("Rocket Man")
            while True:
                command = takeCommand()
                if 'exit' in command or 'close' in command:
                    speak("Exiting from games")
                    break
                elif 'Bottle shoot' in command or '1' in command or 'one' in command:
                    speak("Opening bottle shoot")
                    webbrowser.open(
                        'https://www.gamezop.com/g/B1fSpMkP51m?id=cfuucl7YgA&lang=en')
                elif 'slap fest' in command or '2' in command or 'two' in command:
                    speak("Opening slap fest")
                    webbrowser.open(
                        'https://www.gamezop.com/g/ryN9EGAQa?id=cfuucl7YgA&lang=en')
                elif 'rocket man' in query or '3' in query or 'three' in query:
                    speak("Opening rocket man")
                    webbrowser.open(
                        'https://www.gamezop.com/g/SyXuN7W1F?id=cfuucl7YgA&lang=en')
                else:
                    speak("Sorry the game you said is not corrently avalible")
                    speak("Please select a avalible game")
        elif 'login' and 'instagram' in query:
            try:
                path = "chromedriver"
                driver = webdriver.Chrome(path)
                driver.get('https://www.instagram.com/')
                speak("Opening instagram please wait")
                time.sleep(6)
                user_bar = driver.find_element_by_name('username')
                user_bar.clear()
                user_bar.send_keys("Instagram User name")
                pass_bar = driver.find_element_by_name('password')
                pass_bar.clear()
                pass_bar.send_keys("Instagram password")
                pass_bar.send_keys(Keys.RETURN)
                speak("Loggin into your account please wait")
                time.sleep(10)
                home = driver.find_element_by_class_name('_8-yf5 ')
                home.click()
                time.sleep(5)
                turn__on = driver.find_element_by_class_name('mt3GC')
                turn__on.click()
            except:
                speak("Sorry sir I am not able to reach your instagram account")
        elif 'login' and 'linkedin' in query:
            try:
                speak("Logging into your linkedin account")
                path = "chromedriver"
                driver = webdriver.Chrome(path)

                driver.get(
                    'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
                driver.find_element_by_xpath(
                    '/html/body/div/main/div[2]/div[1]/form/div[1]/input').send_keys('Linkedin Email')
                driver.find_element_by_xpath(
                    '/html/body/div/main/div[2]/div[1]/form/div[2]/input').send_keys("Linkedin password")
                driver.find_element_by_xpath(
                    '/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()
                speak("Loggedin sucessfull")
            except:
                speak("Sorry sir I couldn't log in into your linkedin account")

        elif "that's ok" in query:
            speak("Thank you sir. I am really impressed")
        elif 'postal code' in query or 'pincode' in query:
            query = query.replace("hey", "")
            query = query.replace("jarvis", "")
            query = query.replace('what', "")
            query = query.replace('is the', "")
            query = query.replace('pincode', "")
            query = query.replace('pin code', "")
            query = query.replace('postalcode', "")
            query = query.replace('of', "")
            query = query.replace(" ", "")
            print(query)
            speak(f"Searching the pincode of {query}")
            base_url = "https://www.google.co.in/search?q=pincode+of"+query
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
            }
            import requests
            from bs4 import BeautifulSoup
            try:
                page = requests.get(base_url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find(class_='Z0LcW').get_text()
                print(result)
                speak(f"Postal code of {query} is {result}")
            except:
                try:
                    query = query.replace("hey", "")
                    query = query.replace("jarvis", "")
                    query = query.replace('what', "")
                    query = query.replace('is the', "")
                    query = query.replace('pincode', "")
                    query = query.replace('pin code', "")
                    query = query.replace('postalcode', "")
                    query = query.replace('of', "")
                    query = query.replace(" ", "")
                    print(query)
                    path = "chromedriver"
                    driver = webdriver.Chrome(path)
                    speak("Google raised some errors")
                    driver.get('https://worldpostalcode.com/lookup')
                    speak("Finding the pincode in world postal code database")
                    speak(f"Searching {query} in world postal code database")
                    driver.find_element_by_xpath(
                        '/html/body/div[1]/div[2]/form/input[2]').send_keys(query)
                    driver.find_element_by_xpath(
                        '/html/body/div[1]/div[2]/form/input[1]').click()
                    time.sleep(3)
                    code = driver.find_element_by_xpath(
                        '/html/body/div[3]/div/div[4]/div[1]/div[6]/div/div[1]/div/div[1]/b')
                    print(code.text)
                    speak(f"Postal code of {query} is {code.text}")
                    driver.quit()

                except:
                    speak(
                        "Sorry sir can't find the pincode in google or world postal code database")
        elif 'tell me about' in query:
            query = query.replace('jarvis', '')
            query = query.replace('tell me about', '')
            print("About" + query)
            base_url = 'https://www.google.co.in/search?q=about+'+query
            print(base_url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
            }
            import requests
            from bs4 import BeautifulSoup
            try:
                page = requests.get(base_url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find(class_='kno-rdesc').get_text()
                print(result)
                speak(result)
            except:
                try:

                    query = query.replace('jarvis', '')
                    query = query.replace('tell me about', '')
                    query = query.replace(' ', '')
                    print("About" + query)
                    base_url = 'https://simple.wikipedia.org/wiki/' + query
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
                    }
                    import requests
                    from bs4 import BeautifulSoup
                    try:
                        page = requests.get(base_url, headers=headers)
                        soup = BeautifulSoup(page.content, 'html.parser')
                        result = soup.find(
                            class_='mw-parser-output').get_text()
                        print(result)
                        speak(result)
                    except:
                        print("Couldn't find in second try")
                except:
                    speak(f"Sir I couldn't find about {query}")
                    speak(f'Please try {query} wikipedia')
        elif 'height of' in query:
            query = query.replace("jarvis", "")
            query = query.replace('what is', '')
            query = query.replace('the', "")
            query = query.replace('height of', '')
            query = query.replace(' ', "")
            print("Searching the height of " + query)

            base_url = 'https://www.google.co.in/search?q=what+is+the+height+of+'+query
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
            }
            import requests
            from bs4 import BeautifulSoup
            try:
                page = requests.get(base_url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find(class_='Z0LcW').get_text()
                print(result)
                speak(f"Height of {query} is {result}")
            except:
                speak(f"Sorry sir i couldn't find the height of {query}")
        elif 'distance between' in query:
            query = query.replace("what", "")
            query = query.replace("is the", "")
            query = query.replace("between", "")
            query = query.replace('hey', "")
            query = query.replace('jarvis', '')
            query = query.replace('what', "")
            query = query.replace('is', "")
            query = query.replace('the', "")
            query = query.replace(" ", "")
            base_url = 'https://www.google.co.in/search?q=what+is+the+distance+between'+query
            print(base_url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
            }
            import requests
            from bs4 import BeautifulSoup
            try:
                print("Try 1")
                page = requests.get(base_url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find(class_='UdvAnf').get_text()
                print(result)
                speak(result)
                speak("Would you like to show the direction")
                command = takeCommand()
                if 'yes' in command or 'ok' in command or 'show' in command:
                    path = "chromedriver"
                    driver = webdriver.Chrome(path)
                    driver.get(base_url)
            except:
                speak("Sorry sir i couldn't reach the server")
        elif 'show me direction' in query:
            query = query.replace('show me direction', "")
            places = query.split()
            print(places)
            from_place = places[1]
            to_place = places[3]
            print(places[1])
            print(places[3])
            path = "chromedriver"
            base_url = 'https://www.google.co.in/maps/dir/' + \
                str(from_place)+',+/'+str(to_place)+','
            print(base_url)
            driver = webdriver.Chrome(path)
            driver.get(base_url)
        elif 'what is' in query:
            query = query.replace('hey', "")
            query = query.replace('jarvis', '')
            query = query.replace('what', "")
            query = query.replace('is', "")
            query = query.replace(" ", "")

            base_url = 'https://www.google.co.in/search?q=what+is+'+query
            print(base_url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
            }
            import requests
            from bs4 import BeautifulSoup
            try:
                print("Try 1")
                page = requests.get(base_url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find(class_='Z0LcW').get_text()
                print(result)
                speak(result)
            except:
                try:
                    print("Try 2")
                    page = requests.get(base_url, headers=headers)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    result = soup.find(class_='hgKElc').get_text()
                    print(result)
                    speak(result)
                except:
                    try:
                        print("Try 3")
                        page = requests.get(base_url, headers=headers)
                        soup = BeautifulSoup(page.content, 'html.parser')
                        result = soup.find(class_='kno-rdesc').get_text()
                        print(result)
                        speak(result)
                    except:
                        print("Cannot find in third try")
                        try:
                            print("Try 4")
                            page = requests.get(base_url, headers=headers)
                            soup = BeautifulSoup(page.content, 'html.parser')
                            result = soup.find(class_='qv3Wpe').get_text()
                            print(result)
                            speak(result)
                        except:
                            print("Cannot find in fourth try")
                            speak(f"Sorry sir I couldn't find {query}")
                    print("Cannot find in second try")
        elif 'who is' in query:
            query = query.replace("jarvis", "")
            query = query.replace("who is", "")
            query = query.replace("the", "")
            query = query.replace(" ", "+")
            base_url = 'https://www.google.co.in/search?q=who+is+'+query
            print(base_url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
            }
            import requests
            from bs4 import BeautifulSoup
            try:
                print("Try 1")
                page = requests.get(base_url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                result = soup.find(class_='FLP8od').get_text()
                print(result)
                speak(result)
            except:
                try:
                    print("Try 2")
                    page = requests.get(base_url, headers=headers)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    result = soup.find(class_='iKJnec').get_text()
                    print(result)
                    speak(result)
                except:
                    print("Try 2 failed")
                    speak("Sorry sir I couldn't find it")
        elif 'covid updates' in query or 'corona updates' in query or 'covid update' in query or 'corona update' in query:
            query = query.replace("jarvis", "")
            query = query.replace("what", "")
            query = query.replace(" ", "+")
            base_url = 'https://www.worldometers.info/coronavirus/'
            print(base_url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
            }
            import requests
            from bs4 import BeautifulSoup
            try:
                print("Try 1")
                page = requests.get(base_url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                total_corona_cases_world = soup.find(
                    class_='maincounter-number').get_text()
                total_corona_death_world = soup.find_all(
                    "div", class_="maincounter-number")
                total_corona_recover_world = soup.find_all(
                    "div", class_="maincounter-number")
                total_active_cases_world = soup.find(
                    class_='number-table-main').get_text()

                print("Total corana cases in world" + total_corona_cases_world)
                speak(
                    f"Total corana cases in world {total_corona_cases_world}")
                print(total_corona_death_world[1].get_text())
                total_death_number = total_corona_death_world[1].get_text()
                speak(f"Total death number is {total_death_number}")
                total_recover_number = total_corona_recover_world[2].get_text()
                print(total_recover_number)
                speak(f"Total recover number is {total_recover_number}")
                print("There are " + total_active_cases_world +
                      " active casses in the world")
                speak(
                    f"There are {total_active_cases_world} active cases in the world")

                old_corona_cases = total_corona_cases_world
                new_corona_cases = soup.find(
                    class_='maincounter-number').get_text()
                print("new corona casses : "+new_corona_cases)
                print("Old corona casses : " + old_corona_cases)
                if old_corona_cases < new_corona_cases:
                    speak("Corona casses are slightly increaseing")
            except:
                speak("Soory sir Some error occure")

        elif 'sleep' in query or 'take some rest' in query:
            speak("I will be sleeping for 50 second")
            time.sleep(50)
        elif 'good morning' in query:
            hour = int(datetime.datetime.now().hour)
            print(hour)
            if hour >= 0 and hour < 12:
                speak(f"Good morning {my_name}")
            elif(hour >= 12 and hour < 18):
                StrTime = datetime.datetime.now().strftime("%H:%M:%S")
                print("The time is " + StrTime)
                speak(f"It's {StrTime} afternoon so, Good afternoon {my_name}")
            else:
                StrTime = datetime.datetime.now().strftime("%H:%M:%S")
                print("The time is " + StrTime)
                speak(f"It's {StrTime} evening so, Good evening {my_name}")
        elif 'good afternoon' in query:
            hour = int(datetime.datetime.now().hour)
            print(hour)
            if hour >= 0 and hour < 12:
                speak(f"Good morning sir.I think you are on you bed")
                time.sleep(1)
                speak("Wake up sir")

            elif(hour >= 12 and hour < 18):
                speak("Good afternoon")
            else:
                StrTime = datetime.datetime.now().strftime("%H:%M:%S")
                print("The time is " + StrTime)
                speak(f"It's {StrTime} evening so, Good evening {my_name}")
        elif 'my name is' in query or 'i am' in query:
            speak("You have a beautifull name")
            speak("I am Jarvis")
        elif 'hey jarvis' in query or 'hello jarvis' in query or 'hi jarvis' in query:
            speak("Hello sir, I am here for you")
        elif 'hi' in query or 'hello' in query:
            speak("Hello")
