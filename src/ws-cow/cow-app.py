#!/usr/bin/env python


from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


def getFortune(topic):
	sent=subprocess.check_output(["curl -s datecon:5000/dt"], shell = True)
	sent+="\nRequest from: "
	sent+=request.headers.get('User-Agent')
	sent+="\n\n"

	if topic == 'cow':
		curlthis = "curl -s fortcon:5000/fortune"
	elif topic == 'star':
		curlthis = "curl -s fortcon:5000/fortune/startrek"
	elif topic == 'fame':
		curlthis = "curl -s fortcon:5000/fortune/people"
	else:
		curlthis = "curl -s fortcon:5000/fortune"

	sent+=subprocess.check_output([curlthis], shell = True)

	# .replace formats the ' char in the fortunes quote, else this leads to trouble in a cli call
	fortune=subprocess.check_output(["/usr/games/cowsay -f docker '%s'" % sent.replace("'","")], shell = True)

	# format fixed font output with <PRE>...</PRE> for Browsers
	if ('curl' or 'wget') not in request.headers.get('User-Agent'):
		prefortune="<PRE>"
		prefortune+=fortune
		prefortune+="</PRE>"
		return prefortune

	return fortune


@app.route('/', methods=['GET'])
def hello():
	welcomestr="This is COW Webservice v0.2\n"
	welcomestr+="Please use the following Urls:\n"
	welcomestr+="/help - delivers nothing than senseless output\n"
	welcomestr+="/cow - returns a cow mow with a general quote\n"
	welcomestr+="/star - returns a cow mow with a star trek quote\n"
	welcomestr+="/fame - returns a cow mow with a famous people's quote\n"
	welcomestr+="\n"
	return welcomestr



@app.route('/help', methods=['GET'])
def help():
	return "The HELP!\n"


@app.route('/cow', methods=['GET'])
def cow():
	return getFortune('cow')

@app.route('/star', methods=['GET'])
def star():
	return getFortune('star')


@app.route('/fame', methods=['GET'])
def fame():
	return getFortune('fame')


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
