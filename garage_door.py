import time
import RPi.GPIO as GPIO
    
GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector not the chip
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP) # set up pin ?? (one of the above listed pins) as an input with a pull-up resistor
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP) # set up pin ?? (one of the above listed pins) as an input with a pull-up resistor
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.HIGH)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.HIGH)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.HIGH)

class GarageDoor:
    def OpenDoor():
        GPIO.output(7, GPIO.LOW)
        time.sleep(1)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(2)