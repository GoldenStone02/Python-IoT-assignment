from .sensors.buzzer import buzzer_on
from .sensors.LCD import LCD
from .sensors.LED import LED_State
from .sensors.rfid import rfid
from .sensors.servo import servo

from time import sleep

import requests

# This function is to allow user to open the door remotely 
def remoteUnlock():
    servo("OPEN")
    LCD('Door is unlocked!', '----->')
    resp = requests.post(f"https://api.thingspeak.com/apps/thingtweet/1/statuses/update",
        json={"api_key":"WFZR29Y48NUDO6H4","status":"Door has been unlocked!"})
    sleep(20)

# This function is for users to remotely change rfid tag with a button on the website
def registerRFID():
    result = rfid("REGISTER", LCD, buzzer_on, LED_State)  
    if result == "REGISTERED":
        sleep(20)
    