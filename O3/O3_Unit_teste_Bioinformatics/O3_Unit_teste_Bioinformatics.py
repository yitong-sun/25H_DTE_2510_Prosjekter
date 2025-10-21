'''
Programmet: O3_Unit_teste_Bioinformatics

Oppsummering av endringer fra Oblig 2 (for å få testene gjennom):
- Endret signatur til find_genes(genome: str) -> list[str] (tidligere streng-retur).
- Fjernet all utskrift (ingen print), ingen I/O i funksjonen.
- Standardiserte retur uten funn til nøyaktig ['No genes found'] (case-sensitivt).
- Beholdt logikken: ATG som start, stopper før TAG/TAA/TGA, lengde delelig på 3,
  og ingen av kodonene ATG/TAG/TAA/TGA får forekomme inni gen-sekvensen.
- Renset input-behandling: bare A/T/C/G er gyldig; ellers returneres ['No genes found'].
- Gjorde implementasjonen deterministisk og testbar (ingen global tilstand).
'''

from __future__ import annotations

import re
from typing import List


_NO_GENES: List[str] = ['No genes found']
_STOP = {'TAG', 'TAA', 'TGA'}
_START = 'ATG'
_VALID_RE = re.compile(r'^[ATCG]+$')


def _check_no_invalid_triplet(gene: str) -> bool:
    '''Verifiserer at genet ikke inneholder ATG/TAG/TAA/TGA i midten.

    Args:
        gene: Kandidatgen uten start/stoppkodon (ren indre del).

    Returns:
        True hvis ingen forbudte kodoner finnes i tripletter; ellers False.

    '''
    invalid = {'ATG', 'TAG', 'TAA', 'TGA'}
    g = gene.upper()
    # Itererer i tripleskritt; avkortede haler kan ikke forekomme siden vi
    # kun danner gene fra leseramme (alltid 3-multipler).
    for k in range(0, len(g), 3):
        if g[k : k + 3] in invalid:
            return False
    return True


def find_genes(genome: str) -> List[str]:
    '''Finner alle gyldige gener i en genom-streng.

    Genereres fra følgende regler:
    - Et gen starter rett etter 'ATG' (startkodon) og slutter rett før en av 'TAG'/'TAA'/'TGA'.
    - Lengden på selve gen-sekvensen (mellom start og stopp) er delelig med 3.
    - Ingen av kodonene 'ATG'/'TAG'/'TAA'/'TGA' får forekomme inni gen-sekvensen.
    - Bare bokstavene A/T/C/G er gyldige i input.

    Args:
        genome: Genomstreng bestående av A/T/C/G (uavhengig av case).

    Returns:
        Liste med funnede gener (uten start/stoppkodon). Hvis ingen funn/ugyldig input,
        returneres ['No genes found'].

    '''
    if not genome:
        return _NO_GENES

    s = genome.upper()

    # Godta kun A/T/C/G; alt annet gir "ingen funn" per oppgaveteksten.
    if _VALID_RE.fullmatch(s) is None:
        return _NO_GENES

    genes: List[str] = []
    n = len(s)
    i = 0

    # Lineært søk etter startkodon; deretter leter vi etter nærmeste stopp i leserammen.
    while i <= n - 3:
        if s[i : i + 3] != _START:
            i += 1
            continue

        # Finn nærmeste stoppkodon i samme ramme (skritt i 3)
        found_stop = False
        for j in range(i + 3, n, 3):
            codon = s[j : j + 3]
            if codon in _STOP:
                gene = s[i + 3 : j]  # indre del mellom ATG og stopp
                # Krav: ikke tomt, delelig på 3 (garantert av rammen), ingen forbudte kodoner inni
                if gene and _check_no_invalid_triplet(gene):
                    genes.append(gene)
                    i = j + 3   # fortsett etter stoppkodon for å finne neste gen
                else:
                    i = i + 1   # Ugyldig kandidat: gå bare ett steg fram, slik at den interne ATG-en kan treffes.

                found_stop = True
                break

        if not found_stop:
            # Ingen stopp i ramme; flytt én posisjon og forsøk på nytt
            i += 1


    return genes if genes else _NO_GENES





