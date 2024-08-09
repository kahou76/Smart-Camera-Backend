from flask import Flask, request, render_template_string
from db import LocalDB
from db_car_plate_only import SimpleDB
from car_plate_recognition import CarPlateRecognition
# from camera import Camera
# from garage_door import GarageDoor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return app.send_static_file('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)