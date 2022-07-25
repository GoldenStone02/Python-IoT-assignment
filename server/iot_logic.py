# Need to follow structure of ppt 

# Importing various functions for sensor logic via the sensors folder.
from sensors.buzzer import buzzer_on
from sensors.camera import take_pic
from sensors.keypad import keypad
from sensors.LCD import LCD
from sensors.LED import LED_State
from sensors.PIR import PIR
from sensors.rfid import rfid
from sensors.servo import servo

# Main Programme
while True:
    servo("CLOSED")
    LCD('Awaiting Motion..', '-------->')
    motion_detected = PIR()
    if motion_detected == 'MOTION DETECTED': # For when motion is finally detected, continue onwards to the programme.
        LCD('Motion Detected', 'ON RFID....')
        # With motion detected, we first want to take a picture 
        take_pic()      # picture taken will be stored in /database/image_upload/picture.jpg
        # RFID will go into READ mode, result == "ACCESS GRANTED" if valid. Else, if invalid, result == "ACCESS DENIED"
        result = rfid("READ", LCD, buzzer_on, LED_State("ON"))   

        if result == "ACCESS GRANTED":
            # With RFID tag verified, we now need to verify the password from keypad. 
            result = keypad(LCD, buzzer_on)  # this will return "CORRECT PASSWORD" if it is valid
            if result == "CORRECT PASSWORD": 
                servo("OPEN")
                # TO DO: notify owner of unlocked door in web site
                # LCD OFF? 
                # Remote change rfid or passwords or unlock 