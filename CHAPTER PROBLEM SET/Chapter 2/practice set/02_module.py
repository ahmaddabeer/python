from gtts import gTTS
import os

def speak(text, lang='hi'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")

if __name__ == "__main__":
    text = "नमस्ते,asjaad"
    speak(text)