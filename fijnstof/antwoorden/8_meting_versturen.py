from usys import exit
from utime import sleep, ticks_ms
from machine import UART, Pin
from lib.rak3172 import RAK3172
from lib.sps30 import SPS30

# Maak de software UART verbinding voor de lora module en de sensor
lora_uart = UART(id=0, tx=Pin(0), rx=Pin(1), baudrate=9600)
sensor_uart = UART(id=1, tx=Pin(4), rx=Pin(5), baudrate=115200)

# Maak de lora en sensor objecten
lora = RAK3172(lora_uart)
sensor = SPS30(sensor_uart)

# Print het serienummer van de sensor om de werking v/d verbinding te bevestiging
print("Serie nummer: " + sensor.serie_nummer())

# Begin met het maken van een lora verbinding
print("Verbinding maken")
succes = lora.verbind("70B3D57ED0049AAB", "0000000000000000", "1D7A8E7408DF809B5E86FB2C342759DC")
if not succes:
    print("Niet verbonden...")
    exit()  # Stop met alles
print("Verbonden!")

# Begin met het maken van metingen
sensor.start()
# De sensor de tijd geven om te starten
sleep(2)

# Oneindig herhalen
while True:
    # Lees een meting uit
    meting = sensor.meting()
    # Verstuur de meting via LoRa
    lora.zend(meting)
    # Wacht 10 seconden
    sleep(10)
