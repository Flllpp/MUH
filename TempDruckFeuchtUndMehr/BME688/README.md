# BME688 Druck-/Feuchtigkeits-/Temperatur-/Organics-/Boschqualitysensor

*"How is the air quality calculated?  
The air quality is calculated by using BSEC software from Bosch."*

Doku:
https://github.com/BoschSensortec/BME68x-Sensor-API  
https://pi3g.com/wp-content/uploads/2021/04/BME688-Breakout-Board-v1.1-datasheet-0.2.pdf  
https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme688-ds000.pdf
https://community.bosch-sensortec.com/t5/Knowledge-base/FAQs-BME688/ta-p/24822
https://www.bosch-sensortec.com/software-tools/software/BME688-software/

Die simplen Features sind über diverse Libraries abgreifbar, für die coole AI und IAQ braucht es eine closed source library von Bosch.. zur Einrichtung eine passende Windows-Software (BME-AI-Studio).  
Es kann dann supercoole Sachen, man muss es aber auf die Sache trainieren (Beispiel: Kaffeebohnen erschnüffeln)

## Für den Download der 2.0 Library von Bosch müssen Email, Name und Adresse hinterlegt sowie die [Lizenz](https://www.bosch-sensortec.com/media/boschsensortec/downloads/software/bme688_development_software/bosch-sensortec-clickthrough-license-bme688.pdf) akzeptiert werden...
### Kompilierte Software darf nur weitergegeben werden wenn auch ein Device mitgegeben wird. Da wir modular bauen wollenist dieser Sensor dann eigentlich raus für uns, oder?

- Gedacht für den Pi, geht aber sicher auch am Arduino
- **Logic level ist 3.3V!** Der MKR macht das aber ein Arduino Uno läuft auf 5V
