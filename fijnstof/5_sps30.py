# Om `UART` te gebruiken moeten we dit ook importeren
# dit doen we hetzelfde als de import van `Pin`
from machine import UART, Pin
# Dit doen we ook met de SPS30 sensor
from lib.sps30 import SPS30

# Hier maken we twee variabelen aan die beide een
# van de UART pinnen representeren:
# - De zendpin    (TX)
# - De ontvangpin (RX)
tx_pin = Pin(4)
rx_pin = Pin(5)

# Net als dat een variabele een pin en zijn functies kan representeren,
# kan een variabele ook de UART verbinding representeren
# De de parameters hebben hier namen (id, baudrate, tx, rx)
# dus specificeren we welke parameter welke waarde heeft.
# Zo heeft parameter `id` waarde 1 en parameter `baudrate` waarde 115200
verbinding = UART(id=1, baudrate=115200, tx=tx_pin, rx=rx_pin)

# Nu kunnen we via de UART verbinding data sturen naar de sensor en data
# ontvangen.
# In plaats van deze verbinding zelf te beheren, gebruiken
# we een object dat - net als Pin en UART - functies biedt.
sensor = SPS30(verbinding)

# Nu kunnen we op een makkelijke manier vragen naar bijvoorbeeld het
# serienummer.
# Deze slaan we eerst op in een variabele en daarna printen we het.
serienummer = sensor.serie_nummer()
print(serienummer)

# Klopt het serienummer met wat er op je sensor staat?
# Het serienummer staat onder de QR-Code op de sensor.
