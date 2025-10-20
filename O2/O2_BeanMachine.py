'''
Program: Bean Machine (Galtonbrett)
----------------------------------
Dette programmet simulerer en Bean Machine.
Kulene faller gjennom rader og havner i spor nederst.
Programmet teller hvor mange kuler som havner i hvert spor
og skriver ut et stående histogram.

Hvis høyden overstiger 20 linjer, blir søylene skalert ned
slik at alt vises innenfor 20 linjer.

Histogrammet bruker forskjellige symboler for høyde:
    █ = full blokk
    ▓ = 2/3 fylt
    ▒ = 1/3–2/3 fylt
    ░ = <1/3 fylt

----------------------------------
Eksempel 1 på kjøring: (forutsigbart)
Antall rader (rows): 4
Antall kuler (balls): 10

Counts: [0, 3, 2, 4, 1]

Stående histogram (smoothed):
          █
    █     █
    █  █  █
    █  █  █  █
---------------
 0  1  2  3  4

----------------------------------
Eksempel 2 på kjøring: (forutsigbart)
Antall rader (rows): 20
Antall kuler (balls): 2000

Counts: [0, 0, 0, 8, 11, 25, 81, 149, 260, 319, 328, 340, 226, 145, 72, 26, 6, 4, 0, 0, 0]

Stående histogram (smoothed):
                               ░  █
                            ▓  █  █
                            █  █  █
                            █  █  █
                         ░  █  █  █
                         █  █  █  █
                         █  █  █  █  ░
                         █  █  █  █  █
                         █  █  █  █  █
                         █  █  █  █  █
                         █  █  █  █  █
                      ▓  █  █  █  █  █  ▒
                      █  █  █  █  █  █  █
                      █  █  █  █  █  █  █
                      █  █  █  █  █  █  █
                   ▓  █  █  █  █  █  █  █  ░
                   █  █  █  █  █  █  █  █  █
                   █  █  █  █  █  █  █  █  █
                ▒  █  █  █  █  █  █  █  █  █  ▒
          ▒  ▒  █  █  █  █  █  █  █  █  █  █  █  ▒  ░
---------------------------------------------------------------
 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
Til brukere:
Histogrammet er begrenset til maks 20 linjer høyde
Søylene er skalert ned med faktor ≈ 17.00.
Symboler brukt for høyde:
█ = full blokk
▓ = 2/3 fylt
▒ = 1/3–2/3 fylt
░ = <1/3 fylt
'''

import math
import random


# Simulerer en Bean Machine:
# rows = antall rader
# balls = antall kuler
# Returnerer en liste counts som viser hvor mange kuler som havner i hvert spor.
def simulate_bean_machine(rows: int, balls: int):
    slots = rows + 1
    counts = [0] * slots
    for _ in range(balls):
        # Hver rad gir tilfeldig venstre (0) eller høyre (1)
        right_number = sum(random.choice((0, 1)) for _ in range(rows))

        counts[right_number] += 1

    return counts


# Tegner et stående histogram av counts.
# - Bruker blokksymboler for delvis fylling.
# - Skalerer ned hvis høyden er større enn max_height_limit.
def draw_histogram(counts, mark='█', marks=('░', '▒', '▓'),
                   cell_width=3, max_height_limit=20):

    # Legger et tegn midtstilt i en celle med fast bredde.
    def cell(mark_char: str) -> str:
        return mark_char.center(cell_width)

    # Velger riktig symbol (░, ▒, ▓) avhengig av fyllingsgrad mellom 0 og 1.
    # Hvis verdien er helt fylt (≥ 1), brukes '█' utenfor denne funksjonen.
    def pick_mark(fraction: float, marks_tuple) -> str:
        pick_mark_index = min(int(fraction * len(marks_tuple)), len(marks_tuple) - 1)
        return marks_tuple[pick_mark_index]

    max_height = max(counts) if counts else 0
    slots = len(counts)

    if not counts:
        print('Ingen data.')
        return
    if max_height == 0:
        print('Alle null.')
        print(counts)
        return

    # Beregn skala (for å begrense høyden)
    scale = (max_height / max_height_limit) if max_height > max_height_limit else 1.0
    height = math.ceil(max_height / scale)

    height_scaled = [k / scale for k in counts]

    # Tegn histogram linje for linje (fra topp til bunn)
    for level in range(height, 0, -1):
        base = level - 1
        line = []

        for h in height_scaled:
            if h <= base:
                mark_char = ' '
            elif h >= level:
                mark_char = mark
            else:
                fraction = h - base
                mark_char = pick_mark(fraction, marks)

            line.append(cell(mark_char))
        print(''.join(line))

    # Bunnlinje og spor-indekser
    print(''.join(cell('---') for _ in range(slots)))
    print(''.join(f'{index_number:^{cell_width}}' for index_number in range(slots)))

    # Skriver ut informasjon til brukere om histogrammets begrensning, skalering og symbolforklaring.
    def print_info(scale: float, max_height_limit: int):
        if scale > 1:
            print(f'Til brukere:\n'
                  f'Histogrammet er begrenset til maks {max_height_limit} linjer høyde\n'
                  f'Søylene er skalert ned med faktor ≈ {scale:.2f}.\n'
                  f'Symboler brukt for høyde:\n'
                  f'█ = full blokk\n'
                  f'▓ = 2/3 fylt\n'
                  f'▒ = 1/3–2/3 fylt\n'
                  f'░ = <1/3 fylt\n'
                  )

    print_info(scale, max_height_limit)

def main(debug: bool = False):
    # Hvis debug=True er det alltid samme "tilfeldige" resultat
    if debug:
        random.seed(0)  # gjør resultatet forutsigbart (nyttig for testing)

    try:
        rows = int(input('Antall rader (rows): '))
        balls = int(input('Antall kuler (balls): '))
        if rows < 0 or balls < 0:
            print('Ugyldig input: må være ikke-negative heltall.')
            return
    except ValueError:
        print('Ugyldig input: må være heltall.')
        return

    counts = simulate_bean_machine(rows, balls)

    print("\nCounts:", counts)
    print("\nStående histogram (smoothed):")
    draw_histogram(counts)


if __name__ == "__main__":
    # Velg om du vil ha forutsigbart eller ekte tilfeldig
    main(debug=True)   # fast resultat
    # main(debug=False)  #ekte tilfeldig