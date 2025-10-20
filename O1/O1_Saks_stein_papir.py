'''
Program: Saks–stein–papir-spill
Beskrivelse:
    Dette programmet lar brukeren spille det klassiske spillet
    'saks–stein–papir' mot datamaskinen.

    Reglene er:
        - Saks (0) slår papir (2)
        - Stein (1) slår saks (0)
        - Papir (2) slår stein (1)
        - Hvis begge velger det samme da blir det uavgjort

    Programmet ber brukeren om å velge et tall (0, 1 eller 2) og gir resultatet.
    Hvis brukeren skriver inn ugyldig input, får man en feilmelding
    og blir bedt om å prøve igjen.

Eksempel på kjøring:
    Saks-stein-papir-spill
    0: Saks
    1: Stein
    2: Papir
    Velg 0, 1 eller 2: 1
    Du valgte: 1
    Machine valgte: 0
    Du vant!
'''
# Importerer random-modulen for å generere tilfeldige tall
import random

while True:
    # Be brukeren taste inn et tall
    try:
        din_valg = input('''Saks-stein-papir-spill
        0: Saks
        1: Stein
        2: Papir
        q: for å avslutte
        Velg 0, 1 eller 2: ''').strip()

        if din_valg == 'q':
            print('Avslutter spillet. Ha det bra!\n')
            break

        din_valg = int(din_valg)

    # Feilhåndtering hvis brukeren ikke skriver inn et heltall
    except ValueError:
        print('Feil: du må skrive inn et tall (0, 1 eller 2).\n')
        continue # Start på nytt

    # Sjekk at tallet er innenfor gyldig område (0–2)
    if din_valg not in [0, 1, 2]:
        print('Feil: ugyldig valg. Du må velge 0, 1 eller 2.\n')
        continue # Start på nytt

    # Datamaskinen velger tilfeldig mellom 0, 1 og 2
    machine = random.randint(0, 2)
    print(f'Du valgte: {din_valg}\nMachine valgte: {machine}')

    # Sammenlign valg og avgjør resultat
    if din_valg == machine:
        print('Uavgjort!\n')
    elif (din_valg == 0 and machine == 2) or (din_valg == 1 and machine == 0) or (din_valg == 2 and machine == 1):
        print('Du vant!\n')
    else:
        print('Du tapte!\n')
