import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, professor! How can I help you?")
    
    while True:
        with sr.Microphone() as source:
            print("Listening.......")
            audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            speak("You said: " + command)

            if "hello" in command.lower():
                speak("Hello, professor!")
            elif "goodbye" in command.lower():
                speak("Goodbye, professor!")
                break  # Exit the loop

        except sr.UnknownValueError:
            speak("Professor, I could not understand the audio.")
        except sr.RequestError as e:
            speak(f"Professor, there was an error: {e}")
