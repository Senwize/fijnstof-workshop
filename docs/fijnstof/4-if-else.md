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
