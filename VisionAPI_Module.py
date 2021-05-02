import io
import os
import pandas as pd

from google.cloud import vision

# set the os GCP APP variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'.\VisionAPIKey.json'
# this is also just a placeholder for what was on my device
# will need to change this to the json

# client for image annotate vision
client = vision.ImageAnnotatorClient()

# image to send
file_name = os.path.abspath(
    r'.\example_01.png')
image_path = f'.\\{file_name}'

# reading in the image file to memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

# setting the image
image = vision.Image(content=content)

# making the request to vision
response = client.face_detection(image=image)

faceAnnotations = response.face_annotations

likehood = ('Unknown', 'Very Unlikely', 'Unlikely',
            'Possibly', 'Likely', 'Very Likely')

print('faces: ')
for face in faceAnnotations:
    print('')
    print('Detection Confidence {0}'.format(face.detection_confidence))
    print('Angry likelihood: {0}'.format(likehood[face.anger_likelihood]))
    print('Joy likelihood: {0}'.format(likehood[face.joy_likelihood]))
    print('Sorrow likelihood: {0}'.format(likehood[face.sorrow_likelihood]))
    print('Surprised likelihood: {0}'.format(
        likehood[face.surprise_likelihood]))
    print('Headwear likelihood: {0}'.format(
        likehood[face.headwear_likelihood]))

face_vertices = ['({0},{1})'.format(vertex.x, vertex.y)
                 for vertex in face.bounding_poly.vertices]
print('Face bound: {0}'.format(', '.join(face_vertices)))
print('\n')
