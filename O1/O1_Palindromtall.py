# Be brukeren om et tresifret heltall og sjekk om input er et tall, ikke som str'aaaaaa'
while True:
    try:
        tall = int(input('Skriv inn et tresifret heltall: '))
        break
    except ValueError:
        print('Feil: Du må skrive inn et tall.')


# Sjekk om tallet er et tresifret
if 100 <= abs(tall) <= 999:
    # Hent ut sifrene
    hundreds = abs(tall) // 100
    ones = abs(tall) % 10

    # Sjekk om tallet er et palindrom
    if hundreds == ones:
        print(f'{tall} er et palindromtall.')
    else:
        print(f'{tall} er ikke et palindromtall.')

# Feil melding
else:
    print('Feil: Du må skrive inn et tresifret heltall (100–999).')
