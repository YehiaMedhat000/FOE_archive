#!usr/bin/env python3
from flask import Flask, render_template

""" This is the main module of the project """

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/courses")
def courses():
    return render_template("courses.html", title="Courses")


@app.route("/exams")
def exams():
    return render_template("exam.html", title="Exams")


@app.route("/lessons")
def lessons():
    return render_template("lessons.html", title="Lessons")


if __name__ == "__main__":
    # To show immediately all the changes on the app
    app.run(debug=True)
