import json
from db import LocalDB
from db_car_plate_only import SimpleDB
from car_plate_recognition import CarPlateRecognition
from camera import Camera

def main():
    None

def carPlateTestWithCar():
    cplr = CarPlateRecognition()
    result = cplr.recognize_plate(r"C:\Users\silas\Downloads\car_plate_test.jpg")
    
    vehicles_info = result.get('results')

    if not vehicles_info:
        print("No car detected")

    for each in vehicles_info:
        plate_number = each.get('plate')
        print(f"Plate_number: {plate_number}")


def carPlateTestNoCar():
    cplr = CarPlateRecognition()
    result = cplr.recognize_plate(r"C:\Users\silas\Downloads\image_with_no_car.jpg")
    vehicles_info = result.get('results')

    if not vehicles_info:
        print("No car detected")

    for each in vehicles_info:
        plate_number = each.get('plate')
        print(f"Plate_number: {plate_number}")

def operationTest():
    # add a vehicle car plate, and check db if the car plate exist
    db = SimpleDB()
    db.add_vehicle('BQU4895', 'ValidVehicle')

    cplr = CarPlateRecognition()
    result = cplr.recognize_plate(r"C:\Users\silas\Downloads\car_plate_test.jpg")

    vehicles_info = result.get('results')

    if not vehicles_info:
        print("No car detected")
    
    for each in vehicles_info:
        plate_number = each.get('plate')
        if db.is_vehicle_existed(plate_number, 'BannedVehicle'):
            print("it is banned vehicle!!")
        
        if db.is_vehicle_existed(plate_number, 'ValidVehicle'):
            print("it is valid vehicle!")
        

def dbTest():
    db = LocalDB()

    db.add_vehicle(
        'ABC123',
        'camary',
        'No',
        'Red',
        'Toyota',
        'Corolla',
        'ValidVehicle'
    )

    # Check if the vehicle is in the valid vehicle table
    vehicle = db.is_vehicle_info_correct(
        'ABC123',
        'camary',
        'No',
        'Red',
        'Toyota',
        'Corolla',
        'ValidVehicle'
    )
    print(vehicle)

    # Delete the vehicle from the valid vehicle table
    db.delete_vehicle('ABC123', 'ValidVehicle')

    # Check again to confirm deletion
    vehicle = db.is_vehicle_info_correct(
        'ABC123',
        'camary',
        'No',
        'Red',
        'Toyota',
        'Corolla',
        'ValidVehicle'
    )
    print(vehicle)

def cameraTakePhotoTest():
    db = SimpleDB()
    db.add_vehicle('BCW7229', 'ValidVehicle')

    cam = Camera()
    photo_path = cam.takePhoto()

    cplr = CarPlateRecognition()
    result = cplr.recognize_plate(photo_path)

    vehicles_info = result.get('results')

    if not vehicles_info:
        print("No car detected")
    
    for each in vehicles_info:
        plate_number = each.get('plate')
        if db.is_vehicle_existed(plate_number, 'BannedVehicle'):
            print("it is banned vehicle!!")
        
        if db.is_vehicle_existed(plate_number, 'ValidVehicle'):
            print(plate_number)
            print("it is valid vehicle!")



if __name__ == '__main__':
    cameraTakePhotoTest()