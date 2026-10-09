# Leerplan moderne datastack

Van beginnend programmeur naar iemand die ML-modellen en RAG-toepassingen bouwt en in productie brengt, met daarna de data engineering eronder. Start 5 oktober 2026, 8 uur per week (ongeveer 5 bouwen, 2 lezen, 1 documenteren), met een bufferweek na elke fase.

Vink af wat klaar is en commit de wijziging, dan staat je voortgang in de Git-geschiedenis. De werkafspraak over AI-gebruik staat in `CLAUDE.md`.

## Overzicht

| Fase | Onderwerp | Weken | Weeknummers | Periode |
|---|---|---|---|---|
| 0 | Fundament | 8 | 1 t/m 8 | 5 okt 2026 t/m 29 nov 2026 |
| 1 | Polars en Parquet | 6 | 9 t/m 14 | 7 dec 2026 t/m 31 jan 2027 |
| 2 | Statistiek en ML-basis | 8 | 15 t/m 22 | 8 feb 2027 t/m 4 apr 2027 |
| 3 | ML in productie | 11 | 23 t/m 33 | 12 apr 2027 t/m 27 jun 2027 |
| 4 | RAG: WKR/BTW-assistent | 8 | 34 t/m 41 | 5 jul 2027 t/m 29 aug 2027 |
| 5 | Pipeline en datamodel | 5 | 42 t/m 46 | 6 sep 2027 t/m 10 okt 2027 |
| 6 | Tabelformaat en catalogus | 3 | 47 t/m 49 | 18 okt 2027 t/m 7 nov 2027 |
| 7 | Cloud, Airflow en DP-700 | 9 | 50 t/m 58 | 15 nov 2027 t/m 30 jan 2028 |
| 8 | Schaal voelen | 2 | 59 t/m 60 | 7 feb 2028 t/m 20 feb 2028 |

Na elke fase volgt een bufferweek. Twee kerstpauzes van twee weken zitten al in de periodes verwerkt: 21 dec 2026 t/m 3 jan 2027 en 20 dec 2027 t/m 2 jan 2028.

### Uitloopbeleid

De weekplannen noemen alleen weeknummers, geen datums. Dat is bewust: loop je uit, dan hoef je niet zestig regels bij te werken.

- De bufferweek na elke fase is rust, geen reserve. Gebruik je hem voor uitloop, dan heb je die fase geen rust gehad. Dat mag, maar weet dat je het doet.
- Loopt een fase meer dan één week uit, werk dan alleen de periodekolom in de tabel hierboven bij. De weeknummers blijven staan.
- Schrap liever een opdracht dan dat je een fase afraffelt. De eindcriteria zijn de ondergrens, de opdrachtenlijst is het ideaal.

## Werkafspraken

- **Eén project dat groeit.** De uitgavendata loopt door fase 1, 2, 3, 5, 6 en 7.
- **Lezen volgt bouwen.** Lees het hoofdstuk dat past bij waar je vastloopt. De boekenlijst is naslag, geen leeslijst: bij 2 leesuren per week haal je nooit alles, en dat hoeft ook niet.
- **Klaar is meetbaar.** Pas door naar de volgende fase als het eindcriterium gehaald is.
- **Alles in Git, met een README-sectie per fase.** Wat je bouwde, welke keuzes, waarom.
- **AI eerst als docent, daarna als assistent.** Zie `CLAUDE.md`.
- **SQL blijft in beeld.** In fase 1 en 2 staat bij elke week welke analyse je ook in DuckDB-SQL doet. In fase 3 en 4 vervalt die wekelijkse afspraak, omdat die fasen al vol zitten; je SQL-verdieping komt in fase 5.
- **Geen echte bankdata in een openbare repository.** `data/` staat in `.gitignore`.
- **Geen echte bankdata in de cloud zonder bewuste keuze.** Vanaf fase 4 gaat data naar Azure, en vanaf fase 7 naar OneLake. Beslis vóór fase 4 of je daar een geanonimiseerde set voor gebruikt of je echte data, en schrijf de afweging in je README. De gitignore-regel dekt dit niet.
- **Kostenbewaking vóór de eerste cloudresource.** Budgetwaarschuwing instellen is de eerste stap van de eerste Azure-week, niet een latere.
- **Beslismoment solliciteren.** Na fase 3 en na fase 5 staat een expliciete keuze: solliciteren en het plan vertragen, of doorleren. Maak die keuze hardop, anders maak je hem stilzwijgend.

## Deel A: Polars en machine learning

Fase 0 tot en met 4. Van Python-basis tot modellen en een RAG-toepassing die in productie draaien.

### Fase 0 · Fundament

8 weken, weken 1 t/m 8. Alles hierna leunt op vlot Python, dus deze fase is ruim genomen. Polars wordt je hoofdgereedschap voor data. SQL leer je op basisniveau, omdat vacatures en later dbt erom vragen. Debuggen en opgeruimde code zijn hier eigen onderwerpen, geen bijproduct.

**Opdrachten**

- [x] Werkomgeving: VS Code, Python met uv, Git en een GitHub-account
- [ ] Tien kleine scripts die bestanden inlezen, bewerken en wegschrijven
- [ ] Foutmeldingen zelfstandig lezen en oplossen, met debugger en logging
- [ ] `ruff` als formatter en linter, draaiend op al je scripts
- [ ] Polars-oefenreeks: filteren, groeperen, joinen en windowberekeningen met `over()`
- [ ] Korte SQL-reeks in DuckDB: SELECT, WHERE, JOIN, GROUP BY

**Leren**

- Python: datatypes, functies, modules, foutafhandeling, virtuele omgevingen
- Een traceback lezen: van onder naar boven, welke regel en welk type
- Polars: DataFrames, expressies, `group_by`, `join`, `over()`
- SQL-basis: dezelfde bewerkingen in SQL kunnen lezen en schrijven
- Git: commit, branch, pull request; werken op de command line

**Bronnen**

- Officiële Python-tutorial (docs.python.org)
- Polars user guide, de delen "Getting started" en "Expressions"
- *Pro Git*, gratis online
- DuckDB-documentatie, SQL-introductie
- uv-documentatie over projecten en lockfiles; ruff-documentatie

**Weekplan**

- [x] **Week 1: Werkomgeving en Python-basis.** Installeer VS Code, uv en Git; zet automatische codesuggesties in je editor uit. Maak een GitHub-account en je eerste repository. Zet het project op met `uv init` en begrijp wat `.venv` en `uv.lock` doen. Leer variabelen, datatypes, lijsten, dictionaries, `if` en `for`. *Resultaat:* Repository met een eerste script en README.
- [ ] **Week 2: Functies, modules en bestanden.** Functies met argumenten en returnwaarden, eigen modules importeren, `pathlib` en de `csv`-module. Scripts 1 tot 3: regels tellen, rijen filteren, totalen per categorie. *Resultaat:* Drie scripts, elk met een eigen commit.
- [ ] **Week 3: Foutmeldingen en debuggen.** Lees tracebacks: welke regel, welk type, van onder naar boven. Print-debugging, de debugger in VS Code met breakpoints, en `logging` in plaats van `print`. Daarna `try/except` en bewust kiezen welke fouten je opvangt. Scripts 4 en 5: datums omzetten, CSV's samenvoegen. *Resultaat:* Vijf scripts; je kunt een onbekende foutmelding zelf terugbrengen tot de regel die hem veroorzaakt.
- [ ] **Week 4: Opgeruimde code en Git-werkwijze.** `ruff` toevoegen als formatter en linter, één keer over al je scripts, en begrijpen waarom hij klaagt. Werk voor het eerst met een branch en een pull request. *Resultaat:* Alle scripts ruff-schoon; eerste pull request samengevoegd.
- [ ] **Week 5: Scripts 6 tot 10.** Dubbele regels verwijderen, JSON naar CSV, foute regels loggen, bestanden hernoemen op datum, een script met opties via `argparse`. *Resultaat:* Tien scripts.
- [ ] **Week 6: Polars-basis.** `read_csv`, `select`, `filter`, `with_columns`, `group_by`, `sort`. Herschrijf script 3 en 5 in Polars en vergelijk de code met je pure-Python-versie. *Resultaat:* Twee scripts in Polars.
- [ ] **Week 7: Polars: joins en windowberekeningen.** `join`, datumkolommen, `over()`. Bereken een lopend saldo per maand en het aandeel van elke categorie in het maandtotaal. *Resultaat:* Lopend saldo per maand in Polars.
- [ ] **Week 8: SQL-basis en eindopdracht.** SELECT, WHERE, JOIN en GROUP BY in DuckDB op dezelfde data. Eindopdracht: CSV inlezen met Polars, bewerken, wegschrijven, en dezelfde aggregatie in SQL. *Resultaat:* Eindcriterium fase 0 gehaald.

**Klaar als:** je zonder voorbeeldcode met Polars een CSV inleest, bewerkt en opslaat, zelf een lopend saldo per maand berekent met `over()`, in SQL een JOIN met GROUP BY schrijft, en een onbekende foutmelding kunt terugbrengen tot de regel die hem veroorzaakt.

### Fase 1 · Polars en Parquet

6 weken, weken 9 t/m 14. Start van het uitgavenproject. Je zet ruwe exports om naar schone, getypeerde Parquet-data. Dat is de invoer voor je eerste ML-model in fase 2.

**Opdrachten**

- [ ] `ingest.py`: bankexports omzetten naar Parquet
- [ ] `clean.py`: datums, bedragen en omschrijvingen correct omzetten
- [ ] `categorize.py` met een regeltabel in `rules/categorieen.csv`
- [ ] Meting CSV tegenover Parquet, en één analyse ook in DuckDB-SQL
- [ ] Tests met pytest en één commando dat alles draait

**Leren**

- Kolomopslag, compressie en row groups
- Lazy queries en pushdown: alleen lezen wat nodig is
- Datatypes en null-waarden goed behandelen
- Gevorderde expressies: `when/then`, tekst, lijsten
- Arrow als gedeeld geheugenformaat tussen Polars en DuckDB
- Code testen

**Bronnen**

- *Python Polars: The Definitive Guide* (Janssens, Nieuwdorp)
- Polars user guide
- pytest-documentatie

**Weekplan**

- [ ] **Week 9: Van export naar Parquet.** Schrijf `ingest.py`: bankexport inlezen, schema vastleggen, wegschrijven met `write_parquet`. Probeer compressie `snappy` en `zstd` en bekijk de metadata met `pyarrow.parquet`. *SQL:* dezelfde rijtelling in DuckDB op de Parquet. *Resultaat:* Ruwe data als Parquet in `data/raw`.
- [ ] **Week 10: Lazy analyses en meten.** Analyses met `scan_parquet` en `.explain()`. Meet grootte en leestijd van CSV tegenover Parquet. Blaas je data op met *variatie*, niet met kopieën: genereer nieuwe rijen met willekeurige bedragen, datums en omschrijvingen. Honderd keer dezelfde rijen plakken meet alleen hoe goed Parquet duplicaten inpakt met dictionary- en run-length-encoding, en geeft een spectaculaire maar misleidende uitkomst. *SQL:* dezelfde aggregatie in DuckDB, en vergelijk de tijd. *Resultaat:* Meetresultaten in de README, met een regel over hoe je de data hebt opgeblazen.
- [ ] **Week 11: Datatypes en opschonen.** Schema afdwingen bij inlezen. Nederlandse exports gebruiken vaak een komma als decimaalteken en dd-mm-jjjj als datum; zet beide correct om. Bepaal per kolom wat een ontbrekende waarde betekent. *SQL:* tel per kolom de null-waarden in DuckDB. *Resultaat:* `clean.py` met getypeerde, schone kolommen.
- [ ] **Week 12: Omschrijvingen en regels.** Omschrijvingen normaliseren met tekstfuncties. Categoriseren via een regeltabel (zoekterm naar categorie), zodat je regels toevoegt zonder te programmeren. *SQL:* totalen per categorie met GROUP BY. *Resultaat:* `categorize.py` plus regeltabel.
- [ ] **Week 13: Lazy en Arrow.** Maak het script lazy en lees het queryplan. Geef het resultaat zonder kopie door aan DuckDB en doe één analyse in SQL. Meet geheugengebruik eager tegenover lazy. *Resultaat:* Lazy pipeline; notitie over het verschil.
- [ ] **Week 14: Testen en afronden.** `pytest`-tests voor je opschoonfuncties met lastige invoer. Eén commando dat ingest, opschonen en categoriseren draait. Test het op een nieuwe maand. *SQL:* je maandoverzicht als één SQL-query. *Resultaat:* Eindcriterium fase 1.

**Klaar als:** één commando een nieuwe maandexport zonder aanpassingen omzet naar een schone Parquet-tabel, je tests slagen en je meting in de README staat, inclusief hoe je de data hebt opgeblazen.

### Fase 2 · Statistiek en ML-basis

8 weken, weken 15 t/m 22. Eerst de statistiek waarmee je een model eerlijk beoordeelt, daarna je eerste echte model: transacties automatisch categoriseren. Je regels uit fase 1 zijn de lat die het model moet halen, maar alleen als je labels onafhankelijk van die regels tot stand komen.

**Opdrachten**

- [ ] Verkennende analyse van je eigen data met Polars en grafieken
- [ ] ISLP-labs over regressie, classificatie en resampling
- [ ] Handmatig gelabelde steekproef, gezet zonder naar je regels te kijken
- [ ] Baselinescore van je regels, gemeten tegen die steekproef
- [ ] Classificatiemodel op omschrijving en bedrag, geëvalueerd op de nieuwste maanden
- [ ] Model in je pipeline, met regels als vangnet
- [ ] SQL bijhouden: elke week één analyse ook in DuckDB-SQL

**Leren**

- Verdelingen, spreiding, steekproeven
- Lineaire en logistische regressie
- Train/test-split, cross-validation, bias en variantie
- Metrics bij scheve klassen: precision, recall, F1
- Data leakage herkennen en voorkomen, ook in je labels
- Onzekerheid: wanneer is een verschil tussen twee scores te klein om iets te betekenen
- Boommodellen en gradient boosting

**Bronnen**

- *An Introduction to Statistical Learning, with Python*, gratis online
- *Hands-On Machine Learning* (Géron), nieuwste editie
- scikit-learn user guide

**Weekplan**

- [ ] **Week 15: Statistiek en verkennen.** Gemiddelde, mediaan, spreiding, verdelingen. Verken je eigen uitgavendata met Polars en een paar grafieken. Lees ISLP hoofdstuk 1 en 2. *SQL:* dezelfde verkenning met GROUP BY en percentielen in DuckDB. *Resultaat:* Notebook met verkenning en bevindingen.
- [ ] **Week 16: Regressie.** Lineaire regressie: coëfficiënten interpreteren, residuen bekijken. ISLP hoofdstuk 3 met de lab-opdrachten. *SQL:* maandtotalen per categorie als basistabel voor je analyse. *Resultaat:* Lab afgerond; eigen samenvatting.
- [ ] **Week 17: Classificatie.** Logistische regressie, kansen, drempels, confusion matrix. ISLP hoofdstuk 4. *SQL:* tel je categorieën en hun aandeel; zie hoe scheef de verdeling is. *Resultaat:* Lab afgerond.
- [ ] **Week 18: Resampling en overfitting.** Train/test-split, cross-validation, bias en variantie. ISLP hoofdstuk 5. *SQL:* splits je data op datum in SQL en vergelijk de categorieverdeling per periode. *Resultaat:* Eigen uitleg van overfitting in de README.
- [ ] **Week 19: Blind labelen.** Trek een steekproef transacties en label die met de hand, *zonder* je regeltabel of de uitvoer van `categorize.py` erbij. Label eerst, kijk daarna. Zet vast hoe groot je steekproef is en hoeveel transacties per categorie erin zitten; bij minder dan ongeveer 20 per categorie kun je over die categorie later niets zeggen. Noteer waar je zelf twijfelde: dat is de bovengrens van wat een model kan halen. *SQL:* trek je steekproef met een reproduceerbare query. *Resultaat:* Gelabelde steekproef plus een notitie over je eigen twijfelgevallen.
- [ ] **Week 20: Baseline en eerste model.** Nu pas: meet hoe goed je regels scoren op die blinde steekproef. Dat is je baseline, en die is eerlijk omdat de labels de regels niet kennen. Bouw daarna je eerste model: TF-IDF op de omschrijving plus het bedrag, logistische regressie in een scikit-learn-pipeline, cross-validation. *SQL:* welke categorieën missen je regels het vaakst. *Resultaat:* Eerlijke baselinescore en een eerste model met score.
- [ ] **Week 21: Eerlijk evalueren.** Precision en recall per categorie; zeldzame categorieën. Split op tijd: train op oudere maanden, test op de nieuwste. Kijk hoe groot je testset is en hoeveel het verschil met de baseline mag schelen voordat het iets betekent. Probeer LightGBM. ISLP hoofdstuk 8. *SQL:* bouw je evaluatietabel per categorie in SQL. *Resultaat:* Evaluatierapport tegenover de baseline, met een uitspraak over onzekerheid.
- [ ] **Week 22: Integreren.** Het model voorspelt de categorie in je pipeline; regels blijven als vangnet of overrule. Model opslaan en laden met versienummer. *SQL:* vergelijk voorspelde en regelcategorie in één query. *Resultaat:* Eindcriterium fase 2.

**Klaar als:** je op een testset van de nieuwste maanden met cijfers onderbouwt of je model beter is dan je regels, *of* onderbouwt waarom je testset te klein is om daar iets over te zeggen, met de berekening erbij en wat je zou meten als je meer data had. Winnen de regels, dan is dat een geldige uitkomst. "Geen verschil aantoonbaar" is dat ook.

> Let op: de meestgemaakte fout in deze fase is je labels afleiden van je regels. Doe je dat, dan scoort je regelsysteem per definitie bijna perfect en meet je alleen of het model je regels kan imiteren. Daarom labelt week 19 blind en meet week 20 pas daarna.

> Koppel dit aan je Mastership: gebruik de statistiek- en ML-vakken als theorie en dit project als toepassing.

### Fase 3 · ML in productie

11 weken, weken 23 t/m 33. Je uitgavenproject wordt een keten die zichzelf draait: data, features, model en voorspellingen als assets in Dagster, experimenten in MLflow. Dit is het deel dat de meeste ML-portfolio's missen, en het is de zwaarste fase van het plan: MLflow, Dagster, Docker en driftbewaking zijn alle vier nieuw. Daarom elf weken in plaats van negen, en één project in plaats van twee.

**Opdrachten**

- [ ] Reproduceerbare featuretabel in Parquet, los van je notebooks
- [ ] Experimenten en beste model in MLflow
- [ ] Dagster-assets: ruwe data, features, model, voorspellingen, met maandpartities
- [ ] Scoringspipeline en Dagster in containers met docker compose
- [ ] Asset checks en driftcontrole
- [ ] Model card en README die jouw bijdrage afbakent
- [ ] Optioneel: NHS PROMs als tweede dataset voor subgroepevaluatie

**Leren**

- Experimenten en modellen bijhouden
- Kalibratie en prestaties per subgroep
- Orchestratie met assets, afhankelijkheden en partities
- Containers: images, Dockerfile, docker compose, vaste versies
- Datakwaliteit bewaken met checks
- Drift en wanneer je hertraint
- Een model documenteren voor anderen

**Bronnen**

- *Designing Machine Learning Systems* (Huyen)
- MLflow-documentatie
- Dagster-documentatie en de gratis cursussen van Dagster University
- Docker-documentatie, de gids Get started

**Weekplan**

- [ ] **Week 23: Featuretabel en projectkeuze.** Haal je featurebouw uit je notebooks en zet hem in een script dat je twee keer kunt draaien met hetzelfde resultaat. Featuretabel als Parquet. Besluit nu of je NHS PROMs als tweede dataset meeneemt: controleer of je de data mag hergebruiken en leg vast welk deel van het groepswerk van jou is. Kan dat niet, dan draait deze hele fase op je uitgavendata en verlies je niets aan leerstof. *Resultaat:* Reproduceerbare featuretabel.
- [ ] **Week 24: MLflow-basis.** MLflow lokaal: runs, parameters en metrics loggen bij je model uit fase 2. *Resultaat:* Experimenthistorie die je kunt doorzoeken.
- [ ] **Week 25: MLflow verdiepen.** Meerdere modellen naast elkaar, runs vergelijken, het beste model registreren en weer inladen uit de registry. *Resultaat:* Geregistreerd model dat je pipeline ophaalt op versienummer.
- [ ] **Week 26: Evaluatie verdiepen.** Kalibratie, feature importance, en prestaties per subgroep: per rekening, per maand, per bedragklasse. Heb je NHS-data, dan per procedure en leeftijdsgroep. *Resultaat:* Evaluatie per subgroep.
- [ ] **Week 27: Dagster-basis.** Zet de keten om naar assets: ruwe data, features, model, voorspellingen. Start met `dagster dev` en bekijk de lineage. *Resultaat:* Keten zichtbaar in de Dagster-interface.
- [ ] **Week 28: Partities.** Een partitie per maand, zodat je één maand opnieuw kunt draaien zonder de rest aan te raken. Doe een backfill over een half jaar. *Resultaat:* Maanden los opnieuw te draaien.
- [ ] **Week 29: Scoren en tonen.** Voorspellingen als asset per periode. Een eenvoudige Streamlit- of Power BI-weergave erop. *Resultaat:* Voorspellingen zichtbaar voor een gebruiker.
- [ ] **Week 30: Docker.** Images, containers, Dockerfile en volumes. Verpak je scoringspipeline in een image met vastgezette versies via de lockfile van uv. *Resultaat:* Image die je pipeline draait.
- [ ] **Week 31: docker compose.** Dagster en je keten samen met docker compose. Test op een andere machine, of in een schone map zonder je `.venv`. *Resultaat:* Keten draait in containers, ook op een andere machine.
- [ ] **Week 32: Bewaken.** Asset checks op datakwaliteit. Vergelijk de invoerverdeling tussen periodes en leg een drempel vast om te hertrainen. *Resultaat:* Checks en driftcontrole in de keten; een check die faalt op bewust verpeste data.
- [ ] **Week 33: Afronden.** Model card: wat voorspelt het, hoe goed, voor wie minder goed, waar niet voor gebruiken. Lees Designing ML Systems over deployment en monitoring. *Resultaat:* Eindcriterium fase 3.

**Klaar als:** één run in Dagster de hele keten van data tot voorspellingen draait, in containers op elke machine, met checks die falen bij slechte data, en je model card af is.

**Mijlpaal:** Portfolio voor een junior data scientist- of ML-rol, met aantoonbare productievaardigheden.

> **Beslismoment.** Je portfolio is hier sterk genoeg om op te solliciteren. Kies expliciet: solliciteren en het plan vertragen, of doorleren tot en met fase 4. Schrijf je keuze en je reden in `LOGBOEK.md`, zodat je later weet waarom.

### Fase 4 · RAG: WKR/BTW-assistent

8 weken, weken 34 t/m 41. Vragen beantwoorden op openbare Belastingdienst-documenten. Het grootste deel is data: parsen, opknippen, indexeren, actueel houden. Met je financiële achtergrond kun je zelf beoordelen of een antwoord klopt.

Dit is de eerste fase die geld kost. Zet je budgetwaarschuwing in Azure op scherp vóór je de eerste resource aanmaakt, en beslis vooraf welke data je naar een cloudmodel stuurt.

**Opdrachten**

- [ ] Minimale versie: 20 documenten, LanceDB, een API-model, zonder framework
- [ ] Evaluatieset van 30 tot 50 vragen met bekend antwoord en bronpassage
- [ ] Hybride zoeken en een reranker, effect gemeten
- [ ] Jaartal als metadata, incrementeel laden als Dagster-asset
- [ ] Cloudversie als container op Azure Container Apps, met Azure OpenAI en logging van kosten
- [ ] Optioneel: self-hosted model op dezelfde evaluatieset

**Leren**

- Embeddings en vectorzoeken
- Chunking van PDF's met tabellen en voetnoten
- Hybride zoeken en reranking
- Evaluatie: juiste passage gevonden, antwoord trouw aan de bron
- Het systeem laten zeggen dat iets niet in de bronnen staat
- Kosten en responstijd afwegen
- Een container deployen en geheimen veilig beheren

**Bronnen**

- *AI Engineering* (Huyen), vooral de hoofdstukken over evaluatie
- *Hands-On Large Language Models* (Alammar, Grootendorst)
- Documentatie van LanceDB en Azure OpenAI

**Weekplan**

- [ ] **Week 34: Corpus en parsing.** Verzamel 20 openbare Belastingdienst-documenten over WKR en btw, zoals het Handboek Loonheffingen. Parse ze, knip ze in stukken en leg jaar, bron en onderwerp vast als metadata. Begin met de kleinste documenten; het Handboek Loonheffingen is honderden pagina's en tabellen daarin parsen kost meer tijd dan je denkt. Twintig documenten halen is het doel, niet twintig perfecte documenten. *Resultaat:* Opgeknipt corpus met metadata.
- [ ] **Week 35: Minimale RAG.** Embeddings in LanceDB, top-k ophalen, prompt met de stukken, antwoord met bronvermelding. Zonder framework. *Resultaat:* Werkende vraag-antwoordloop.
- [ ] **Week 36: Evaluatieset.** 30 tot 50 vragen met bekend antwoord en bronpassage. Meet hoe vaak de juiste passage in de top-k zit en beoordeel de antwoorden; controleer een steekproef zelf. *Resultaat:* Nulmeting.
- [ ] **Week 37: Retrieval verbeteren.** Hybride zoeken (full-text plus vector), een reranker, verschillende chunkgroottes. Meet elk effect apart. *Resultaat:* Verbeteringen met cijfers onderbouwd.
- [ ] **Week 38: Actualiteit en weigeren.** Filter op jaar; laad alleen gewijzigde documenten opnieuw, als asset in Dagster. Test met vragen buiten het corpus of het systeem zegt dat het antwoord ontbreekt. *Resultaat:* Geen verouderde percentages meer.
- [ ] **Week 39: Interface en container.** Streamlit-interface. Verpak de app in een Docker-image en test hem lokaal. *Resultaat:* App draait lokaal in een container.
- [ ] **Week 40: Naar Azure.** Begin met de kostenkant: resource group, budget en een waarschuwing per e-mail bij een bedrag dat jij kiest. Pas daarna Azure OpenAI-deployment in je eigen subscription, image naar Azure Container Registry, app op Azure Container Apps, geheimen buiten je code, logging van vragen, tokens en kosten. Zet aan het eind van de week stil wat je niet nodig hebt. Optioneel: een self-hosted model op dezelfde evaluatieset. *Resultaat:* Demo online die je kunt laten zien, met een budgetwaarschuwing die eerder bestond dan de resources.
- [ ] **Week 41: Afronden.** README met architectuur, resultaten per iteratie en kosten per vraag. Lees in AI Engineering de hoofdstukken over evaluatie. *Resultaat:* Eindcriterium fase 4.

**Klaar als:** je met je evaluatieset laat zien dat elke verbetering meetbaar helpt, het systeem geen verouderde percentages geeft, en je kosten per vraag kent.

**Mijlpaal:** Geëvalueerde AI-toepassing: aansluiting op AI engineering en je eigen RAG-chatbotidee.

## Deel B: data engineering

Fase 5 tot en met 8. Datamodel, tabelformaten, cloud en orchestratie. Eerder oppakken kan als een baan of klant erom vraagt; fase 5 bouwt alleen op fase 0 en 1.

### Fase 5 · Pipeline en datamodel

5 weken, weken 42 t/m 46. Begin van het data engineering-deel. Van werkende pipeline naar een betrouwbaar datamodel dat anderen kunnen gebruiken. Hier verdiep je ook je SQL.

**Opdrachten**

- [ ] Lagen `raw`, `clean` en `mart`, gepartitioneerd en idempotent
- [ ] Stermodel: feittabel transacties, dimensies datum, categorie en rekening
- [ ] dbt-project met dbt-duckdb en datakwaliteitstests
- [ ] dbt-modellen als assets in Dagster

**Leren**

- Medaillonarchitectuur: brons, zilver, goud
- Idempotentie en herlaadbaarheid
- Het verschil tussen een dubbele rij en twee identieke gebeurtenissen
- Dimensioneel modelleren: feiten, dimensies, granulariteit
- SQL-verdieping: CTE's en windowfuncties
- Data testen in dbt

**Bronnen**

- *The Data Warehouse Toolkit* (Kimball)
- *Fundamentals of Data Engineering* (Reis, Housley)
- dbt-documentatie

**Weekplan**

- [ ] **Week 42: Lagen en idempotent laden.** Mappen `raw`, `clean` en `mart`, gepartitioneerd op jaar en maand. Overschrijf per maand de hele partitie en ontdubbel op een transactiesleutel. Let op bij die sleutel: een hash van alleen datum, bedrag, omschrijving en tegenrekening gooit echte transacties weg, want twee keer dezelfde koffie op dezelfde dag is geen dubbele boeking. Neem het regelnummer uit de export mee, of een rangnummer binnen de groep gelijke rijen. Test dat allebei: twee keer laden geeft identieke data, én twee identieke transacties op één dag blijven twee rijen. *Resultaat:* Test op idempotentie en test op echte duplicaten, beide groen.
- [ ] **Week 43: Datamodel ontwerpen.** Lees de eerste hoofdstukken van Kimball. Bepaal de granulariteit (één rij per transactie) en schets de feittabel en de dimensies. *Resultaat:* Modelschets in de README.
- [ ] **Week 44: dbt opzetten.** dbt-duckdb installeren, sources op de clean-Parquet, staging-modellen. SQL met CTE's. *Resultaat:* Werkend dbt-project met staging.
- [ ] **Week 45: Marts en tests.** Feit- en dimensiemodellen; lopend saldo met een windowfunctie in SQL. Tests `unique`, `not_null`, `accepted_values` en `relationships`. *Resultaat:* Mart-laag met geslaagde tests.
- [ ] **Week 46: dbt in Dagster.** Laad je dbt-modellen als assets in Dagster, zodat data, marts en ML-modellen in één lineage staan. *Resultaat:* Eindcriterium fase 5.

**Klaar als:** twee keer dezelfde maand laden identieke tabellen oplevert, twee identieke transacties op één dag toch twee rijen blijven, alle dbt-tests slagen en de hele keten in één Dagster-lineage staat.

**Mijlpaal:** Je portfolio dekt nu ook een analytics engineer-rol.

> **Beslismoment.** Tweede expliciete keuze: solliciteren op een analytics engineer- of data engineer-rol, of doorleren tot en met fase 7 met de certificering erbij. Schrijf je keuze in `LOGBOEK.md`.

### Fase 6 · Tabelformaat en catalogus

3 weken, weken 47 t/m 49. Databasefuncties op gewone bestanden. Je bouwt dezelfde tabel drie keer, zodat je de verschillen zelf ziet.

**Opdrachten**

- [ ] Mart-tabel in DuckLake: UPDATE, kolom toevoegen, eerdere versie opvragen
- [ ] Dezelfde tabel in Iceberg via PyIceberg met een SQLite-catalogus
- [ ] Dezelfde tabel in Delta via `deltalake`, plus een vergelijkende README

**Leren**

- Transacties (ACID) op bestanden
- Snapshots en time travel
- Schema-evolutie
- Wat een catalogus doet
- Metadata in bestanden (Iceberg, Delta) tegenover in een database (DuckLake)

**Bronnen**

- *Designing Data-Intensive Applications*, 2e editie (Kleppmann, Riccomini)
- Documentatie van DuckLake, PyIceberg en delta-rs

**Weekplan**

- [ ] **Week 47: DuckLake.** Maak een DuckLake-catalogus, laad je mart-tabel, corrigeer een categorie met UPDATE, voeg een kolom toe en vraag een eerdere versie op. Kijk na elke stap welke bestanden erbij komen. *Resultaat:* Notities: wat er op schijf gebeurde.
- [ ] **Week 48: Iceberg.** PyIceberg met een SQLite-catalogus. Tabel maken vanuit Arrow, toevoegen, overschrijven, schema aanpassen, snapshots bekijken. *Resultaat:* Dezelfde tabel in Iceberg.
- [ ] **Week 49: Delta en vergelijken.** `deltalake`: schrijven, `merge`, `history`, time travel; lees de tabel in Polars. Vergelijkingstabel van de drie formaten. *Resultaat:* Eindcriterium fase 6.

**Klaar als:** je voor alle drie formaten uitlegt wat er op schijf gebeurt bij een UPDATE.

> Delta krijgt bewust een plek: Fabric en Databricks gebruiken het als standaard, dus dit sluit aan op fase 7 en op DP-700.

### Fase 7 · Cloud, Airflow en DP-700

9 weken, weken 50 t/m 58. Alles naar de omgeving waar de meeste Nederlandse werkgevers op draaien. Je eigen Azure-subscription en je Data Factory-oefenproject zijn het vertrekpunt. Airflow leer je hier, via de ingebouwde Airflow-optie van Fabric.

De kerstpauze valt midden in deze fase, en dat bepaalt de indeling. De Fabric-proefcapaciteit duurt voor zover bekend 60 dagen en loopt door tijdens een pauze. Daarom staat alles wat geen Fabric-capaciteit nodig heeft vóór de pauze: Azure, Spark lokaal en de DP-700-stof. De capaciteit zet je pas aan in de eerste week ná de pauze, en dan heb je ruim genoeg dagen over, ook voor fase 8. Controleer de actuele voorwaarden; een kleine betaalde capaciteit die je tussen sessies pauzeert is het alternatief.

**Opdrachten**

- [ ] Fabric-lakehouse met Delta-tabellen in OneLake
- [ ] PySpark-notebook en een maandelijkse Fabric-pipeline
- [ ] Airflow-DAG die pipeline en scoring aanstuurt
- [ ] Categorisatiemodel in Fabric met MLflow; Power BI-rapport
- [ ] GitHub Actions voor tests en kostenbewaking
- [ ] DP-700-examen gehaald

**Leren**

- Cloudopslag, identiteit en rechten (Entra ID, RBAC)
- Spark: DataFrames, partities, lazy uitvoering
- Orchestratie met taken (Airflow) tegenover assets (Dagster)
- Monitoring, foutafhandeling en kosten
- DP-700-stof, inclusief real-time

**Bronnen**

- Microsoft Learn-leerpad voor DP-700 en het praktijkassessment
- Microsoft Learn over Apache Airflow Job in Fabric
- Airflow-documentatie

**Weekplan, deel 1: vóór de kerstpauze, zonder Fabric-capaciteit**

- [ ] **Week 50: Azure-basis.** Resource group, storage account met ADLS Gen2, rollen in Entra ID. Controleer de budgetwaarschuwing die je in fase 4 hebt ingesteld en pas het bedrag aan op wat deze fase gaat kosten. Beslis nu, niet later, of je echte of geanonimiseerde transacties naar OneLake zet, en schrijf die afweging op. *Resultaat:* Beveiligde opslag met kostenbewaking.
- [ ] **Week 51: Spark leren zonder Fabric.** PySpark lokaal installeren. Herschrijf je opschoonlogica in PySpark en vergelijk met je Polars-versie: wat is omslachtiger, wat is makkelijker. *Resultaat:* Opschoonlogica in PySpark, lokaal werkend.
- [ ] **Week 52: Delta met Spark.** Schrijf Delta-tabellen met PySpark en koppel dat aan wat je in fase 6 over Delta leerde. *Resultaat:* Clean-laag als Delta, lokaal.
- [ ] **Week 53: DP-700-leerpad.** Werk het Microsoft Learn-leerpad door: lakehouse, warehouse, security. Besteed extra tijd aan de real-time-stof (Eventstream, KQL), want die komt in je project niet voor. *Resultaat:* Leerpad door, aantekeningen op de real-time-onderdelen.
- [ ] **Week 54: Examenvoorbereiding.** Praktijkassessment afleggen. Herhaal de onderdelen waar je onder de grens zat. *Resultaat:* Assessment ruim boven de slaaggrens.

**Weekplan, deel 2: ná de kerstpauze, met Fabric-capaciteit**

- [ ] **Week 55: Fabric-start.** Zet nu de proefcapaciteit aan en noteer de einddatum in je logboek. Workspace, lakehouse, data laden of een shortcut naar ADLS. Zet je PySpark-notebook uit week 51 in Fabric aan het werk. *Resultaat:* Lakehouse met je data en een werkend notebook.
- [ ] **Week 56: Pipelines en Airflow.** Een Fabric-pipeline die je notebook aanroept, maandelijks gepland, met een melding bij fouten. Daarnaast een Apache Airflow Job in Fabric met een DAG die ingest, opschonen en scoring aanstuurt. Vergelijk in je README met Dagster: taken tegenover assets. *Resultaat:* Automatische maandrun en een werkende DAG met vergelijking.
- [ ] **Week 57: ML, rapportage en CI.** Categorisatiemodel trainen en registreren met MLflow in Fabric; voorspellingen als tabel. Power BI-rapport op de mart-laag. GitHub Actions voor je tests en Git-koppeling van de workspace. *Resultaat:* Rapport met voorspelde categorieën; tests draaien bij elke wijziging.
- [ ] **Week 58: Examen en afronding.** DP-700 afleggen. Verbruik nakijken met de capacity-metrics. Architectuurschets en README bijwerken. Houd de capaciteit aan of pauzeer hem, want fase 8 heeft hem nog nodig. *Resultaat:* Eindcriterium fase 7.

**Klaar als:** je pipeline elke maand zonder handwerk in Fabric draait, inclusief scoring, en je DP-700 hebt.

**Mijlpaal:** Data engineer of ML engineer met een complete cloudpipeline en certificering.

> Microsoft werkt het DP-700-examen regelmatig bij, voor het eerst weer op 19 oktober 2026. Gebruik de studiegids die geldt op het moment dat je aan deze fase begint.

### Fase 8 · Schaal voelen

2 weken, weken 59 t/m 60. Je eigen data is klein. Met een grote openbare dataset leer je waar de grenzen van elke tool liggen.

**Opdrachten**

- [ ] Benchmark op een jaar NYC Taxi-ritten: pandas, Polars en DuckDB
- [ ] Dezelfde queries in Spark in Fabric, plus een rapport met advies

**Leren**

- Wanneer één machine volstaat en wanneer niet
- Streaming en out-of-core verwerking
- Queryplannen lezen

**Bronnen**

- NYC TLC Trip Record Data (al in Parquet)
- *Designing Data-Intensive Applications*, de delen over batchverwerking

**Weekplan**

- [ ] **Week 59: Benchmark lokaal.** Een jaar NYC Taxi-ritten, tientallen tot ruim honderd miljoen rijen. Drie vaste queries in pandas, Polars (eager, lazy en streaming) en DuckDB. Meet tijd en piekgeheugen. Verwacht dat pandas omvalt met een geheugenfout, en dat Polars eager dat misschien ook doet: dát is de meetuitkomst, niet een mislukking. Noteer bij welke omvang het omslagpunt lag en hoeveel geheugen je machine heeft. *Resultaat:* Meettabel, inclusief de gevallen die niet draaiden en waarom.
- [ ] **Week 60: Spark en rapport.** Dezelfde queries in een Spark-notebook in Fabric. Vergelijk de queryplannen en schrijf je advies per datavolume. Zet daarna je Fabric-capaciteit uit. *Resultaat:* Eindcriterium fase 8.

**Klaar als:** je met eigen cijfers onderbouwt welke tool je bij welke omvang kiest, inclusief bij welke omvang een tool het niet meer trekt.

## Certificering

- **DP-700** Fabric Data Engineer: in fase 7.
- **DP-600** Fabric Analytics Engineer: alleen als je rol richting Power BI en semantische modellen gaat.
- **Databricks Data Engineer Associate:** later, als klanten op Databricks draaien.

## Boeken

Als je er maar drie koopt: *Designing Machine Learning Systems* (fase 2 en 3), *AI Engineering* (fase 4) en *Fundamentals of Data Engineering* (deel B). ISLP, Pro Git, Dagster University en Microsoft Learn zijn gratis.

Reken je leestijd eerlijk: 2 uur per week over 60 weken is ongeveer 120 uur, en technische stof met begrip gaat op zo'n 15 pagina's per uur. Je leest dus rond de 1800 pagina's, niet de 3000 die hierboven staan. Dat is precies waarom "lezen volgt bouwen" de regel is: je leest het hoofdstuk dat je nu nodig hebt, en de rest is naslag.
