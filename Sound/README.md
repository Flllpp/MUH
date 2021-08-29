Konfiguration von DFROBOT SEN0232 Analog Sould Level Meter

Anleitung unter: https://wiki.dfrobot.com/Gravity__Analog_Sound_Level_Meter_SKU_SEN0232

USB-Treiber für Arduino Nano CDM v2.12.36.4 WHQL Certified.zip von https://ftdichip.com/drivers/vcp-drivers/

Wichtig in Arduino 1.8.15 den alten Boatloader einstellen

im Skript der Anleitung muss die Baud-Rate auf 9600 angepasst werden  Serial.begin(115200) mit  Serial.begin(9600) ersetzen
