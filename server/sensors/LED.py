def LED_State():
    from time import sleep
    import RPi.GPIO as GPIO #import RPi.GPIO module, rename it as GPIO

    GPIO.setmode(GPIO.BOARD) #choose BOARD mode, refer to pins as GPIO no.
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT) #set GPIO 29 as output

    GPIO.output(18,1) #output logic high/'1'
    sleep(2)
    GPIO.output(18,0) # off the led 
    
