# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session

import requests #To access our API

# -- Initialization section --
app = Flask(__name__)

## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    session["name"] = "Anoopa"
    return render_template('index.html', question='data[0]["question"]')
@app.route("/random")
def jeopardy_random():
    #Use jservice API/random to get 1 jeopardy clue
    return render_template("jeopardy.py")

# def index():
    # return render_template('index.html', question='data[0]["question"]')