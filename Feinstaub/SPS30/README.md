# SPS30
Supplier Doku: https://www.berrybase.de/media/pdf/89/50/21/produkt_downloads-Datenblatt_Datasheet.pdf

## Arduino-Stuff
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


