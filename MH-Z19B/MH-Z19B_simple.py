#!/usr/bin/python3
import sys, datetime, time, serial

DATA_XFF_POS  = 0
DATA_CMD_POS  = 1
DATA_CO2_HIGH_POS  = 2
DATA_CO2_LOW_POS  = 3
DATA_CKS_POS  = 8
PORT_SERIAL0  = '/dev/serial0'
CMD_READ_VAL  = b"\xff\x01\x86\x00\x00\x00\x00\x00\x79"
SENS_DATA_LEN = 9
SENS_SLEEP_TIME = 0.1
SENS_BAUD_RATE=9600
SENS_TIME_OUT=2.0
CO2_MIN_PPM = 400
CO2_MAX_PPM = 5000
#TIME_FORMAT_STR = "%Y-%m-%dT%H:%M:%S.%f"
WAIT_TIME = datetime.timedelta(seconds=60)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

#MH-Z19 Checksum
def dataCheckSum( data ):
    return (~sum( data[1:DATA_CKS_POS] ) + 1) % 256

def checkChecksum( data ):
    badata = bytearray(data)
    if len(badata) < DATA_CKS_POS:
        eprint( f"ERROR: Read only {len(badata)} bytes, expected {SENS_DATA_LEN}" )
        return None
    chksum = dataCheckSum( data )
    if chksum != badata[DATA_CKS_POS]:
        eprint( "WARNING: Checksum mismatch:\n" +
                "       crc8(" + bytes(badata[0:7]) + 
                f") with checksum {badata[DATA_CKS_POS]} != {chksum}" )
        return False
    return True

def calcCO2ppmFrmData( data ):
    co2ppm = -1
    if len( data ) > DATA_CO2_LOW_POS:
        co2ppm = (data[DATA_CO2_HIGH_POS] << 8) + data[DATA_CO2_LOW_POS]
    if data[DATA_XFF_POS] == 0xff and data[DATA_CMD_POS] == 0x86:
        return co2ppm
    else:
        eprint( "WARNING: XFF CMD ",data[DATA_XFF_POS]," ",s[DATA_CMD_POS],
                " co2 ppm=", co2ppm )
        return co2ppm


#TODO: Calibration could be done by hand, but ABC should
#      help if CO2 level can be kept low every few days

def readSensor( bus ):
    res = bus.write( CMD_READ_VAL )
    time.sleep( SENS_SLEEP_TIME )
    data = bus.read( SENS_DATA_LEN )
    chksumcheck = checkChecksum( data )
    if chksumcheck is not None:
        co2ppm = calcCO2ppmFrmData( data )
        eprint( f"ppm(CO2) = {co2ppm} at {datetime.datetime.now()}", end="\r" )
        if co2ppm < CO2_MIN_PPM:
            eprint( f"WARNING: CO2 ppm {co2ppm} below minimum of {CO2_MIN_PPM}.\n"
                    f"         Recalibration recommended!" )
        return co2ppm
    return False

def startupSensor():
    eprint( "Starting..." )
    starttime = datetime.datetime.now()
    logfn = f"MH-Z19B_CO2_{starttime:%Y-%m-%dT%H:%M:%S.%f}.log"
    eprint(f'Opening port {PORT_SERIAL0}')
    sbus = serial.Serial(PORT_SERIAL0, SENS_BAUD_RATE, timeout=SENS_TIME_OUT)
    eprint( "Serial bus set." )
    # Do test read
    if not readSensor( sbus ):
        eprint( "ERROR: Could not read from sensor. Exiting." )
        quit()
    eprint( "WARNING: If this the first start of the sensor after a while,\n"
            "         let it run for at least 20 minutes in clean air\n"
            "         at ~400 ppm CO2 concentration.\n"
            "         Automatic baseline correction will occur every 24 hours.\n"
            "         Values below 400 ppm are indicative of calibration errors!\n"
            )
    return sbus, logfn

def logSensorData(
        bus,
        logfn = f"MH-Z19B_CO2_{datetime.datetime.now():%Y-%m-%dT%H:%M:%S.%f}.log",
        ):
    ltime = datetime.datetime.now()
    with open( logfn, 'a' ) as logf:
        while True:
            co2ppm = readSensor( bus )
            logf.write( f"{datetime.datetime.now():%Y-%m-%dT%H:%M:%S.%f}\t{co2ppm:4}\n" )
            ctime = datetime.datetime.now()
            wait_td = WAIT_TIME - (ctime - ltime)
            time.sleep(wait_td.total_seconds())
            ltime = datetime.datetime.now()

def main():
    try:
        sbus, logfn = startupSensor()
        logSensorData( sbus, logfn=logfn )
    except Exception as e:
        sbus.close()
        eprint(f'ERROR {type(e).__name__}: {e}')
    except KeyboardInterrupt as e:
        sbus.close()
        eprint(f'STOP: Keyboard interrupt, stopping log of port {PORT_SERIAL0} to {logfn}\n')

if __name__ == '__main__':
    main()

