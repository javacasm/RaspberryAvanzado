# GPIO avanzado

Usando DMA, interrupciones, autoupdate...

Librerías que permiten usar Servos y pwm en todos los pines

## [Remote GPIO](https://github.com/metachris/RPIO)

Permite la actualización, control y supervisión desde una conexión TCP/IP


## [PIGio](http://abyz.me.uk/rpi/pigpio/)

* hardware timed sampling and time-stamping of GPIO 0-31 every 5 µs
* hardware timed PWM on all of GPIO 0-31
* hardware timed servo pulses on all of GPIO 0-31

* callbacks on GPIO 0-31 level change (time accurate to a few µs)

* notifications via pipe on GPIO 0-31 level change
* callbacks at timed intervals

* reading/writing all of the GPIO in a bank (0-31, 32-53) as a single operation

* GPIO reading, writing, modes, and internal pulls
* socket and pipe interfaces for the bulk of the functionality

* waveforms to generate GPIO level changes (time accurate to a few µs)

* software serial links using any user GPIO

* rudimentary permission control through the socket and pipe interfaces
* creating and running scripts on the pigpio daemon


### [PyScope](http://abyz.me.uk/rpi/pigpio/piscope.html)

![PyScope](http://abyz.me.uk/rpi/pigpio/images/pisc-1.jpg)
