# Need to follow structure of ppt 

# Importing various functions for sensor logic via the sensors folder.
from concurrent.futures import thread
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
import _thread, time

data = ''

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8000))


# Define a function for the thread
def listening_thread():
    global data     # data needs to be defined as global inside the thread
    while True:
        data_raw, addr = sock.recvfrom(1024)
        data = data_raw.decode()    # My test message is encoded
        print ("Received message inside thread:", data)

try:
   _thread.start_new_thread(listening_thread, ())
except:
    print ("Error: unable to start thread")
    quit()


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
                    resp = requests.post("https://api.thingspeak.com/apps/thingtweet/1/statuses/update?api_key=KP60V4Y3POZWNP19&status=Door has been unlocked!")

                    sleep(30)
                    LCD(None, None)  # Offing LCD   
                    # TO DO: notify owner of unlocked door in web site  
                    # Remote change rfid or passwords or unlock (changing of text files)

thread_count = 0

while 1:
    if data and thread_count == 1:
        print ("Stop program because of remote unlock/ rfid")
        thread_count = 0
        data = ''   # Empty the variable ready for the next one
        _thread.exit(main, ())
    else:
        thread_count += 1
        _thread.start_new_thread(main, ())
    time.sleep(2)


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
