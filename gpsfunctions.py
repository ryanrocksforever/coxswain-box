import serial
import pynmea2

ser = serial.Serial('COM7', 9600)


def filterVowels(alphabet):
    if alphabet.find('.') > 0:
        return alphabet


def filterSpeed():
    data = ser.readline().decode()
    data = str(data)
    # data = filterData(data)
    data = str(data)
    msg = pynmea2.parse(data)
    print(msg)
    if len(msg.data) is 12:
        fad = list(filter(None, msg.data))
        print(fad)
        return fad[6]


def filterLon():
    data = ser.readline().decode()
    data = str(data)
    # data = filterData(data)
    data = str(data)
    msg = pynmea2.parse(data)
    print(msg)
    if len(msg.data) is 12:
        fad = list(filter(None, msg.data))
        print(fad)
        return fad[2]


def filterLat():
    data = ser.readline().decode()
    data = str(data)
    # data = filterData(data)
    data = str(data)
    msg = pynmea2.parse(data)
    print(msg)
    if len(msg.data) is 12:
        fad = list(filter(None, msg.data))
        print(fad)
        return fad[3]


def filterData():
    msg = beforestuff()
    if msg.sentence_type is "RMC":
        return msg


def getLon():
    lat = filterLat()
    return lat


def getLat():
    lon = filterLon()
    return lon


def getSpd():
    hhh = filterSpeed()
    if hhh is None:
        return 1
    else:
        return hhh


def beforestuff():
    data = ser.readline().decode()
    # data = bytes(data)
    # print(data)
    if data.find('$GPGSV'):
        data = str(data)
        # data = filterData(data)
        data = str(data)
        msg = pynmea2.parse(data)
        return msg

