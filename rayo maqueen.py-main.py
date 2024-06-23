# Imports go at the top
from microbit import *

from maqueen import *

robot = Maqueen()

robot.set_led(LEFT, 1)
sleep(1000) # esperamos 1 segundo
robot.set_led(LEFT, 0)
sleep(1000) # esperamos 1 segundo
robot.set_led(RIGHT,1)

while True:
    if button_b.is_pressed():
        robot.set_led(LEFT,1)
        robot.set_motor(LEFT,255)
    else:
        robot.set_led(LEFT,0)
        robot.set_motor(LEFT,0)
        
    
    if button_a.is_pressed():
        robot.set_led(RIGHT,1)
        robot.set_motor(RIGHT,2555)
    else:
        robot.set_led(RIGHT,0)
        robot.set_motor(RIGHT,0)
