#!/usr/bin/python3
import sys

import adafruit_dht
import board

# choose one or the other
dht = adafruit_dht.DHT22(board.D24)
# dht = adafruit_dht.DHT11(board.D24)

for i in range(1,10):
    try:
        t = dht.temperature
        h = dht.humidity
        if t and h:
            print('{0:0.1f} {1:0.1f}'.format(t, h))
            break
    except:
        pass
if not t or not h:
    print('Failed to get reading. Try again!')
    sys.exit(1)
