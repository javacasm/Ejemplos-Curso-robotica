# Imports go at the top
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin15, 4)
COLOR_NEGRO = (0,0,0) # Tupla, entre parentesis
COLOR_BLANCO = (50,50,50) 
tiempo_espera = 1000
while True:
    # Blanco en newpixel 0
    np[0] = COLOR_BLANCO
    np[1] = COLOR_NEGRO
    np[2] = COLOR_NEGRO
    np[3] = COLOR_NEGRO
    np.show()
    sleep(tiempo_espera) # espera
   # Blanco en newpixel 1
    np[1] = COLOR_BLANCO # Blanco claro
    np[0] = COLOR_NEGRO # negro
    np[2] = COLOR_NEGRO # negro
    np[3] = COLOR_NEGRO # negro
    np.show()    
    sleep(tiempo_espera)
   # Blanco en newpixel 2
    np[2] = COLOR_BLANCO # Blanco claro
    np[0] = COLOR_NEGRO # negro
    np[1] = COLOR_NEGRO # negro
    np[3] = COLOR_NEGRO # negro
    np.show()    
    sleep(tiempo_espera)
   # Blanco en newpixel 3
    np[3] = COLOR_BLANCO # Blanco claro
    np[0] = COLOR_NEGRO # negro
    np[2] = COLOR_NEGRO # negro
    np[1] = COLOR_NEGRO # negro
    np.show()    
    sleep(tiempo_espera)