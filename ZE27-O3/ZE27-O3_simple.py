#! /usr/bin/env python3

import smbus
import time

ADDR_0=0x73
ADDR_1=0x72
ADDR_2=0x71
ADDR_3=0x70
ADDR=ADDR_0
START_POS=0x05
DATA_LEN=0x09
BUS_RPI = 1
DATA_UNIT_POS=0x02
DATA_UNIT_PPB=0x04
ACT_HB_POS=0x04
ACT_LB_POS=0x05
PAS_HB_POS=0x02
PAS_LB_POS=0x03
DATA_CKS_POS=0x08
MODE_ACTIVE =0x00
MODE_PASSIVE=0x01
MODE_REGISTER=0x03
PASSIVE_READ_REGISTER=0x04

PPB_BUF_NUM=1
PPB_BUF_MAX=0xFFFF
PPB_BUFFER=[0]*PPB_BUF_MAX

def setMode( bus, mode, addr=ADDR ):
    bus.write_i2c_block_data(addr, MODE_REGISTER, [mode] )

def dataCheckSum( data ):
    return (~sum( data[1:DATA_CKS_POS] ) + 1) % 256

def checkChecksum( data ):
    return dataCheckSum(data) == data[DATA_CKS_POS]

def readData( bus, mode, addr=ADDR, start=START_POS, nof_bytes=DATA_LEN ):
    if mode == MODE_ACTIVE:
        return bus.read_i2c_block_data(addr,start,nof_bytes)
    if mode == MODE_PASSIVE:
        bus.write_i2c_block_data(addr,PASSIVE_READ_REGISTER,[MODE_PASSIVE])
        return bus.read_i2c_block_data(addr,start,nof_bytes)

def dataToPPB( data, mode=MODE_ACTIVE ):
    if mode == MODE_ACTIVE:
        if data[DATA_UNIT_POS] == DATA_UNIT_PPB:
            #print(data[ACT_LB_POS])
                ppb = (data[ACT_HB_POS] << 8) + data[ACT_LB_POS]
        else:
            print( "ERROR: Unknown unit ", data[DATA_UNIT_POS] );
            ppb = 0
    elif mode == MODE_PASSIVE:
        ppb = (data[PAS_HB_POS] << 8) + data[PAS_LB_POS]
    else:
        print( "ERROR: Unknwon mode ", mode );
        ppb = 0
    return ppb

def printPPB( ppb, average=0, bnum=PPB_BUF_NUM, end="\r" ):
    print( f"Ozone ppb: {ppb} Average: {average}", end=end )


def averageUsingBuffer( value, buf=PPB_BUFFER, blen=PPB_BUF_MAX, bnum=PPB_BUF_NUM ):
    if bnum >= blen:
        bnum = blen
        buf = buf[1:bnum]
    buf[bnum-1] = value
    #print(buf)
    return sum( buf[:bnum] ) / bnum

def exitClose(bus, nmeasure=0):
    if nmeasure > 0:
        print( f"Did {nmeasure} measurements." )
        with open( "ozone_data.out", "w" ) as ozout:
            for i in range(nmeasure):
                ozout.write( str(PPB_BUFFER[i]) + "\n" )
    bus.close()


def main():
    nof_measurements = PPB_BUF_NUM;
    sbus = smbus.SMBus(BUS_RPI)
    mode=MODE_PASSIVE
    setMode(sbus, mode)
    try:
        while True:
            data = readData( sbus, mode )
            if not checkChecksum( data ):
                print( "WARNING: The checksum was checked to be wrecked." )
            #print(data)
            ppb=dataToPPB(data, mode)
            printPPB( ppb, averageUsingBuffer(ppb,bnum=nof_measurements) )
            nof_measurements+=1
            time.sleep(1)
    except KeyboardInterrupt:
        printPPB( ppb, averageUsingBuffer(ppb,bnum=nof_measurements), end="\n" )
        exitClose(sbus, nof_measurements)
    finally:
        exitClose(sbus)

if __name__=="__main__":
    main()


