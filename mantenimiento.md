# [Raspberry Pi: Introducción al uso y programación](http://www.juntadeandalucia.es/educacion/portals/web/cep-jaen/index.php/es-ES/formacion/convocatorias/771-abierto-plazo-de-inscripcion-a-la-actividad-raspberry-pi-introduccion-al-uso-y-programacion-162319ge102)

## CEP de Jaen

16, 23 y 28 de Noviembre de 2017

![CC](./images/Licencia_CC.png)
## José Antonio Vacas  @javacasm

### [https://github.com/javacasm/RaspberryJaen](https://github.com/javacasm/RaspberryJaen)

# Mantenimiento

Una vez instalado el sistema, necesitamos de vez en cuando actualizarlo.

## Actualización (update)

Desde un terminal/consola usamos los siguientes comandos

Para buscar cambios

	sudo apt update

Para instalar estos cambios

	sudo apt upgrade

Para actualizar el sistema

	sudo apt dist-upgrade

Para instalar un paquete determinado

	sudo apt install paquete

(siempre podemos instalar desde la herramienta visual "Añadir programas" en el menú Preferencias)

#### Actualización de los distintos firmware

Los diferentes componentes de la Raspberry necesitan de varios firmwares para funcionar, que también conviene tener actualizados. Podemos actualizarlos con


	sudo rpi-update

#### Instalación de paquetes a partir del código fuente

* Descargamos el código fuente (normalmente comprimido)
* Lo descomprimimos con

	unzip codigo_fuente.zip

ó

	tar xvf cofigo_fuente.tgz

(según el formato en el que esté comprimido)

Dentro del directorio del código ya descomprimido normalmente encontramos un fichero README o INSTALL que nos dará las instrucciónes, pero suelen ser muy parecidas a estas:

Preparan el código para que compile en nuestro sistema y además comprueban que tengamos las herramientas y librerías necesarias con:

	cmake .

ó

	configure

Compila el código y generamos un ejecutable

	make

Lo instalamos en el sistema (por eso necesitamos usar sudo)

	sudo make install



## Cuidados eléctricos

* No existe protección en los terminales, con lo que es muy, muy sencillo quemar la placa.
* Cuidado con colocar la placa sobre un instrumento o superficie metálica. Mejor usar una caja
* Cuidado con los dispositivos que conectamos, pudieran demandar más potencia de la que le puede dar
