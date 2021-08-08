# Konfiguration/Prokoll Feinstaubsensor SM-UART-04L

- Raspbian geflashed
- ssh per usb
- ssh per wifi
- passwort geändert, authorized key geadded

feinstaubsensor läuft mit uart auf 3,3V. das passt mit dem pi, 5V wär gefährlich

- pi hat zwei uart-controller:
  - mini-uart ist an prozessorspeed gekoppelt
  - PL011 UART ist unabhängig, kümmert sich aber ums bluetooth
    - --> bluetooth ist uns egal, PL011 ist energiesparender und weniger nervenaufreibend

nun: 
- [x] löten von pi und connector
- [ ] einrichten von uart via rasp-config (wie wechsel von mini?)

