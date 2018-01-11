# Neopixels


[Tutorial adafruit](https://learn.adafruit.com/neopixels-on-raspberry-pi/software)

Usaremos la liberria rpi_ws281x que la que permite usar los Neopixels en la raspberry


Actualizamos

    sudo apt-get update

Instalamos todo lo necesario para compilar la libreria (en python y en C)

    sudo apt-get install build-essential python-dev git scons swig

Descargamos el código

    git clone https://github.com/jgarff/rpi_ws281x.git

Compilamos

    cd rpi_ws281x
    scons

Ahora entramos en la carpeta "python" para compilar la librería y la Instalamos

    cd python
    sudo python setup.py install

Una vez instalado podemos ejecutar los ejemplos


    sudo python SK6812_strandtest.py
