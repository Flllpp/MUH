#include <BH1750.h>

BH1750 lightsensor = BH1750();

void setup() {
  Serial.begin(9600);
  lightsensor.begin();
}

void loop() {
  Serial.println(lightsensor.getLightIntensity());
  delay(25);
}
