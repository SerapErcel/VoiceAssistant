import datetime
import os
import fonks

def run_alexa():
    fonks.speak("nasıl yardımcı olabilirim")
    command=fonks.take_command()
    print(command)
    
    if 'çal' in command:
        fonks.sing(command)
    
    elif 'kapat' in command:
        fonks.speak("Hoşça kal")
        exit()

    elif 'döviz' in command:
        fonks.döviz()
      
    elif 'notlarımı yaz' in command:
        fonks.writeNote()
    
    elif 'notlarımı oku' in command:
        fonks.readNote()
        
    elif 'saat' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        fonks.speak('Şu an saat '+time)

    elif 'ara' in command:
        fonks.ara(command)
        
    elif 'beni seviyor musun' in command:
        fonks.speak('elbette çünkü sen çok güzel bir insansın')

    elif 'sosyal' in command:
        fonks.twitter()
        
    elif 'fal' in command:
        fonks.fortuneteller()

    else: 
        fonks.speak('Lütfen tekrar söyler misin?')
    

while True:
    run_alexa()
    