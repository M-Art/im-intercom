import cherrypy
import time

import buttons
import lcd
import linphone

registered = {}
current_position = 0
busy = False

class IntercomServer(object):
    @cherrypy.expose
    def login(self, name, address):
        global registered
        registered[name] = address
        lcd_refresh()
        return "logged in"

    @cherrypy.expose
    def logout(self, name, address):
        global registered
        if name in registered:
            del registered[name]
        lcd_refresh()
        return "logged out"

def prev_button():
    global current_position, busy
    if not busy:
        current_position -= 1
        lcd_refresh()

def next_button():
    global current_position, busy
    if not busy:
        current_position += 1
        lcd_refresh()

def call_button():
    global registered, current_position, busy
    busy = True
    keys = registered.keys()
    l = len(keys)
    address = registered[keys[current_position % l]]
    success = linphone.call(address)
    if success:
        # TODO:
        pass
    else:
        busy = False
        lcd.println(0, "Call failed.")
        time.sleep(2)
        lcd_refresh()

def lcd_refresh():
    global registered, current_position
    lcd.println(0, "Choose:")
    l = len(registered)
    if l == 0:
        lcd.println(1, "--")
    else:
        keys = registered.keys()
        name = keys[current_position % l]
        lcd.println(1, name)

def init():
    RPi.GPIO.cleanup()
    buttons.init()
    lcd.init()

    lcd_refresh()

    buttons.set_up_btn_callback(next_button)
    buttons.set_down_btn_callback(prev_button)
    buttons.set_enter_btn_callback(call_button)

if __name__ == "__main__":
    init()
    cherrypy.quickstart(IntercomServer())
