from .sensors.buzzer import buzzer_on
from .sensors.LCD import LCD
from .sensors.LED import LED_State
from .sensors.rfid import rfid
from .sensors.servo import servo

from time import sleep

# This function is to allow user to open the door remotely 
def remoteUnlock():
    servo("OPEN")
    LCD('Door is unlocked!', '----->')
    sleep(20)

# This function is for users to remotely change rfid tag with a button on the website
def registerRFID():
    result = rfid("REGISTER", LCD, buzzer_on, LED_State)  
    if result == "REGISTERED":
        sleep(20)
    