from machine import UART, Pin
# Gebruik ook de RAK3172 functionaliteit
from rak3172 import RAK3172

# We gebruiken de standaard UART0 pinnen en configuratie
# dat is pin 0 en 1 met een baudrate van 9600
verbinding = UART(id=0, baudrate=9600, tx=Pin(0), rx=Pin(1))
# Maak een object dat de RAK3172 module representeert
# dit object beheerd de communicatie naar de module en
# helpt om met handige functies zoals "verbind" en "zend"
lora = RAK3172(verbinding)

# Met de lora variabele aangemaakt is het nu tijd om te verbinden
# Kan je met behulp van de volgende functies:
# - verbinding maken
# - iets printen als het (niet)lukt
# - iets versturen als de verbinding gelukt is
#
# Functies:
# - lora.verbind(dev_eui, join_eui, app_key) # Deze functie geeft een succeswaarde terug: True of False
# - lora.zend(een_string) # bijvoorbeeld "Hallo LoRa!"
#
# Denk aan:
# - functie resultaten opslaan in variabelen
# - if conditie:
#       ...
#   else:
#       ...
