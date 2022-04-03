# Tijd om echt te meten

Nu we het serienummer van de fijnstofsensor hebben kunnen uitlezen weten we dat de verbinding werkt. In dit hoofdstuk gaan we dan eindelijk meetresultaten krijgen, maar voor een allerlaatste keer vatten we nog een en ander samen wat je tot nu toe geleerd hebt.

## Wat je tot nu toe weet

In alle afgelopen hoofdstukken hebben we veel naar theorie en code gekeken. Als het goed is heb je nu een goed idee hoe bepaalde functionaliteiten van de microcontroller, code en sensor werkt. Hieronder staan de belangrijke punten nog eens samengevat:

- je kan de microcontroller tekst en waardes terug laten sturen naar de computer (`#!python print(..)`);
- je kan stukken code laten herhalen (`#!python while <voorwaarde>:`);
- je kan stukken code alleen uitvoeren als een bepaalde voorwaarde voldoet (`#!python if <voorwaarde>:` en `#!python else:`);
- je hebt een idee wat objecten zijn en dat deze objecten eigenschappen en functies hebben (`#!python led = Pin(...)` en `#!python led.on()`)
- je begrijpt dat de microcontroller naar de sensor communiceert via UART en hoe je deze verbinding opstelt;
- en misschien de belangrijkste twee: 
    - je kan gebruik maken van de ontwikkelomgeving om suggesties en aanvullingen te krijgen;
    - je kan gebruik maken van de ontwikkelomgeving om een omschrijving van een functie / object te zien.

In de komende delen van de workshop kan je deze kennis zelf gaan toepassen bij het starten en uitlezen van de sensor, bij het verbinden van de radio module en het verzend van informatie.

## Code schrijven en fijnstof meten

De SPS30 fijnstof sensor maakt gebruikt van een kleine ventilator en een laser. Voordat we een meting kunnen uitlezen moeten we de sensor laten starten met meten, het duurt ongeveer 2 seconden na het starten van de sensor voordat de eerste meetresultaten beschikbaar zijn.

Maak gebruik van het volgende diagram en het workshop bestand genaamd: **6_sps30.py** om een meting uit te gaan lezen. Gebruik de comments in de code als hints om zelf de code de schrijven waarmee je de sensor aanstuurt.

<figure markdown="1">
![Process diagram on starting and reading a measurement from the particulate matter sensor](./media/sps30_flow.png){width=700}
<figcaption>Process weergave van het uitlezen van de fijnstof sensor</figcaption>
</figure>

!!! question "Oefening A: Maken van een meting"
    Schrijf code om een meetresultaat te krijgen met behulp van het bovenstaande diagram, de suggesties en aanvulling van je ontwikkelomgeving en de comments in de code.

!!! question "Oefening B: Continu meten"
    Mocht je het nog niet gedaan hebben in de vorige oefening: Kan je je code aanpassen zodat er elke 2 seconde een meting word verricht? Denk aan het laten knipperen van het LED lampje via een while-loop

!!! question "Oefening C: Oneindig herhalen?"
    Kan je zorgen dat de while-loop nooit stopt? Hiervoor moet de voorwaarde altijd voldoen.