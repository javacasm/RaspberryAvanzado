# Administrando imágenes y tarjetas SD





[Programa para instalar imágenes (img)](https://etcher.io/)

![etcher](https://etcher.io/static/screenshot.gif)


## Formateo de SD

[Formateo de SD en Linux](https://raspberrypi.stackexchange.com/questions/1446/how-can-i-reformat-my-sd-card-to-use-it-normally-again)

[Formateo de SD en Windows](https://www.raspberrypi.org/learning/software-guide/quickstart/)




## Clonado de tarjetas


[Clonado de tarjetas en Linux, MacOS y Windows](https://beebom.com/how-clone-raspberry-pi-sd-card-windows-linux-macos/)

## Linux

[Uso de compresión para imágenes](http://www.linuxweblog.com/dd-image)


## Imágenes con todo instalado

[Imagen de 16Gb](https://drive.google.com/open?id=1NdKMl2-K0YoaexgrHVVbpullZbci7TOc)
[Imagen de 8Gb](https://drive.google.com/open?id=1RlXLZYrvds83ryIP1t_4Rz5XcpTdmNyJ)


Para grabarla en la tarjeta SD (del tamaño adecuado) podemos usar [etcher](https://etcher.io/)

o

    gunzip -c fichero.gz | dd of=/dev/UNIDADTARJETA conv=sync,noerror status=progress bs=10M
