import os

from flask import Flask, send_file
from PIL import Image, ImageDraw

app = Flask(__name__)


@app.route("/image.png")
def hello_world():
    img = Image.new('RGB', (100, 30), color=(73, 109, 137))

    d = ImageDraw.Draw(img)
    d.text((10, 10), os.getenv("SERVER"), fill=(255, 255, 0))

    img.save("/usr/src/app/pil_text.png")
    return send_file("/usr/src/app/pil_text.png", mimetype='image/png')
