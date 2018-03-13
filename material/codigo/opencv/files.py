import cv2

imagen = cv2.imread('imagen.png')
cv2.imwrite('imagen2.jpg', imagen)

grayImage = cv2.imread('imagen2.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('imagen_gris.jpg', grayImage)

