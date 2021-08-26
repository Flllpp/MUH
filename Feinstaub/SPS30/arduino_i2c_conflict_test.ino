#include <sps30.h>
#include <Adafruit_BME280.h>
#include <Wire.h>

Adafruit_BME280 bme;

#define cs_pin 7; // CS am SD-Modul

String stamp(){
  return String(millis() / 1000.0F) + ": ";
}

void setup() {
  int16_t ret; //return values, genutzt um fehler abzufangen

  Serial.begin(9600);
  delay(2000);

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

  sensirion_i2c_init(); //initialisierung

  while (sps30_probe() != 0) {
    Serial.println(stamp() +"SPS sensor nicht gefunden..");
    delay(1000);
  }
  Serial.println(stamp() +"SPS sensor gefunden!");

  ret = sps30_start_measurement();
  if (ret < 0) {
    Serial.println(stamp() +"Error beim Start der Messung");
  }
  Serial.println(stamp() +"Messung gestartet");
}

void loop() {
  int16_t ret; //return values, genutzt um fehler abzufangen
  struct sps30_measurement sps_out; //entält unsere Messdaten

  float Tempe = bme.readTemperature();
  float Press = bme.readPressure() / 100.0F; // Pa to bar
  float Humid = bme.readHumidity();
  
  Serial.println("---" + stamp() + "BME280");
  Serial.println("Temperature: " + String(Tempe) + " °C, ");
  Serial.println("Pressure:    " + String(Press) + " mbar, ");
  Serial.println("Humidity:    " + String(Humid) + "%");

  // es kann abgefragt werden ob neue Daten bereit sind (1 Messung/s)
  // wir messen aber nicht so oft und skippen das deswegen
  ret = sps30_read_measurement(&sps_out);
  if (ret < 0) {
    Serial.println(stamp() +"Error beim auslesen der Messwerte");
  }
  Serial.println("---" + stamp() + "SPS30");
  Serial.print("PM  1.0: ");
  Serial.println(sps_out.mc_1p0);
  Serial.print("PM  2.5: ");
  Serial.println(sps_out.mc_2p5);
  Serial.print("PM  4.0: ");
  Serial.println(sps_out.mc_4p0);
  Serial.print("PM 10.0: ");
  Serial.println(sps_out.mc_10p0);
  Serial.print("NC  0.5: ");
  Serial.println(sps_out.nc_0p5);
  Serial.print("NC  1.0: ");
  Serial.println(sps_out.nc_1p0);
  Serial.print("NC  2.5: ");
  Serial.println(sps_out.nc_2p5);
  Serial.print("NC  4.0: ");
  Serial.println(sps_out.nc_4p0);
  Serial.print("NC 10.0: ");
  Serial.println(sps_out.nc_10p0);

  Serial.print("Typical particle size: ");
  Serial.println(sps_out.typical_particle_size);
  delay(1000);
}
