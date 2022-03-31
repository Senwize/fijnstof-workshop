# Als ... dan ... wat?

In de vorige opdracht hebben we gezien hoe we code kunnen herhalen, maar wat als we code willen overslaan of alleen uitvoeren in specifieke omstandigheden? Dan gebruiken we `#!python if`, `#!python else` en `#!python elif`. Dat bijna letterlijk vertaald naar `als ...`, `anders` en `anders als ...` (in plaats van `else if` gebruikt deze programmeer taal een afkorting: `#!python elif`)

## Conditionele code

Open het volgende workshop bestand in je ontwikkelomgeving: **3_if_else.py**

```py
x = 5

if x < 5:
    print("x is onder de 5")
elif x < 10:
    print("x is onder de 10")
else:
    print("x is niet onder de 10")
```

Net als de while-loop kan je een if-statement vrij goed vertalen naar het nederlands.  
Regel 3/4 vertaald zegt: `als x is lager dan 5, dan print "x is onder de 5"`.

Ook in de if-statement komen blokken code voor. Namelijk het blok aan code dat uitgevoerd moet woorden als de voorwaarde voldoet (x lager is dan 5). 

!!! question "Vraag A: Waarom elif?"
    Welk cruciaal verschil is er tussen de code uit je workshop bestand en de onderstaande code?  
    **Tip** Rechtsboven in elke code-venster staat een knop om de code te kopieren. Probeer de code eens uit te voeren en kijk naar het verschil.

    ```py title="Zonder elif"
    x = 5

    if x < 5:
        print("x is onder de 5")
    
    if x < 10:
        print("x is onder de 10")
    ```

## Herhaling

Voor nu is `x` nog altijd `5`, maar met behulp van een while-loop kunnen we getallen van 1 tot 10 krijgen. Voor je gemak staat hieronder het voorbeeld van de while-loop:

```py title="2_while_loop.py"
x = 1
while x < 10:
    print(x)
    x = x + 1
```

!!! question "Oefening B: 1 tot 10 met een if-statement"
    Nu je de code voor een while-loop hebt en de code voor een if-statement, kan je deze twee combineren zodanig dat de if statement meerdere keren wordt uitgevoerd?

    Pseudo code:
    ```py
    x is 1
    zolang x lager is dan 10
        als x lager is dan 5
            zeg "x is lager dan 5"
        anders
            zeg "x is hoger dan 5"
        x is x plus 1
    ```

## Tijd voor willekeurigheid

!!! danger "Als je snel bent"
    De volgende oefeningen zijn geadvanceerder en hoef je niet per-se te snappen voor het maken van de sensor. Mocht je de vorige oefeningen snel door zijn gelopen dan kan je deze oefening ook doen. Mocht je niet genoeg tijd hebben, ga dan door naar de volgende oefening.

Tot zo ver weten we elke keer al wat er geprint gaat worden, we zetten tenslotte zelf neer dat `x` gelijk aan `5` moet zijn. Dit kunnen we spannender maken door de microcontroller zelf een getal te laten verzinnen.

In tegenstelling tot de `print` functie die vaak gebruik wordt, hoeft de functie voor het genereren van een willekeurig getal niet altijd bij de hand te zijn en zijn er veel verschillende vormen voor willekeurigheid: 

- een heel getal tussen a en b
- een decimaal tussen 0 en 1 
- een willekeurige item uit een lijst met keuzes
- etc...

Vanwege de bovenstaande redenen valt deze functionaliteit onder de zogenaamde `random` module. We moeten de microcontroller laten weten dat we deze functionaliteit willen gaan gebruiken. Dat doen we door middel van een `import`-statement:

```py
import random
```

Nu kunnen we functies vanuit de `random` module aanspreken zoals:

```py
# Een willekeurig (random) heel getal (integer) tussen 0 en 10
random.randint(0, 10)
```

We kunnen ook alleen de `randint` functie importeren:

```py
from random import randint

randint(0, 10)
```

!!! info "Suggesties en autocompletion"
    De ontwikkelomgeving waarin je de code schrijft is "slim". Het weet vrijwel precies hoe de syntaxis in elkaar zit en welke functies je kan aanroepen. Dit is een mooi moment om dat uit te proberen.

    Importeer de random module, begin met het schrijven van `random.` en kijk hoe de suggesties verschijnen, nadat je de punt (.) typt. Zie je niks? Klik dan op CTRL+Spatie.

    <figure markdown="1">
    ![Editor giving suggestions](./media/autocomplete_2.png)
    <figcaption>De ontwikkelomgeving geeft suggesties</figcaption>
    </figure>

Om het af te maken hoef je nu niet meer `x` gelijk te zetten aan `5` maar kan je gebruik maken van willekeurige getallen.

!!! question "Oefening C: willekeurige getallen"
    Kan je x gelijk stellen aan een willekeurig getal tussen 0 en 10 en daaropvolgend een if-statement uitvoeren?  

!!! question "Oefening D: veel willekeurige getallen"
    Is de vorige oefening met de while-loop en if-statement gelukt? Kan je nu elke loop een willekeurige waarde gebruiken voor de if-statement? Let op dat je een ander variabel gebruik dan `x`, anders breekt je while-loop. (Snap je ook waarom?)