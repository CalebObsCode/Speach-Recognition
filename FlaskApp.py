#import Libraries
from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)


# Creating a recognition object
#r = sr.Recognizer()

# route
@app.route("/", methods=["GET", "POST"])

def index():

    transcript = ""
    #verify if file was recieved
    if request.method == "POST":
        print("Audio File was recieved")

        #Check if file exists
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)


        if file:
            recognizer = sr.Recognizer()
            get_AudioFile = sr.AudioFile(file)

            with get_AudioFile as source:
                data = recognizer.record(source)

            transcript = recognizer.recognize_google(data, key=None)


            

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
        app.run(debug=True, threaded=True)