import os
import sys
import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
from openai import OpenAI
import pyaudio

# ================== INITIAL SETUP ==================
load_dotenv()

ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Manu")
VOICE_RATE = int(os.getenv("VOICE_RATE", 170))
MUSIC_PATH = os.getenv("MUSIC_PATH")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

client = OpenAI(api_key=OPENAI_API_KEY)

engine = pyttsx3.init()
engine.setProperty("rate", VOICE_RATE)

SITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://en.wikipedia.org",
    "github": "https://github.com",
    "linkedin": "https://www.linkedin.com",
    "gmail": "https://mail.google.com",
    "spotify": "https://open.spotify.com",
    "portfolio": "https://sarthaksinghaniya.netlify.app",
}

APPS = {
    "chrome": "chrome",
    "vs code": "code",
    "notepad": "notepad",
    "calculator": "calc",
    "command prompt": "cmd"
}

# ================== SPEECH FUNCTIONS ==================
def say(text: str):
    """Speak the given text using TTS engine."""
    engine.say(text)
    engine.runAndWait()


def get_working_mic_index() -> int | None:
    """Return the first microphone index with input channels, or None if no mic available."""
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxInputChannels'] > 0:
            p.terminate()
            return i
    p.terminate()
    return None


def takecommand() -> str:
    """
    Listen to user's voice and return recognized text.
    Falls back to typed input if no microphone available.
    """
    mic_index = get_working_mic_index()
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = False

    if mic_index is not None:
        try:
            with sr.Microphone(device_index=mic_index, sample_rate=48000) as mic:
                say("Listening")
                r.adjust_for_ambient_noise(mic, duration=0.3)
                audio = r.listen(mic, timeout=5, phrase_time_limit=6)

            say("Recognizing")
            query = r.recognize_google(audio, language="en-IN")
            print("User:", query)
            return query.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            say("I did not catch that")
            return ""
        except sr.RequestError:
            say("Speech service is unavailable")
            return ""
        except Exception as e:
            print("Mic error:", e)
            return ""
    else:
        # Fallback to typed input
        return input("No mic detected. Type your command: ").lower()


# ================== AI FUNCTION ==================
def ai_response(query: str) -> str:
    """Get AI-generated response for a query."""
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a smart Windows desktop assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=120
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "I am having trouble connecting to my intelligence module."


# ================== UTILITY FUNCTIONS ==================
def open_sites(query: str) -> bool:
    """Open a website if matched in query."""
    for name, url in SITES.items():
        if f"open {name}" in query:
            say(f"Opening {name}")
            webbrowser.open(url)
            return True
    return False


def open_apps(query: str) -> bool:
    """Open an application if matched in query."""
    for app, cmd in APPS.items():
        if f"open {app}" in query:
            say(f"Opening {app}")
            os.system(cmd)
            return True
    return False


# ================== MAIN LOOP ==================
def run_assistant():
    say(f"Hey, I'm {ASSISTANT_NAME}, your desktop assistant.")

    while True:
        query = takecommand()
        if not query:
            continue

        # Exit commands
        if any(word in query for word in ["exit", "quit", "stop"]):
            say("Goodbye. Have a productive day.")
            sys.exit()

        # Open websites or applications
        if open_sites(query) or open_apps(query):
            continue

        # Play music
        if "play music" in query:
            if MUSIC_PATH and os.path.exists(MUSIC_PATH):
                say("Playing music")
                os.startfile(MUSIC_PATH)
            else:
                say("Music file not found")
            continue

        # Time & Date
        if "time" in query:
            now = datetime.datetime.now()
            say(f"It is {now.hour} {now.minute}")
            continue
        if "date" in query:
            today = datetime.date.today().strftime("%B %d, %Y")
            say(f"Today's date is {today}")
            continue

        # System controls
        if "shutdown" in query:
            say("Shutting down system")
            os.system("shutdown /s /t 5")
            continue
        if "restart" in query:
            say("Restarting system")
            os.system("shutdown /r /t 5")
            continue
        if "lock system" in query:
            say("Locking system")
            os.system("rundll32.exe user32.dll,LockWorkStation")
            continue

        # AI fallback
        response = ai_response(query)
        say(response)


# ================== ENTRY POINT ==================
if __name__ == "__main__":
    run_assistant()
