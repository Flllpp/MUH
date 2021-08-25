#!/usr/bin/env python3

import bme280
from datetime import datetime
import time

while 1:
    temp,press,hum = bme280.readBME280All()
    height = (1 - (press / 1013.25) ** (1/5.255)) / 6.5 * 288150
    print(datetime.now().strftime("%d-%b-%Y,%H:%M:%S.%f")[:-5],
            f", %6.2f °C, %7.2f mbar, %6.2f %%, %7.2f m" % (temp,press,hum,height),
            sep="",
            flush=True
            )
    time.sleep(.5)
