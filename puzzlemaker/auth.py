import hashlib
import Crypto.Cipher.AES as AES
import hashlib
import uuid
import base64

from puzzlemaker import session
from puzzlemaker import setting
from puzzlemaker import fireDB

def encrypt(plainText):
    if(plainText == ""):
        return 0

    aes = AES.new(setting.key,AES.MODE_EAX,setting.iv)

    cipherText = aes.encrypt(plainText.encode("utf-8"))

    return base64.b64encode(cipherText)

def decrypto(cipherText):
    cipherText = base64.b64decode(cipherText)
    
    if(cipherText == ""):
        return 0
    de = AES.new(setting.key,AES.MODE_EAX,setting.iv)

    plainText = de.decrypt(cipherText)

    return plainText.decode("utf-8")

def makeHash(data,salt):
    data = data + salt
    result = hashlib.sha256(data.encode()).hexdigest()
    return result


def signup(email="",password=""):

    if(email is "" or password is ""):
        return 0
    
    emailEncrypt = encrypt(email)
    fdb = fireDB.Firebase(setting.cred,setting.option)
    
    ref = fdb.getRef("users/" + emailEncrypt.decode())
    user = fdb.getData(ref)

    if(user is not None):
        fdb.close()
        del fdb
        return 1

    salt = str(uuid.uuid4())
    result = {
        "id": str(uuid.uuid4()),
        "salt": salt,
        "password": makeHash(password,salt)
    }

    fdb.insert(ref,result)
    fdb.close()
    del fdb

    token = session.makeSession(result["id"])

    return token

def login(email = "",password = ""):

    if(email is "" or password is ""):
        return 0

    emailEncrypt = encrypt(email)
    fdb = fireDB.Firebase(setting.cred,setting.option)
    
    ref = fdb.getRef("users/" + emailEncrypt.decode())
    user = fdb.getData(ref)

    fdb.close()
    del fdb

    if(user is None):
        return 1

    if(user["password"] != makeHash(password,user["salt"])):
        return 1
    else:
        return session.makeSession(user["id"])

def logout(userId = "",token = ""):
    if(userId == "" or token == ""):
        return 0

    session.revokeSession(userId,12)

    