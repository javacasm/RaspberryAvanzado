import os
import cv2
import math

## Capturamos la imagen con la cámara de la Raspberry Pi
os.system("raspistill -o image.jpg")
## Cargamos la imagen
img = cv2.imread("/home/pi/Desktop/image.jpg")
grey = cv2.imread("/home/pi/Desktop/image.jpg",0) #0 para la escala de grises


## convertimos la imagen en grises en una en blanco y negro
ret, thresh = cv2.threshold(grey,50,255,cv2.THRESH_BINARY)

## Re-escalamos las imágenes
img = resizeImage(img)
thresh = resizeImage(thresh)
## las mostramos en pantalla
cv2.imshow("thresh",thresh)
cv2.imshow("img",img)
