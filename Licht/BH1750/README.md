# Konfiguration BH1750 Lichtsensor mit Raspberry Pi

- Die Pinleiste muss zunächst aufgelötet werden.
- Kabel entsprechend des Schemas verbinden:
  - Pi 3V to sensor VCC
  - Pi GND to sensor GND
  - Pi SCL to sensor SCL
  - Pi SDA to sensor SDA  

mit dem Pi über ssh verbinden dann:  

python 3 installieren
  - `sudo apt-get install python3-pip`
- smd installieren
  - `python3 -m pip install smbus`
- I2C aktivieren (https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/)
  - `sudo raspi-config`
  - Im Menü: Interfacing Options -> I2C -> Yes 
  - `sudo reboot now`


- Transfer des python scripts auf den Pi
  - das python script BH1750_simple.py auf den PC downloaden
  - in der bash des lokalen PCs in den Ordner navigieren in dem das Skript liegt und das skript transferieren 
  - `scp ./BH1750_simple.py pi@IPADRESSE:/home/pi/`  


- Wieder mit dem Pi verbinden und das Skript ausführen
  - `python3 BH1750_simple.py 0 #Option1`
  - `python3 BH1750_simple.py 1 #Option2`
- Detaillierte Anleitung zum Sensor (auch mit Arduinoanleitung)  
  - https://learn.adafruit.com/adafruit-bh1750-ambient-light-sensor/overview

# Konfiguration BH1750 Lichtsensor mit Arduino

Anleitung: https://learn.adafruit.com/adafruit-bh1750-ambient-light-sensor/arduino

- Libraries: `hp_BH1750` ist von Adafruit vorgeschlagen
  - Man könnte sich auch mal `OneTime-BH1750` [anschauen](https://github.com/JVKran/OneTime-BH1750), die soll sehr lightweight sein und wenig strom verbrauchen
    - Die funktioniert super! Nice!
