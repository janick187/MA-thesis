import cv2 as cv
import time
import requests
from pathlib import Path

api_url = "http://0.0.0.0:8080"

def processImage(name):
 url = "{}/image".format(api_url)
 files = {'images': open('webcam{}.jpg'.format(name), 'rb')}

 filename = Path('webcam{}_result.png'.format(name))
 response = requests.post(url, files=files)
 with open(filename, 'wb') as f:
  f.write(response.content)

camera = cv.VideoCapture(0)
name = 1

while(True):
 ret, image = camera.read()
 cv.imwrite('webcam'+str(name)+'.jpg', image)
 processImage(name)
 name += 1

camera.release()
cv.destroyAllWindows()

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)


