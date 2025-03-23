import speech_recognition as sr
import pyttsx3
import requests

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def chat_with_gpt(prompt):
    response = requests.post(
        "http://localhost:11434/api/chat",
        headers={"Content-Type": "application/json"},
        json={
            "model": "mistral",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant named Jarvis."},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }
    )
    return response.json()['message']['content']

# Main loop
def run_jarvis():
    speak("Hello, I am Jarvis. How can I help you today?")
    while True:
        user_input = listen()
        if user_input.lower() in ["exit", "quit", "goodbye"]:
            speak("Goodbye, Austin.")
            break
        if user_input:
            response = chat_with_gpt(user_input)
            speak(response)

run_jarvis()