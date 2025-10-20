'''
Program: Monte Carlo-estimering av π
----------------------------------------------------
Tre metoder:
1. Ren Python for-løkke
2. NumPy vektoriserte beregning
3. NumPy med chunking (minne-effektiv og in-place)
Programmet sammenligner tid og feil for hver metode.

Eksempler på kjøring:
1,Hvor mange punkter vil du simulere? Skriv inn: 1_000_000
Metode          |      Estimat |        Avvik |  Tid (sek)
------------------------------------------------------------
Python for      |   3.14113200 |   0.00046065 |     0.2295
NumPy           |   3.14210400 |   0.00051135 |     0.0191
NumPy chunked   |   3.14312800 |   0.00153535 |     0.0076

2,Hvor mange punkter vil du simulere? Skriv inn: 10_000_000
Metode          |      Estimat |        Avvik |  Tid (sek)
------------------------------------------------------------
Python for      |   3.14171040 |   0.00011775 |     2.0676
NumPy           |   3.14195200 |   0.00035935 |     0.1060
NumPy chunked   |   3.14124160 |   0.00035105 |     0.0633

3,Hvor mange punkter vil du simulere? Skriv inn: 100_000_000
Metode          |      Estimat |        Avvik |  Tid (sek)
------------------------------------------------------------
Python for      |   3.14146020 |   0.00013245 |    20.4396
NumPy           |   3.14177460 |   0.00018195 |     1.4978
NumPy chunked   |   3.14167040 |   0.00007775 |     0.6194

4,Feil håndtering
Hvor mange punkter vil du simulere? Skriv inn: aaa
Vennligst skriv inn et heltall.
Hvor mange punkter vil du simulere? Skriv inn: -1
Antall må være større enn 0.

Konklusjon
Alle metoder gir liten feil.
- Python for: treg ved stort n.
- NumPy: rask for middels n.
- NumPy chunked: raskest og mest skalerbar for svært stort n.
'''
import math
import random
import time
import numpy as np


'''Alternativ 1: Ren Python for-løkke'''
def estimate_pi_for(n: int) -> float:
    hits = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:    # sjekk om punktet ligger i sirkelen
            hits += 1
    return 4 * hits / n


'''Alternativ 2: NumPy vektoriserte beregning'''
def estimate_pi_numpy(n: int) -> float:
    x = np.random.uniform(-1, 1, size = n)
    y = np.random.uniform(-1, 1, size = n)
    hits = np.sum(x ** 2 + y ** 2 <= 1) # boolsk array summeres direkte
    return 4 * hits / n


'''Alternativ 3: NumPy med chunking (unngå minneproblemer ved stor n)'''
def estimate_pi_numpy_chunked(n: int, chunk: int = 1_000_000) -> float:
    hits = 0
    left = n
    while left > 0:
        m = min(left, chunk)    # kjør i biter hvis n er stort
        x = np.random.uniform(-1, 1, size=m)
        y = np.random.uniform(-1, 1, size=m)
        np.square(x, out=x)     # in-place kvadrering
        np.square(y, out=y)
        x += y                  # unngår å lage ny array
        hits += np.sum(x <= 1.0)
        left -= m
    return 4 * hits / n


def benchmark(n: int):
    methods = [
        ('Python for', estimate_pi_for),
        ('NumPy', estimate_pi_numpy),
        ('NumPy chunked', estimate_pi_numpy_chunked),
    ]
    # Skriv tabell-header (alle kolonner med samme bredde)
    print(f'{"Metode":<15} | {"Estimat":>12} | {"Avvik":>12} | {"Tid (sek)":>10}')
    print('-' * 60)

    for name, func in methods:
        t0 = time.perf_counter()
        estimated_pi = func(n)
        t1 = time.perf_counter()
        error = abs(estimated_pi - math.pi)
        # print(f'{name:<15} | {estimated_pi:.8f} | {error:.8f} | {t1 - t0:.4f}')
        print(f'{name:<15} | {estimated_pi:12.8f} | {error:12.8f} | {t1 - t0:10.4f}')



def main(debug: bool = False):
    # Hvis debug=True er det alltid samme "tilfeldige" resultat
    if debug:
        random.seed(0)  # gjør resultatet forutsigbart (nyttig for testing)

    n: int = 0
    while True:
        try:
            n = int(input('Hvor mange punkter vil du simulere? Skriv inn: '))
            if n > 0:
                break
            print('Antall må være større enn 0.')
        except ValueError:
            print('Vennligst skriv inn et heltall.')
            continue

    benchmark(n)


if __name__ == "__main__":
    # Velg om du vil ha forutsigbart eller ekte tilfeldig
    main(debug=True)  # fast resultat
    # main(debug=False)  # ekte tilfeldig