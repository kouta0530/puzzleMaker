#from test import db
import os
import random
import datetime
import uuid

from puzzlemaker import imageToPeace as itp
from puzzlemaker import fireDB
from puzzlemaker import setting

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
    fdb = fireDB.Firebase(setting.cred,setting.option)
    id = str(uuid.uuid4())
    fdb.setblob(id + ".jpg")
    fdb.uploadImageToStorage(file)
    
    ref = fdb.getRef("puzzle/" + id)
    exp = datetime.datetime.now()
    data = {
        "user_id":user_id,
        "name":name,
        "ref":name + ".jpg",
        "size":size,
        "url":fdb.getImgSrc(exp)
    }
    fdb.insert(ref,data)

    fdb.close()
    del fdb

    return 1

def getYourPuzzle(user_id):
    fdb = fireDB.Firebase(setting.cred,setting.option)
    ref = fdb.getRef("puzzle")
    query = ref.order_by_child("user_id").equal_to(user_id)

    data = fdb.getQuearyData(query)

    fdb.close()
    del fdb

    return data



"""クライアントに渡す情報をまとめる """
def get_puzzleList():
    fdb = fireDB.Firebase(setting.cred,setting.option)
    ref = fdb.getRef("puzzle")
    puzzleList = fdb.getData(ref)
    
    
    fdb.close()
    del fdb

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
    fdb = fireDB.Firebase(setting.cred,setting.option)

    ref = fdb.getRef("puzzle").child(query_id)
    data = fdb.getQuearyData(ref)

    fdb.setblob(query_id + ".jpg")
    image = fdb.getImageDataromStorage()

    fdb.close()
    del fdb

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

def update(id,name,size):
    fdb = fireDB.Firebase(setting.cred,setting.option)
    ref = fdb.getRef("puzzle").child(id)

    renew_data= {"name":name,"size":size}
    fdb.update(ref,renew_data)

    fdb.close()
    del fdb

def delete(id):
    fdb = fireDB.Firebase(setting.cred,setting.option)
    ref = fdb.getRef("puzzle").child(id)

    fdb.delete(ref)
    fdb.setblob(id + ".jpg")
    fdb.deleteImg()

    fdb.close()
    del fdb

    return 0