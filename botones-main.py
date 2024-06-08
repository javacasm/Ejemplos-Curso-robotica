# Imports go at the top
from microbit import *

print('Programa de botones')

while True:  # bucle para siempre
    if button_a.was_pressed():
        print('Botón A pulsado')
        display.scroll('A')

    if button_b.was_pressed():
        print("Se ha pulsado el botón B")
        display.scroll('B') 
        
    if pin_logo.is_touched():
        display.show(Image('70307:'
                           '03630:'
                           '36963:'
                           '03630:'
                           '70307'))
        
        
