
# 🎙 **AI Desktop Voice Assistant**

*A Personal AI-Powered Desktop Assistant built with Python*

This project is a **personal desktop voice assistant** that can recognize your voice commands, process them using AI, and perform various system-level and online tasks—just like Jarvis or Alexa but running locally on your computer.

---

## ✅ **Features**

* 🎤 **Voice Command Recognition** (using Speech-to-Text)
* 🔊 **Text-to-Speech Responses**
* 🌐 **Performs Web Searches** (Google, Wikipedia, YouTube, etc.)
* 🗂 **Opens Applications & Files on your System**
* 📧 **Sends Whatsapp Messages** 
* 📰 **Reads News, Weather, and Other Information**
* 🧠 **AI-Powered Q\&A** 

---

## 🛠 **Tech Stack & Libraries**

* **Python 3.x**
* **Speech Recognition:** `speechrecognition`
* **Text-to-Speech:** `pyttsx3` (offline) / `gTTS` (Google TTS)
* **Web Browsing & APIs:** `webbrowser`, `requests`, `wikipedia`
* **System Tasks:** `os`, `subprocess`, `pyautogui`
* **Optional AI Integration:** `openai`, `transformers` (for LLM-based Q\&A)

---

## 🚀 **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/AI-DesktopAssistant.git
cd AI-DesktopAssistant
```

### **2. Install Required Libraries**

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, here’s what to install:

```
speechrecognition
pyttsx3
wikipedia
requests
pyautogui
pyaudio      # needed for microphone input
```

(If using OpenAI or Hugging Face for AI Q\&A, add: `openai` or `transformers`)

### **3. Run the Assistant**

```bash
python assistant.py
```

---

## 💻 **How to Use**

1. Run the program and **allow microphone access**.
2. Say a wake word like `"Hello Jarvis"` *(if implemented)* or directly give commands.
3. Examples of voice commands:

   * `"Open YouTube"`
   * `"Search Wikipedia for Artificial Intelligence"`
   * `"Play music"`
   * `"What is the weather today?"`
   * `"Shut down the system"`

