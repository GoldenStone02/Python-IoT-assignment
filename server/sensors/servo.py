def servo(state): # State = UNLOCKED OR CLOSED
    import RPi.GPIO as GPIO #import RPi.GPIO module
    from time import sleep

    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(26,GPIO.OUT) #set GPIO 26 as output

    PWM=GPIO.PWM(26,50) #set 50Hz PWM output at GPIO26

    if state == 'CLOSED':
        PWM.start(3) #3% duty cycle
        print('duty cycle:', 3) #3 o'clock position for close position
        sleep(4) #allow time for movement
        print('servo motor is closed')
        return 

    elif state == 'OPEN':
        PWM.start(12) #13% duty cycle
        print('duty cycle:', 12) #9 o'clock position for open position
        sleep(4) #allow time for movement
        print('servo motor is unlocked')
        return

    else:
        print('error')

