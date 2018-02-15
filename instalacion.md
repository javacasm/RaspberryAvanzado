# [Raspberry Pi: Introducción al uso y programación](http://www.juntadeandalucia.es/educacion/portals/web/cep-jaen/index.php/es-ES/formacion/convocatorias/771-abierto-plazo-de-inscripcion-a-la-actividad-raspberry-pi-introduccion-al-uso-y-programacion-162319ge102)

## CEP de Jaen

16, 23 y 28 de Noviembre de 2017

![CC](./images/Licencia_CC.png)

## José Antonio Vacas  @javacasm

### [https://github.com/javacasm/RaspberryJaen](https://github.com/javacasm/RaspberryJaen)

# Instalación

¿Qué necesitamos?

* Formatear tarjeta ([http://www.sdcard.org/downloads/formatter_4/](http://www.sdcard.org/downloads/formatter_4/))
* Descargamos la imagen del sistema que queramos [http://www.raspberrypi.org/download](http://www.raspberrypi.org/download)
* ¿Qué imagen usar?
	* Empecemos con [Noobs](https://www.raspberrypi.org/blog/tag/noobs/)
	* [Instalación de Noobs](https://www.raspberrypi.org/help/noobs-setup/)

![noobs](./images/noobs.png)

* ¡¡¡Arrancar!!!
* Configuración

## Configuración

	sudo raspi-config

(Puede variar algo según la versión)

![config](./images/config.png)

![teclado](./images/teclado.png)

![avanzado](./images/avanzados.png)

![overclock](./images/overcock.png)


Una vez configurado podemos abrir el entorno visual con

	startx



![Arrancamos el entorno visual con startx](./images/raspX.png)

En cualquier momento podemos volver a reconfigurar

	sudo raspi-config
