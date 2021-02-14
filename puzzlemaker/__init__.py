import puzzlemaker.views
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)

CORS(app, allow_headers="Content-Type")
