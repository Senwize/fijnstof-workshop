from machine import UART, Pin
from lib.rak3172 import RAK3172

verbinding = UART(id=0, baudrate=9600, tx=Pin(0), rx=Pin(1))
lora = RAK3172(verbinding)

# Verbinden kan enkele seconden duren, daarom printen we eerst dat we
# gaan verbinden. Zo weten we dat de code niet is vastgelopen, maar bezig is
print("Verbinding maken")
# Roep de verbind functie aan op de lora variabele.
# De parameters van de verbind functie zijn te zien door met je muis over de naam
# van de functie te houden en even te wachten. (dev_eui, join_eui, app_key)
succes = lora.verbind("70B3D57ED0049AAB", "0000000000000000", "1D7A8E7408DF809B5E86FB2C342759DC")

# De succes variabele is een 'boolean', dit is True of False.
# in plaats van kijken of het mislukt is, kan je ook eerst kijken of het gelukt is:
#
# if succes:
#   print("Gelukt!")
# else:
#   print("mislukt!")

if not succes:
    print("Verbinding niet gelukt!")
else:
    print("Verbinding gelukt!")
    # Verbinding gelukt, dus we gaan wat tekst verzenden
    lora.zend("Hallo wereld!")
