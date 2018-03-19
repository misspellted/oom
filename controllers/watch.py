from controllers import Controller
import sys
import time

class WatchController(Controller):
    def __init__(this):
        Controller.__init__(this)
        this.__timer = time.clock if "win32" in sys.platform else time.time

    def getTime(this):
        return this.__timer()
