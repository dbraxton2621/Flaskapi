from flask import Flask
from flask import request
from flask import jsonify
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for


app= Flask(__name__)
app.secret_key = "thisisarandomstring"

data=   {"sport" : "football", 
        "state" : "South Carolina",
        "job" : "Software Development Engineer"}

@app.route("/")
def req1():
	return jsonify(data)

@app.route("/protected/<name>")
def session_option(name):
	session["username"] = name

	if session["username"] == "Devin":
		return (jsonify(data))
	else: 
		return "Only for the boss!"	

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

