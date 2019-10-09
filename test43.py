import pyttsx3 as py
import speech_recognition as sr
import urllib.request as ur
import urllib.parse as up
engine = py.init()
engine.say('search something')
engine.runAndWait()
webUrl = ur.urlopen('https://www.youtube.com/watch?v=dWeWCQmewLc&list=PLiHa1s-EL3vjr0Z02ihr6Lcu4Q0rnRvjm&index=2&t=177s')
print(webUrl.read())