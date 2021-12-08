import json, requests

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    with open("settings.json") as f:
        settings = json.load(f)
    return render_template("index.html", **settings)

@app.route('/candidate/<id>/')
def prof(id):
    with open("candidates.json") as f:
        candidates = json.load(f)
    for candidate in candidates:
        if candidate["id"] == int(id):
            return render_template("candidate.html", **candidate)

@app.route('/list/')
def candidates_():
    with open("candidates.json") as f:
        candidates = json.load(f)
    return render_template("list.html", users=candidates)


if __name__ == "__main__":
    app.run()
