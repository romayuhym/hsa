import os
import uuid

import boto3
from chalice import Chalice
from PIL import Image

app = Chalice(app_name='image_converter')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.on_s3_event(bucket=os.environ['MEDIA_BUCKET_NAME'],
                 events=['s3:ObjectCreated:*'])
def image_converter(event):
    image_path = f"/tmp/image_{event.key}"
    session = boto3.session.Session(
        aws_access_key_id=os.environ['AWS_KEY'],
        aws_secret_access_key=os.environ['AWS_SECRET']
    )
    s3 = session.client("s3")
    s3.download_file(event.bucket, event.key, image_path)

    image = Image.open(image_path)

    for image_type in ("png", "bmp", "gif"):
        result_path = f"/tmp/image_{uuid.uuid4().hex}.{image_type}"
        image.save(result_path)
        s3.upload_file(result_path, os.environ['RESULT_BUCKET_NAME'], f"{uuid.uuid4().hex}.{image_type}")
