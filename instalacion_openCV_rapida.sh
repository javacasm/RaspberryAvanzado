## Instalación rápida
## https://github.com/jabelone/OpenCV-for-Pi

## Actualizamos
sudo apt-get update
sudo apt-get upgrade


## instalacion de paquetas de foramtos
sudo apt-get install libjpeg-dev
sudo apt-get install libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev


# libreria GTK
sudo apt-get install libgtk2.0-dev

## Optimizaiones codigo
sudo apt-get install libatlas-base-dev gfortran

## pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

## numpy
sudo pip install numpy

## version compilada

wget "https://github.com/jabelone/OpenCV-for-Pi/raw/master/latest-OpenCV.deb"
sudo dpkg -i latest-OpenCV.deb

# test
# python
# import cv2
# cv2.__version__
