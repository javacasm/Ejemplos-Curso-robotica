# Imports go at the top
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin15, 4)
COLOR_NEGRO = (0,0,0) # Tupla, entre parentesis
COLOR_BLANCO = (50,50,50) 
tiempo_espera = 100

''' pone todos los leds a negro'''
def apaga_led():
    np[0] = COLOR_NEGRO
    np[1] = COLOR_NEGRO
    np[2] = COLOR_NEGRO
    np[3] = COLOR_NEGRO

while True:
    apaga_led()
    # Blanco en newpixel 0
    np[0] = COLOR_BLANCO
    np.show()
    sleep(tiempo_espera) # espera


    apaga_led()
   # Blanco en newpixel 1
    np[1] = COLOR_BLANCO # Blanco claro
    np.show()    
    sleep(tiempo_espera)


    apaga_led()
   # Blanco en newpixel 2
    np[2] = COLOR_BLANCO # Blanco claro
    np.show()    
    sleep(tiempo_espera)

    apaga_led()
   # Blanco en newpixel 3
    np[3] = COLOR_BLANCO # Blanco claro
    np.show()    
    sleep(tiempo_espera)