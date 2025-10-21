# O3_The_Rectangle2D_Class — README

## Kort beskrivelse

Et **aksejustert 2D-rektangel** definert ved sentrum, bredde og høyde.
Støtter areal/omkrets, punkt- og rektangelrelasjoner (inne/overlapp), `in`-operator og sammenligning på areal.
Hovedprogrammet skriver ut resultat i **tabellform**.

---

## Filstruktur

```
O3_The_Rectangle2D_Class.py      # Klasse + main() med tabellutskrift
test_O3_The_Rectangle2D_Class.py # Enhetstester (unittest)
```

---

## Kjøring

```bash
python O3_The_Rectangle2D_Class.py
```

Programmet ber om to rektangler (`r1`, `r2`) og skriver:

* Måltabell: `Area`, `Perimeter` for r1 og r2
* Relasjonstabell: `contains_point`, `contains`, `in`, `overlaps`, `r1 < r2?`

> Tall vises med én desimal i tabellen.

---

## Bruk (API kort)

**Klasse:** `Rectangle2D(x: float, y: float, width: float, height: float)`
**Properties:** `x`, `y`, `width`, `height` (validering: `> 0`)
**Avledet:** `area`, `perimeter`
**Metoder:** `get_area()`, `get_perimeter()`, `contains_point(px, py)`, `contains(other)`, `overlaps(other)`
**Operatorer:** `other in self` (`__contains__`), sammenligning på areal (`==, <, <=, >, !=`)

---

## Geometrikriterier (inkluderer kanter)

* **Punkt inne:** (|x-x_c| \le \tfrac{w}{2}) og (|y-y_c| \le \tfrac{h}{2})
* **Rektangel inne:** (|\Delta x| \le \tfrac{w-w'}{2}), (|\Delta y| \le \tfrac{h-h'}{2})
* **Overlapp:** (|\Delta x| \le \tfrac{w+w'}{2}), (|\Delta y| \le \tfrac{h+h'}{2})

Flyttall sammenlignes med toleranse: `rel=1e-9`, `abs=1e-12`.

---

## Testing

Kjør enhetstester:

```bash
python -m unittest -v test_O3_The_Rectangle2D_Class.py
```

Dekker areal/omkrets, punkt/rek­tangel-relasjoner, `in`, sammenligning og validering av bredde/høyde.

