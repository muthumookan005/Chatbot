import speech_recognition as sr
from gtts import gTTS
import uuid


def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return "Sorry, I could not understand your voice."

    except sr.RequestError:
        return "Sorry, speech recognition is not available."


def text_to_speech(text):
    filename = f"response_{uuid.uuid4().hex}.mp3"

    tts = gTTS(text=text, lang="en")
    tts.save(filename)

    return filename