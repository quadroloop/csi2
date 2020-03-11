# csi2
An Electronic Sensor Interfacing platform built with python and NodeJS on Raspberry Pi 

> csi2 is tested with Raspberry Pi Moodel B+, and supports 9 sensors in 
total.

[![prototype](https://quadroloop.github.io/bobaux/rodrigo.jpg)](https://github.com/quadroloop/csi2)

> A picture of the Raspberry Pi 3 will all 9 sensors, connected on a 
protyping board.
### Installation: 
```sh
git clone https://github.com/quadroloop/csi2
cd csi2
sudo python csi2.py
sudo python fastSense.py
```
you need to modify the scripts first at the nad modify the request links 
to your server or which ever destination, or method it needs to call.

### Sensors:

| Name | Function |
| ---- | ---- |
| DHT22 | Temperature and Humidity |
| HC-SR04 | Humidity Sensor |
| Sound Module | Sound |
| Raindrop Sensor | Water |
| LDR Light Sensor | Light |
| Hall effect | Magnetic Fields |
| Capacitive Touch Sensor | Touch |
| Flame Sensor | Flame | 
| MQ4 | Methane Gas Sensor |

### Dashboard:

> this project is connected to a Dashboard Web Application built on 
NodeJS, link to the that project can be found below.

 https://github.com/quadroloop/morphDash 


