# In this function, it will constantly wait and detect if there is any motion.
# If there is motion detected, it will return a string 'MOTION DETECTED' else, it will continue to detect until there is motion
def PIR():
    import RPi.GPIO as GPIO #import RPi.GPIO module
    from time import sleep

    GPIO.setmode(GPIO.BOARD) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.IN) # set GPIO 17 as input

    sleep(5) #to allow sensor time to stabilize
    PIR_state=0 #use this, so that only a change in state is reported
    while (True):
        if GPIO.input(17): #read a HIGH i.e. motion is detected
            if PIR_state==0:
                print('detected HIGH i.e. motion detected')
                PIR_state=1
                return 'MOTION DETECTED'
        else: #read a LOW i.e. no motion is detected
            if PIR_state==1:
                print('detected LOW i.e. no motion detected')
                PIR_state=0
        sleep(1)
