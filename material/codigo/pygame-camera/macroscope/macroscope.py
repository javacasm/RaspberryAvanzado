#!/usr/bin/env python

# RPi Macroscope by 648.ken@gmail.com, December 2017
# https://www.raspberrypi.org/learning/push-button-stop-motion/worksheet/
# https://raspberrypi.stackexchange.com/questions/28302/python-script-with-loop-that-detects-keyboard-input

import os, sys, time
from picamera import PiCamera
from time import sleep
from datetime import datetime, timedelta
from gpiozero import Button, LED
import pygame
import RPi.GPIO as GPIO
from PIL import Image


# Pin assignments
zoomOutButton = 22
zoomInButton = 27
redButton = 17
LEDring = 18
greenLED = 4

# Flags / counters
zoomOutPressed = False
zoomInPressed = False
redButtonPressed = False
redPressCount = 0
LEDringOn = True
OUT = True
IN = False
timeLapseSeconds = 5
msgPostTime = datetime.now()
msgShowTime = 5
helpScreen = False

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(zoomOutButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(zoomInButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(redButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEDring, GPIO.OUT)
GPIO.setup(greenLED, GPIO.OUT)
GPIO.output(LEDring, GPIO.HIGH)
GPIO.output(greenLED, GPIO.LOW)

# Pygame / camera setup
pygame.init()
pygame.display.set_mode((1,1))
camera = PiCamera()
zoomfactor = 0
camera.start_preview()
camera.vflip = True
camera.hflip = True

os.chdir('/boot') # save folders to /boot directory


def zoom(direction):
    global zoomfactor
    if direction == IN:
        zoomfactor = zoomfactor + 10
        if zoomfactor > 40:
            zoomfactor = 40
    if direction == OUT:
        zoomfactor = zoomfactor - 10
        if zoomfactor < 0:
            zoomfactor = 0
    zoom1 = zoomfactor / 100.0
    zoom2 = 1.0 - zoom1 * 2
    camera.zoom = (zoom1, zoom1, zoom2, zoom2)
    print(camera.zoom, zoomfactor)


def getFileName():
    last_date = time.strftime("%Y%m%d", time.localtime())
    img_count = 0

    ds = time.strftime("%Y%m%d", time.localtime())

    #Figure out if USB drive attached
    dirList = os.listdir('/media/pi')
    if dirList:
        os.chdir('/media/pi/%s' % dirList[0])
    else:
        os.chdir('/boot')

    if not os.path.isdir(ds):
        os.mkdir(ds)
        print("%s directory created." % ds)
    else: # find highest number
        dir_list = os.listdir(os.path.join(os.getcwd(), ds))
        max_count = 0
        for file_name in dir_list:
            try:
                count = int(file_name.split("_")[0])
            except ValueError:
                count = 0
            if count >= max_count:
                max_count = count + 1
        img_count = max_count
        print("img_count = %s" % img_count)

    start_time = time.localtime()
    ds = time.strftime("%Y%m%d", start_time)
    ts = time.strftime("%H%M", start_time)

    if last_date != ds and os.path.isdir(last_date):
        img_count = 0
        last_date = time.strftime("%Y%m%d", time.localtime())

    if not os.path.isdir(ds):
        os.mkdir(ds)
        logging.debug("%s directory created." % ds)
        img_count = 0

    new_name =  '%s/%04d_%s_%s' % (ds, img_count, ds, ts)
    return new_name


def takePicture():
    global msgPostTime
    new_name = getFileName()
    GPIO.output(greenLED, GPIO.HIGH)
    camera.annotate_text = ''
    camera.capture('%s.jpg' % new_name, use_video_port=True)
    print('capture %s/%s.jpg' % (os.getcwd(), new_name))
    camera.annotate_text = 'Saved %s/%s.jpg' % (os.getcwd(), new_name)
    msgPostTime = datetime.now()
    GPIO.output(greenLED, GPIO.LOW)


def takeVideo():
    global msgPostTime
    new_name = getFileName()
    o = camera.add_overlay(red_dot.tobytes(), size=red_dot.size, layer=3)
    camera.annotate_text = ''
    camera.start_recording('%s.h264' % new_name)
    print('recording')
    GPIO.output(greenLED, GPIO.HIGH)
    while camera.recording:
        camera.wait_recording(1)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                camera.stop_recording()
                GPIO.output(greenLED, GPIO.LOW)
                print('video %s.h264' % new_name)
                camera.annotate_text = 'Saved %s.h264' % new_name
                camera.remove_overlay(o)
                if event.key == pygame.K_q:
                    GPIO.output(LEDring, GPIO.LOW)
                    sys.exit()

    os.system('sudo MP4Box -add %s.h264 %s.mp4' % (new_name, new_name)) 
    camera.annotate_text = 'Converted to %s.mp4' % new_name
    msgPostTime = datetime.now()


def takeSequence(seconds):
    o = camera.add_overlay(green_dot.tobytes(), size=green_dot.size, layer=3)
    print('starting sequence')
    while True:
        camera.annotate_text = ''
        takePicture()
        nextShot = (datetime.now() + timedelta(seconds=seconds)).replace(microsecond=0)
        while datetime.now() < nextShot:
            sleep(1)
            txt = str(int((nextShot- datetime.now()).total_seconds()))
            camera.annotate_text = txt
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    camera.remove_overlay(o)
                    camera.annotate_text = ''
                    if event.key == pygame.K_q:
                        GPIO.output(LEDring, GPIO.LOW)
                        sys.exit()
                    else:
                        print('end sequence')
                        return

red_dot = Image.open(os.path.join('macroscope', 'red_dot.png'))
green_dot = Image.open(os.path.join('macroscope', 'green_dot.png'))
help = Image.open(os.path.join('macroscope', 'help.png'))

while True:
    # button handling
    if(not GPIO.input(zoomInButton)):
        if not zoomInPressed:
           zoomInPressed = True
           zoom(IN)
    else:
        zoomInPressed = False

    if(not GPIO.input(zoomOutButton)):
        if not zoomOutPressed:
            zoomOutPressed = True
            zoom(OUT)
    else:
        zoomOutPressed = False

    # Clear message
    if (datetime.now() - timedelta(seconds=msgShowTime)) <  msgPostTime:
        pass
    else:
        camera.annotate_text = ''

    if(not GPIO.input(redButton)):
        while (not GPIO.input(redButton)): # button still pressed
            redPressCount += 1
            if redPressCount == 10:
                if LEDringOn:
                    GPIO.output(LEDring, GPIO.LOW)
                    LEDringOn = False
                else:
                    GPIO.output(LEDring, GPIO.HIGH)
                    LEDringOn = True
            if redPressCount > 20:
                camera.stop_preview()
                GPIO.output(LEDring, GPIO.LOW)
                os.system('sudo shutdown now')
            sleep(0.1)
        if redPressCount < 10:
            takePicture()
    else:
        redPressCount = 0

    # key handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GPIO.output(18, GPIO.LOW)
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_h:
                if not helpScreen:
                    o = camera.add_overlay(help.tobytes(), size=help.size, layer=3)
                    helpScreen = True
                else:
                    camera.remove_overlay(o)
                    helpScreen = False
            if event.key == pygame.K_SPACE:
                takePicture()

            if event.key == pygame.K_v:
                takeVideo()

            if event.key == pygame.K_t:
                takeSequence(timeLapseSeconds)

            if event.key == pygame.K_a:
                print('camera.resolution:     ', camera.resolution)
                print('camera.iso:            ', camera.iso)
                print('camera.exposure_speed: ', camera.exposure_speed)
                print('camera.awb_gains:      ', camera.awb_gains)
                print('camera.awb_mode:       ', camera.awb_mode)

            if event.key == pygame.K_q:
                camera.stop_preview()
                GPIO.output(18, GPIO.LOW)
                dirList = os.listdir('/media/pi')
                if dirList:
                    os.system('sync') 
                    os.system('sudo umount /media/pi/%s' % dirList[0])
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_MINUS or event.key == pygame.K_EQUALS:
                if event.key == pygame.K_EQUALS:
                    zoom(IN)
                if event.key == pygame.K_MINUS:
                    zoom(OUT)

            if event.key == pygame.K_f:
                camera.hflip = not(camera.hflip)
                camera.vflip = not(camera.vflip)
                print("flip!")
