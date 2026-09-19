"""
MASA 06_Video Transcription Video Application using Python Source Code Free Do
Developer: MASA
"""

import os
import io
import PySimpleGUI as sg
import speech_recognition as sr
from pydub import AudioSegment


def transcribe_video(input_video_path):
    try:
        audio = AudioSegment.from_file(input_video_path, format="mp4")
        audio.export("temp_audio.wav", format="wav")

        recognizer = sr.Recognizer()

        audio_file = "temp_audio.wav"
        with sr.AudioFile(audio_file) as source:
            print("Processing audio...")

            audio_data = recognizer.record(source)

            text = recognizer.recognize_google(audio_data)
            return text

    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"


layout = [
    [sg.Text("Select an MP4 video to transcribe:*max 10MB")],
    [sg.Input(key="-FILE-", enable_events=True, size=(45, 1)), sg.FileBrowse()],
    [sg.Button("Transcribe")],
    [sg.Text("Transcription:", size=(40, 1))],
    [sg.Multiline(size=(40, 10), key="-TRANSCRIPT-", autoscroll=True)],
    [sg.Text("www.wshopcode.com", text_color="blue", enable_events=True, key="-WEBSITE-")],
]

window = sg.Window("Video Transcription App - wshopcode", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Transcribe":
        video_path = values["-FILE-"]

        if not video_path:
            sg.popup_error("Please select an MP4 video file.")
        elif os.path.getsize(video_path) > 10 * 1024 * 1024:
            sg.popup_error("File size exceeds 10 megabytes.")
        else:
            transcription = transcribe_video(video_path)

            window["-TRANSCRIPT-"].update(transcription)

    elif event == "-WEBSITE-":
        sg.popup("Visit our website at www.wshopcode.com")

window.close()
