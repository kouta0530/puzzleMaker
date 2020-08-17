import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db

class Firebase():
    def __init__(self,cred,option):
        self.cred = credentials.Certificate(cred)
        firebase_admin.initialize_app(self.cred,options = option)
        self.bucket = storage.bucket()

    def getRef(self,ref):
        return db.reference(ref)

    def getData(self,query):
        return query.get()

    def insert(self,query,data):
        return query.set(data)

    def update(self,query,data):
        return query.update(data)

    def setblob(self,ref):
        self.blob = self.bucket.blob(ref)

    def getImageDataromStorage(self):
        return self.blob.download_as_string()
    
    def uploadImageToStorage(self,data):
        return self.blob.upload_from_file(data)

    def getImgSrc(self,exp):
        return self.blob.generate_signed_url(exp)

