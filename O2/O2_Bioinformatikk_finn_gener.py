'''
Program: Bioinformatikk: finn gener
----------------------------------------------------
Dette programmet analyserer en streng av bokstavene A, T, C og G og et gen defineres som en delstreng som:
  - starter etter ATG
  - slutter rett før TAG, TAA eller TGA
  - har lengde som er delelig med 3
  - ikke inneholder noen av kodonene ATG, TAG, TAA eller TGA imidten

Programmet:
  - tar inn en gene streng (kun bokstavene A, T, C, G er tillatt)
  - finner alle gyldige gener i strengen
  - returnerer gener som kommaseparert streng (f.eks. "TTT,GGGCGT")
  - returnerer "NO GENE FOUND" dersom ingen gyldige gener finnes

Nåvarende programmet:
Eksempel 1 på kjøring:
(Ingen input trenges)
TTT,GGGCGT

Dette programmet har et alternativ til å skrive inn en gene streng i main funksjonen:
Eksempel 2 på kjøring:
Vennligst skriv inn en gene streng: TTATGTTTTAAGGATGGGGCGTTAGTT
TTT,GGGCGT
'''

import re

# Sjekker om genet inneholder ugyldige kodoner
def check_invalid_triplet(gene: str) -> bool:
    invalid = {'ATG', 'TAG', 'TAA', 'TGA'}
    gene = gene.upper()
    for k in range(0, len(gene), 3):
        if gene[k:k + 3] in invalid:
            return False
    return True


def find_genes(genome: str) -> str:
    # Store bokstaver, og kun A, T, C, G er tillatt
    genome = genome.upper()
    if not re.fullmatch(r'^[ATCG]+$', genome):
        return 'NO GENE FOUND'

    length = len(genome)
    genes = []
    stop = {'TAG', 'TAA', 'TGA'}

    i = 0
    # Går gjennom en gene streng posisjon for posisjon
    while i <= length - 3:
        if genome[i:i + 3] != 'ATG': # Ikke startkodon
            i += 1
        else:
            found_stop = False
            # Søker etter nærmeste stoppkodon i 'gene reading frame'
            for j in range(i + 3, length, 3):
                codon = genome[j:j + 3]
                if codon in stop:
                    gene = genome[i + 3:j]  #Extract gene
                    if gene and check_invalid_triplet(gene):
                        genes.append(gene)
                    i = j + 3   # Fortsetter etter stoppkodon til å finne et annet gene
                    found_stop = True
                    break
            if not found_stop:
                i += 1 # Ingen stoppkodon funnet, hopper videre til neste posisjon

    # Returnerer gener som streng, eller melding hvis ingen finnes
    return ','.join(genes) if genes else 'NO GENE FOUND'


def main():
    # Standard teststreng
    gene_string = 'TTATGTTTTAAGGATGGGGCGTTAGTT'
    genome = gene_string.strip().upper()
    print(find_genes(genome))

    # # Alternativ: brukerinput
    # genome = input('Vennligst skriv inn en gene streng: ').strip().upper()
    # print(find_genes(genome))


if __name__ == '__main__':
    main()