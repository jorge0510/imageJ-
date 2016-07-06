import picamera

import os

import RPi.GPIO as GPIO


camera = picamera.PiCamera()


camera.resolution = (1024, 768)

GPIO.setmode(GPIO.BCM) 

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

camera.start_preview()





while 1:

     print "waitting fot the buton to be pushed..."

     GPIO.wait_for_edge(21, GPIO.FALLING)

     print "taking picture"

     camera.capture('image.png', resize=(200,127))


     camera.stop_preview()


     print "Processing..."


     os.system("imagej -p 1 image.png -p easy2.txt")


     break 
