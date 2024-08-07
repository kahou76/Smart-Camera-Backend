import requests
import base64
import json
import os
from dotenv import load_dotenv

load_dotenv()

class CarPlateRecognition:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.api_url = 'https://api.openalpr.com/v3/recognize'

    def recognize_plate(self, image_path):
        url = f'{self.api_url}?country=us&secret_key={self.api_key}'

        with open(image_path, 'rb') as image_file:
            files = {
                'image': image_file
            }

            response = requests.post(url, files=files)

            if response.status_code == 200:
                return response.json()
            else:
                print(json.dumps(response.json(), indent=2))




