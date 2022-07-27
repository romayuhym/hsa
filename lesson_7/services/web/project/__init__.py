import os
import random

from flask import (
    Flask,
    send_from_directory,
    jsonify,
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route("/media/<path:filename>")
def mediafiles(filename):
    file_list = [
        "4456190.png",
        "05crouse-square640.jpeg",
        "average-time-to-run-5k-1588696912.jpeg",
        "how-to-start-running-5k-indybest-0.jpeg"
    ]
    return send_from_directory(f"{os.getenv('APP_FOLDER')}/project/media", random.choice(file_list))
