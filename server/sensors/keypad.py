password = 123456  # password for now is set as 123456

from time import sleep


def keypad(LCD, buzzer):
    import RPi.GPIO as GPIO
    from time import sleep

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    MATRIX=[ [1,2,3],
            [4,5,6],
            [7,8,9],
            ['*',0,'#']] #layout of keys on keypad
    ROW=[9,25,19,13] #row pins
    COL=[11,5,15] #column pins

    #set column pins as outputs, and write default value of 1 to each
    for i in range(3):
        GPIO.setup(COL[i],GPIO.OUT)
        GPIO.output(COL[i],1)

    #set row pins as inputs, with pull up
    for j in range(4):
        GPIO.setup(ROW[j],GPIO.IN,pull_up_down=GPIO.PUD_UP)

    #scan keypad
    keyPressed = []  # this will be used to store all key presses 
    while (True):
        count = 0   # count will help keep track of number of wrong attempts 

        for i in range(3): #loop thru’ all columns
            GPIO.output(COL[i],0) #pull one column pin low
            for j in range(4): #check which row pin becomes low
                if GPIO.input(ROW[j])==0: #if a key is pressed
                    print(f"key pressed: {MATRIX[j][i]}") #print the key pressed
                    keyPressed.append(MATRIX[j][i])
                    
                    # now, we will check whether user deletes or presses enter. 
                    # we will use the symbols * for delete and # for enter
                    if MATRIX[j][i] == "*":
                        keyPressed.pop(-1) # Delete last element from list (last number typed)
                    elif MATRIX[j][i] == "#":
                        # we will check the password here 
                        if ' '.join(keyPressed) == password:  # password for now is set as 123456 on line 1
                            return "CORRECT PASSWORD"
                        else: 
                            count += 1
                            buzzer()
                            if count >= 5:   # after 5 wrong attempts, we will tell user to redo whole operation again 
                                LCD("5 Incorrect Attempts. Please try again.", "Offing keypad...")
                                sleep(15)
                                
                            LCD("INCORRECT PASSWORD.", "Please try again...")

                    LCD(' '.join(keyPressed), "# For Enter and * For Delete---->")    #print the key pressed on LCD one by one

                    while GPIO.input(ROW[j])==0: #debounce
                        sleep(0.1)
            GPIO.output(COL[i],1) #write back default value of 1

        count += 1
        if count == 10000:   # This is for the case if user decides to quit midway, the keypad will off by itself
            return "KEYPAD OFF"