import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Hello, I am your AI assistant. How can I help you?")
    while True:
        try:
            user_input = listen()
            print("User said:", user_input)
            speak("You said: " + user_input)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you repeat?")
        except sr.RequestError:
            speak("Sorry, I'm having trouble processing your request.")

if __name__ == "__main__":
    main()
