from time import sleep
from gpiozero import Robot
tiempo =  5
robot = Robot(left = (7, 8), right = (9, 10))
while True:
        robot.forward()
        sleep(tiempo)
        robot.stop()
        robot.right()
        sleep(tiempo)
        robot.stop()
        robot.left()
        sleep(tiempo)
        robot.stop()
        robot.backward()
        sleep(tiempo)
        robot.stop()
