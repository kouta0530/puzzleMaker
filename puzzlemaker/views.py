from flask import render_template,request,session,redirect,url_for
from puzzlemaker import models
from puzzlemaker import app
#from flask_login import login_user,logout_user,login_required,LoginManager
import os


"""
login_manager = LoginManager()
login_manager.init_app(app)
"""
@app.route('/')
def index():
    return render_template("index.html")
"""
@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.User(user_id)

@app.route("/login",methods= ["GET","POST"])

def login():
    if(request.method == "GET" ):
        return render_template("login.html")
    
    name = request.form["name"]
    password = request.form["password"]
    
    check = User.Users.query.filter(User.Users.name == name).first()
    print(check.password)
    if(check is None):
        return render_template("login.html")
    
    if(check.password != password):
        return  render_template("login.html")

    user = User.User(os.urandom(24))
    login_user(user)
    User.update_session_id(check,user.get_id())

    return redirect(request.args.get('next') or url_for("myPage"))

@app.route("/logout")
@login_required

def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/mypage')
@login_required

def myPage():
    user_id = User.get_user_id(session["_user_id"])
    data = models.select_filter(models.Puzzle.user_id == user_id)
    works = models.get_puzzleList(data)

    return render_template("myPage.html",works = works)
"""

@app.route("/upload")
#@login_required

def form():
    return render_template("upload.html")

@app.route("/makepuzzle", methods = ["POST"])

def puzzle():
    file = request.files["file"].stream
    name = request.form["name"]
    size = int(request.form["size"])
    user_id = 1#User.get_user_id(session["_user_id"])

    ok = models.create_puzzleData(file,name,size,user_id)
    
    if(ok == 1):
        msg = "true"

    return render_template("index.html",msg = msg)

@app.route("/select")

def show_list():
    #datas = models.select_all()
    datas = models.get_puzzleList()
    return render_template("select.html",datas = datas)

@app.route("/play",methods = ["POST"])

def play_game():
    id = request.form["id"]

    image,data = models.get_pannel(id)
    puzzles = models.make_puzzle_gameset(data,image)

    return render_template("game.html",data = data,puzzles = puzzles)