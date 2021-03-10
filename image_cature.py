from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180  #rotate image
camera.brightness = 60 #Aadjust brightness
camera.resolution = (1028,760)

camera.start_preview()
sleep(5)
camera.capture('img.jpg')
camera.stop_preview()