import pyjokes

print("hello py")

joke=pyjokes.get_joke()
print("joke-python")

import pyttsx3
engine = pyttsx3.init()
engine.say("hello python master")
engine.runAndWait()

