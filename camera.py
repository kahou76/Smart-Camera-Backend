from picamera2 import Picamera2

class Camera:

    def takePhoto(self):
        cam = Picamera2()
        photo_path = "/home/andychankahou76/Desktop/carplate.jpg"
        cam.start_and_capture_file(photo_path)
        cam.close()
        return photo_path
    