def LED_State():
    import RPi.GPIO as GPIO #import RPi.GPIO module, rename it as GPIO

    GPIO.setmode(GPIO.BOARD) #choose BOARD mode, refer to pins as GPIO no.
    GPIO.setwarnings(False)
    GPIO.setup(29,GPIO.OUT) #set GPIO 29 as output

    GPIO.output(29,1) #output logic high/'1'
    
