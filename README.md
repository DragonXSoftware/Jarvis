# Jarvis UI – Your Local AI Assistant

**Jarvis UI** is a lightweight, personal chatbot that runs entirely on your own machine using [Ollama](https://ollama.com/) for local LLM capabilities. No cloud. No tracking. Full control.

---

## Features
- Local-only AI assistant (powered by Ollama)
- Simple Python-based UI
- Voice and text interaction
- Complete data privacy with local processing

---

## Requirements

- [Python 3.8+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/) (must be installed and running)
- A compatible LLM served by Ollama (e.g., `llama3`, `mistral`, `phi`, etc.)

---

## Setup Instructions

1. **Install and Start Ollama**
   - Download and install Ollama from [ollama.com](https://ollama.com/).
   - In your terminal, run the following command to serve a model:
     ```bash
     ollama serve
     ```
   - (Optional) Pull a model if you haven’t already:
     ```bash
     ollama run llama3
     ```

2. **Prepare Your Files**
   - Ensure that `Jarvis.py` and `JarvisUI.py` are in the same folder.

3. **Install Python Dependencies**
   - If you have a `requirements.txt` file, run:
     ```bash
     pip install -r requirements.txt
     ```
   - Otherwise, manually install any required libraries as indicated in your code.

4. **Run Jarvis UI**
   - In your terminal, execute:
     ```bash
     python JarvisUI.py
     ```

---

## Configuration & Customization

- **Ollama Connection:**  
  Jarvis UI connects to your local Ollama instance at `http://localhost:11434` by default.  
  Adjust the URL or port in the source code if needed.

- **Model Selection:**  
  You can modify the model name in `Jarvis.py` (default is likely set to `llama3`).  
  Change it to any model you prefer as long as it's served by your Ollama instance.

- **Audio Support:**  
  Audio input/output functionality may depend on your operating system.  
  Ensure you have the necessary dependencies installed if using voice features.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

*Enjoy your local AI assistant and feel free to contribute or provide feedback!*