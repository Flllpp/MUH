# Konfiguration/Prokoll Feinstaubsensoren SM-UART-04L und SPS30

## SM-UART-04L (legacy)
Supplier Doku: https://www.mouser.com/pdfDocs/SM-UART-04LApplicationNote.pdf  
Nur per UART ansprechbar --> **wir nehmen den SPS30 weiter unten mit I2C**

### Pi-Stuff
- Raspbian geflashed
- ssh per usb
- ssh per wifi
- passwort geändert, authorized key geadded

feinstaubsensor läuft mit uart auf 3,3V. das passt mit dem pi, 5V wär gefährlich

- pi hat zwei uart-controller:
  - mini-uart ist an prozessorspeed gekoppelt
  - PL011 UART ist unabhängig, kümmert sich aber ums bluetooth
    - --> bluetooth ist uns egal, PL011 ist energiesparender und weniger nervenaufreibend
  - https://www.programmersought.com/article/93804026224/
 
- löten von pi und connector
- python script für serial read (serial_read.py)
  - wie decode ich den readout?
  - bits 5-16 sind interessant. rest wegwerfen und nach int konvertieren
    - zwei aufeinanderfolgende bytes ergeben je einen wert in µg/m³. wert1 * 256 + wert2
- ergebnis plotten :)
- was ist der unteschied zwischen werten 1-6 (standard smoke) und 7-12 (environment)?

## SPS30
Supplier Doku: https://www.berrybase.de/media/pdf/89/50/21/produkt_downloads-Datenblatt_Datasheet.pdf

### Arduino-Stuff
- Kommunikation via I2C
-- Hersteller rät, doch lieber UART zu verwenden oder bei gut abgeschirmten Kabeln bzw. Kabeln < 10cm zu bleiben

|Pin|Label|etc|
|---|---|---|
|Pin 1|VDD|5V|
|Pin 2|SDA / RX|Data / Receive|
|Pin 3|SCL / TX|Clock / Transmit|
|Pin 4|SEL|Wählt zwischen UART (floating) und I2C (auf ground)|
|Pin 5|GND|Ground|

- An SDA und SCL werden 10kOhm pullup-Widerstände empfohlen
- Sensor kann sehr viele Sachen!
-- Ist nach Start im idle-mode, Messmodus muss aktiviert werden, dann jede Sekunde ein Datenpunkt
--- Aufwärmzeit?
-- Setzbares Interval für automatische Lüfterreinigung, default sind 604800s (168h (1 Woche))
- Sensorion hat eine Arduino-Library gebastelt! https://github.com/Sensirion/arduino-sps

