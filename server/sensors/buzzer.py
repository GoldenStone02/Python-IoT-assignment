def buzzer_on():
    import RPi.GPIO as GPIO #import RPi.GPIO module
    from time import sleep #used to create delays

    GPIO.setmode(GPIO.BOARD) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(12,GPIO.OUT) #set GPIO 12 as output

    GPIO.output(12,1) #output logic high/'1'
    sleep(1) #delay 1 second
    GPIO.output(12,0) #output logic low/'0'
    sleep(0.5) #delay 0.5 second
