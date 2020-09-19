import uuid
import datetime
import uuid

from puzzlemaker import setting
from puzzlemaker import fireDB

def revokeSession(userId,exp):
    date = datetime.datetime.now()
    hour = date.hour - exp

    if(hour < 0):
        date = date.replace(day = date.day - 1)
        date = date.replace(hour = 24 + hour)

    fdb = fireDB.Firebase(setting.cred,setting.option)
    ref = fdb.getRef("session").child(userId)
    res = fdb.getData(ref)
    
    if(res is not None):
        ref.delete()
    
    fdb.close()
    del fdb
    
def makeSession(userId):
    print(datetime.datetime.now())
    result = {
        "token": str(uuid.uuid4()),
        "create": str(datetime.datetime.now())
    }

    revokeSession(userId,12)

    fdb = fireDB.Firebase(setting.cred,setting.option)
    ref = fdb.getRef("session/" + userId)
    fdb.insert(ref,result)

    res = fdb.getData(ref)
    res["userId"] = userId
    fdb.close()
    del fdb


    return res
