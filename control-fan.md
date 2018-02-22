## Controlando un ventilador para refrigerar la Raspberry Pi

(Basado en el tutorial de [hackernoon](https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c) con algunos retoques/arreglos)

Se trata de controlar un ventilador desde los GPIO para refrigerar la Raspberry Pi.

Se establecerá una temperatura umbral (60º en nuestro caso) a partir de la cual se encenderá un ventilador. Inicialmente se va a usar control todo/nada, dejando para más adelante la posibilidad de usar diferentes velocidades del ventilador mediante PWM

Este es el script ([control-fan.py](./codigo/control-fan.py)) para encender/apagar el ventilador en función de

    #!/usr/bin/env python3
    # Author: Edoardo Paolo Scalafiotti <edoardo849@gmail.com>
    # Some changes&typos by @javacasm

    import os
    from time import sleep
    import signal
    import sys
    import RPi.GPIO as GPIO

    pin = 18 # The pin ID, edit here to change it
    maxTMP = 60 # The maximum temperature in Celsius after which we trigger the fan

    def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.setwarnings(False)
        return()

    def getCPUtemperature():
        res = os.popen('vcgencmd measure_temp').readline()
        temp =(res.replace("temp=","").replace("'C\n",""))
        #print("temp is {0}".format(temp)) #Uncomment here for testing
        return temp

    def fanON():
        setPin(True)
        return()

    def fanOFF():
        setPin(False)
        return()

    def getTEMP():
        CPU_temp = float(getCPUtemperature())
        if CPU_temp>maxTMP:
            fanON()
        else:
            fanOFF()
        return()

    def setPin(mode): # A little redundant function but useful if you want to add logging
        GPIO.output(pin, mode)
        return()

    try:
        setup()
        while True:
            getTEMP()
            sleep(5) # Read the temperature every 5 sec, increase or decrease this limit if you want
    except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
        GPIO.cleanup() # resets all GPIO ports used by this program

Copiamos el script run-fan.py en la carpeta del sistema

    sudo cp run-fan.py /usr/local/bin/

Le damos permisos de ejecución

    sudo chmod u+x /usr/local/bin/run-fan.py

Veamos ahora el script para arrancar/parar el servicio de control del ventilador según la temperatura ([run-fan.sh](./codigo/run-fan.sh)).

## Servicio control fan

        #! /bin/sh

        ### BEGIN INIT INFO
        # Provides:          run-fan.py
        # Required-Start:    $remote_fs $syslog
        # Required-Stop:     $remote_fs $syslog
        # Default-Start:     2 3 4 5
        # Default-Stop:      0 1 6
        ### END INIT INFO

        # If you want a command to always run, put it here

        # Carry out specific functions when asked to by the system
        case "$1" in
          start)
            echo "Starting control-fan.py"
            /usr/local/bin/run-fan.py &
            ;;
          stop)
            echo "Stopping listen-for-shutdown.py"
            pkill -f /usr/local/bin/run-fan.py
            ;;
          *)
            echo "Usage: /etc/init.d/control-fan.sh {start|stop}"
            exit 1
            ;;
        esac

        exit 0

Copiamos el script de control del servicio en la carpeta _/etc/init.d/_

    sudo cp control-fan.sh /etc/init.d/

Le damos permisos de ejecución

    sudo chmod u+x /etc/init.d/control-fan.sh

Y registramos el servicio en el sistema

    sudo update-rc.d control-fan.sh defaults

Arrancamos el servicio para probarlo (en el siguiente rearranque se hará automáticamente)

    sudo service control-fan start
