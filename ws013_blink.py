# We importeren een "slaap" functie, hiermee
# kunnen we een bepaalde tijd wachten.
# `sleep(..)` is een functie die een parameter heeft
# voor hoelang er gewacht moet worden in seconden
from utime import sleep
# Voordat we gebruik kunnne maken van de pinnen,
# moeten we deze functionaliteit "importeren"
# van buitenaf. Dit doen we met de "import" statement.
from machine import Pin

# De Pin 'functie' maakt een object aan en slaat dit op
# in de variabele.
# Dit object representeert een fysieke pin. Hieraan
# zitten ook functies vergelijkbaar met de functionaliteiten
# van de pin, zoals de functie `on()` (stroom erop) en `off()` (stroom eraf).
led = Pin(25, Pin.OUT)

# Zet stroom op led (Pin 25)
led.on()

# Kan je met wat je in de stappen tot nu toe gezien heb
# het LED lampje laten knipperen? (aan/uit/aan/uit)
