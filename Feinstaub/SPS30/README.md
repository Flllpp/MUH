# SPS30
Supplier Doku: https://www.berrybase.de/media/pdf/89/50/21/produkt_downloads-Datenblatt_Datasheet.pdf

## Arduino-Stuff
- Kommunikation via I2C
  - Hersteller rät, doch lieber UART zu verwenden oder bei gut abgeschirmten Kabeln bzw. Kabeln < 10cm zu bleiben

|Pin|Label|etc|
|---|---|---|
|Pin 1|VDD|5V|
|Pin 2|SDA / RX|Data / Receive|
|Pin 3|SCL / TX|Clock / Transmit|
|Pin 4|SEL|Wählt zwischen UART (floating) und I2C (auf ground)|
|Pin 5|GND|Ground|

- An SDA und SCL werden 10kOhm pullup-Widerstände empfohlen
- Sensor kann sehr viele Sachen!
  - Ist nach Start im idle-mode, Messmodus muss aktiviert werden, dann jede Sekunde ein Datenpunkt
    - Aufwärmzeit? **<8 s** laut Hersteller. Stelle aber auch nach 2 Minuten starke Schwankungen fest. Wir sollten lang aufwärmen lassen und über mehrere Messwerte mitteln
  - Setzbares Interval für automatische Lüfterreinigung, default sind 604800s (168h (1 Woche))
    - Counter wird beim Idlen genullt. Sollten wir ihn nicht dauerhaft anlassen müssen wir cleaning cycle einbauen! `sps30_start_manual_fan_cleaning()`
- Sensorion hat eine Arduino-Library gebastelt! https://github.com/Sensirion/arduino-sps
- **Library bringt eigene Version von Wire.h mit**, kann das mit anderer I2C-Hardware vielleicht doch zu Problemen führen?
  - Test mit BME280 zeigt: es geht trotzdem ^-^ siehe `arduino_i2c_conflict_test.ino`
- Test-example aus der sps-Library läuft schonmal einwandfrei, ist aber auf Dauermessung ausgelegt
- Daten werden nach Start des Sensors in ein sps30_measurement struct geworfen und können von dort einfach ausgegeben werden, beinhaltet 10 floats
  - `mc_1p0`, `mc_2p5`, `mc_4p0`, `mc_10p0` für µg/m³
  - `nc_0p5`, `nc_1p0`, `nc_2p5`, `nc_4p0`, `nc_10p0` für n/m³
  - `typical_particle_size` selbsterklärend
  - Kategorien sind jeweils "kleiner als x µm", größere cutoffs beinhalten also immer die kleineren

