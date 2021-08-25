#!/usr/bin/env python3
from datetime import datetime
import serial

ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )

while 1:
    x = ser.read(32)
    #print(x)
    y = [int(x[i]) for i in range(4,16)]
    #print(*y)
    #print int.frombytes(y)
    #for byte in y:
    #    print(ord(byte))
    #print("Relevant values: %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d" % 1,2,2,2,2,2,2,2,2,2,2,2,2)
    #print("Relevant values:", *y)
    pm1   = y[0]*256 + y[1]
    pm25  = y[2]*256 + y[3]
    pm10  = y[4]*256 + y[5]
    pm1e  = y[6]*256 + y[7]
    pm25e = y[8]*256 + y[9]
    pm10e = y[10]*256 + y[11]
    #print(datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")[:-5], "  ", *y, flush=True)
    #print(datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")[:-5], "  ",  pm1, pm25, pm10, pm1e, pm25e, pm10, flush=True)
    print(datetime.now().strftime("%d-%b-%Y,%H:%M:%S.%f")[:-5],
            f", %3d, %3d, %3d, %3d, %3d, %3d" % (pm1, pm25, pm10, pm1e, pm25e, pm10),
            sep="",
            flush=True
            )

