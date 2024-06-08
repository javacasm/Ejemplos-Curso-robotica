# Imports go at the top
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin15, 4)
while True:
    # Color 1
    np[0] = (63, 63, 0) # RGB
    np[1] = (0, 0, 255) # a tope de azul
    np[2] = (255, 0, 0) # a tope de rojo
    np[3] = (12, 90, 68) # morado
    np.show()
    sleep(1000) # espera
    # Color 2
    np[0] = (82, 3, 252) # RGB
    np[1] = (231, 252, 3) 
    np[2] = (17, 171, 237) 
    np[3] = (166, 16, 181) 
    np.show()
    sleep(1000)
    