from microbit import *
import neopixel
import math

# Función para mapear el valor del acelerómetro a ángulo del servo
def map_value(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) // (from_high - from_low) + to_low

# Inicializar servos en pines 0 y 1
servo_pin_2 = pin2
servo_pin_8 = pin8

while True:
    # Leer valores del acelerómetro
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    
    # Mapear valores del acelerómetro (de -1024 a 1024) a ángulos del servo (de 0 a 180)
    angle_x = map_value(x, -1024, 1024, 0, 180)
    angle_y = map_value(y, -1024, 1024, 0, 180)
    
    # Mover servos a los ángulos correspondientes
    servo_pin_2.write_analog(angle_x)
    servo_pin_8.write_analog(angle_y)
    
    # Pausar para evitar sobrecarga
    sleep(50)
