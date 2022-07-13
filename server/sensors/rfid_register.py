import RPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
reader = SimpleMFRC522()
auth = []

while True:
        print("Hold card near the reader to register it in the database")
        id = reader.read_id()
        id = str(id)
        f = open("authlist.txt", "a+")
        f = open("authlist.txt", "r+")
        if f.mode == "r+":
              auth=f.read()
        if id not in auth:
              f.write(id)
              f.write('\n')
              f.close()
              pos = auth.count('\n')
              print("New card with UID", id,  "detected; registered as entry #", pos)
        else:
              number = auth.split('\n')
              pos = number.index(id)
              print("Card with UID", id, "already registered as entry #", pos)
        sleep(2)
