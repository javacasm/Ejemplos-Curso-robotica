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
        display.show(Image('90000:'
                           '70000:'
                           '50000:'
                           '30000:'
                           '10000'))
        sleep(100)
        display.show(Image('09000:'
                           '07000:'
                           '05000:'
                           '03000:'
                           '01000'))    
        sleep(100)
        display.show(Image('00900:'
                           '00800:'
                           '00700:'
                           '00500:'
                           '00300'))         
        sleep(100)
        display.show(Image('00090:'
                           '00080:'
                           '00070:'
                           '00060:'
                           '00050')) 
        sleep(100)
        display.show(Image('00009:'
                           '00008:'
                           '00008:'
                           '00007:'
                           '00007'))         
        sleep(100)
#display.show(Image('70307:'
        #                   '03630:'
        #                   '36963:'
        #                   '03630:'
        #                   '70307'))        
        
