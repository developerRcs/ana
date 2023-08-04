from vosk import KaldiRecognizer, Model
import os
import pyaudio
import pyttsx4
import json
import core

engine = pyttsx4.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[-2].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()




model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048
)
stream.start_stream()

while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result["text"]
            print(text)

            if text == "que horas são" or text == "me diga as horas":
                speak(core.SystemInfo.get_time())