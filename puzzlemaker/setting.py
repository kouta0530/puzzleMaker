"""
from dotenv import load_dotenv
from os.path import join, dirname
"""
import os
import json

"""
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path,encoding="utf-8_sig")
"""
key = os.environ["CRYPT_KEY"].encode()
iv = os.environ["IV"].encode()
cred = os.environ["FIREBASE_KEY"]
cred = json.loads(cred)

option = {
    'databaseURL':os.environ["FIREBASE_DATABASE"],
    'storageBucket':os.environ["FIREBASE_STORAGE"]
}