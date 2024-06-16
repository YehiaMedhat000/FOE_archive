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
	return render_template("courses.html")

@app.route("/exams")
def exams():
	title = "Circuits"
	return render_template("exam.html", title=title)

if __name__ == "__main__":
	# To show immediately all the changes on the app
	app.run(debug=True)
