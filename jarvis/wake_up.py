import os
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listerning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    
    try:
        print("Recoganizing...")
        query = r.recognize_google(audio , language='en-in')
        print("User said :" + query)

    except Exception as e:
        #print(e)
        print("Say that again")
        return "None"
    return query

while True:
    wake_up = takeCommand()
    print("You said : " + wake_up)
    if 'wake up' in wake_up or 'jarvis' in wake_up:
        
        url = "C:\\Users\\Admin\\Music\\jarvis\\jarvis.py"
        os.startfile(url)
        speak("Online and active sir")
        break
    else:
        print("Nothing..")

    