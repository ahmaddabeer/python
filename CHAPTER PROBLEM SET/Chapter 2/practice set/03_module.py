import webbrowser
import os
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")

def open_gallery():
    speak("Opening Gallery")
    os.startfile(os.path.expanduser("~/Pictures"))

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            speak("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-IN')
            speak(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None