from flask import Flask, render_template
from flask import *

app = Flask(__name__)

#@app.route("/")
#def hello_world():
#	app.logger.info('logging successfully')
#	return render_template("index.html")

@app.route("/", methods=['POST', 'GET'])
def load():
	if request.method == "POST":
		return render_template('test.html')
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)