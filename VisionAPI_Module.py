import sys
import io
import os
import pandas as pd

from google.cloud import vision


def vision_function():
    # set the os GCP APP variable
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\DeRya\Desktop\My Engineering Career\Personal Projects & Skill Development\RUHacks 2021\RU Hacks 2021-349d1f7b9c70.json'
    # this is also just a placeholder for what was on my device
    # will need to change this to the json

    # client for image annotate vision
    client = vision.ImageAnnotatorClient()

    # image to send
    file_name = os.path.abspath(
        r'C:\Users\DeRya\Desktop\My Engineering Career\Personal Projects & Skill Development\RUHacks 2021\example_01.png')
    image_path = f'.\\{file_name}'

    # reading in the image file to memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    # setting the image
    image = vision.Image(content=content)

    # making the request to vision
    response = client.face_detection(image=image)

    faceAnnotations = response.face_annotations

    likelihood = ('Unknown', 'Very Unlikely', 'Unlikely',
                  'Possibly', 'Likely', 'Very Likely')

    print('faces: ')
    for face in faceAnnotations:
        print('')
        print('Detection Confidence {0}'.format(face.detection_confidence))
        print('Angry likelihood: {0}'.format(
            likelihood[face.anger_likelihood]))
        print('Joy likelihood: {0}'.format(likelihood[face.joy_likelihood]))
        print('Sorrow likelihood: {0}'.format(
            likelihood[face.sorrow_likelihood]))
        print('Surprised likelihood: {0}'.format(
            likelihood[face.surprise_likelihood]))
        print('Headwear likelihood: {0}'.format(
            likelihood[face.headwear_likelihood]))

    face_vertices = ['({0},{1})'.format(vertex.x, vertex.y)
                     for vertex in face.bounding_poly.vertices]

    print('Face bound: {0}'.format(', '.join(face_vertices)))
    print('\n')

# in this module, I intend on getting data and sending a one word mood (happy/sorrowful/angry) to the Sentence Generator
# To do this, I must be able to detect if the output contains "Joy likelihood: likely" to send a joy mood
# The mood_function() will find this from the results


def mood_function(mood):
    # assume the moods are mutually exclusive (yes I know it's a bad assumption but we have to make do with what we have right now)
    # if results contains a minimum likelihood of at least: likely
    if results.find('Angry likelihood: Likely') > -1:
        # the way the results.find() thing works is that if the text we're looking for doesn't exist in the string we're looking at
        # it will return -1. If the text we're looking for does exist, then it will return the index where it is located, with that index > -1
        mood = 'Angry'

    elif results.find('Joy likelihood: Likely') > -1:
        mood = 'Joy'

    elif results.find('Sorrow likelihood: Likely') > -1:
        mood = 'Sorrow'

    elif results.find('Surprised likelihood: Likely') > -1:
        mood = 'Surprised'

    else:
        # i don't know what to put in for here, so i'll just say mood = any
        mood = 'Any'

    return(mood)


def main():

    results = vision_function()
    mood_function()
    # do I really need the above mood_function() if Sentence_Generator.py
    # Is going to call it? If not, then I'll just get rid of the above.


main()
