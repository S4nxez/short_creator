import moviepy.editor as mp
import speech_recognition as sr
import os

name = "sample.mp4"
# Cargamos el fichero .mp4
clip = mp.VideoFileClip(name)
# Lo escribimos como audio y `.mp3`
clip.audio.write_audiofile("transformado_a.mp3")

r = sr.Recognizer()

audio_file = "transformado_a.mp3"
wav_file = "example.wav"

os.system(f"ffmpeg -i {audio_file} {wav_file}")

with sr.AudioFile(wav_file) as source:
    audio = r.record(source)
    text = r.recognize_google(audio)
    print(text)