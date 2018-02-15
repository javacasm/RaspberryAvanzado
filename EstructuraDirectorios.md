# [Raspberry Pi: Introducción al uso y programación](http://www.juntadeandalucia.es/educacion/portals/web/cep-jaen/index.php/es-ES/formacion/convocatorias/771-abierto-plazo-de-inscripcion-a-la-actividad-raspberry-pi-introduccion-al-uso-y-programacion-162319ge102)

## CEP de Jaen

16, 23 y 28 de Noviembre de 2017

![CC](./images/Licencia_CC.png)
## José Antonio Vacas  @javacasm

### [https://github.com/javacasm/RaspberryJaen](https://github.com/javacasm/RaspberryJaen)

# Estructura de ficheros

Algunas características de sistema de fichero de linux

* Usa un formato de partición ext4 (también existen aunque en desuso el ext3 y el ext2), aunque permite usar FAT
* El árbol de directorios tiene un único directorio raíz del que cuelga todo. Todos los dispositivos (pen drives, discos externos, discos de red) se integran dentro de este árbol, **montando** su raiz en un directorio determinado (montamos y desmontamos con __mount__ y __unmonut__ )

El usuario sólo acceso a su directorio y el solo el administrador (**root**) puede acceder al resto de directorios

## Algunos directorios

* / raiz
* /etc configuración
* /home usuario
* /usr programas para usuarios
* /usr/share recursos de programas (imágenes, traducciones)
* /usr/share/doc documentación
* /bin ejecutables del sistema
* /lib librerías
* /boot Arranque del sistema
* /usr/bin ejecutables para usuarios
