import pyttsx3
import speech_recognition
import datetime
import requests
from bs4 import BeautifulSoup
import random
import pyautogui
from dictApp import openappweb
import webbrowser
from INTRO import play_gif



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

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        # These commands can be given to jarvis....

        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                elif "Hello" in query:
                    speak("Hello sir, How are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")

                # To operate web servers give these commands

                elif "google" in query:
                 from Search_Now import searchGoogle
                 searchGoogle(query)

                elif "youtube" in query:
                 from Search_Now import searchYoutube
                 searchYoutube(query)

                elif "wikipedia" in query:
                 from Search_Now import searchWikipedia
                 searchWikipedia(query)

                #command to get current temperature,weather and time

                elif "temperature" in query:
                  search = "temperature in Ratlam"
                  url = f"https://www.google.com/search?q={search}"
                  r  = requests.get(url)
                  data = BeautifulSoup(r.text,"html.parser")
                  temp = data.find("div", class_ = "BNeawe").text
                  speak(f"current{search} is {temp}")

                elif "weather" in query:
                        search = "temperature in ratlam"
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

                # youtube control commands
                elif "open" in query:
                 from dictapp import openappweb
                 openappweb(query)
                elif "close" in query:
                 from dictapp import closeappweb
                 closeappweb(query)
                elif "pause" in query:
                 pyautogui.press("k")
                 speak("video paused")
                elif "play" in query:
                 pyautogui.press("k")
                 speak("video played")
                elif "mute" in query:
                 pyautogui.press("m")
                 speak("video muted")
                elif "volume up" in query:
                 from keyboard import volumeup
                 speak("Turning volume up,sir")
                 volumeup()
                elif "volume down" in query:
                 from keyboard import volumedown
                 speak("Turning volume down, sir")
                 volumedown()
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=72gdIjo78oQ&list=RD72gdIjo78oQ&start_radio=1")
                    if b==2:
                        webbrowser.open("https://youtu.be/TaR6kZwF8jc?si=_n6ydYX_wX6JbGlJ")    
                    if b==3:
                        webbrowser.open("https://youtu.be/AETFvQonfV8?si=vojHTX_yLilcn2Jr")
                elif "news" in query:
                 from NewsRead import latestnews
                 latestnews()

                elif "finally sleep" in query:
                 speak("Going to sleep,sir")
                exit()    