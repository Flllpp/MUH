#include <SPI.h>
#include <SD.h>

File Log;
int cs_pin = 8; // CS am SD-Modul

void setup() {
  Serial.begin(9600);
  Serial.println("Arduino gestartet.");

  while(!SD.begin(cs_pin)){ // Warten falls keine SD-Karte im Slot
    Serial.println("Keine SD-Karte erkannt...");
    delay(1000);
  }
  Serial.println("SD-Karte initialisiert.");

  Log = SD.open("BME280.log", FILE_WRITE);

  Log.println("Erster Logbucheintrag!");
  Log.flush();
}

int i = 0;
void loop() {
  Serial.println(String(i) + " wird geschrieben.");
  Log.println(String(i));
  Log.flush();

  i++;
  delay(500);
}
