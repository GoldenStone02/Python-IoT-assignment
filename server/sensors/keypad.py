from datetime import datetime
from time import sleep


def keypad(LCD, buzzer, LED):
    import RPi.GPIO as GPIO
    from time import sleep

    timeON = datetime.now() # this will help keypad to auto off if user leaves midway 

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    MATRIX=[ [1,2,3],
            [4,5,6],
            [7,8,9],
            ['*',0,'#']] #layout of keys on keypad

    # ROW=[26,23,33,10] #row pins other class one
    # COL=[32,29,36] #column pins other class one

    ROW=[31, 38, 35, 33]  # Correct one for gpio.board
    COL = [32, 29, 36]    # Correct one for gpio.board

    #set column pins as outputs, and write default value of 1 to each
    for i in range(3):
        GPIO.setup(COL[i],GPIO.OUT)
        GPIO.output(COL[i],1)

    #set row pins as inputs, with pull up
    for j in range(4):
        GPIO.setup(ROW[j],GPIO.IN,pull_up_down=GPIO.PUD_UP)

    #scan keypad
    keyPressed = []  # this will be used to store all key presses 
    count = 0   # count will help keep track of number of wrong attempts 
    LCD(''.join(keyPressed), "# ENTER * DEL")    #print the key pressed on LCD one by one
    while (True):
            
        f = open('../server/database/password.txt', "r+")
        password = f.read()  # password is stored in ../server/database/password.txt folder 

        f = open('../server/database/otp.txt', "r+")
        otp = f.read()  # password is stored in ../server/database/password.txt folder 
        timeNOW = datetime.now()
        for i in range(3): #loop thru’ all columns
            GPIO.output(COL[i],0) #pull one column pin low
            for j in range(4): #check which row pin becomes low
                if GPIO.input(ROW[j])==0: #if a key is pressed
                    print(f"key pressed: {MATRIX[j][i]}") #print the key pressed
                    if MATRIX[j][i] != '#' and MATRIX[j][i] != '*':
                        keyPressed.append(f"{MATRIX[j][i]}")
                    
                    # now, we will check whether user deletes or presses enter. 
                    # we will use the symbols * for delete and # for enter
                    if MATRIX[j][i] == "*" and keyPressed != []:
                        print(f"Deleted: {keyPressed[-1]}")
                        keyPressed.pop(-1) # Delete last element from list (last number typed)
                    elif MATRIX[j][i] == "#":
                        # we will check the password here 
                        if ''.join(keyPressed) == password or ''.join(keyPressed) == otp:  # password for now is set as 123456 on line 1
                            return "CORRECT PASSWORD"
                        else: # incorrect password
                            count += 1
                            buzzer()   # on buzzer for sound
                            LED()      # on LED indicating that incorrect password
                            keyPressed.clear()
                            if count >= 5:   # after 5 wrong attempts, we will tell user to redo whole operation again 
                                LCD("5 Incorrect Attempts. Please try again.", "Offing keypad...")
                                sleep(15)
                                return 
                                
                            LCD("INCORRECT PASSWORD.", "Please try again...")  

                    LCD(''.join(keyPressed), "# ENTER * DEL")    #print the key pressed on LCD one by one

                    while GPIO.input(ROW[j])==0: #debounce
                        sleep(0.1)
            GPIO.output(COL[i],1) #write back default value of 1

        if (timeNOW - timeON).seconds >= 3000:   # This is for the case if user decides to quit midway, the keypad will off by itself
            return "KEYPAD OFF"