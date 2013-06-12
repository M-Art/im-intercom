import RPi.GPIO
import atexit
import cherrypy
import time

import buttons
import lcd
import linphone

busy = False
current_position = 0
registered = {}

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
    l = len(registered)
    if not busy and l != 0:
        # lock buttons
        busy = True

        # get address
        keys = registered.keys()
        keys.sort()
        address = registered[keys[current_position % l]]

        # call
        lcd.println(0, "Calling...")
        success = linphone.call(address)
        if success:
            # wait for the call to end
            lcd.println(0, "Call in progress.")
            while linphone.is_in_call():
                time.sleep(0.5)
        else:
            # print info
            lcd.println(0, "Call failed.")
            time.sleep(2)

        # refresh screen and unlock buttons
        lcd_refresh()
        busy = False

def lcd_refresh():
    global registered, current_position
    
    # print first line
    lcd.println(0, "Choose:")

    # print second line
    l = len(registered)
    if l == 0:
        lcd.println(1, "--")
    else:
        keys = registered.keys()
        keys.sort()
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

    linphone.init('/home/mateusz/.linphonerc')
    def linphone_atexit():
        linphone.unregister()
        linphone.exit()
    atexit.register(linphone_atexit)

def main():
    init()
    cherrypy.config.update({ 'server.socket_host': '0.0.0.0' })
    cherrypy.quickstart(IntercomServer())
