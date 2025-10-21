# Bioinformatics — (Oblig 2 → Unit testing)

## Kort beskrivelse

`find_genes(genome: str) -> list[str]` finner **alle gyldige gener** i en DNA-sekvens (A/T/C/G):

* Starter rett etter `ATG`
* Slutter rett før `TAG`/`TAA`/`TGA`
* Lengden mellom start og stopp er **delelig på 3**
* **Ingen** av `ATG`/`TAG`/`TAA`/`TGA` forekommer **inni** genet
  Ingen funn/ugyldig input ⇒ `['No genes found']`. Funksjonen har **ingen I/O**.

---

## Mappestruktur

```
.
├─ O3_Unit_teste_Bioinformatics.py   # Implementasjon (find_genes)
└─ test_O3_Unit_teste_Bioinformatics.py  # Enhetstester (unittest)
```

---

## Krav

* Python **3.9+**
* Kun standardbibliotek

---

## Installasjon

```bash
# valgfritt: venv
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

---

## Bruk (API)

```python
from O3_Unit_teste_Bioinformatics import find_genes

result = find_genes('TTATGTTTTAAGGATGGGGCGTTAGTT')
# ['TTT', 'GGGCGT']

result = find_genes('invalid-letters-here')
# ['No genes found']
```

**Kontrakt**

* Input: vilkårlig streng (case-insensitiv). Andre tegn enn A/T/C/G ⇒ **ugyldig**.
* Output: `list[str]` med gener (uten start-/stoppkodon). Ingen funn ⇒ `['No genes found']`.
* Ingen utskrift eller global tilstand.

---

## Kjør tester

```bash
python -m unittest -v test_O3_Unit_teste_Bioinformatics.py
```

Testene dekker: tom/ugyldig input, eksempelsekvenser, kanttilfeller (overlapp/rand), forbudte kodoner i midten, lengre sekvenser.

---

## Designnotater

* Lineært søk etter `ATG`, deretter nærmeste stopp i **samme leseramme** (steg 3).
* Robust validering av alfabet (regex), case-insensitiv behandling, deterministisk retur.

---

## Endringslogg (fra Oblig 2)

* Returtype endret fra streng til `list[str]`; fjernet `print()`.
* Standardiserte “ingen funn” til `['No genes found']`.
* Beholdt reglene for start/stopp/ramme/forbudte kodoner; ryddigere input-validering.
