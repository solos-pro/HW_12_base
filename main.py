from flask import Flask, request, render_template
import json, requests     # for .json

app = Flask(__name__)


@app.route('/')
def index():
    with open('settings.json') as f:
        entities = json.load(f)
        return render_template("main-all-items.html", entities=entities)





if __name__ == "__main__":
    app.run()