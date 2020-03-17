import tkinter
import datetime
from tkinter import Tk, mainloop, TOP
# import tkinter as TK
import os
from gps import *
from time import *
import time
import threading
import tkinter.font as font
import tmp
import rate
import distance
import datetime
import csv
import save

countm = 0
counter = 0
running = False

gpsd = None  # seting the global variable

os.system('clear')  # clear the terminal (optional)


def counter_label(label, meters):
    def count():
        if running:
            global counter
            global countm
            global writer
            global split
            global strate
            global display
            global displaym
            if counter == 0:  # To manage the intial delay.
                display = "Starting..."
                displaym = "starting..."
            else:
                counter = round(counter, 2)
                countm = round(countm, 1)
                display = datetime.timedelta(seconds=counter)
                display = str(display)
                display = display[2:]
                displaym = countm

            label['text'] = display  # Or label.config(text=display)
            meters['text'] = displaym  # Or label.config(text=display)
            # lat = gpsd.fix.latitude
            # lon = gpsd.fix.longitude
            lat = 0
            lon = 0
            label.after(100, count)  # Delays by 1000ms=1 seconds and call count again.
            counter += 0.1
            # lat1 = gpsd.fix.latitude
            # lon1 = gpsd.fix.longitude
            lat1 = 0
            lon1 = 0
            dist = distance.distance(lat, lat1, lon, lon1)
            countm = countm + dist

    # Triggering the start of the counter.
    count()


def filename():
    now = datetime.datetime.now()
    date = now.strftime('%m:%M:%S')
    date = date + '.csv'
    date = date.replace(':', '')
    file = 'C:/Users/Brend/PycharmProjects/coxbox/' + date
    aaa = file
    return aaa


# start function of the stopwatch
def Start(label, meters):
    global running
    global writer
    running = True
    counter_label(label, meters)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# Stop function of the stopwatch
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


# Reset function of the stopwatch
def Reset(label, meters):
    global counter
    global countm
    countm = 0
    counter = 0
    if running == False:  # If rest is pressed after pressing stop.
        reset['state'] = 'disabled'
        label['text'] = 'Welcome!'
    else:  # If reset is pressed while the stopwatch is running.
        label['text'] = 'Starting...'


class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd  # bring it in scope
        gpsd = gps(mode=WATCH_ENABLE)  # starting the stream of info
        self.current_value = None
        self.running = True  # setting the thread running to true

    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next()  # this will continue to loop and grab EACH set of gpsd info to clear the buffer


root = Tk()
# but = tkinter.Button(root)
# but1 = tkinter.Button(root)
# lab1 = tkinter.Label(root)
# lab = tkinter.Label(root)
myFont = font.Font(family='Arial', weight="bold", size='60')
lab2 = tkinter.Label(root)
lab3 = tkinter.Label(root)
label = tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
meters = tkinter.Label(root, text="Meters", fg="black", font="Verdana 30 bold")
start = tkinter.Button(root, text='Start', width=15, command=lambda: Start(label, meters))
stop = tkinter.Button(root, text='Stop', width=15, state='disabled', command=Stop)
reset = tkinter.Button(root, text='Reset', width=15, state='disabled', command=lambda: Reset(label, meters))
# but.grid(row=1, column=1, padx=5, pady=5)
# but1.grid(row=1, column=3, padx=5, pady=5)
label.grid(row=15, column=1, padx=5, pady=5)
meters.grid(row=15, column=5, padx=5, pady=5)
start.grid(row=16, column=1, padx=5, pady=5)
stop.grid(row=16, column=3, padx=5, pady=5)
reset.grid(row=16, column=5, padx=5, pady=5)
# lab.grid(row=10, column=1, padx=5, pady=5)
# lab1.grid(row=10, column=3, padx=5, pady=5)
lab2.grid(row=5, column=1, padx=5, pady=5)
lab3.grid(row=5, column=5, padx=5, pady=5)
# lab['font'] = myFont
# lab1['font'] = myFont
lab2['font'] = myFont
lab3['font'] = myFont
root.minsize(width=250, height=70)

# gpsp = GpsPoller()  # create the thread
# gpsp.start()


aaaaa = filename()
def clock():
    global split
    global strate
    # lat = gpsd.fix.latitude
    # lon = gpsd.fix.longitude
    lat = 0
    lon = 0
    # strate = my_queue.get()
    # strate = rate.Main.doit()
    strate = 0
    # spd = functs.getSpd()
    dist = 500
    # meterss = gpsd.fix.speed
    meterss = 0
    print(meterss)
    if meterss is not NaN:
        # split = float(dist) / meterss
        split = 0
    else:
        split = 0
    # lat2 = gpsd.fix.latitude
    # lon2 = gpsd.fix.longitude

    displayable = str(datetime.timedelta(seconds=split))
    # lab.config(text=lat)
    # lab1.config(text=lon)
    lab2.config(text=strate)
    lab3.config(text=displayable)
    # but.config(text="start timer")
    # but1.config(text="end timer")
    # lab['text'] = time
    if running is True:
        save.record(None, filename(), displaym, strate, split)
    root.after(500, clock)  # run itself again after 1000 ms

    # run first time


clock()

root.mainloop()
