import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import os
import random
import requests
import json
from playsound import playsound
from gtts import gTTS
from twitter import Twitter
from twitterUserInfo import username, password
  

api_url="https://api.exchangeratesapi.io/latest?base="
listener= sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            print('dinleniyor')
            voice=listener.listen(source)
            command=listener.recognize_google(voice, language='tr-TR')
            command=command.lower()
            if 'sero' in command:
                command = command.replace('sero','')
                print(command)
    except sr.UnknownValueError:
        speak("anlayamadım")
        take_command()

    print(command)
    return command


def speak(string):
    tts= gTTS(string,lang='tr')
    file="audio.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def fortuneteller():
    list=["Üç vakte kadar kısmetin görünüyor.",
    "Kuşun kanadında haberin var.",
    "Deve yükü ile eşya görünüyor.",
    "Hanene ay doğmuş.",
    "Sana bi yol görünüyor",
    "aaa göz var göz, bak işte burada"
    ]
    speak(random.choice(list))

def ara(command):
    command=command.replace('ara','')
    url="https://google.com/search?q="+command
    webbrowser.get().open(url)
    speak(command+' için bulduklarım')

def writeNote():
    speak('notunuz nedir')
    text="\n"+take_command()
    try:
        with open('C:\\Users\\SERAP\\Desktop\\notlarım.txt',"a",encoding="utf-8") as notes:
            notes.write(text)
            speak("not alındı")
    except:
        speak("not alırken hata oluştu")

def readNote():
    try:
        if os.path.exists('C:\\Users\\SERAP\\Desktop\\notlarım.txt'):
            with open('C:\\Users\\SERAP\\Desktop\\notlarım.txt',"r",encoding="utf-8") as notes:
                metin=notes.read()
                if metin=='':
                    speak("dosya boş")
                else:
                    speak(metin)
        else:
            speak("notunuz bulunmamaktadır")
    except:
        speak("notlar okunurken hata oluştu")

def twitter():
    twitter = Twitter(username,password)
    twitter.singIn()
    speak("Twitter açıldı")

def take():
        döviz=take_command()
        if döviz=="dolar":
            döviz="USD"
        elif döviz=="türk lirası":
            döviz="TRY"
        elif döviz=="yuro":
            döviz="EUR"
        else:
            speak("geçersiz seçim")
            döviz()
        return döviz
def döviz():
    speak("bozulacak döviz türü nedir 1 dolar 2 türk lirası 3 euro")
    bozulan_döviz=take()
    
    speak("alınacak döviz türü nedir 1-dolar 2-türk lirası 3-euro")
    alinan_döviz=take()
    
    speak(f"ne kadar {bozulan_döviz}bozdurmak istiyorsunuz")
    miktar=float(take_command())
    result=requests.get(api_url+bozulan_döviz)
    result = json.loads(result.text)
    speak("1 {0} = {1} {2}".format(bozulan_döviz, float(result["rates"][alinan_döviz]), alinan_döviz))
    speak("{0} {1} = {2} {3}".format(miktar, bozulan_döviz, float(miktar * result["rates"][alinan_döviz]),alinan_döviz))

def sing(command):
    song=command.replace('çal','')
    speak(song + 'oynatılıyor')
    pywhatkit.playonyt(song)
    
