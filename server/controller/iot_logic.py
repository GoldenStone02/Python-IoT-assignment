# Need to follow structure of ppt 

# Importing various functions for sensor logic via the sensors folder.
from ..sensors.buzzer import buzzer_on
from ..sensors.camera import take_pic
from ..sensors.keypad import keypad
from ..sensors.LCD import LCD
from ..sensors.LED import LED_State
from ..sensors.PIR import PIR
from ..sensors.rfid import rfid
from ..sensors.servo import servo

# Main Programme
while True:
    
    LCD('Awaiting Motion..')
    servo('CLOSED') 
    motion_detected = PIR()
    if motion_detected == 'MOTION DETECTED': # For when motion is finally detected, continue onwards to the programme.
