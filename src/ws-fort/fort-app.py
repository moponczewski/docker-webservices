#!/usr/bin/env python

from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	welcomestr="This is FORTUNE Webservice v0.1\n"
	welcomestr+="Please use the following Urls:\n"
	welcomestr+="/help - delivers nothing than senseless output\n"
	welcomestr+="/dt - returns date and time\n"
	welcomestr+="/fortune - returns a general quote\n"
	welcomestr+="/fortune/startrek - returns a specific startrek quote\n"
	welcomestr+="/fortune/people - returns a quote from famous people\n"
	welcomestr+="\n"
	return welcomestr

@app.route('/help', methods=['GET'])
def help():
	return "The HELP!\n\n"

@app.route('/dt', methods=['GET'])
def datetime():
	output = subprocess.check_output(['date'], shell = True)
	return output

@app.route('/fortune', methods=['GET'])
def fortune():
	output = subprocess.check_output(['/usr/games/fortune'], shell = True)
	return output

@app.route('/fortune/people', methods=['GET'])
def fortunep():
	output = subprocess.check_output(['/usr/games/fortune people'], shell = True)
	return output

@app.route('/fortune/startrek', methods=['GET'])
def fortunest():
	output = subprocess.check_output(['/usr/games/fortune startrek'], shell = True)
	return output

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
