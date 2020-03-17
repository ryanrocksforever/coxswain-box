
import os
from gps import *
from time import *
import time
import threading

gpsd = None  # seting the global variable

os.system('clear')  # clear the terminal (optional)


class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd  # bring it in scope
        gpsd = gps(mode=WATCH_ENABLE)  # starting the stream of info
        self.current_value = None
        self.running = True  # setting the thread running to true

    def run(self):
        global gpsd
        gpsp = GpsPoller()
        while gpsp.running:
            gpsd.next()  # this will continue to loop and grab EACH set of gpsd info to clear the buffer

class Main:
    def stroke():
        velocity = gpsd.fix.speed
        past = velocity
        time.sleep(500)
        velocity = gpsd.fix.speed
        now = velocity
        if past < now + 1:
            return True
        else:
            return False



    def calc():
        stroke = Main.stroke()
        count = 0
        if stroke is True:
            while Main.stroke() is False:
                count = count + 0.1
                time.sleep(100)
            else:
                if count is not 0:
                    strokerate = 60 / count
                    return strokerate

    def doit():
        gpsp = GpsPoller()  # create the thread
        gpsp.start()
        return Main.calc()

