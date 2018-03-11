# Control del robot con teclas

import sys, tty, termios, time
from gpiozero import Robot

def getch():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
  finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch

robot = Robot(left = (7, 8), right = (9, 10))

speed = 0.4

print("Usar:\n\tw forward\n\ts stop\n\td leftt\n\ta right\n\tz backward\n\t1,5,9  speed\n\tq quit\n")

while True:
  # Keyboard character retrieval method is called and saved
  # into variable

  char = getch()

  # The car will drive forward when the "w" key is pressed
  if(char == "w"):
       robot.forward(speed)

  # The car will reverse when the "z" key is pressed
  if(char == "z"):
      robot.backward(speed)

  # The "a" key will toggle the steering left
  if(char == "a"):
      robot.left(speed)

  # The "d" key will toggle the steering right
  if(char == "d"):
      robot.right(speed)

  # The "s" key will  stop the car
  if(char == "s"):
      robot.stop()

  # The "1" key will toggle  lowest speed
  if(char == "1"):
      speed = 0.1

  # The "5" key will toggle  medium speed
  if(char == "5"):
      speed = 0.5

  # The "9" key will toggle  hiwest speed
  if(char == "9"):
      speed = 0.9




  # The "l" key will toggle the LEDs on/off
  if(char == "l"):
      toggleLights()

  # The "x" key will break the loop and exit the program
  if(char == "q"):
      print("Program Ended")
      break
