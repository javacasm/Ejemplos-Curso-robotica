from microbit import *
import neopixel

# Inicializar los LEDs RGB (4 LEDs conectados al pin 12)
num_leds = 4
np = neopixel.NeoPixel(pin15, num_leds)

# Función para mapear el valor del acelerómetro a un valor de color RGB (0-255)
def map_value(value, from_low, from_high, to_low, to_high):
    return int((value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low)

while True:
    # Leer valores del acelerómetro
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    
    # Mapear valores del acelerómetro (de -1024 a 1024) a valores de color (de 0 a 255)
    r = map_value(x, -1024, 1024, 0, 255)
    g = map_value(y, -1024, 1024, 0, 255)
    b = map_value(z, -1024, 1024, 0, 255)
    
    print(f'({r:3.0d},{g:3.0},{b:3.0d})',end='\r')
    
    # Asignar el color mapeado a los 4 LEDs
    for i in range(num_leds):
        np[i] = (r, g, b)
    
    # Actualizar los LEDs
    np.show()
    
    # Pausar para evitar sobrecarga
    sleep(100)
