import io
import os

from google.cloud import vision
from google.cloud.vision_v1 import types

# set the os GCP APP variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'RU Hacks 2021-349d1f7b9c70.json'
# this is also just a placeholder for what was on my device
# will need to change this to the json

# client for image annotate vision
client = vision.ImageAnnotatorClient()

# image to send
file_name = os.path.abspath(
    r"C:\Users\DeRya\Desktop\My Engineering Career\Personal Projects & Skill Development\RUHacks 2021\example_01.png")  # placeholder

# reading in the image file to memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

# setting the image
image = types.Image(content=content)

# making the request to vision
response = client.label_detection(image=image)


labels = response.label_annotations

for label in labels:
    print(label)
