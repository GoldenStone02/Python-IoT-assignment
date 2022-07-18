def LED_State(state):   # state = on / off 
    import RPi.GPIO as GPIO #import RPi.GPIO module, rename it as GPIO

    GPIO.setmode(GPIO.BOARD) #choose BCM mode, refer to pins as GPIO no.
    GPIO.setwarnings(False)
    GPIO.setup(24,GPIO.OUT) #set GPIO 24 as output

    GPIO.output(24,1) #output logic high/'1'
