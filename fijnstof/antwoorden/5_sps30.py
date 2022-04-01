from utime import sleep
from machine import UART, Pin
from lib.sps30 import SPS30

tx_pin = Pin(4)
rx_pin = Pin(5)
verbinding = UART(id=1, baudrate=115200, tx=tx_pin, rx=rx_pin)
sensor = SPS30(verbinding)

# Begin met metingen verrichten
sensor.start()

# Het opstarten duurt een aantal seconden
sleep(2)

# Lees een meting uit
resultaat = sensor.meting()

# Stop met metingen uitvoeren, we hebben nu een meting opgeslagen
sensor.stop()

# Print de meting
print(resultaat)
