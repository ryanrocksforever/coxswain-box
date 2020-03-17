import os
from gps import *
from time import *
import time
import threading
import rate
import csv

gpsd = None

global run
run = 0


def record(distance, name, meter, strate, split):
    global run
    if distance is None:
        if run >= 1:
            with open(name, 'a') as file:
                writer = csv.writer(file)
                writer.writerow([meter, strate, split])
        else:
            with open(name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["meter", "rate", "split"])
            run = 1