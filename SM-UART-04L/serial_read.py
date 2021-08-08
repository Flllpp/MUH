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
    x=ser.read(32)
    #print(x)
    y=[int(x[i]) for i in range(4,16)]
    #print(*y)
    #print int.frombytes(y)
    #for byte in y:
    #    print(ord(byte))
    #print("Relevant values: %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d" % 1,2,2,2,2,2,2,2,2,2,2,2,2)
    #print("Relevant values:", *y)
    print(datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")[:-5], "  ", *y, flush=True)
