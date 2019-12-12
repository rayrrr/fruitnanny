#!/usr/bin/python
import sys

import adafruit_dht
import board

# choose one or the other
# dht_device = adafruit_dht.DHT22(board.D24)
dht_device = adafruit_dht.DHT11(board.D24)

humidity = dht_device.humidity
temperature = dht_device.temperature
if humidity is not None and temperature is not None:
    print('{0:0.1f} {1:0.1f}'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

