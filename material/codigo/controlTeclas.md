Control con teclas

  while True:
      # Keyboard character retrieval method is called and saved
      # into variable
      
      char = getch()

      # The car will drive forward when the "w" key is pressed
      if(char == "w"):
          motor2_forward()
          motor2.ChangeDutyCycle(99)

      # The car will reverse when the "s" key is pressed
      if(char == "s"):
          motor2_reverse()
          motor2.ChangeDutyCycle(99)

      # The "a" key will toggle the steering left
      if(char == "a"):
          toggleSteering("left")

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
