import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen to user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)

# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle hospital management tasks based on user input
def handle_command(command):
    if 'make appointment' in command:
        speak("Please provide your patient ID.")
        patient_id = listen()
        # Logic to check appointments for the patient ID (placeholder)
        appointment_info = f"Your appointment is scheduled for tomorrow at 10 AM."
        speak(appointment_info)
    elif 'what of doctors' in command:
        speak("Our hospital has a team of experienced doctors specializing in various fields.")
    elif 'father information' in command:
        speak("Our hospital provides a wide range of medical services including consultations, surgeries, and diagnostics.")
    elif 'jummah ' in command:
        speak("Jummah is a passionate politicians from Homabay learning in Maseno University,.")
       
    elif 'and emergency' in command:
        speak("In case of emergency, please dial 911.")
    else:
        speak("Sorry, I couldn't understand. Can you repeat? ask Jack who created me")

# Main function to interact with the user
def main():
    speak("Hello, I am your hospital management assistant created by jack . How can I assist you today?")
    while True:
        try:
            user_input = listen().lower()
            print("User said:", user_input)
            handle_command(user_input)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you repeat?")
        except sr.RequestError:
            speak("Sorry, I'm having trouble processing your request.")

if __name__ == "__main__":
    main()
