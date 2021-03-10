#Python code for Recording Video

from picamera import PiCamera
from time import sleep  
camera = picamera.PiCamera()  
camera.start_preview()    
camera.start_recording('/home/pi/Desktop/videofile.h264') 
sleep(5)
camera.stop_recording()
camera.stop_preview()
