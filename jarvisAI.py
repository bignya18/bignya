import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



print("Initializing Jarvis")

MASTER = "your name"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)




def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning " + MASTER)


    elif hour>=12 and hour<18:
        speak("Good Afternoon " + MASTER)

    else:
        speak("Good Evening " + MASTER)

    # speak("I am jarvis. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception  as e:
        print("Say that again please")
        query = None
    return query   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gamil.com', 'password')
    server.sendmail("someone@gmail.com", to, content)
    server.close()

def main():
    speak("Initializing Jarvis...")
    wishMe()
    query = takeCommand()


    #logic for executing tasks as per the query
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=5)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        webbrowser.open ("youtube.com")
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open github' in query.lower():
        webbrowser.open ("youtube.com")
        url = "github.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "songs\\location"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")  
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        speak("opening")
        codePath = "C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'send an email' in query.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = "someone@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent to someone")
        except Exception as e:
            print(e)

main()
        

        