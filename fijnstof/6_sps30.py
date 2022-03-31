from utime import sleep
from machine import UART, Pin
from lib.sps30 import SPS30

# Opstellen van de UART verbinding
tx_pin = Pin(4)
rx_pin = Pin(5)
verbinding = UART(id=1, baudrate=115200, tx=tx_pin, rx=rx_pin)
# Een variabele die ons helpt met de verbinding en ons extra functies geeft
sensor = SPS30(verbinding)

# Print het serienummer zodat we zeker weten dat alles werkt
print(sensor.serie_nummer())

# Probeer de code hieronder zelf te schrijven.
# Maak hierbij gebruik van de functies die de `sensor` variabele biedt.
# Typ `sensor.` om een lijst met mogelijkheden te zien.
# Zie je niks? Klik ctrl+spatie
#
# Laat de sensor *starten* met metingen doen

# Haal een *meting* op van de sensor en sla deze op in een variabele

# *Stop* met het maken van metingen

# Print het meetresultaat
