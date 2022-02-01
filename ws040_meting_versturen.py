# Gebruik deze imports en functies
from machine import Pin, UART
from utime import sleep
from rak3172 import RAK3172
from sps30 import SPS30

# De laatste opdracht: alles samenvoegen met elkaar.
# Dus:
#  - UART verbindingen maken voor de sensor en de lora module
#  - Een sensor (SPS30) object maken
#  - Een lora (RAK3172) object maken
#  - Lora verbinding maken
#  - De sensor metingen starten
#  - Elke ~8 seconden:
#       - een sensor meting doen
#       - een bericht met meetresultaat versturen
#
# Gebruik de vorige stappen - en eventueel de `antwoorden` folder -
# als referentie materiaal om deze code te schrijven.
