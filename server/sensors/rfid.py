def rfid(state, LCD, buzzer, LED):  # state = "REGISTER" or "READ" and LCD will help display messages, buzzer for sounding when wrong rfid tag
      import RPi.GPIO as GPIO
      from time import sleep
      import sys
      from .mfrc522 import SimpleMFRC522

      GPIO.setwarnings(False)
      reader = SimpleMFRC522()
      auth = []

      # Code for read
      count = 0
      while True:
            LCD("Place RFID TAG...","---->")
            if state == "READ":
                  print("Hold card near the reader to check if it is in the database")
                  id = reader.read_id()
                  id = str(id)
                  print(f"card id is : {id} ")   # printing of card id
                  f = open('../server/database/authlist.txt', "r+")
                  if f.mode == "r+":
                        auth=f.read()
                  if id in auth:
                        number = auth.split('\n')
                        pos = number.index(id)
                        print("Card with UID", id, "found in database entry #", pos, "; access granted")
                        LCD("Valid RFID Tag","---->")
                        return "ACCESS GRANTED"
                  else:
                        count += 1
                        print("Card with UID", id, "not found in database; access denied")
                        LCD('Incorrect RFID, Please Try again', "---x---")
                        LED()
                        buzzer()
                        
                        if count == 5:  # this is to ensure that rfid will get out of loop after a number of attempts and off. 
                              return "ACCESS DENIED"

                  sleep(2)

            # Code for registering card remotely
            elif state == "REGISTER":   
                  print("Hold card near the reader to register it in the database")
                  id = reader.read_id()
                  id = str(id)
                  f = open('server/database/authlist.txt', "a+")
                  f = open('/database/authlist.txt', "r+")
                  if f.mode == "r+":
                        auth=f.read()
                  if id not in auth:
                        f.write(id)
                        f.write('\n')
                        f.close()
                        pos = auth.count('\n')
                        print("New card with UID", id,  "detected; registered as entry #", pos)
                        LCD("New card with UID", id,  "detected; registered as entry #", pos)
                        return "REGISTERED"
                  else:
                        count += 1 
                        number = auth.split('\n')
                        pos = number.index(id)
                        LCD("Card with UID", id, "already registered as entry #", pos)
                        buzzer()
                        print("Card with UID", id, "already registered as entry #", pos)
                        if count == 5:  # this is to ensure that rfid will get out of loop after a number of attempts and off. 
                              return "ALREADY EXISTS"
                  sleep(2)
