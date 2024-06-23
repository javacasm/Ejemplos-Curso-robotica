# from https://github.com/krzysztof-sawicki/micromaqueen-python/tree/master

from time import sleep_ms
from maqueen import Maqueen, LEFT, RIGHT

v = 0.5

print('test maqueen v'+str(v))

robot = Maqueen()


def test_leds_digital(repeatN = 10):
    for _ in range(repeatN):
        robot.set_led(LEFT,1)
        robot.set_led(RIGHT,0)        
        sleep_ms(100)
        robot.set_led(LEFT,0)
        robot.set_led(RIGHT,1)                 
        sleep_ms(100)

def test_leds_analog(pausa = 10):
    for value in range(255):
        robot.set_led_PWM(LEFT,value)
        robot.set_led_PWM(RIGHT,255-value)


def test_rgb():
    for i in range(4):
        robot.rgbleds[i] = (i * 25,i*5, 255 - i * 50)
    robot.rgbleds.write()
        

def line_tracking(forward_speed = 60, turn_speed = 20):
    while True:
        if robot.read_patrol(LEFT):
            robot.set_motor(LEFT,forward_speed)
        else:
            robot.set_motor(LEFT,turn_speed)
        if robot.read_patrol(RIGHT):
            robot.set_motor(RIGHT,forward_speed)
        else:
            robot.set_motor(RIGHT,turn_speed)    

while True:
    if robot.is_maqueen() != True:
        print('No hay maqueen')
        break
    try:
        print('Testing leds')
        test_leds_digital()
        test_leds_analog()
        
        print('Testing RGB')
        test_rgb()
        
        for i in range(0, 10):
            print("\rDistance: %d    " % robot.read_distance(),end='')
            sleep_ms(300)
        print()
        for i in range(0, 10):
            l = robot.read_patrol(LEFT)
            p = robot.read_patrol(RIGHT)
            print("\rPatrol: %d %d   " % (l, p),end='')
            sleep_ms(100)
        print()
        print('Testing motors')
        d = [-100, 50, 20, -200, 200, 40]
        for i in d:
            robot.set_motor(LEFT, i)
            sleep_ms(1000)
            robot.set_motor(RIGHT, i)
            sleep_ms(1000)

        #robot.motor_stop_all()
        print('Testing line-tracking')
        line_tracking()
    except Exception as e:
        print(e)
    finally:
        print('Motor stop')
        robot.motor_stop_all()
        break
