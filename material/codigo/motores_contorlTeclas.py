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
      print("forward")
      robot.forward(speed)

  # The car will reverse when the "z" key is pressed
  if(char == "z"):
      print("backward")
      robot.backward(speed)

  # The "a" key will toggle the steering left
  if(char == "a"):
      print("left")
      robot.left(speed)

  # The "d" key will toggle the steering right
  if(char == "d"):
      print("right")
      robot.right(speed)

  # The "s" key will  stop the car
  if(char == "s"):
      print("stop")
      robot.stop()

  # The "1" key will toggle  lowest speed
  if(char == "1"):
      print("speed:0.1")
      speed = 0.1

  # The "5" key will toggle  medium speed
  if(char == "5"):
      print("speed:0.5")
      speed = 0.5

  # The "9" key will toggle  hiwest speed
  if(char == "9"):
      print("speed:0.9")
      speed = 0.9

  # The "q" key will break the loop and exit the program
  if(char == "q"):
      print("Program Ended")
      break
