# DTE2510 - Matrisesystem med tilfeldig utvalg

## Beskrivelse
Dette programmet genererer en **N x N matrise** med tilfeldige heltall mellom `0` og `9`.  
For hver rad velger programmet et tilfeldig tall, og lager en **subliste** som starter fra  
det valgte tallet og går ut til slutten av raden.

Resultatene vises i konsollen, og brukeren kan velge å **lagre resultatene til en JSON-fil**  
med metadata (størrelse, seed, tidsstempel).

---

## Funksjoner
- Genererer matriser med tilfeldige tall
- Tilfeldig utvalg fra hver rad
- Viser resultatene i ryddig format
- Valgfri lagring til `.json` i `results/`-mappen
- Støtte for `config.json` og kommandolinjeargumenter
- Logging (INFO/DEBUG)
- Feilhåndtering for ugyldig input

---

## Eksempel på kjøring


Eksempel på kjøring:
    Oppgi størrelse på matrisen (N): 5

    2025-10-20 15:01:04,634 - main - INFO - Generer matrise N=5
    === Resulater ===
    Rad0: [6, 9, 2, 2, 5],tilfeldig_tall = 2,start_index = 2,subliste = [2, 2, 5]
    Rad1: [0, 1, 7, 2, 0],tilfeldig_tall = 0,start_index = 0,subliste = [0, 1, 7, 2, 0]
    Rad2: [4, 2, 9, 2, 9],tilfeldig_tall = 9,start_index = 2,subliste = [9, 2, 9]
    Rad3: [9, 0, 0, 9, 6],tilfeldig_tall = 9,start_index = 0,subliste = [9, 0, 0, 9, 6]
    Rad4: [4, 7, 7, 5, 6],tilfeldig_tall = 7,start_index = 1,subliste = [7, 7, 5, 6]

    Vil du lagre resultatene til JSON? (y/N): y

    2025-10-20 15:01:08,191 - main - INFO - Resultater skrevet til /Users/yitongsun/PyCharmMiscProject/DTE_2510/results/resultater_20251020_150108.json
    Lagret: /Users/yitongsun/PyCharmMiscProject/DTE_2510/O3/results/resultater_20251020_150108.json


## Bruk
Kjør programmet med Python (versjon 3.13):

```bash
python main.py
```


Du kan også bruke kommandolinjeargumenter:
python main.py --size 5 --seed 42 --save


Argumenter:

| Flag           | Forklaring                        |
| -------------- | --------------------------------- |
| `-n, --size`   | Matrisestørrelse (N)              |
| `--seed`       | Tilfeldighetsfrø for reproduksjon |
| `--save`       | Lagre resultatene uten spørsmål   |
| `-o, --output` | Egendefinert filnavn              |
| `--debug`      | Slå på detaljert logging          |


## Eksempel på config.json

Du kan opprette en valgfri config.json i samme mappe som main.py:
{
    "size": 5,
    "seed": 42,
    "save": true,
    "debug": false
}

## Output

Når lagring er aktivert, opprettes filer automatisk i results/-mappen:
results/
└── resultater_20251020_214300.json

JSON-filen inneholder både resultatene og metadata:
{
    "metadata": {
        "N": 5,
        "seed": 42,
        "timestamp": "20251020_214300"
    },
    "resultater": [...]
}


## Versjon

v1.0 - Første stabile versjon

