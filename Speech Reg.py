import speech_recognition as sr
from gtts import gTTS
#from pygame import mixer
#import os


               
while (True):
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening from microphone........")
    print("Say something!")
    audio = r.listen(source,phrase_time_limit=0)
    response = r.recognize_google(audio)
    print("I think you said '" + response + "'")
    tts = gTTS(text="I think you said "+str(response), lang='en')


  

