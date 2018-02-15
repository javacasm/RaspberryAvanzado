
# Raspberry Avanzado

Febrero-Marzo 2018

## CEP Linares-Andujar ([182319GE077](https://www.juntadeandalucia.es/educacion/secretariavirtual/consultaCEP/actividad/182319GE077/))

## https://github.com/javacasm/RaspberryAvanzado

### José Antonio Vacas @javacasm

![CC](./images/Licencia_CC.png)

# Manejando tu Raspberry Pi

Como sabes es una máquina Linux, con lo que podrás manejarla igual que se maneja cualquier otra máquina Linux


## Consola (línea de comandos)

![console](./images/console.png)

### Comandos básicos:

* **ls** : muestra los archivos y directorios ( **ls -l** para más detalles y **ls -a** para mostrar todos)
* **cd** : cambia de directorio (**cd ~** nos lleva a nuestro directorio home y **cd ..** sale del directorio actual)
* **chmod** : cambia los permisos de un fichero/directorio (**chmod ugo-w fichero** quita todos los permisos de escritura)
* **pwd** : nos dice el directorio actual
* **mv** : mueve directorios/ficheros a un nuevo destino
* **rm** : borra directorios/ficheros
* **mkdir** : crea un directorio
* **passwd** : cambia la contraseña del usuario actual
* **ps -ef** : muestra los procesos en ejecución
* **top** : administrador de tareas
* **clear** : borra todo el contenido del terminal
* **df** : muestra el % de disco ocupado
* **nano** : editor de texto básico
* **vi** : editor de texto avanzado pero complejo
* **du** : muestra lo que ocupa un directorio (**du -s *** muestra lo que ocupa un directorio y todo lo que contiene)
* **sudo halt** apaga la raspberry
* **sudo shutdown -h now** apaga la raspberry
* **history** : muestra todos los comandos que se han ejecutado antes. Podemos ejecutar el comando de la posición n, con !n . Las teclas abajo/arriba del cursor nos permiten iterar por los comandos usados.
* La tecla Tabulador nos permite completar el nombre del fichero/directorio
* **man comando**: Para obtener ayuda sobre comando
* Para hacer fichero script: añadimos los comandos, chmod u+x fichero y para ejecutarlo ./fichero


### Usuarios

El usuario por defecto es "**pi**" con contraseña "**raspberry**"

### Cuidado con sudo

Nos da todo el poder del usuario administrador (**root**)

## Arrancar Interface gráfico

Para arrancar el interface gráfico (si no está arrancado) usaremos

		startx


![startx](./images/raspX.png)

## Acceso remoto


### ssh

Es el protocolo de acceso por consola

Entramos en la configuración avanzada

	sudo raspi-config

![ssh](./images/ssh.png)

Podemos hacerlo también por comandos con

	sudo service ssh start
	sudo insserv ssh

Ahora podremos conectarnos remotamente con ssh

	ssh pi@192.189.0.123

O bien usando algún software como [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)

Conviene cambiar la contraseña para evitar que cualquiera pueda acceder
