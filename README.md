# Leertraject moderne datastack

Werkboek van een leertraject van beginnend programmeur naar het bouwen en in productie brengen van
machine learning- en RAG-toepassingen, met daarna de data engineering eronder. Looptijd oktober 2026
tot februari 2028, acht uur per week.

Aan het eind van dit traject staat er een maandelijkse pipeline die bankexports omzet naar een
getypeerde Parquet- en Delta-laag, transacties automatisch categoriseert met een geëvalueerd model,
en die geörkestreerd in containers draait in Azure en Microsoft Fabric. Plus een RAG-toepassing op
openbare Belastingdienst-documenten met een eigen evaluatieset.

Deze repository is het werkboek: het plan, de voortgang en de oefeningen van fase 0. De projecten
zelf krijgen eigen repositories.

## Opzet

| Bestand | Wat |
|---|---|
| [`LEERPLAN.md`](LEERPLAN.md) | Negen fasen, zestig weken, met per week een resultaat en per fase een toetsbaar eindcriterium |
| [`LOGBOEK.md`](LOGBOEK.md) | Eén entry per sessie: gedaan, geleerd, vastgelopen op, volgende stap |
| [`CLAUDE.md`](CLAUDE.md) | Werkafspraak over AI-gebruik: docent tijdens het leren, assistent zodra ik iets beheers |
| `oefeningen/` | De scripts van fase 0 |

De fasen in het kort:

| Fase | Onderwerp | Weken |
|---|---|---|
| 0 | Fundament: Python, Polars, SQL, Git | 8 |
| 1 | Polars en Parquet: van bankexport naar schone data | 6 |
| 2 | Statistiek en ML: transacties automatisch categoriseren | 8 |
| 3 | ML in productie: MLflow, Dagster, Docker, driftbewaking | 11 |
| 4 | RAG: een WKR- en btw-assistent met eigen evaluatieset | 8 |
| 5 | Pipeline en datamodel: medaillonlagen, Kimball, dbt | 5 |
| 6 | Tabelformaat en catalogus: DuckLake, Iceberg, Delta vergeleken | 3 |
| 7 | Cloud, Airflow en DP-700: Azure en Fabric | 9 |
| 8 | Schaal voelen: benchmark op NYC Taxi-data | 2 |

## Projecten

| Repository | Vanaf | Wat |
|---|---|---|
| `uitgaven-pipeline` | week 9 | Het hoofdproject. Loopt door fase 1, 2, 3, 5, 6 en 7 |
| `wkr-assistent` | week 34 | De RAG-toepassing uit fase 4 |

Nog niet aangemaakt. Links volgen zodra ze er zijn.

## Draaien

Python via [uv](https://docs.astral.sh/uv/), niet via pip.

```bash
uv run oefeningen/01_basis.py
```

uv maakt bij de eerste run zelf een `.venv` aan op basis van `pyproject.toml` en `uv.lock`, dus je
hoeft niets te installeren of te activeren.

## Voortgang

**Fase 0 · Fundament** (week 1 t/m 8)

- [x] **Week 1: werkomgeving en Python-basis.** VS Code, uv, Git en GitHub werkend. Project opgezet
  met `uv init`. Variabelen, de vier basisdatatypen, lijsten, dictionaries, `for` en `if`, uitgewerkt
  in `oefeningen/01_basis.py`.
- [ ] Week 2: functies, modules en bestanden
- [ ] Week 3: foutmeldingen en debuggen
- [ ] Week 4: opgeruimde code met ruff, en werken met branches
- [ ] Week 5: scripts 6 tot 10
- [ ] Week 6: Polars-basis
- [ ] Week 7: Polars joins en windowberekeningen
- [ ] Week 8: SQL-basis in DuckDB en de eindopdracht

Per fase komt hier een korte terugblik: wat ik bouwde, welke keuzes ik maakte en wat ik leerde.
