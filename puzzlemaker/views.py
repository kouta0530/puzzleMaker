from flask import render_template, request, session, redirect, url_for, make_response
from puzzlemaker import models
from puzzlemaker import app
from puzzlemaker import auth
import os
import json
import datetime

user_is_authenticated = False


@app.route('/')
def index():
    return render_template("index.html", auth=user_is_authenticated)


@app.route("/signup", methods=["POST"])
def signup():
    global user_is_authenticated

    formData = request.json

    email = formData["email"]
    password = formData["password"]
    token = auth.signup(email, password)

    if(token == 0):
        return json.dumps({"user_is_authenticated": False})

    if(token == 1):
        return json.dumps({"user_is_authenticated": False, "message": "emailがすでに登録されています"})

    expires = int(datetime.datetime.now().timestamp()) + 60 * 60 * 24
    user_is_authenticated = True

    res = make_response(json.dumps({"user_is_authenticated": True}))
    res.set_cookie("token", expires=expires, value=json.dumps(token))

    return res


@app.route("/login", methods=["GET", "POST"])
def login():
    global user_is_authenticated
    if(request.method == "GET"):
        return render_template("login.html", auth=user_is_authenticated)

    email = request.form["email"]
    password = request.form["password"]
    token = auth.login(email, password)

    if(token == 0):
        return render_template("login.html", err="パスワードとemailを入力してください")
    if(token == 1):
        return render_template("login.html", err="パスワードかemailが間違っています")

    expires = int(datetime.datetime.now().timestamp()) + 60 * 60 * 24
    user_is_authenticated = True

    res = make_response(redirect(url_for("index")))
    res.set_cookie("token", expires=expires, value=json.dumps(token))

    return res


@app.route("/logout")
def logout():
    cookie = request.cookies.get("token", None)
    if(cookie is None):
        print("cookie is none")
        return redirect(url_for("index"))

    token = json.loads(cookie)
    auth.logout(token["userId"], token["token"])

    global user_is_authenticated
    user_is_authenticated = False

    res = make_response(redirect(url_for("index")))
    res.delete_cookie("token")

    return res


@app.route('/mypage')
def myPage():
    cookie = request.cookies.get("token", None)
    if(cookie is None):
        return redirect(url_for("login"))

    token = json.loads(cookie)

    data = models.getYourPuzzle(token["userId"])

    return render_template("myPage.html", data=data, len=len(data), auth=user_is_authenticated)


@app.route("/upload")
# @login_required
def form():
    cookie = request.cookies.get("token", None)
    if(cookie is None):
        return redirect(url_for("login"))

    return render_template("upload.html", auth=user_is_authenticated)


@app.route("/makepuzzle", methods=["POST"])
def puzzle():
    cookie = request.cookies.get("token", "anymous")
    user_id = json.loads(cookie)["userId"]

    file = request.files["file"].stream
    name = request.form["name"]
    size = int(request.form["size"])
    # User.get_user_id(session["_user_id"])

    ok = models.create_puzzleData(file, name, size, user_id)

    return render_template("index.html", auth=user_is_authenticated)


@app.route("/select")
def show_list():
    datas = models.get_puzzleList()
    response = [datas[k] for k in datas]
    print(response)

    return json.dumps(response)


@app.route("/play/<string:id>")
def play_game(id):
    image, data = models.get_pannel(id)
    puzzles = models.make_puzzle_gameset(data, image)

    return render_template("game.html", data=data, puzzles=puzzles, auth=user_is_authenticated)


@app.route("/work/<string:id>")
def work(id):

    return render_template("updateForm.html", id=id)


@app.route("/update/<string:id>", methods=["POST"])
def update(id):
    name = request.form.get("name")
    size = request.form.get("size")
    if(name == ""):
        return redirect(url_for("myPage"))

    models.update(id, name, int(size))

    return redirect(url_for("myPage"))


@app.route("/delete/<string:id>", methods=["POST"])
def delete(id):
    if(request.form.get("delete") != "DELETE"):
        return redirect(url_for("myPage"))

    models.delete(id)

    return redirect(url_for("myPage"))
