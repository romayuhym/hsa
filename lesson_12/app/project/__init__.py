import os

from flask import (
    Flask,
    jsonify,
    request
)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(
        hello="world",
        server=os.getenv("SERVER"),
        heder=request.headers.get('GEOIP2')
    )
