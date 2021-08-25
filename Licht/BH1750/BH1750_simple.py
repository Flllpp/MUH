#! /usr/bin/env python3
# Read from BH1750 light sensor using I2C over smbus package

import sys
import time
import smbus

# Define some constants from the datasheet

ADDR     = 0x23 # Default I2C address of BH1750
ALTADDR  = 0x50 # Alternative I2C address

POWER_DOWN = 0x00 # No active state (TODO)
POWER_ON   = 0x01 # Waiting for measurement command
RESET      = 0x07 # Reset data register value (Only in power on mode)

# Start measurement at 1 lx resolution. Measurement Time is typically 120ms
CONTINUOUS_H_RES_MODE_1 = 0x10
# Start measurement at 0.5 lx resolution. Measurement Time is typically 120ms
CONTINUOUS_H_RES_MODE_2 = 0x11
# Start measurement at 4 lx resolution. Measurement Time is typically 16ms.
CONTINUOUS_L_RES_MODE = 0x13
# Start measurement at 1 lx resolution. Measurement Time is typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_H_RES_MODE_1 = 0x20
# Start measurement at 0.5 lx resolution. Measurement Time is typically 120ms
# Automatically set to Power Down after measurement. --> Save Power
ONE_TIME_H_RES_MODE_2 = 0x21
# Start measurement at 1 lx resolution. Measurement Time is typically 120ms
# Automatically set to Power Down after measurement. --> Save Power
ONE_TIME_L_RES_MODE = 0x23
#Typical minimum wait times
CONTINUOUS_MIN_WAIT_H_RES_1 = 0.12
CONTINUOUS_MIN_WAIT_H_RES_2 = 0.15
CONTINUOUS_MIN_WAIT_L_RES   = 0.02
ONE_TIME_MIN_WAIT_H_RES_1   = 0.2
ONE_TIME_MIN_WAIT_H_RES_2   = 0.2
ONE_TIME_MIN_WAIT_L_RES     = 0.03
#TODO: Change Mesurement Time (Datasheet page 12)
# see here: https://wolles-elektronikkiste.de/bh1750fvi-lichtsensormodul

#bus = smbus.SMBus(0) # Revision 1 Pi uses 0
bus = smbus.SMBus(1)  # Revision 2 Pi uses 1

def readLuxSensor(addr=ADDR, mode=ONE_TIME_H_RES_MODE_1):
  # Read lux from I2C sensor device
  data = bus.read_i2c_block_data(addr,mode)
  return convert2Byte2Lux(data)

def convert2Byte2Lux(indata):
  # Convert low and high byte from senser
  # to lux. (Datashee p. 7)
  result=((indata[0] << 8 ) + indata[1] ) / 1.2
  return (result)

def giveOutputType( i ):
    if 0 <=int(i) <= 1:
        return int(i)
    else:
        print( "ERROR: Output types are 0 (simple) or 1 (suns)" );
        quit()

def main(args=[]):

  output_type=1
  if len(args) > 1:
      output_type = giveOutputType( args[1] )

  if output_type == 0:
    #Simple OT measurement every half second
    while True:
      print(f"{readLuxSensor():.2f}")
      time.sleep(0.5)

  if output_type == 1:
    #Graphical representation of continuous low res mode
    max_points = 200
    #To change the maximum lux, change the measurement time. TODO
    #Absolute maximum is 65535 * (69/31) / 1.2 ≈ 121557 lx 
    #(or 100000 according to datasheet(?))
    max_lx = (1 << 16) / 1.2
    while True:
      l = readLuxSensor(ADDR,CONTINUOUS_L_RES_MODE)
      print("[", "".join( ["☀️"] * ( round( l / max_lx * max_points ) ) ),
            "".join( [" "] * ( round( ( max_lx - l) / max_lx * max_points ) ) ) ,
            "]", f" {l:8.2f} lx", end="\r", sep="" )
      time.sleep(CONTINUOUS_MIN_WAIT_L_RES)

if __name__=="__main__":
   main(sys.argv)
