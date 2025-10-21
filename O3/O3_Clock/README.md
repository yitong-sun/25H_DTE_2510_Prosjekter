# DTE2510 – O3_Clock

## Oversikt

En liten, selvstendig **Clock**-klasse som representerer dato og tid (år–måned–dag–time–minutt–sekund) **uten** å bruke standardbibliotek for dato/tid.
Klassen **validerer og korrigerer** alle felt og håndterer rulling ved inkrement (sek → min → time → dag → måned → år).

## Forutsetninger

* Python **3.13**
* Ingen tredjepartsavhengigheter

## Filstruktur

```
O3_Clock/
├─ O3_Clock.py         # Hovedklassen: Clock
└─ test_O3_Clock.py    # Enhetstester (unittest)
```

## Installasjon og kjøring

Fra mappen som inneholder filene:

```bash
python -m unittest -v
```

Forventning: alle tester passerer (OK).

## Kort brukseksempel

```python
from O3_Clock import Clock

clk = Clock(2023, 12, 31, 23, 59, 58)
print(clk)           # 2023-12-31 23:59:58
clk.inc_sec()
print(clk)           # 2023-12-31 23:59:59
clk.inc_sec()
print(clk)           # 2024-01-01 00:00:00

clk.month = 2        # Februar
clk.day = 31         # Ugyldig i februar → korrigeres til 1
print(clk.day)       # 1
repr(clk)            # f.eks. "Clock(2024, 2, 1, 0, 0, 0)"
```

## API (utdrag)

### Klasse

`Clock(year=0, month=1, day=1, hour=0, min=0, sec=0)`

* Private felt: `_year, _month, _day, _hour, _minute, _sec`
* Properties med validering: `year, month, day, hour, min, sec`

  * Endring av `month` **revaliderer** `day` automatisk (over maks → settes til `1`).
  * Ugyldig `day` settes til **1**.

### Hjelpemetoder

* `is_leapyear(year: int) -> bool` – Skuddår: (delelig med 4 og ikke 100) eller (delelig med 400).
* `days_in_month(month: int, year: int) -> int` – 31/30/28/29 basert på måned og skuddår.

### Inkrement

* `inc_sec()` → ruller til minutt ved 60
* `inc_min()` → ruller til time ved 60
* `inc_hour()` → ruller til dag ved 24
* `inc_day()` → ruller til måned ved månedsslutt
* `inc_month()` → ruller til år ved 13
* `inc_year()` → øker år med 1

### Samlet setting

* `set_clock(year, month, day, hour, min, sec)` – Setter alle verdier i korrekt rekkefølge med validering.

### Strengrepresentasjon

* `__str__()` → `"YYYY-MM-DD HH:MM:SS"` (nullpadding)
* `__repr__()` → f.eks. `Clock(2024, 1, 1, 0, 0, 0)` (debug-vennlig)

## Testdekning (høydepunkter)

* Init med gyldige/ugyldige verdier
* Skuddår og `days_in_month`
* Rulling ved sek/min/time/dag/måned/år
* Property-validering og revalidering (`month` → `day`)
* `set_clock(...)` med korrigering
* Stabil `__repr__`

## Designvalg (kort)

* **Invariants** holdes sanne etter hver setter og inkrement.
* Ugyldig `day` **klampes** til `1` (i tråd med oppgaven).
* Internt navn for minutt: `_minute` (tydelig internt), property: `min`.
* Ingen bruk av `datetime`/`time` for logikk; alt beregnes manuelt.
