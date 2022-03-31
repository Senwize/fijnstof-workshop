# We importeren de `sleep(...)` functie zodat we de microcontroller
# even niks kunnen laten doen
from utime import sleep
from machine import Pin

led = Pin(25, Pin.OUT)
led.on()

# Om oneindig te herhalen kan je een conditie gebruiken
# die altijd waar is zoals: `1 is 1` of `1 < 2`
# maar je kan ook gelijk de constante `True` gebruiken
while True:
    led.on()
    sleep(1)
    led.off()
    # Vergeet hier niet ook te slapen,
    # anders is `led.on()` (lijn 13) gelijk na led.off()
    # en dan lijkt het alsof er niks gebeurt
    sleep(1)
