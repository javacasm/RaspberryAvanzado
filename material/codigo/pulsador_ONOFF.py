#!/usr/bin/env python

from gpiozero import Button
from signal import pause

button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
