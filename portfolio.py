from flask import Flask, render_template

app = Flask(__name__)


# API for the home page
@app.route('/')
def index():
    return render_template('index.html')