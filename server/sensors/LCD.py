def LCD(message, message2): # message is variable we want to display on the LCD
    import I2C_LCD_driver #import the library
    from time import sleep

    LCD = I2C_LCD_driver.lcd() #instantiate an lcd object, call it LCD
    sleep(0.5)
    LCD.backlight(0) #turn backlight off
    sleep(0.5)
    LCD.backlight(1) #turn backlight on 
    
    if (message != None or message2 != None):
        LCD.lcd_display_string(message, 1) #write on line 1
        LCD.lcd_display_string(message2, 2) #write on line 2 
        sleep(2) # wait 0.1 sec
        return 

    elif (message == None):  # For no messages, we will clear display
        LCD.lcd_clear() #clear the display
        sleep(2) #wait 1 sec
        return
