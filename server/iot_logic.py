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
import requests

import socket

# Socket establising connection to web_iot.py script for remote login and remote register rfid

# This function creates a new connection with the server
# it returns the socket being connected
def newConnection():
    # Connecting to server
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8000

    try:
        soc.connect((host, port))
    except:
        print('\n' + '\33[41m' + "[ERROR] Connection Error. Cannot connect to server" + '\33[0m' )
        pass
    
    return soc

# This function receives the binary input sent from a client
# It then decodes the message and returns it as a string
# The arguments of this function are connection which is the socket connection and the max buffer size 
def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    decodedInput = client_input.decode("utf8").rstrip()
    return decodedInput

def main():
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
                    resp = requests.post(f"https://api.thingspeak.com/apps/thingtweet/1/statuses/update",  # Sending to twitter acc notification 
                        json={"api_key":"KP60V4Y3POZWNP19","status":"Door has been unlocked!"})

                    sleep(30)
                    LCD(None, None)  # Offing LCD   
                    # TO DO: notify owner of unlocked door in web site  
                    # Remote change rfid or passwords or unlock (changing of text files)

# # This function is to allow user to open the door remotely 
# def remoteUnlock():
#     servo("OPEN")
#     LCD('Door is unlocked!', '----->')
#     sleep(30)

# # This function is for users to remotely change rfid tag with a button on the website
# def registerRFID():
#     result = rfid("REGISTER", LCD, buzzer_on, LED_State)  
#     if result == "REGISTERED":
#         return "SUCCESS"

if __name__ == "__main__":
    main()