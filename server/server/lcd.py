# coding=UTF-8
import RPi.GPIO as GPIO
import time

LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
 
LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
 
# Time constants
E_PULSE = 0.00005
E_DELAY = 0.00005
 
def init():
    """ Init drivers
    """
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(LCD_E, GPIO.OUT)
    GPIO.setup(LCD_RS, GPIO.OUT)
    GPIO.setup(LCD_D4, GPIO.OUT)
    GPIO.setup(LCD_D5, GPIO.OUT)
    GPIO.setup(LCD_D6, GPIO.OUT)
    GPIO.setup(LCD_D7, GPIO.OUT)
 
    __lcd_init()

    println(0, "LCD initialized")
    println(1, "kotek :)")

def println(line, string):
    """Prints line on the LCD

    line - number of line (0 or 1)
    string - string to display (more than 16 characters will be trimmed)
    """
    if line == 0:
        __lcd_byte(LCD_LINE_1, LCD_CMD)
    else:
        __lcd_byte(LCD_LINE_2, LCD_CMD)
    __lcd_string(string)

def __lcd_init():
    __lcd_byte(0x33,LCD_CMD)
    __lcd_byte(0x32,LCD_CMD)
    __lcd_byte(0x28,LCD_CMD)
    __lcd_byte(0x0C,LCD_CMD)  
    __lcd_byte(0x06,LCD_CMD)
    __lcd_byte(0x01,LCD_CMD)  
 
def __lcd_string(message):
    message = message.ljust(LCD_WIDTH," ")  
 
    for i in range(LCD_WIDTH):
        __lcd_byte(ord(message[i]),LCD_CHR)
 
def __lcd_byte(bits, mode):
    GPIO.output(LCD_RS, mode)
 
    # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x10==0x10:
        GPIO.output(LCD_D4, True)
    if bits&0x20==0x20:
        GPIO.output(LCD_D5, True)
    if bits&0x40==0x40:
        GPIO.output(LCD_D6, True)
    if bits&0x80==0x80:
        GPIO.output(LCD_D7, True)
 
    time.sleep(E_DELAY)    
    GPIO.output(LCD_E, True)  
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)  
    time.sleep(E_DELAY)
 
    # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x01==0x01:
        GPIO.output(LCD_D4, True)
    if bits&0x02==0x02:
        GPIO.output(LCD_D5, True)
    if bits&0x04==0x04:
        GPIO.output(LCD_D6, True)
    if bits&0x08==0x08:
        GPIO.output(LCD_D7, True)

    time.sleep(E_DELAY)    
    GPIO.output(LCD_E, True)  
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)  
    time.sleep(E_DELAY)
