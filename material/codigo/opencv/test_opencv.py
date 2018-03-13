import os
import cv2
import math

# Usamos el metodo resize para re-escalar
def resizeImage(img):
        dst = cv2.resize(img,None, fx=0.25, fy=0.25, interpolation =
        cv2.INTER_LINEAR)
        return dst

## Capturamos la imagen con la camara de la Raspberry Pi
os.system("raspistill -o image.jpg")
## Cargamos la imagen
img = cv2.imread("./image.jpg")
grey = cv2.imread("./image.jpg",0) #0 para la escala de grises

cv2.imshow("img",img)
cv2.imshow("grey",grey)
## convertimos la imagen en grises en una en blanco y negro
ret, thresh = cv2.threshold(grey,50,255,cv2.THRESH_BINARY)
## Re-escalamos las imagenes
img = resizeImage(img)
thresh = resizeImage(thresh)
## las mostramos en pantalla
cv2.imshow("thresh",thresh)

