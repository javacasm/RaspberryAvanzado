import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
if camlist:
    cam = pygame.caemra.Camera(camlist[0],(640,480))
    cam.start()
    image = cam.get_image()
    cam.set_controls(hflip = True, vflip = False)
    print camera.get_controls()
else :
    print "No camera detected"
