import pyttsx3

engine = pyttsx3.init()

while True:
    msg = input("Enter your message: ")
    engine.say(msg)
    engine.runAndWait()