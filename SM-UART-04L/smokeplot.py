#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def maketime(zeit):
    return datetime.strptime(zeit.decode(), "%d-%b-%Y %H:%M:%S.%f")

data = np.genfromtxt(
        "serial_output.txt",
        delimiter = ",",
        converters = {0:maketime})

print(str(data[0][0]))
