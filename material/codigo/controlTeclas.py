Control con teclas

  import getch
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

  while True:
      # Keyboard character retrieval method is called and saved
      # into variable

      char = getch()

      # The car will drive forward when the "w" key is pressed
      if(char == "w"):
           robot.forward(1)

      # The car will reverse when the "s" key is pressed
      if(char == "s"):
          robot.right(0.4)

      # The "a" key will toggle the steering left
      if(char == "a"):
          robot.right(0.4)

      # The "d" key will toggle the steering right
      if(char == "d"):
          toggleSteering("right")

      # The "l" key will toggle the LEDs on/off
      if(char == "l"):
          toggleLights()

      # The "x" key will break the loop and exit the program
      if(char == "x"):
          print("Program Ended")
          break
