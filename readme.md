# Windows Desktop Assistant - Manu

A smart desktop assistant for Windows that can **open websites, launch applications, play music, provide time/date, control system actions**, and respond using **AI-powered chat**.

## Features

* **Voice Commands** using microphone (Google Speech Recognition)
* **AI Responses** via OpenAI API
* **Website & Application Launcher** (e.g., Google, YouTube, Chrome, VS Code)
* **Music Player** (local files)
* **System Controls**: shutdown, restart, lock
* **Time & Date announcements**
* **Fallback to Typed Commands** if no microphone is available

## Requirements

* Python 3.10+
* Windows OS
* Libraries:

  ```bash
  pip install pyttsx3 speechrecognition pyaudio python-dotenv openai
  ```

## Setup

1. Clone the repository:

   ```bash
   git clone <repo_url>
   cd windows-desktop-assistant
   ```

2. Create a `.env` file with:

   ```env
   ASSISTANT_NAME=Manu
   VOICE_RATE=170
   MUSIC_PATH=C:/path/to/music/file.mp3
   OPENAI_API_KEY=your_openai_api_key
   OPENAI_MODEL=gpt-4o-mini
   ```

3. Run the assistant:

   ```bash
   python assistant.py
   ```

## Usage

* Say commands like:

  * `"Open Google"`
  * `"Play music"`
  * `"What is the time?"`
  * `"Shutdown system"`

* Or type commands if no microphone is available.

## Author

**Sarthak Singhaniya**

* Portfolio: [sarthaksinghaniya.netlify.app](https://sarthaksinghaniya.netlify.app)
* GitHub: [github.com/sarthaksinghaniya](https://github.com/sarthaksinghaniya)

---
