# Herhalen van code

In de vorige opdracht zagen we dat code van boven naar beneden uitgevoerd word. Echter, als iets meer dan één keer uitgevoerd moet worden is het niet handig om steeds die code te kopieren. Daarom kunnen we gebruik maken van "while-loops". 

## De While-Loop

Een while-loop (of while-statement) is een manier om een stuk code te laten herhalen zolang er aan een bepaalde voorwaarde wordt voldaan.

Open het bestand `2_while_loop.py` in je ontwikkelomgeving:

```py title="2_while_loop.py"
x = 1
while x < 10:
    print(x)
    x = x + 1
```

??? note "Variabelen gebruiken (net als bij wiskunde)"
    We kunnen variabelen gebruiken om waarden bij te houden en veranderen. Bijvoorbeeld een getal op te laten tellen, of een stuk tekst bijhouden.

    ```py
    leeftijd = 22
    print(leeftijd) # dit print "22"
    leeftijd = 30
    print(leeftijd) # nu print het "30"
    ```

!!! info "Comments"
    Omdat deze pagina ook toelichting geeft op de code, zijn de comments weggelaten. In jouw code zullen ze wel aanwezig zijn.

Een while-loop begint altijd met het woord `#!python while` gevolgd door een voorwaarde of vergelijking, zoals `#!python x < 10` en wordt afgesloten met een dubbele punt `:`. Het afsluiten op een dubbele punt geeft aan dat de volgende - ingresprongen - regels bij de while-loop horen. Het is in wijze een "blok" aan code dat bijn elkaar hoort.

Omdat inspringen een belangrijk aspect is in deze programmeer taal, is je ontwikkelomgeving ingesteld om een kleur te geven aan elk ingesprongen niveau:

<figure markdown="1">
![Indentation coloring in the editor](./media/indentations.png)
<figcaption>Elk ingesprongen niveau krijgt een eigen kleur</figcaption>
</figure>

## Uitvoeren van de code

Met het tweede workshop bestand (2_while_loop.py) geopend, klik op de Run knop in de groene balk en observeer wat de microcontroller terugstuurt naar de computer.

??? example "Uitkomst"
    De microcontroller zal reageren met:
    
    ``` title="Reactie van microcontroller" linenums="0"
    1
    2
    3
    4
    5
    6
    7
    8
    9
    ```

!!! question "Vraag A"
    Waarom eindigt het getal bij 9 en niet 10?

!!! question "Vraag B"
    Hoe kan je de code zo aanpassen dat je de onderstaande reactie krijg:
    
    ``` title="Uitkomst van aangepaste code" linenums="0"
    2
    4
    6
    8
    10
    12
    14
    16
    18
    ```

??? warning "Antwoorden zien?"
    Als je er echt niet aan uit komt of je er dreigt tijd te kort, dan kan je de map **antwoorden** openen en kijken naar het antwoord van de stap waar je nu op zit.

    ??? info "Antwoorden!?!?"
        Of bekijk alle antwoorden, het is tenslotte geen toets :)