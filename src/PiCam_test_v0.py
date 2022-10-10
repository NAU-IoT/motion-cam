from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)


sleep(1)
#camera.capture('/home/pi/Work/IoT/my_projs/PIR_PiCam_proj/imgs/picture.jpg')
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

cv2.imshow("Image", image)
cv2.waitkey(0)
