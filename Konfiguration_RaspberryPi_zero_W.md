#1.0 Die Pinleiste muss beim Pi W (nicht beim Pi WH) aufgelötet werden. (https://www.etechnophiles.com/raspberry-pi-zero-gpio-pinout-specifications-programming-language/)  

#2.0 Einrichtung einer headless Konfiguration des Pi's (Steuerung über einen anderen Rechner) auf Win10 mit aktivierter bash. orientiert sich an: https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows  <br />
#2.1 Über den "Raspberry Pi Imager" auf der microSD Karte "Raspberry Pi OS Lite" installieren. https://www.raspberrypi.org/software/operating-systems/  <br />
#2.2 Über den Editior im Laufwerk "boot" die Datei "ssh" (wichtig: ohne Dateiendung) und "wpa_supplicant.conf" erstellen.  <br />
#2.3 "wpa_supplicant.conf" editieren und den Wifi-Namen und das Passwort eintragen. <br />

```
  country=DE
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1

  network={
      ssid="NETWORK-NAME"
      psk="NETWORK-PASSWORD"
  }
```

#2.4 SD Karte im Pi verbauen und über den Router die IP des Pi's herausfinden.  <br />
#2.5 SSH Verbindung zum Pi aufnehmen: Das Standardpasswort für den Benutzer "pi" ist "raspberry" 

```
ssh pi@"IP"
```

#3.0 Passwort des Users pi ändern

```
passwd
```

#4.0 Pakete updaten

```
sudo apt-get update
sudo apt-get upgrade
```

#5.0 Installation eines Editors (hier neovim)

```
sudo apt-get install neovim
```

