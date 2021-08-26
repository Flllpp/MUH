#include <sps30.h>

String stamp(){
  return String(millis() / 1000.0F) + ": ";
}

void setup() {
  int16_t ret; //return values, genutzt um fehler abzufangen

  Serial.begin(9600);
  delay(2000);

  sensirion_i2c_init(); //initialisierung

  while (sps30_probe() != 0) {
    Serial.println(stamp() +"SPS sensor nicht gefunden..");
    delay(1000);
  }
  Serial.println(stamp() +"SPS sensor gefunden!");

}

void loop() {
  int16_t ret; //return values, genutzt um fehler abzufangen
  struct sps30_measurement sps_out; //entält unsere Messdaten

  //Messung starten, 30 s messen, 30 s Standby
  ret = sps30_start_measurement();
  if (ret < 0) {
    Serial.println(stamp() +"Error beim Start der Messung");
  }
  Serial.println(stamp() +"Messung gestartet");

  for (int i=0; i!=30; i++) {
    // es kann abgefragt werden ob neue Daten bereit sind (1 Messung/s)
    // wir messen aber nicht so oft und skippen das deswegen
    ret = sps30_read_measurement(&sps_out);
    if (ret < 0) {
      Serial.println(stamp() +"Error beim auslesen der Messwerte");
    }
    Serial.println("---" + stamp());
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
  sps30_stop_measurement();
  delay(30000);
}
