from machine import UART, Pin
# Gebruik ook de SPS30 functionaliteit
from sps30 import SPS30

tx_pin = Pin(4)
rx_pin = Pin(5)
verbinding = UART(1, baudrate=115200, tx=tx_pin, rx=rx_pin)

# Maak een object dat de SPS30 representeert
sensor = SPS30(verbinding)

# Vraag naar het serie nummer
print(sensor.serie_nummer())
