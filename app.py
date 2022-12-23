
Config = {
  "apiKey": "AIzaSyBO6vI1RPI-dMF89LSvvc4zlahqlwWUCEQ",
  "authDomain": "christmas-f727d.firebaseapp.com",
  "projectId": "christmas-f727d",
  "storageBucket": "christmas-f727d.appspot.com",
  "messagingSenderId": "419346374485",
  "appId": "1:419346374485:web:c639ca9e7fa031bd2659dc",
  "measurementId": "G-E9NQNFFV2L"
}

from flask import Flask, render_template, request, redirect, url_for, flash

from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

'''@app.route("/contact")
def contact():
    return render_template('contact.html')'''

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/mainwork", methods=["GET", "POST"])
def mainwork():
    if request.method == "POST":
        name= request.form.get("name")
        phone= request.form.get("phone")
        return render_template('main.html', name=name, phone=phone)


if __name__ == '__main__':
    app.run(debug=True)