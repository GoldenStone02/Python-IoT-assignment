import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep

GPIO.setmode(GPIO.BCM) #choose BCM mode
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.IN) # set GPIO 17 as input

sleep(5) #to allow sensor time to stabilize
PIR_state=0 #use this, so that only a change in state is reported
while (True):
    if GPIO.input(17): #read a HIGH i.e. motion is detected
        if PIR_state==0:
            print('detected HIGH i.e. motion detected')
            PIR_state=1
    else: #read a LOW i.e. no motion is detected
        if PIR_state==1:
            print('detected LOW i.e. no motion detected')
            PIR_state=0
    sleep(1)
    print("...")
