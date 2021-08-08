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
    print(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)") + " next read:")
    x=ser.read(32)
    print(x)
