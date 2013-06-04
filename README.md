im-intercom
===========

Drivers
-------
Use RPi.GPIO.cleanup before using drivers

    RPi.GPIO.cleanup()

Init drivers before usage

    buttons.init()
    lcd.init()

You can add callback to buttons with

    buttons.set_up_button_callback(callback_up)
    buttons.set_down_button_callback(callback_down)
    buttons.set_enter_button_callback(callback_enter)

Where callbacks are parameterless functions.
To print line on LCD use

    lcd.println(num, "text")

where num is 0 or 1
    
