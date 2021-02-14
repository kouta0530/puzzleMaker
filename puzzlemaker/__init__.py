from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

import puzzlemaker.views

CORS(app, allow_headers="Content-Type")
