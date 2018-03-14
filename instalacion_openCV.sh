# Instalacion OpenCV

## Instrucciones tomadas de https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/

# Por si necesitas hacer espacio en tu tarjetas

# sudo apt-get purge wolfram-engine
# sudo apt-get purge libreoffice*
# sudo apt-get clean
# sudo apt-get autoremove

## actualizacion
sudo apt-get update && sudo apt-get upgrade

##  compiladores de proyectos
sudo apt-get install build-essential cmake pkg-config

## Formatos de imagenes
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev

## formatos de video
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev

## Construccion de librerias con IU
sudo apt-get install libgtk2.0-dev libgtk-3-dev

## Optimizacion de codigo
sudo apt-get install libatlas-base-dev gfortran

## Entornos de python para 2.7 y 3
sudo apt-get install python2.7-dev python3-dev

## Descargamos OpenCV

cd ~
# wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.1.zip
unzip opencv.zip

## Descargamos OpenCV opencv_contrib

# wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.1.zip
unzip opencv_contrib.zip

## pip para distinguir 2.7 y 3.x

wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py

## Instalamos virtualenv

sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip

## hacemos que se ejecute en .profile

echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile

## Hacemos que se reejecute .profile

# source ~/.profile

## Creamos un entorno de python3 llamado cv
mkvirtualenv cv3 -p python3

## para entrar en el entorno virtual
workon cv3

## Veremos que aparece (cv)
![dentro del entorno cv](https://www.pyimagesearch.com/wp-content/uploads/2017/08/cv_virtualenv.png)

## Salimos del entorno con deactivate

## Instalamos numpy

pip install numpy

cd ~/opencv-3.4.1/
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.4.1/modules \
    -D BUILD_EXAMPLES=ON ..

## Comprobamos que python a nuestro env cv3


## ampliamos el swap para compilar (luego lo quitaremos)
## Cambiamos CONF_SWAPSIZE=100 a  Cambiamos CONF_SWAPSIZE=1024
##

sudo nano /etc/dphys-swapfile

## reactivamos el nuevo tamaño

sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start

## Compilamos OpenCV

make -j1 

## funcionará más rápido con  make  -j4 pero puede dar más errores al usar los 4 cores

## lo instalamos

sudo make install 
sudo ldconfig

##  comprobamos que se ha instalado correctamente

cd /usr/local/lib/python3.5/site-packages/
sudo mv cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so

## enlazamos a nuestro entorno virtual

cd ~/.virtualenvs/cv3/lib/python3.5/site-packages/
ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so

## Para probar

python
## y desde dentro: 
## >>> import cv2
## >>> cv2.__version__
## y veremos
## '3.4.1'


## completamos los ficheros de los ejemplos

sudo cp -r data gpu hal java open* tapi va_intel/ winrt* wp8/ cpp android/ directx/ dnn  /usr/local/share/OpenCV/samples/

## Borramos el codigo para recuperar espacio
rm -rf opencv-3.4.1 opencv_contrib-3.4.1
