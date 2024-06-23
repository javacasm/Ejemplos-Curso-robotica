# Imports go at the top
from microbit import *
from maqueen import *
import sys

v = 0.4

print('Test maqueen v'+str(v))

robot = Maqueen()

    
robot.set_led(LEFT, 1)
sleep(1000) # esperamos 1 segundo
robot.set_led(LEFT, 0)
sleep(1000) # esperamos 1 segundo
robot.set_led(RIGHT,1)

while True:
    distancia_front = robot.read_distance_front()
    if distancia_front < 10:
        robot.set_led(LEFT,1)
    else:
        robot.set_led(LEFT,0)
    sleep(50)
    distancia_back = robot.read_distance_back()    
    if distancia_back < 10:
        robot.set_led(RIGHT,1)
    else:
        robot.set_led(RIGHT,0)
    print('distancia front:',int(distancia_front),'distancia back',distancia_back)
    sleep(250)