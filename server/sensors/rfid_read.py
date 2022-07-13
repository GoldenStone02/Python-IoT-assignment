import RPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
reader = SimpleMFRC522()
auth = []

while True:
        print("Hold card near the reader to check if it is in the database")
        id = reader.read_id()
        id = str(id)
        f = open("authlist.txt", "r+")
        if f.mode == "r+":
              auth=f.read()
        if id in auth:
              number = auth.split('\n')
              pos = number.index(id)
              print("Card with UID", id, "found in database entry #", pos, "; access granted")
        else:
              print("Card with UID", id, "not found in database; access denied")
        sleep(2)
