from microbit import *

# Función para mapear el valor del joystick a ángulo del servo
def map_value(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) // (from_high - from_low) + to_low

# Inicializar servos en pines 2 y 8
servo_pin_2 = pin2
servo_pin_8 = pin8

# Señales cada 20 milisegundos
servo_pin_2.set_analog_period(20)
servo_pin_8.set_analog_period(20)

MAX_JOYSTICK = 1023
MAX_SERVO = 180
while True:
    # Leer valores del joystick
    x = pin0.read_analog()
    y = pin1.read_analog()
    
    # Mapear valores del joystick (de 0 a 1023) a ángulos del servo (de 0 a 180)
    angle_x = map_value(x, 0, MAX_JOYSTICK, 0, MAX_SERVO)
    angle_y = map_value(y, 0, MAX_JOYSTICK, 0, MAX_SERVO)
    
    # Mover servos a los ángulos correspondientes
    servo_pin_2.write_analog(angle_x)
    servo_pin_8.write_analog(angle_y)
    
    # Pausar para evitar sobrecarga
    sleep(50)
