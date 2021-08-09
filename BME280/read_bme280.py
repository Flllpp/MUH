#!/usr/bin/env python3

import bme280
from datetime import datetime
import time

while 1:
    temp,press,hum = bme280.readBME280All()

    print(datetime.now().strftime("%d-%b-%Y,%H:%M:%S.%f")[:-5],
            f",   %.2f °C,  %.2f mbar,   %.2f %%" % (temp,press,hum),
            sep="",
            flush=True
            )
    time.sleep(.5)
