#include <SD.h>
#include <Adafruit_BME280.h>
#include <Wire.h>  // I2C
  
Adafruit_BME280 bme;

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

  Wire.begin();

  unsigned status;  // kopiert aus adafruit-beispiel
  status = bme.begin();
  if (!status) {
      Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
      Serial.print("SensorID was: 0x"); Serial.println(bme.sensorID(),16);
      Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
      Serial.print("   ID of 0x56-0x58 represents a BMP 280,\n");
      Serial.print("        ID of 0x60 represents a BME 280.\n");
      Serial.print("        ID of 0x61 represents a BME 680.\n");
      while (1) delay(10);
  }  

  Log = SD.open("BME280.log", FILE_WRITE);

//  Log.println("Erster Logbucheintrag!");
//  Log.flush();
}


void loop() {
  float Tempe = bme.readTemperature();
  float Press = bme.readPressure() / 100.0F; // Pa to bar
  float Humid = bme.readHumidity();
  
  Serial.print("[" + String(millis() / 1000.0F) + "]");
  Serial.print(" BME280: ");
  Serial.print(String(Tempe) + " °C, ");
  Serial.print(String(Press) + " mbar, ");
  Serial.println(String(Humid) + "%");

  Log.print(String(millis() / 1000.0F) + ";");
  Log.print(String(Tempe) + ";");
  Log.print(String(Press) + ";");
  Log.println(String(Humid));
  Log.flush();
  
  delay(500);
}
