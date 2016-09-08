from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
	welcomestr="Welcome... This is the COW Webservice v0.1\n"
	welcomestr+="Please use the following Urls:\n"
	welcomestr+="/help - this makes nothing but senseless output\n"
	welcomestr+="/cow - this returns a cow mow\n"
	welcomestr+="\n"
	return welcomestr

@app.route('/help', methods=['GET'])
def help():
	return "Cry for help baby... no one will hear you!\n"

@app.route('/cow', methods=['GET'])
def cow():
	sent=subprocess.check_output(["curl -s datecon:5000/dt"], shell = True)
	sent+="\nRequest from: "
	sent+=request.headers.get('User-Agent')
	sent+="\n\n"
	sent+=subprocess.check_output(["curl -s fortcon:5000/fortune/startrek"], shell = True)

	# .replace formats the ' char in the fortunes quote, else this leads to trouble in a cli call
	output=subprocess.check_output(["/usr/games/cowsay -f docker '%s'" % sent.replace("'","")], shell = True)
	return output

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
