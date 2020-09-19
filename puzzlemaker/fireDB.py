import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db

class Firebase():
    def __init__(self,cred,option):
        self.cred = credentials.Certificate(cred)
        self.app = firebase_admin.initialize_app(self.cred,options = option)
        self.bucket = storage.bucket()

    def getRef(self,path):
        return db.reference(path)

    def getData(self,ref):
        return ref.get()

    def equal(self,query,param):
        return query.equal_to(param)

    def getQuearyData(self,query):
        return query.get()

    def insert(self,ref,data):
        return ref.set(data)

    def update(self,ref,data):
        return ref.update(data)

    def delete(self,ref):
        return ref.delete()

    def close(self):
        return firebase_admin.delete_app(self.app) 

    def setblob(self,ref):
        self.blob = self.bucket.blob(ref)

    def getImageDataromStorage(self):
        return self.blob.download_as_string()
    
    def uploadImageToStorage(self,data):
        return self.blob.upload_from_file(data)

    def getImgSrc(self,exp):
        return self.blob.generate_signed_url(exp)

    def deleteImg(self):
        return self.blob.delete()

