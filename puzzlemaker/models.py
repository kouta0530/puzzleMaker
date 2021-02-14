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


def create_puzzleData(file, name, size, user_id):
    fdb = fireDB.Firebase(setting.cred, setting.option)
    id = str(uuid.uuid4())
    fdb.setblob(id + ".jpg")
    fdb.uploadImageToStorage(file)

    ref = fdb.getRef("puzzle/" + id)
    exp = datetime.datetime.now().replace(year=2030)
    data = {
        "user_id": user_id,
        "name": name,
        "ref": name + ".jpg",
        "size": size,
        "url": fdb.getImgSrc(exp)
    }
    fdb.insert(ref, data)

    fdb.close()
    del fdb

    return 1


def getYourPuzzle(user_id):
    fdb = fireDB.Firebase(setting.cred, setting.option)
    ref = fdb.getRef("puzzle")
    query = ref.order_by_child("user_id").equal_to(user_id)

    data = fdb.getQuearyData(query)

    fdb.close()
    del fdb

    return data


"""クライアントに渡す情報をまとめる """


def get_puzzleList():
    fdb = fireDB.Firebase(setting.cred, setting.option)
    ref = fdb.getRef("puzzle")
    puzzleList = fdb.getData(ref)

    fdb.close()
    del fdb

    return puzzleList


def get_pannel(query_id):
    fdb = fireDB.Firebase(setting.cred, setting.option)

    ref = fdb.getRef("puzzle").child(query_id)
    data = fdb.getQuearyData(ref)

    fdb.setblob(query_id + ".jpg")
    image = fdb.getImageDataromStorage()

    fdb.close()
    del fdb

    return image, data  # puzzles


def make_puzzle_gameset(data, image):
    ndarray = itp.read_img(image)
    Puzzles = itp.create_picies(data, ndarray)

    return Puzzles  # puzzles


def update(id, name, size):
    fdb = fireDB.Firebase(setting.cred, setting.option)
    ref = fdb.getRef("puzzle").child(id)

    renew_data = {"name": name, "size": size}
    fdb.update(ref, renew_data)

    fdb.close()
    del fdb


def delete(id):
    fdb = fireDB.Firebase(setting.cred, setting.option)
    ref = fdb.getRef("puzzle").child(id)

    fdb.delete(ref)
    fdb.setblob(id + ".jpg")
    fdb.deleteImg()

    fdb.close()
    del fdb

    return 0
