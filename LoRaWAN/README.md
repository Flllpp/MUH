# Verbindung zum Things Network

[The Things Network](www.thethingsnetwork.org)

## Test
- EUI rausfinden: `MKRWAN`-library installieren, Beispiel `FirstConfiguration` ausführen, OTAA auswählen
- Auf TheThingsNetwork ein neues Gerät anlegen
- `AppEUI` erstmal egal (fill with zeros)
- bei `DevEUI` die herausgefundene einfügen
- `AppKey` generieren und dem Skript auf dem MKR mitteilen
- --> Gerät versucht zu verbinden und gibt passende Rückmeldung!

## Payload  
*Payload should be as small as possible. This means that you should not send JSON or plain (ASCII) text, but instead encode your data as binary data. This is made really easy with the Cayenne Low Power Payload format which is fully supported by The Things Network.*
- [https://www.thethingsnetwork.org/docs/devices/arduino/api/cayennelpp/](Cayennelpp)
  - Problem: sieht gewisse sensordaten vor und encodiert passend. es sind nicht alle unsere sensoren unterstützt und man müsste deswegen basteln was declaration angeht (`addGenercSensor` ist von TTN auch nicht unterstützt)
  - Wenn wir immer alles auf einmal schicken ists wahrscheinlich sinnvoll anders zu encodieren

Unser Payload:

|Sensor|		Anspruch|Datentyp|Bytes|
|---|---|---|---|
|Licht|			+wert ohne komma		|int	|2|
|Temperatur|		+-wert mit komma		|float	|4|
|Luftdruck|		+wert mit komma			|float	|4|
|Rel. Luftfeuchte|	+wert mit komma			|float	|4|
|CO2|			+-wert mit komma		|float	|4|
|Feinstaub|		bis zu 10 +werte mit komma	|10 floats	|40|
|Ozon|			+wert mit komma			|float  |4|
|Sound|			+wert mit komma?		|float  |4|
|insgesamt||							|66|

- angemessene Paketgröße ist abhängig von Verbindungsqualität
- LoRaWAN-Protokoll fügt 13 bytes hinzu
  - die meißten libraries supporten nur 51 bytes für alle übertragungsraten (51+13=64)
- es sieht so aus als müssten wir mehrere Pakete schicken oder weniger werte übertragen
  - 4 floats sparen wäre genug
