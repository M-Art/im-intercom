im-intercom
===========

Drivers
-------
Use RPi.GPIO.cleanup before using drivers

    RPi.GPIO.cleanup()

Init drivers

    buttons.init()
    lcd.init()

You can add callback to buttons with

    buttons.set_up_button_callback(callback_up)
    buttons.set_down_button_callback(callback_down)
    buttons.set_enter_button_callback(callback_enter)

where callbacks are parameterless functions. You can set callbacks before init drivers.
To print line on the LCD use

    lcd.println(num, "text")

where num is 0 or 1.
    
