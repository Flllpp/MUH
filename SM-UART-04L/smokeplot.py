#!/usr/bin/env python3
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import argparse

def makedate(zeit):
    return datetime.strptime(zeit.decode(), "%d-%b-%Y")

def maketime(zeit):
    return datetime.strptime(zeit.decode(), "%H:%M:%S.%f").time()

parser = argparse.ArgumentParser(description="Plot some smoke.")
parser.add_argument("input", nargs=1, help="Input as csv")
parser.add_argument("output", nargs=1, help="Output as png")
parser.add_argument("--xkcd", action="store_true", help="Plot all wobbly")
parser.add_argument("--minterval", metavar = "interval", type=int, default=1, help="Distance between x-ticks, default=1") 
args = parser.parse_args()

data = np.genfromtxt(args.input[0],
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
if args.xkcd:
    plt.xkcd()
else:
    plt.rcParams["font.size"] = "16"

plt.figure(figsize=(20,10))
plt.plot(ndata[:,0],ndata[:,1], label="PM 1")
plt.plot(ndata[:,0],ndata[:,2], label="PM 2.5")
plt.plot(ndata[:,0],ndata[:,3], label="PM 10")

plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=args.minterval))

plt.xlim([ndata[:,0].min(),ndata[:,0].max()])
plt.ylabel("μg/m$^3$")

plt.legend()

plt.savefig(args.output[0], bbox_inches="tight")

#print(data[0])
#print(ndata[:10,0])
