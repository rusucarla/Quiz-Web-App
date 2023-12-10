import re
from datetime import datetime
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello")
@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")