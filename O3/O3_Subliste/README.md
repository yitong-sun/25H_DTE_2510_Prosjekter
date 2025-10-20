# DTE2510 – Matrisesystem med tilfeldig utvalg

## Beskrivelse

Programmet genererer en **N × N matrise** med heltall i intervallet `0–9`.
For **hver rad** velges ett **tilfeldig tall**; programmet lager deretter en **subliste** fra **indeksen til den første forekomsten** av dette tallet og ut til slutten av raden.
Sublisten lages **med list comprehension** (krav i oppgaven) – **uten** slicing og uten eksplisitt `for`-løkke.

Resultatene skrives til konsollen. Du kan valgfritt **lagre som JSON** med metadata (`N`, `random_seed`, tidsstempel i ISO-8601).

---

## Forutsetninger

* Python **3.13**
* (Valgfritt) `config.json` i samme mappe som programmet

---

## Funksjoner

* Genererer matriser med tilfeldige tall (`0–9`)
* For hver rad: tilfeldig verdi → subliste fra første forekomst til slutt
* Ryddig utskrift til konsoll
* Valgfri lagring til **`.json`**
* Støtte for **`config.json`** og **kommandolinjeargumenter**
* **Logging** (`INFO`/`DEBUG`), robust håndtering av ugyldig input
* **Interaktiv** og **ikke-interaktiv** kjøring:

  * Interaktiv: ber om `N` og (ev.) bekreftelse på lagring
  * Ikke-interaktiv: `--no-interactive` eller oppgi alle nødvendige flagg

> **Merk om duplikater i raden:** Dersom det valgte tallet finnes flere ganger, brukes **indeksen til første forekomst**.

---

## Bruk

### Interaktiv kjøring

```bash
python O3_Subliste.py
```

* Programmet spør etter `N`.
* Deretter kan du velge om du vil lagre resultatene.

### Ikke-interaktiv kjøring (eksempler)

```bash
# Generer N=5 og lagre automatisk til default-fil i results/
python O3_Subliste.py -n 5 --save

# Generer og lagre til egendefinert filnavn i results/
python O3_Subliste.py -n 5 -o foo.json --save

# Generer og lagre til en absolutt sti (respekteres uendret)
python O3_Subliste.py -n 5 -o /Users/dittnavn/Desktop/foo.json --save
```

### Argumenter

| Flag               | Forklaring                                                                      |
| ------------------ | ------------------------------------------------------------------------------- |
| `-n, --size`       | Matrisestørrelse `N`. Mangler denne, spør programmet interaktivt.               |
| `--seed`           | Tilfeldighetsfrø for reproduksjon (samles internt til `random_seed`).           |
| `--save`           | Lagre uten å spørre.                                                            |
| `-o, --output`     | Utdatafil. **Relativt** navn lagres i `results/`; **absolutt** sti respekteres. |
| `--debug`          | Slå på detaljert logging (`DEBUG`).                                             |
| `--no-interactive` | Deaktiver interaktiv input (krever gyldig `-n/--size`).                         |

> **Tips:** I enkelte IDE-konsoller er ikke stdin interaktiv. Programmet forsøker interaktiv input, og faller kontrollert tilbake med tydelig feilmelding om input ikke er tilgjengelig. Bruk da `-n/--size` (og ev. `--save`).

---

## Eksempler (kort oppsummering)

1. **Ren terminalinteraksjon + bekreftet lagring**
2. **Ikke-interaktiv** – direkte lagring (`-n 5 --save`)
3. **Ugyldig N** → interaktiv korrigering
4. **Ikke-interaktiv + ugyldig N** → kontrollert avslutning
5. **Relativt filnavn** lagres i `results/` (f.eks. `-o foo.json`)
6. **Absolutt sti** lagres uendret (f.eks. til `Desktop`)

---

## `config.json` (valgfritt)

Plasseres i samme mappe som `O3_Subliste.py`. Felt i `config.json` flettes med CLI og standardverdier (prioritet **CLI > config.json > defaults**).

```json
{
  "size": 5,
  "random_seed": 42,
  "save": true,
  "debug": false
}
```

> For bakoverkompatibilitet kan også `"seed"` i config leses, men internt samles dette til `"random_seed"`.

---

## Output

* **Standardmappe:** `results/`

  * Relativt filnavn (`-o foo.json`) → `results/foo.json`
* **Absolutt sti:** respekteres uendret

**Eksempel på struktur:**

```
results/
└── resultater_20251020_214300.json
```

**Eksempel på JSON-innhold:**

```json
{
  "metadata": {
    "N": 5,
    "random_seed": 42,
    "timestamp": "2025-10-20T21:43:00+02:00"
  },
  "resultater": [
    {
      "radnummer": 0,
      "rad": [6, 9, 2, 2, 5],
      "tilfeldig_tall": 2,
      "start_index": 2,
      "subliste": [2, 2, 5]
    }
    // ...
  ]
}
```

> `timestamp` er i **ISO-8601** med tidssone og sekundoppløsning.

---

## Logging

* `INFO` som standard, `--debug` gir mer detaljert output.
* Logger-navn: `main`. Logging konfigureres med `force=True` for å unngå dupliserte handlere ved gjentatte kjøringer.

---

## Versjon

v1.0 - Første stabile versjon
