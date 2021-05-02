import sys
import io
import os
import pandas as pd

from google.cloud import vision


def vision_function():
    # set the os GCP APP variable
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./VisionAPIKey.json'
    # this is also just a placeholder for what was on my device
    # will need to change this to the json

    # client for image annotate vision
    client = vision.ImageAnnotatorClient()

    # image to send
    file_name = os.path.abspath(sys.argv[1])
    image_path = f'./{file_name}'

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

    highest = 0
    mood = ""

    for face in faceAnnotations:

        if face.anger_likelihood > highest:
            highest = face.anger_likelihood
            mood = "Angry"

        if face.joy_likelihood > highest:
            highest = face.joy_likelihood
            mood = "Joy"
        
        if face.sorrow_likelihood > highest:
            highest = face.sorrow_likelihood
            mood = "Sorrow"
        
        if face.surprise_likelihood > highest:
            highest = face.surprise_likelihood
            mood = "Surprised"


    print(mood)



# in this module, I intend on getting data and sending a one word mood (happy/sorrowful/angry) to the Sentence Generator
# To do this, I must be able to detect if the output contains "Joy likelihood: likely" to send a joy mood
# The mood_function() will find this from the results




vision_function()
