import I2C_LCD_driver
from time import sleep
from gpiozero import Robot

mylcd = I2C_LCD_driver.lcd()

robot = Robot(left = (7, 8), right = (9, 10))

tiempo  = 10

speed = 0.3

while True:
    mylcd.lcd_display_string("forw ", 1)
    robot.forward(speed)
    sleep(tiempo)
    robot.stop()
    mylcd.lcd_display_string("right", 1)
    robot.right(speed)
    sleep(tiempo)
    robot.stop()
    mylcd.lcd_display_string("left ", 1)
    robot.left(speed)
    sleep(tiempo)
    robot.stop()
    mylcd.lcd_display_string("Back ", 1)
    robot.backward(speed)
    sleep(tiempo)
    robot.stop()
