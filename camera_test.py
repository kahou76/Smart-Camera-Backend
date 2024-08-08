from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()
picam2.start_and_record_video("/home/andychankahou76/Desktop/new_video2.mp4", duration=5, show_preview=False)
picam2.close()