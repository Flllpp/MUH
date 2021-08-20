# BME280 Druck-/Feuchtigkeits-/Temperatursensor

Verschiedene Versionen im Projekt, in Tims Falle ist es [diese](https://www.adafruit.com/product/2652), sonst wohl eher [diese](https://www.berrybase.de/sensoren-module/feuchtigkeit/gy-bme280-breakout-board-3in1-sensor-f-252-r-temperatur-luftfeuchtigkeit-und-luftdruck?c=92). Kram sollte aber übertragbar sein außer, dass zweiterer mit 5V **nicht** klar kommt. --> Direkt mit 3,3V arbeiten.

Kommunikation via I2C oder SPI
- I2C, zusammen mit Licht, Ozon und hoffentlich Feinstaub

|    Pin| |
|---|---|  
|**VIn**| 3,3V input|
|**3VO**| kommen 3,3V raus|
|**GND**| ground|
|**SCK**| I2C clock, sda auf dem pi auf pin5 (**s**erial **da**ta)|
|**SDI**| I2C data, scl auf dem pi auf pin3 (**s**erial **c**lock **l**ine)|
|**SD0**| nur bei SPI benötigt|
| **CS**| nur bei SPI benötigt|

### Pi-Kram:

- `raspi-config` benutzen um I2C zu aktivieren
- installation von `python-smbus` und `i2c-tools`
- python-library von [raspberry-pi-spy](https://www.raspberrypi-spy.co.uk/2016/07/using-bme280-i2c-temperature-pressure-sensor-in-python/) <3
  - nur fix noch mit `2to3` nach python3 konvertiert 😬
- Daten 🙌
```
Chip ID     : 96
Version     : 0
Temperature :  24.59 C
Pressure :  1003.41506951 hPa
Humidity :  43.8059545331 %
```
Jetzt noch ein bisschen selbst coden und gut is.

### Arduino-Kram

Library BME280: https://www.arduino.cc/reference/en/libraries/bme280/  
Library SD-Modul: https://funduino.de/nr-28-das-sd-karten-modul

- SD-Karte fromatieren auf FAT16 oder FAT32
-- Internet sagt, dass Karten >16 GB Probleme machen können. Habe nur 32 GB also mal sehen.


