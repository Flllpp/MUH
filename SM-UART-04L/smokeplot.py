#!/usr/bin/env python3
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def makedate(zeit):
    return datetime.strptime(zeit.decode(), "%d-%b-%Y")

def maketime(zeit):
    return datetime.strptime(zeit.decode(), "%H:%M:%S.%f").time()


data = np.genfromtxt("out.txt",
        delimiter = ",",
        dtype = None,
        converters = {0:makedate, 1:maketime}
        )

ndata = []

for line in data:
    ndata.append([mdates.date2num(datetime.combine(line[0],line[1])),
        line[2],
        line[3],
        line[4],
        line[5],
        line[6],
        line[7]
        ])

ndata = np.array(ndata)

plt.xkcd()

plt.figure(figsize=(20,10))
plt.plot(ndata[:,0],ndata[:,1], label="PM 1")
plt.plot(ndata[:,0],ndata[:,2], label="PM 2.5")
plt.plot(ndata[:,0],ndata[:,3], label="PM 10")

plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=1))

plt.xlim([ndata[:,0].min(),ndata[:,0].max()])
plt.ylabel("μg/m$^3$")

plt.legend()

plt.savefig("wow.png", bbox_inches="tight")

#print(data[0])
#print(ndata[:10,0])
