# Konfiguration MH-Z19B ====
https://www.raspberrypi.org/documentation/configuration/uart.md
1. ```raspi-config``` starten
2. ```Interface Options``` auswählen
3. ```Serial Port``` auswählen
4. Bei "Would you like a login shell to be accessible over serial?" mit "No" antworten
5. Seriellen Port aktivieren mit "Would you like the serial port hardware to be enabled?" -> 2Yes"
Achtung: Im Test funktionierte z.T. hiernach der Login über USB OTP zunächst nicht mehr.
