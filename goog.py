import io
import os
from google.cloud import vision
from google.cloud.vision import types


def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

for i in range(10):
    PATH=os.getcwd()
    print('For picture'+str(i)+':')
    detect_labels(PATH+'/'+'img00'+str(i)+'.jpg')

for i in range(10,12):
    PATH=os.getcwd()
    print('For picture'+str(i)+':')
    detect_labels(PATH+'/'+'img0'+str(i)+'.jpg')
    