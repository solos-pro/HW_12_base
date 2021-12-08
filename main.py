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

@app.route("/search/")
def search_page():
    name = request.args.get("name")
    with open("candidates.json") as f:
        candidates = json.load(f)
    users = []
    if name:
        for candidate in candidates:
            if name in candidate["name"]:
                users.append(candidate["name"])

    return render_template("search.html", users=users, cnt=len(users))

@app.route("/skill/<skill>")
def find_skill(skill):
    with open("settings.json") as f:
        settings = json.load(f)
    with open("candidates.json") as f:
        candidates = json.load(f)
    users = []
    cnt = 0
    for candidate in candidates:
        if skill in candidate["skills"]:
            users.append(candidate["name"])
            cnt += 1
            if settings["limit"] == cnt:
                return render_template("search.html", users=users, cnt=len(users))
    return render_template("search.html", users=users, cnt=len(users))


if __name__ == "__main__":
    app.run()
