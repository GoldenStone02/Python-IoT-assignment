import I2C_LCD_driver #import the library
from time import sleep

LCD = I2C_LCD_driver.lcd() #instantiate an lcd object, call it LCD
sleep(0.5)
LCD.backlight(0) #turn backlight off
sleep(0.5)
LCD.backlight(1) #turn backlight on 
LCD.lcd_display_string("LCD Display Test", 1) #write on line 1
LCD.lcd_display_string("Address = 0x3f", 2, 2) #write on line 2
              #starting on 3rd column

sleep(2) #wait 2 sec
LCD.lcd_clear() #clear the display
