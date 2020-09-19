from flask import render_template,request,session,redirect,url_for,make_response
from puzzlemaker import models
from puzzlemaker import app
from puzzlemaker import auth
#from flask_login import login_user,logout_user,login_required,LoginManager
import os
import json
import datetime

"""
login_manager = LoginManager()
login_manager.init_app(app)
"""
user_is_authenticated = False

@app.route('/')
def index():
    return render_template("index.html",auth=user_is_authenticated)
"""
@login_manager.user_loader
def load_user(user_id):
    return 0
"""
@app.route("/signup",methods = ["POST"])

def signup():
    global user_is_authenticated

    email = request.form["email"]
    password = request.form["password"]
    token = auth.signup(email,password)

    if(token == 0):
        return render_template("index.html",err = "emailとパスワードを入力してください")

    if(token == 1):
        return render_template("index.html",err="既にemailが使われています")

    expires = int(datetime.datetime.now().timestamp()) + 60 * 60 * 24
    user_is_authenticated = True

    res = make_response(redirect(url_for("index")))
    res.set_cookie("token",expires = expires,value = json.dumps(token))

    return res



@app.route("/login",methods= ["GET","POST"])

def login():
    global user_is_authenticated
    if(request.method == "GET"):
        return render_template("login.html",auth=user_is_authenticated)
    
    email = request.form["email"]
    password = request.form["password"]
    token = auth.login(email,password)

    if(token == 0):
        return render_template("login.html",err= "パスワードとemailを入力してください")
    if(token == 1):
        return render_template("login.html",err= "パスワードかemailが間違っています")

    expires = int(datetime.datetime.now().timestamp()) + 60 * 60 * 24
    user_is_authenticated = True

    res = make_response(redirect(url_for("index")))
    res.set_cookie("token",expires = expires,value = json.dumps(token))

    return res

@app.route("/logout")

def logout():
    cookie = request.cookies.get("token",None)
    if(cookie is None):
        print("cookie is none")
        return redirect(url_for("index"))
    
    token = json.loads(cookie)
    auth.logout(token["userId"],token["token"])

    global user_is_authenticated
    user_is_authenticated = False
    
    res = make_response(redirect(url_for("index")))
    res.delete_cookie("token")

    return res

@app.route('/mypage')

def myPage():
    cookie = request.cookies.get("token",None)
    if(cookie is None):
        return redirect(url_for("login"))

    token = json.loads(cookie)

    data = models.getYourPuzzle(token["userId"])

    return render_template("myPage.html",data = data,len= len(data),auth = user_is_authenticated)

@app.route("/upload")
#@login_required

def form():
    cookie = request.cookies.get("token",None)
    if(cookie is None):
        return redirect(url_for("login"))

    return render_template("upload.html",auth=user_is_authenticated)

@app.route("/makepuzzle", methods = ["POST"])

def puzzle():
    cookie = request.cookies.get("token","anymous")
    user_id = json.loads(cookie)["userId"]

    file = request.files["file"].stream
    name = request.form["name"]
    size = int(request.form["size"])
    #User.get_user_id(session["_user_id"])

    ok = models.create_puzzleData(file,name,size,user_id)
    
    return render_template("index.html",auth=user_is_authenticated)

@app.route("/select")

def show_list():
    #datas = models.select_all()
    datas = models.get_puzzleList()
    return render_template("select.html",datas = datas,auth=user_is_authenticated)

@app.route("/play",methods = ["POST"])

def play_game():
    id = request.form["id"]

    image,data = models.get_pannel(id)
    puzzles = models.make_puzzle_gameset(data,image)

    return render_template("game.html",data = data,puzzles = puzzles,auth=user_is_authenticated)