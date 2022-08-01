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

from time import sleep

picList = [1,2,3,4,5,6]
# Main Programme
i = 0 
while True:
    servo("CLOSED")
    LCD('Awaiting Motion..', '-------->')
    motion_detected = PIR()
    if motion_detected == 'MOTION DETECTED': # For when motion is finally detected, continue onwards to the programme.
        LCD('Motion Detected', 'ON RFID....')
        # With motion detected, we first want to take a picture 
        take_pic(picList[i])      # picture taken will be stored in /database/image_upload/picture.jpg
        i += 1
        if i > 5: 
            i = 0   # Resetting of i 

        # RFID will go into READ mode, result == "ACCESS GRANTED" if valid. Else, if invalid, result == "ACCESS DENIED"
        result = rfid("READ", LCD, buzzer_on, LED_State)   

        if result == "ACCESS GRANTED":
            # With RFID tag verified, we now need to verify the password from keypad. 
            result = keypad(LCD, buzzer_on, LED_State)  # this will return "CORRECT PASSWORD" if it is valid
            if result == "CORRECT PASSWORD": 
                servo("OPEN")
                LCD('Door is unlocked!', '----->')
                sleep(30)
                LCD(None, None)  # Offing LCD   

                # TO DO: notify owner of unlocked door in web site  
                # Remote change rfid or passwords or unlock (changing of text files)

def remoteUnlock():
    servo("OPEN")
    LCD('Door is unlocked!', '----->')
    sleep(30)