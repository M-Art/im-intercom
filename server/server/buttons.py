import RPi.GPIO as GPIO
import time

#Buttons map
__BUTTON_UP = 4
__BUTTON_DOWN = 17
__BUTTON_ENTER = 22
__BOUNCE_TIME = 200
__time = time.time()

def __default_button_callback():
    print('Default button callback.')

__button_up_callback = __default_button_callback
__button_down_callback = __default_button_callback
__button_enter_callback = __default_button_callback

def set_up_btn_callback(callback):
    """Set up button callback.

    callback - callback function with no parameters
    """
    global __button_up_callback
    __button_up_callback = callback

def set_down_btn_callback(callback):
    """Set down button callback.

    callback - callback function with no parameters
    """
    global __button_down_callback
    __button_down_callback = callback

def set_enter_btn_callback(callback):
    """Set enter button callback.
    
    callback - callback function with no parameters
    """
    global __button_enter_callback
    __button_enter_callback = callback

def __button_callback(channel):
    global __time
    
    if (time.time() - __time) < (float(__BOUNCE_TIME) / 1000):
        return
    __time = time.time()

    if channel == __BUTTON_UP:
        __button_up_callback()
    elif channel == __BUTTON_DOWN:
        __button_down_callback()
    elif channel == __BUTTON_ENTER:
        __button_enter_callback()
    else:
        print('No button callback.')

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(__BUTTON_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(__BUTTON_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(__BUTTON_ENTER, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(__BUTTON_UP, GPIO.RISING, bouncetime = __BOUNCE_TIME)
    GPIO.add_event_detect(__BUTTON_DOWN, GPIO.RISING, bouncetime = __BOUNCE_TIME)
    GPIO.add_event_detect(__BUTTON_ENTER, GPIO.RISING, bouncetime = __BOUNCE_TIME)

    GPIO.add_event_callback(__BUTTON_UP, __button_callback)
    GPIO.add_event_callback(__BUTTON_DOWN, __button_callback)
    GPIO.add_event_callback(__BUTTON_ENTER, __button_callback)

