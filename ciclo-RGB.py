# Imports go at the top
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin15, 4)
while True:
    # Blanco en newpixel 0
    np[0] = (50, 50, 50) # Blanco claro
    np[1] = (0, 0, 0) # negro
    np[2] = (0, 0, 0) # negro
    np[3] = (0, 0, 0) # negro
    np.show()
    sleep(1000) # espera
   # Blanco en newpixel 1
    np[1] = (50, 50, 50) # Blanco claro
    np[0] = (0, 0, 0) # negro
    np[2] = (0, 0, 0) # negro
    np[3] = (0, 0, 0) # negro
    np.show()    
    sleep(1000)
   # Blanco en newpixel 2
    np[2] = (50, 50, 50) # Blanco claro
    np[0] = (0, 0, 0) # negro
    np[1] = (0, 0, 0) # negro
    np[3] = (0, 0, 0) # negro
    np.show()    
    sleep(1000)
   # Blanco en newpixel 3
    np[3] = (50, 50, 50) # Blanco claro
    np[0] = (0, 0, 0) # negro
    np[2] = (0, 0, 0) # negro
    np[1] = (0, 0, 0) # negro
    np.show()    
    sleep(1000)