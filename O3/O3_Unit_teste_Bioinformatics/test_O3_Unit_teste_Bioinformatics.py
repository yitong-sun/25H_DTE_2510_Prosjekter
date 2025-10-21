'''
# Detaljert README.md:
https://github.com/yitong-sun/25H_DTE_2510_Prosjekter/tree/main/O3/O3_Unit_teste_Bioinformatics

Kort introduksjon:
Enhetstester for find_genes() i O3_Unit_teste_Bioinformatics.
Dekker tom/ugyldig input, eksempler, kanttilfeller, overlapp og stress.
'''

from __future__ import annotations
import unittest


from O3_Unit_teste_Bioinformatics import find_genes


class TestFindGenes(unittest.TestCase):
    '''Samler enhetstester for find_genes().'''

    # --- Null/ugyldig input ---

    def test_empty_string(self) -> None:
        '''Returnerer "No genes found" for tom streng.'''
        self.assertEqual(find_genes(''), ['No genes found'])

    def test_rubbish_string(self) -> None:
        '''Returnerer "No genes found" for streng utenfor A/T/C/G-alfabetet.'''
        self.assertEqual(find_genes('I AM A STRING WITH NO GENES WHATSOEVER'), ['No genes found'])

    def test_invalid_characters_mixed(self) -> None:
        '''Returnerer "No genes found" hvis ikke bare A/T/C/G forekommer.'''
        self.assertEqual(find_genes('ATGxxxTAA'), ['No genes found'])
        self.assertEqual(find_genes('TT-ATGTTTTAAGG'), ['No genes found'])

    # --- Kjent eksempel fra opprinnelig oppgave ---

    def test_given_example_returns_two_genes(self) -> None:
        '''Finner to gener i eksempelsekvensen fra Oblig 2.'''
        seq = 'TTATGTTTTAAGGATGGGGCGTTAGTT'
        self.assertEqual(find_genes(seq), ['TTT', 'GGGCGT'])

    # --- Case-insensitivitet ---

    def test_lowercase_input(self) -> None:
        '''Godtar små bokstaver og behandler dem som store.'''
        self.assertEqual(find_genes('ttatgttttaaggatggggcgttagtt'), ['TTT', 'GGGCGT'])

    # --- Ingen start/stopp ---

    def test_no_start_codon(self) -> None:
        '''Returnerer "No genes found" hvis ATG ikke finnes.'''
        self.assertEqual(find_genes('TTTTTTTAA'), ['No genes found'])

    def test_start_but_no_stop(self) -> None:
        '''Returnerer "No genes found" hvis stoppkodon i ramme ikke finnes.'''
        self.assertEqual(find_genes('CCCATGCCCCCCCCCCC'), ['No genes found'])

    # --- Forbudte kodoner i midten ---

    def test_internal_forbidden_codon_rejects_gene(self) -> None:
        '''Avviser kandidat hvis indre del inneholder ATG/TAG/TAA/TGA.'''
        self.assertEqual(find_genes('ATGTAATAA'), ['No genes found'])  # midten inneholder TAA
        self.assertEqual(find_genes('ATGATGTGA'), ['No genes found'])  # midten inneholder ATG

    # --- Flere gener og ulike rammer ---

    def test_multiple_genes_non_overlapping(self) -> None:
        '''Finner flere adskilte gener.'''
        s = 'AAATGTTTTAA' + 'CCCATGGGGCGTTAG' + 'GGG'
        self.assertEqual(find_genes(s), ['TTT', 'GGGCGT'])

    def test_overlapping_starts(self) -> None:
        '''Håndterer overlappende ATG ved å velge nærmeste gyldige stopp pr start.'''
        # ATGAAAATGCCCTAA → første kandidat avvises (ATG inni), den andre gir 'CCC'
        self.assertEqual(find_genes('ATGAAAATGCCCTAA'), ['CCC'])

    # --- Streng kant: stopp rett etter start ---

    def test_empty_inner_segment_disallowed(self) -> None:
        '''Krever at indre del ikke er tom.'''
        self.assertEqual(find_genes('ATGTAA'), ['No genes found'])

    # --- Stress/robusthet ---

    def test_long_sequence_with_many_distractors(self) -> None:
        '''Fungerer på lengre sekvens med mye støy (gyldig alfabet).'''
        s = (
            'A' * 50
            + 'ATGTTTTAA'
            + 'C' * 33
            + 'ATGGGGCGTTAG'
            + 'G' * 27
            + 'ATGATGATGTGA'  # avvises pga ATG inni
            + 'T' * 40
        )
        self.assertEqual(find_genes(s), ['TTT', 'GGGCGT'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
