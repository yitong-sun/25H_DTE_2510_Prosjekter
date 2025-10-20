# Generer ISBN-10
while True:
    # Be brukeren om de første 9 sifrene, input som str
    isbn_str = input('Skriv inn de første ni sifrene i ISBN-10 (med ledende nuller): ')

    # Sjekk at input er 9 sifre, ellers feil melding
    if len(isbn_str) == 9 and isbn_str.isdigit():
        # Definer sjekksummen
        sum_tall = 0
        # Beregn sjekksummen
        for i in range(len(isbn_str)): # i går fra 0 til 8
            sum_tall += int(isbn_str[i]) * (i + 1)
        break

    else:
        print('Feil: Du må skrive inn nøyaktig 9 sifre.')

# Formelen
tall_10 = sum_tall % 11
# Hvis sjekksum tall_10 er 10, bruk 'X', ellers blir det str(tall_10)
tall_10 = 'X' if tall_10 == 10 else str(tall_10)

# Resultat
isbn = isbn_str + tall_10
print(f'ISBN-10: {isbn}')