import os
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import openai

engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print("Manu got error", e)
        return ""

if __name__ == '__main__':
    print("PyCharm")
    say("Hey, I'm Manu")

    while True:
        query = takecommand()
        sites = [
            # Search & Knowledge
            ["google", "https://www.google.com"],
            ["wikipedia", "https://en.wikipedia.org"],
            ["google scholar", "https://scholar.google.com"],
            ["britannica", "https://www.britannica.com"],
            ["quora", "https://www.quora.com"],

            # Video & Media
            ["youtube", "https://www.youtube.com"],
            ["youtube studio", "https://studio.youtube.com"],
            ["netflix", "https://www.netflix.com"],
            ["prime video", "https://www.primevideo.com"],
            ["spotify", "https://open.spotify.com"],
            ["soundcloud", "https://soundcloud.com"],

            # Developer & Tech
            ["github", "https://github.com"],
            ["gitlab", "https://gitlab.com"],
            ["stackoverflow", "https://stackoverflow.com"],
            ["geeksforgeeks", "https://www.geeksforgeeks.org"],
            ["leetcode", "https://leetcode.com"],
            ["hackerrank", "https://www.hackerrank.com"],
            ["codeforces", "https://codeforces.com"],
            ["kaggle", "https://www.kaggle.com"],
            ["replit", "https://replit.com"],
            ["codepen", "https://codepen.io"],

            # AI / ML / Cloud
            ["openai", "https://www.openai.com"],
            ["huggingface", "https://huggingface.co"],
            ["google ai", "https://ai.google"],
            ["aws console", "https://console.aws.amazon.com"],
            ["azure portal", "https://portal.azure.com"],
            ["google cloud", "https://console.cloud.google.com"],
            ["colab", "https://colab.research.google.com"],

            # Education & Careers
            ["unstop", "https://unstop.com"],
            ["coursera", "https://www.coursera.org"],
            ["udemy", "https://www.udemy.com"],
            ["edx", "https://www.edx.org"],
            ["nptel", "https://nptel.ac.in"],
            ["internshala", "https://internshala.com"],
            ["linkedin learning", "https://www.linkedin.com/learning"],

            # Social & Professional
            ["linkedin", "https://www.linkedin.com"],
            ["twitter", "https://twitter.com"],
            ["instagram", "https://www.instagram.com"],
            ["facebook", "https://www.facebook.com"],
            ["reddit", "https://www.reddit.com"],
            ["discord", "https://discord.com"],
            ["telegram", "https://web.telegram.org"],

            # Productivity & Tools
            ["gmail", "https://mail.google.com"],
            ["google drive", "https://drive.google.com"],
            ["google docs", "https://docs.google.com"],
            ["google sheets", "https://sheets.google.com"],
            ["notion", "https://www.notion.so"],
            ["trello", "https://trello.com"],
            ["slack", "https://slack.com"],
            ["canva", "https://www.canva.com"],

            # Finance & Utilities
            ["paytm", "https://paytm.com"],
            ["phonepe", "https://www.phonepe.com"],
            ["google pay", "https://pay.google.com"],
            ["zerodha", "https://zerodha.com"],
            ["groww", "https://groww.in"],
            ["tradingview", "https://www.tradingview.com"],

            # News & Reference
            ["bbc news", "https://www.bbc.com/news"],
            ["the hindu", "https://www.thehindu.com"],
            ["times of india", "https://timesofindia.indiatimes.com"],
            ["indian express", "https://indianexpress.com"],

            # Your Work / Portfolio
            ["portfolio", "https://sarthaksinghaniya.netlify.app"],
            ["github profile", "https://github.com/sarthaksinghaniya"]
        ]

        if query == "":
            continue
        for site in sites:
            if f"Open {site[0]}".lower() in query:
                say(f"Opening{site[0]} Sir")
                webbrowser.open(site[1])

        if "open music" in query:
            musicpath = r"C:\Users\LOQ\Downloads\sarthak.mp3"
            say("Playing music")
            os.startfile(musicpath)
        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            print(f"Sir the time is {hour} bajjke {min} minutes")

