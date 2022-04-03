# Je eigen code schrijven

## Het 'Hallo Wereld' voorbeeld

De code die je in de vorige opdracht uitvoerde zag er als volgt uit:

```py title="1_print.py"
--8<-- "fijnstof/1_print.py"
```

Tijdens deze workshop zal je erachter komen dat veel uitleg over de code al aanwezig is in het bestand in de vorm van zogenaamde "comments" (opmerkingen). In de bovenstaande code is regel 1 t/m 4 een comment omdat het begint met een `#`.

Regel 5 is de enige code die uitgevoerd wordt in dit bestand.  
De functie `#!python print` wordt uitgevoerd `#!python print()` en voorzien van een parameter `#!python print("Hallo wereld!")`. 

Zoals de comment in de code zegt: de functie print stuurt tekst of een waarde terug naar de computer. In dit geval geven wij het stuk tekst `#!python "Hallo wereld!"` mee.

!!! note
    Wist je dat een letterlijk stuk tekst zoals hieronder een `string` wordt genoemd? Zo worden hele getallen `integers` genoemd en getallen met decimalen een `float`.

Een letterlijk stuk tekst zoals `#!python "Hallo wereld!"` moet tussen aanhalingstekens staan, hierdoor begrijp de microcontroller dat het een stuk tekst is en niet - bijvoorbeeld - een functie.

## Uitdagingen

Hieronder staan een aantal uitdagingen en vragen waarmee jij aan de slag kan om bekend te raken met het schrijven van code.

??? note "Vergeten hoe je code uitvoert?"
    Code kan uitgevoerd worden door op de knop "Run" te klikken in de groene balk. Staat er "Pico disconnected"? Klik dan eerst daarop om opnieuw verbinding te maken met de microcontroller.
    <figure markdown="1">
    ![Run button](./media/run.png){ width=700 }
    </figure>

!!! question "Vraag A: Meerdere keren printen"
    Kan je meerdere keren dezelfde tekst laten versturen? In welke volgorde wordt je code uitgevoerd?

!!! question "Vraag B: Andere waarden printen"
    Wat gebeurd er als je in plaats van tekst een getal als parameter meegeeft?

!!! question "Vraag C: Optellen"
    Het printen van waarden is een ontzettend handige manier om te weten wat je code aan het doen is. Probeer eens een rekensom mee te geven als parameter zoals: `#!python 5 * 25`. Welke andere wiskundige tekens kan je gebruiken?

!!! question "Vraag D: Optellen van strings?"
    Dat getallen op te tellen zijn is logisch... Maar kan dat ook met twee stukken tekst?
