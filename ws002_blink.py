from machine import Pin
from utime import sleep

# Gebruik pin nummer 25 en zet het als een output
led = Pin(25, Pin.OUT)

# While True, blijft oneindig herhalen
# Dit heet een "loop", maar niet alle loops zijn oneindig!
while True:
  led.on()   # Zet de LED aan
  sleep(1)   # Wacht een seconde
  led.off()  # Zet de LED uit
  sleep(1)   # Wacht een seconde
