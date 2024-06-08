from microbit import *
import neopixel

from wukong import WUKONG

wk = WUKONG()

# Función para mapear el valor del acelerómetro a ángulo del servo
def map_value(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) // (from_high - from_low) + to_low

# Inicializar servos en pines 0 y 1
servo_L = pin15
servo_R = pin14

FORWARD_SERVO = 30
BACKWARD_SERVO = 130
FORWARD_MOTOR = 80
BACKWARD_MOTOR = -80

STOP_SERVO = 80
verbose = False

MAX_COLOR = 20

ROJO = (MAX_COLOR,0,0)
VERDE = (0,MAX_COLOR,0)
AZUL = (0,0,MAX_COLOR)
NEGRO = (0,0,0)

np = neopixel.NeoPixel(pin16,4)

def set_color(color,id=-1):
    if id == -1:
        for i in range(4):
            np[i]=color
    else:
        np[id] = color
    np.write()

def speed_servo(speed_l,speed_r):
    servo_L.write_analog(speed_l)
    servo_R.write_analog(speed_r)
    #print('# {} - {}'.format(speed_l,speed_r))

def speed_wk(speed_l,speed_r):
    wk.set_motors(1,speed_l)
    wk.set_motors(2,speed_r)

def stop_servo():
    speed(STOP_SERVO,STOP_SERVO)
    #print('# STOP')

def stop_wk():
    wk.set_motors(1,0)
    wk.set_motors(2,0)
    

UMBRAL_INCLINACION = 20

UMBRAL_CAIDA = 250

N_MUESTRAS = 5

OFFSET = 5

def get_stat(lista):
    suma = 0
    min_valor = lista[0]
    max_valor = lista[0]
    N = len(lista)
    for valor in lista:
        suma += valor
        if min_valor > valor:
            min_valor =valor
        if max_valor < valor:
            max_valor =valor    
    #    media, rango, dispersion, N
    rango = max_valor-min_valor
    media = suma/N
    if media == 0:
        return media, rango, 0, N
    else:
        return media, rango, rango*100/media, N


while True:
    try:
        lista = []
        # Leer valores del acelerómetro en el eje X
        for _ in range(N_MUESTRAS):
             lista.append(accelerometer.get_z())
        media, rango, dispersion, N = get_stat(lista)
        media -= OFFSET
        if verbose: print(media, rango, dispersion, N,end='\r')
        
        if media > UMBRAL_CAIDA:
            stop_wk()
            #stop()
            set_color(ROJO)
        elif media > UMBRAL_INCLINACION :
            #speed(BACKWARD_SERVO,FORWARD_SERVO)
            speed_wk(BACKWARD_MOTOR,BACKWARD_MOTOR)
            set_color((0,int(media),0))
        elif media < -UMBRAL_CAIDA:
            stop_wk()
            #stop()
            set_color(ROJO)  
        elif media < -UMBRAL_INCLINACION :
            #speed(FORWARD_SERVO,BACKWARD_SERVO)
            speed_wk(FORWARD_MOTOR,FORWARD_MOTOR)
            set_color((0,0,-int(media)))  
        else:
            set_color(NEGRO)
            stop_wk()
            #stop()
            
        # Pausar para evitar sobrecarga
        #sleep(1)
    except Exception as e:
        stop_wk()
        #stop()
        print(e,'Adiós!!!')
        break
