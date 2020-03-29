import pyttsx3


engine = pyttsx3.init()


def voice_alert(message):
    engine.say(message)
    engine.runAndWait()
