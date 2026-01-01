import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone(device_index=11, sample_rate=48000) as source:
    print("Listening... Speak now")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

print("Processing...")
try:
    text = r.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print("Error:", e)
