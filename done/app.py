from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)  # Creating an instance of class Flask with argument name


@app.route('/', methods=["GET", "POST"])
def trans():
    transcription = ""

    if request.method == "POST":  # Checking if the user clicked on transcribe
        file = request.files["file"]  # Storing the fileStorage of the selected file in browser from the system

        if file.filename == "":  # Checking if on submit no file was selected eg:(empty)
            return redirect('errors')

        if file.filename != "":
            recognizer = sr.Recognizer()  # Creating an Instance of Recognizer class from speechRecognition package
            audioFile = sr.AudioFile(file)  # Creating an Audiofile instance given a WAV

            with audioFile as source:
                data = recognizer.record(source)  # A method of recognizer which reads audio files
                transcription = recognizer.recognize_google(data)  # google API that permits transcription of audio (1 minute)
    return render_template("Transcrip.html", text=transcription)


@app.errorhandler(404)
def errors(error):
    return render_template("Error.html"), 404


if __name__ == "__main__":
    app.run()
