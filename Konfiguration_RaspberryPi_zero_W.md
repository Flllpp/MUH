
Anleitung Konfiguration Raspberry Pi zero W


#1.0 Die Pinleiste muss beim Pi W im Unterschied zum Pi WH noch aufgelötet werden.

#2.0 Anleitung für headless Konfiguration des Pi's auf Win10 (setzt bash voraus) (https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows)
#2.1 Über den "Raspberry Pi Imager" auf der microSD Karte "Raspberry Pi OS Lite" installieren. https://www.raspberrypi.org/software/operating-systems/
#2.2 Über den Editior im Laufwerk "boot" die Datei "ssh" (wichtig: ohne Dateiendung) und "wpa_supplicant.conf" erstellen.
#2.3 "wpa_supplicant.conf" editieren und für country DE setzen außerdem den Wifi-Namen und das Passwort eintragen. 

  country=US
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1

  network={
      ssid="NETWORK-NAME"
      psk="NETWORK-PASSWORD"
  }
#2.4 SD Karte im Pi verbauen und über den Router die IP des Pi's herausfinden
#2.5 SSH Verbindung zum Pi aufnehmen Passwort für den Benutzer "pi" ist "raspberry" 

ssh pi@"IP"

#2.6 Passwort ändern

passwd

#2.6 Pakete updaten

sudo apt-get update
sudo apt-get upgrade

-Ende-
