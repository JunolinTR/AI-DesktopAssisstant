import pywhatkit
import pyttsx3
import datetime
import speech_recognition
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you wan to message")
    a = int(input('''Person 1 - 1
    Person 2 - 2'''))
    if a == 1:
        speak("Whats the message")
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        message = r.recognize_google(audio, language='en-in')
        print(f"You Said: {message}\n")
        pywhatkit.sendwhatmsg("+919489568381",message,time_hour=strTime,time_min=update)
    elif a==2:
        pass