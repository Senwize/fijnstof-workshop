# Functies die niet standaard zijn zoals print moeten worden geimporteerd
from machine import Pin

# Een variabele is net als in wiskunde een letter of naam dat een waarde
# heeft.
# Een waarde in een variabele kan ook een object zijn met extra functies.
#
# De waardes tussen de haakjes van een functie zijn parameters / instellingen.
led = Pin(25, Pin.OUT)

# Een functie kan ook een waarde teruggeven
is_led_aan = led.value()  # 1 als LED aan is, 0 als LED uit is

# We kunnen code uitvoeren, mits een conditie waar is met "if" en "else"
if is_led_aan is 1:
    print("LED is aan")
else:
    print("LED is uit")

# We voeren code herhaaldelijk uit met een while-loop
x = 0
while x < 10:
    print(x)
    x = x + 1
