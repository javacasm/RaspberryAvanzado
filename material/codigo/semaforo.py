from gpiozero import Button, TrafficLights, Buzzer
from time import sleep
lights = TrafficLights(25, 8, 7)

button = Button(21)
buzzer= Buzzer(15)


while True:
      button.wait_for_press()
      lights.green.on()
      sleep(1)
      lights.amber.on()
      sleep(1)
      lights.red.on()
      sleep(1)
      lights.off()
      buzzer.beep()
