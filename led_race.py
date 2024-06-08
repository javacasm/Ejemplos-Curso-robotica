# test neopixel ring
from neopixel import NeoPixel
from microbit import *
from random import randint
from time import  ticks_ms

MAX_BRIGHT = 30
BLANCO = (MAX_BRIGHT,MAX_BRIGHT,MAX_BRIGHT)
NEGRO = (0,0,0)
LIGHT_BLUE = (MAX_BRIGHT//5,MAX_BRIGHT//5,MAX_BRIGHT)

N = 60

np = None

N_participantes = 4

colors = [] # color de cada partipante
positions = [] # posición de cada partipante
speeds = [] # volicidad de cada partipante
accels = [] # aceleración de cada partipante
last_time_controls=[]

drag = [] # frenada que produce cada parte del circuito (podemos crear subidas)

CONTROL_BUTTON_A = 0
CONTROL_BUTTON_B = 1
CONTROL_PIN0 = 2
CONTROL_PIN2 = 3

verbose = False # para ver información de depuración en la consola

def init_np(pin= pin1,n_pixels = 60 ):    
    global np
    if np == None:
        np = NeoPixel(pin,n_pixels)
        
def set_color(color,pausa=0,noShow=False):
    for i in range(len(np)):
        np[i] = color
        if pausa != 0 and noShow == False:
            np.show()
            sleep(pausa)
    if not noShow:
        np.show()
        
def test_neopixel( pausa = 10):
    
    colores = (NEGRO,(50,0,0),(50,50,0),(50,0,50),(0,0,50),BLANCO)
    pausa = 1
    while True:
        for color in colores:
            set_color(color = color,pausa=1)
            sleep(pausa)  

# maximiza el contraste
colores = ((MAX_BRIGHT,0,0),(0,0,MAX_BRIGHT),(0,MAX_BRIGHT,0),(MAX_BRIGHT//2,0,MAX_BRIGHT//2),(MAX_BRIGHT//2,MAX_BRIGHT//2,0))

def get_random_color():
    return (randint(0,MAX_BRIGHT),randint(0,MAX_BRIGHT),randint(0,MAX_BRIGHT))

def init_carrera():
    print('init')
    accels.clear()
    speeds.clear()
    colors.clear()
    positions.clear()
    last_time_controls.clear()
    for i in range(N_participantes):
        accels.append(0)
        speeds.append(0)
        colors.append(colores[i])
        positions.append(0)
    last_time_controls.append(0) # button A
    last_time_controls.append(0) # button B
    pin0.set_pull(pin0.PULL_UP)
    pin2.set_pull(pin2.PULL_UP)    
    last_time_controls.append(0) # pin0
    last_time_controls.append(0) # pin2    

    #creamos el drag
    for i in range(N):
        drag.append(1) # en todo el circuito hay rozamiento

    # colina en N//2
    drag[N//2 + 1] = 2    
    drag[N//2] = 3
    drag[N//2 - 1] = 2        

def update_positions():
    for i in range(N_participantes):
        if accels[i] > 0:
            speeds[i] += accels[i]
            accels[i] = 0
        else:
            speeds[i] -= drag[positions[i]] 
        if speeds[i] < 0 :
            speeds[i] = 0
        positions[i] = (positions[i] + speeds[i]//10)%N

def draw():
    set_color(NEGRO,noShow=True)
    for i in range(N_participantes):
        np[positions[i]] = colors[i]
        if verbose: print(i,positions[i],speeds[i],accels[i])
    np.show()

    
MIN_CONTROL_TICKS = 300
CONTROL_PUNCH = 20 # impulso de cada pulsación
def check_controls():
    now = ticks_ms()
    if button_a.is_pressed() and now-last_time_controls[CONTROL_BUTTON_A]>MIN_CONTROL_TICKS:
        accels[CONTROL_BUTTON_A] += CONTROL_PUNCH
        last_time_controls[CONTROL_BUTTON_A] = now
    if button_b.is_pressed()and now-last_time_controls[CONTROL_BUTTON_B]>MIN_CONTROL_TICKS:
        accels[CONTROL_BUTTON_B] += CONTROL_PUNCH
        last_time_controls[CONTROL_BUTTON_B] = now
    if pin0.read_digital() == 0 and now-last_time_controls[CONTROL_PIN0]>MIN_CONTROL_TICKS:
        accels[CONTROL_PIN0] += CONTROL_PUNCH
        last_time_controls[CONTROL_PIN0] = now
    if pin2.read_digital() == 0 and now-last_time_controls[CONTROL_PIN2]>MIN_CONTROL_TICKS:
        accels[CONTROL_PIN2] += CONTROL_PUNCH
        last_time_controls[CONTROL_PIN2] = now
    if pin_logo.is_touched():
        init_carrera()
        
pausa = 10 

def carrera():
    init_carrera()
    print('Run')
    while True:
        check_controls()
        update_positions()
        draw()
        sleep(pausa)              
    
def test_controls():
    print('Test controls')
    
    while pin_logo.is_touched() == False:
        status = '1 (A) {} - 2 (B) {} - 3 (P0) {} - 4 (P2) {}'.format(button_a.is_pressed(),button_b.is_pressed(),pin0.read_digital(),pin2.read_digital())
        print(status)
        sleep(100)
        
if __name__ == '__main__':
    init_np(pin=pin1,n_pixels=N)
    test_controls()
    #test_neopixel()    
    carrera() 

