# Importa la extensión microbit
from microbit import *

tiempo = 500

# Código que se repite para siempre 'while True:'
while True:
    display.show(Image.SAD)
    print('triste')
    sleep(tiempo)
    display.show(Image.HAPPY)
    print('feliz')
    sleep(tiempo)
    display.show(Image.ANGRY)
    print('enfadado')
    sleep(tiempo)