import tkinter as tk
from tkinter import scrolledtext
import threading
import requests
import speech_recognition as sr
import pyttsx3

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5)
            command = r.recognize_google(audio)
            return command
        except:
            return "[Say something...]"

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

# GUI logic
def run_jarvis_ui():
    chat_active = threading.Event()  # control flag
    chat_active.set()

    def speak_safe(text):
        def _speak():
            engine.say(text)
            engine.runAndWait()
        root.after(0, _speak)

    def update_chat(role, message):
        chat_display.config(state='normal')
        chat_display.insert(tk.END, f"{role}: {message}\n\n")
        chat_display.config(state='disabled')
        chat_display.see(tk.END)

    def handle_voice():
        while chat_active.is_set():
            user_input = listen()
            update_chat("You", user_input)

            if user_input.lower().strip() == "goodbye":
                update_chat("Jarvis", "Goodbye, shutting down the assistant.")
                speak_safe("Goodbye, shutting down the assistant.")
                break

            if user_input and user_input != "[Say something...]":
                response = chat_with_gpt(user_input)
                update_chat("Jarvis", response)
                speak_safe(response)

    def on_voice_click():
        threading.Thread(target=handle_voice).start()

    def pause_chat():
        nonlocal chat_active
        if chat_active.is_set():
            chat_active.clear()
            pause_button.config(text="▶️ Resume Chat")
        else:
            chat_active.set()
            pause_button.config(text="⏸ Pause Chat")
            threading.Thread(target=handle_voice).start()

    root = tk.Tk()
    root.title("Jarvis UI")

    chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=80, height=25, font=("Courier", 12))
    chat_display.pack(padx=10, pady=10)

    voice_button = tk.Button(root, text="🎤 Speak to Jarvis", command=on_voice_click, font=("Helvetica", 14))
    voice_button.pack(pady=(0, 5))

    pause_button = tk.Button(root, text="⏸ Pause Chat", command=pause_chat, font=("Helvetica", 12))
    pause_button.pack(pady=(0, 10))

    root.mainloop()

if __name__ == "__main__":
    run_jarvis_ui()