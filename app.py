
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