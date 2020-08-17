#from test import db
from puzzlemaker import imageToPeace as itp
import os
import random
from puzzlemaker import fireDB
import datetime
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path,encoding="utf-8_sig")

cred = os.environ["FIREBASE_JSON"]

option = {
    'databaseURL':os.environ["FIREBASE_DATABASE"],
    'storageBucket':os.environ["FIREBASE_STORAGE"]
}
fireBase = fireDB.Firebase(cred,option)

def init():
    return 0

def select_filter(filter):
    return 0

def select_all():
    #puzzle_data = Puzzle.query.order_by(Puzzle.id.desc()).all()
    return 0 #puzzle_data

def create_puzzleData(file,name,size,user_id):

    """
    img = itp.read_img(file)
    width,height = itp.get_img_WidthandHeight(img)
    link = "./test/static/img/" + name
    os.mkdir(link)

    itp.write_img(link + "/samnail.jpg",img)
    itp.create_picies(size,img,link)

    puzzle = Puzzle(name = name,size = size,link = link,width = width,height = height,user_id = user_id)
    db.session.add(puzzle)
    db.session.commit()
    """

    fireBase.setblob(name + ".jpg")
    fireBase.uploadImageToStorage(file)
    
    ref = fireBase.getRef("puzzle/" + name)
    exp = datetime.datetime(3000,7,30)
    data = {
        "id":user_id,
        "name":name,
        "ref":name + ".jpg",
        "size":size,
        "url":fireBase.getImgSrc(exp)
    }
    fireBase.insert(ref,data)


    return 1

"""クライアントに渡す情報をまとめる """
def get_puzzleList():
    ref = fireBase.getRef("puzzle")
    data = fireBase.getData(ref)
    
    puzzleList = [data[key] for key in data]
    
    return puzzleList

def get_pannel(query_id):
    """
    puzzle = select_filter(Puzzle.id == query_id)
    size = puzzle[0].size
    name = puzzle[0].name
    width = puzzle[0].width
    height = puzzle[0].height

    data = {
        "name":name,
        "size":size,
        "width":width,
        "height":height
    }
    """
    fireBase.setblob(query_id + ".jpg")
    image = fireBase.getImageDataromStorage()

    ref = fireBase.getRef("puzzle").child(query_id)
    data = fireBase.getData(ref)

    return image,data#puzzles


def make_puzzle_gameset(data,image):
    """
    puzzle = select_filter(Puzzle.id == query_id)
    size = puzzle[0].size
    name = puzzle[0].name

    puzzles =[]
    for i in range(size * size):
        
        puzzle = {
            "id":i,
            "link":"./static/img/" + name + "/" + str(i) + ".jpg"
        }
        puzzles.append(puzzle)
    
    random.shuffle(puzzles)
    """
    ndarray = itp.read_img(image)
    Puzzles = itp.create_picies(data,ndarray)


    return Puzzles#puzzles