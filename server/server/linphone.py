import subprocess
import re
import time

class LinphoneError(Exception):
    """Linphone error.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def init(config_path = None):
    """Initialize linphonecsh subprocess.

    If .linphonerc exists, tries to register on saved servers.
    May throw LinphoneError.
    """
    if config_path is not None:
        args = ["linphonecsh", "init", "-c", config_path]
    else:
        args = ["linphonecsh", "init"]

    ret = subprocess.check_output(args)
    if ret != "" and not re.search("A running linphonec has been found", ret):
        raise LinphoneError("Init failed: " + ret)
    
    count = 0
    exit_code = subprocess.call(["linphonecsh", "status", "hook"])
    while exit_code == 255 and count < 50:
        time.sleep(0.1)
        count += 1
        exit_code = subprocess.call(["linphonecsh", "status", "hook"])
    if exit_code == 255:
        raise LinphoneError("Init failed: timeout")

def register(username, password, host):
    """Register user.

    Registers user on a host (defaults to sip.linphone.org).
    May throw LinphoneError.
    """
    if is_registered():
        raise LinphoneError("Already registered.")

    try:
        ret = subprocess.check_output(["linphonecsh", "register"
                                       "--host", host,
                                       "--username", username,
                                       "--password", password])
    except subprocess.CalledProcessError:
        raise LinphoneError(ret)

def is_registered():
    """Check if user is registered.
    """
    try:
        ret = subprocess.check_output(["linphonecsh", "status", "register"])
    except subprocess.CalledProcessError as e:
        ret = e.output

    if "identity=" in ret:
        return True
    else:
        return False

def call(address):
    """Makes a call.

    Return true if call succeeded, false otherwise.
    """
    subprocess.call(["linphonecsh", "generic", "call " + address])
    
    count = 0
    ret = subprocess.check_output(["linphonecsh", "status", "hook"])
    while count < 50:
        time.sleep(1)
        count += 1
        ret = subprocess.check_output(["linphonecsh", "status", "hook"])
        if re.search("offhook", ret):
            return False
        elif re.search("^Call out", ret):
            return True
        elif re.search("dialing", ret):
            pass
        elif re.search("ringing", ret):
            pass

def is_in_call():
    ret = subprocess.check_output(["linphonecsh", "status", "hook"])
    if re.search("offhook", ret):
        return False
    elif re.search("^Call out", ret):
        return True
    elif re.search("dialing", ret):
        return True

def unregister():
    """Unregister user.
    """
    subprocess.call(["linphonecsh", "unregister"])

def exit():
    """Exit linphone.
    """
    subprocess.call(["linphonecsh", "exit"])
