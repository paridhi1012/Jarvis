import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import smtplib
import webbrowser as wb
import webbrowser
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
'''voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current Time is")
    speak(Time)
#time()

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current Date is")
    speak(date)
    speak(month)
    speak(year)
#date()

def wishme():
    speak("welcome back!")
    hour=datetime.datetime.now().hour

    if hour>= 6 and hour< 12:
        speak("Good morning")
    elif hour>= 12 and hour< 18:
        speak("Good afternoon")
    elif hour>= 18 and hour<= 24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("paridhi at your service. How can i help you?")
#wishme()

def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language ="en-in")
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say That again please.....")
        return "None"

    return query

#def sendmail(to,content):
#    server =smtplib.SMTP('smtp.gmail.com',587)
#    server.ehlo()
#    server.starttls()
#    server.login("paridhisanghvi@gmail.com","abcd")
#    server.sendmail("paridhisanghvi@gmail.com",to,content)
#    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\windows 10\\Pictures\\Screenshots\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_jokes())

if __name__ == '__main__':
    wishme()

    while True:
        query = takeCommand().lower()
        #print(query)
        if "time" in query:
            time()    
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching.....")
            query =query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences =2)
            speak(result)
        #elif "send email" in query:
        #    try:
        #        speak("what should i say?")
        #        content=takeCommand()
        #        to = ""
        #        sendmail(to,content)
        #        speak("Email sent successfully")

        #    except Exception as e:
        #        speak(e)
        #        speak("unable to sent the message")

        elif "search in chrome" in query:
            speak("What should i search?")
            chromepath = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s'
            search = takeCommand().lower()
            webbrowser.get(chromepath).open(search+".com")
        
        elif "logout" in query:
            os.system("shutdown -l")
        
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")
        
        elif "play song" in query:
            songs_dir = 'F:/music'
            music = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,music[0]))          
        
        elif "remember that" in query:
            speak("what should i remember?")
            data = takeCommand()
            speak("you said me to remember" + data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("you said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done")
        
        elif "cpu" in query:
            cpu()

        elif "jokes" in query:
            jokes()