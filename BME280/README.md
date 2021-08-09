# BME280 Druck-/Feuchtigkeits-/Temperatursensor

Verschiedene Versionen im Projekt, in Tims Falle ist es [diese](https://www.adafruit.com/product/2652), sonst wohl eher [diese](https://www.berrybase.de/sensoren-module/feuchtigkeit/gy-bme280-breakout-board-3in1-sensor-f-252-r-temperatur-luftfeuchtigkeit-und-luftdruck?c=92). Kram sollte aber übertragbar sein außer, dass zweiterer mit 5V **nicht** klar kommt. --> Direkt mit 3,3V arbeiten.

Kommunikation via I2C oder SPI
- was ist besser für uns?
  - da jeder sensor eigenen arduino bekommen soll ist I2C einfacher. SPI ist nur bei mehreren devices wirklich angenehmer

Pins:
**VIn**: 3,3V input
**3VO**: kommen 3,3V raus
**GND**: ground
**SCK**: I2C clock, sda auf dem pi auf pin3 (**s**erial **da**ta)
**SDI**: I2C data, scl auf dem pi auf pin5 (**s**erial **c**lock **l**ine)
**SD0** und **CS**: nur bei SPI benötigt


