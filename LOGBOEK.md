# Logboek

Eén entry per sessie, nieuwste bovenaan. Claude Code stelt de entry op bij "afsluiten"; ik keur hem goed en commit zelf.

## Herhaallijst

Onderwerpen waar ik moeite mee heb. Claude Code vraagt er aan het begin van elke sessie twee van.

Spelregels, zodat het mechanisme ook echt werkt:

- **Maximaal zes onderwerpen.** Komt er een zevende bij, dan gaat het onderwerp met de langste reeks eraf, ook al is die nog geen twee.
- **Wie het langst niet gevraagd is, komt eerst.** Anders blijven dezelfde twee terugkomen.
- **De reeks staat erbij.** `reeks: 0` betekent: laatste keer niet goed of nog niet gevraagd. Bij `reeks: 2` gaat het onderwerp eraf. Zonder deze administratie kan Claude Code de regel de sessie erna niet uitvoeren.

Format: `- onderwerp · reeks: N · laatst gevraagd: JJJJ-MM-DD`

- Naamgeving in Python: snake_case en namen die zeggen wat erin zit · reeks: 0 · laatst gevraagd: -
- `if` tegenover `if/else`: gaten en overlappingen in voorwaarden · reeks: 0 · laatst gevraagd: -

## Format

```
### JJJJ-MM-DD · fase X, week Y
**Herhaald:** welke twee onderwerpen gevraagd zijn en of ze goed waren
**Gedaan:** wat ik gebouwd of gelezen heb
**Geleerd:** in mijn eigen woorden, één of twee zinnen
**Vastgelopen op:** waar het schuurde en hoe ik het oploste, of dat het nog open staat
**Open vragen:** wat ik nog wil uitzoeken
**AI-gebruik:** waarvoor ik Claude gebruikte (uitleg, review, overhoren, code)
**Volgende stap:** waar de volgende sessie begint
```

Bij een beslismoment uit `LEERPLAN.md` (na fase 3 en na fase 5) komt er één regel bij:

```
**Beslissing:** solliciteren of doorleren, en waarom
```

## Entries

### 2026-10-09 · fase 0, week 1
**Herhaald:** niets, de herhaallijst was nog leeg
**Gedaan:** Leerplan geauditeerd en op twaalf punten herzien: fase 0 naar 8 weken, fase 3 naar 11 weken met het uitgavenproject centraal, kerstpauzes en uitloopbeleid, blind labelen in fase 2, rangnummer in de transactiesleutel in fase 5, budgetwaarschuwing vóór de eerste Azure-resource. Werkomgeving ingericht: Git-repository, GitHub, uv-project, ipykernel. Python-basis uitgewerkt in `oefeningen/01_basis.py`: lijsten, dictionaries, `type()`, `for`, `if/else`. README en `.gitignore` toegevoegd. Vijf weekvragen alle vijf goed.
**Geleerd:** Git werkt met drie plekken: mijn werkmap, een wachtruimte en de geschiedenis, en committen blijft volledig op mijn eigen schijf tot ik push. En het verschil tussen een lijst en een dictionary zit niet in de volgorde, maar in waarmee je een element ophaalt: een positie of een sleutel.
**Vastgelopen op:** GitHub weigerde wachtwoordauthenticatie, opgelost met `gh auth setup-git`. VS Code kon de venv niet als kernel gebruiken omdat `ipykernel` niet in het project stond, opgelost met `uv add --dev ipykernel`. Bij opdracht 8 eerst een gat (`> 30` en `< 30`), toen een overlap (`>= 50` en `<= 50`), voordat `if/else` erin kwam.
**Open vragen:** het verschil tussen print en return bij functies
**AI-gebruik:** audit van het leerplan, concepten uitgelegd, overhoord, mijn code gereviewd. Claude schreef de README, de `.gitignore`, het werkblad en de wijzigingen in `LEERPLAN.md` en `CLAUDE.md`. Alle Python-code schreef ik zelf.
**Volgende stap:** week 2, functies met argumenten en returnwaarden
