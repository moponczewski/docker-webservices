#!/usr/bin/env python

from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	welcomestr="This is DATE Webservice v0.1\n"
	welcomestr+="Please use the following Urls:\n"
	welcomestr+="/help - delivers nothing than senseless output\n"
	welcomestr+="/dt - returns date and time\n"
	welcomestr+="\n"
	return welcomestr

@app.route('/help', methods=['GET'])
def help():
	return "The HELP!\n\n"

@app.route('/dt', methods=['GET'])
def datetime():
	output = subprocess.check_output(['date'], shell = True)
	return output

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
