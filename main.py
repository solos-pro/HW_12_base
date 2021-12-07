'''from flask import Flask, request, render_template
import json, requests     # for .json

app = Flask(__name__)


@app.route('/')
def index():
    with open('settings.json') as f:
        entities = json.load(f)
        return render_template("main-all-items.html", entities=entities)





if __name__ == "__main__":
    app.run()'''

import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open("settings.json") as f:
        settings = json.load(f)
    return render_template("index.html", **settings)

@app.route('/candidate/<id>')
def prof():
    with open("candidates.json") as f:
        candidates = json.load(f)
    for candidate in candidates:
        if candidate['id'] == int(id):
            return render_template('candidate.html', **candidate)


if __name__ == "__main__":
    app.run()