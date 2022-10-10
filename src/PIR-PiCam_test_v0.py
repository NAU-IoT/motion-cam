"""
Work in program python script that captures a photo
with the PiCam if motion is detected from the PIR
sensor
"""
from io import BytesIO
import RPi.GPIO as GPIO
import time
from datetime import datetime
import numpy as np
import picamera

# initialize GPIO 4 (pin the PIR is attached to)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# initialize PiCam, set resolution, start preview
PiCam = picamera.PiCamera()
PiCam.resolution = (1024, 768)
PiCam.start_preview()

# set var for datetime import setting current date and time
format_time = datetime.now()
current_stamp = format_time.strftime("%m_%d_%Y_%H:%M:%S.%f")

# define path for output
file_name = "/home/pi/work/IoT/my_projs/PIR_PiCam_proj/imgs/test-img_" + current_stamp + ".jpg"
# file_name = "/home/pi/work/IoT/my_projs/PIR_PiCam_proj/imgs/img_" + str(time.time()) + ".jpg"

# method for when motion is detected, PiCam will take snapshot
def PIR_capture():
    # when motion is detected this block will execute
    while True:
        if GPIO.input(4):
            print("\nActivity Detected!\n")
            PiCam.capture(file_name)
            print("\nPicture Captured!\n")
        else:
            print("\nClear\n");
        time.sleep(5)

def main():
    PIR_capture()

if __name__ == "__main__":
    main()

