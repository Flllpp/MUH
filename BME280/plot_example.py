#!/usr/bin/env python3
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import argparse

# use sed "s/ °C//g; s/ mbar//g; s/ %//g"

def makedate(zeit):
    return datetime.strptime(zeit.decode(), "%d-%b-%Y")

def maketime(zeit):
    return datetime.strptime(zeit.decode(), "%H:%M:%S.%f").time()

parser = argparse.ArgumentParser(description="Plot some temperature, pressure, humidity.")
parser.add_argument("input", nargs=1, help="Input as csv")
parser.add_argument("output", nargs=1, help="Output as png")
parser.add_argument("--xkcd", action="store_true", help="Plot all wobbly")
parser.add_argument("--sinterval", metavar = "interval", type=int, default=30, help="Distance between x-ticks, default=30") 
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
        line[4]
        ])

ndata = np.array(ndata)
if args.xkcd:
    plt.xkcd()
else:
    plt.rcParams["font.size"] = "16"

plt.figure(figsize=(20,10))
fig,ax = plt.subplots()
twin1 = ax.twinx()
twin2 = ax.twinx()

twin2.spines.right.set_position(("axes", 1.25))

c1, = ax.plot(ndata[:,0],ndata[:,1], "b-", label="Temperatur")
c2, = twin1.plot(ndata[:,0],ndata[:,2], "r-", label="Druck")
c3, = twin2.plot(ndata[:,0],ndata[:,3], "g-", label="Relative Luftfeuchte")

ax.set_ylim(0, ndata[:,1].max()+10)
twin1.set_ylim(1000,1010)
twin2.set_ylim(0, 100)

ax.set_ylabel("Temperatur [°C]")
twin1.set_ylabel("Druck [mbar]")
twin2.set_ylabel("Relative Luftfeuchte [%]")

ax.yaxis.label.set_color(c1.get_color())
twin1.yaxis.label.set_color(c2.get_color())
twin2.yaxis.label.set_color(c3.get_color())

plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M:%S')
plt.gca().xaxis.set_major_formatter(myFmt)

ax = plt.gca()
ax.xaxis.set_major_locator(mdates.SecondLocator(interval=args.sinterval))

plt.savefig(args.output[0], bbox_inches="tight")

