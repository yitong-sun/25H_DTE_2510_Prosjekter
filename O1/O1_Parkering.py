'''
Program: Beregn parkeringsavgift
Beskrivelse:
    Dette programmet beregner prisen for parkering i et parkeringshus
    basert på antall timer bilen har stått parkert (0–168 timer).

    Prisregler:
        - 0–3 timer: 50 kr per time
        - 4–24 timer: 30 kr per time
        - 25–48 timer: 20 kr per time
        - 49–168 timer: 10 kr per time
        - Dersom bilen står parkert i mer enn 48 timer, gis en ytterligere rabatt på 20 %.

    Programmet bruker if-else-logikk for å bestemme riktig timesats
    og beregner deretter totalprisen.

Eksempel på kjøring:
    1. Skriv inn hvor mange timer bilen har stått parkert (0–168): 60
       Totalavgift for 60 timer parkering er 480.00 kr
    2. Input ikke et tall → 'Feil: du må skrive inn et heltall.'
    3. Input tall utenfor 0–168 → 'Feil: antall timer må være mellom 0 og 168.'
'''

# Be brukeren skrive inn antall timer
try:
    timer = int(input('Skriv inn hvor mange timer bilen har stått parkert (0–168): '))

    # Sjekk at input er gyldig (mellom 0 og 168 timer)
    if 0 <= timer <= 168:
        # Bestem timeavgift etter hvor lenge bilen står
        if 0 <= timer <= 3:
            avgift_per_time = 50

        elif 4 <= timer <= 24:
            avgift_per_time = 30

        elif 25 <= timer <= 48:
            avgift_per_time = 20

        elif 49 <= timer <= 168:
            avgift_per_time = 10

        # Beregn totalavgift
        total_avgift = timer * avgift_per_time
        # Mer enn 48 timer da legger til 20% rabatt
        if timer > 48:
            total_avgift *= 0.8
        # Skriv ut resultatet med to desimaler
        print(f'Totalavgift for {timer} timer parkering er {total_avgift:.2f} kr')

    # Feil melding
    else:
        print('Feil: antall timer må være mellom 0 og 168.')

#Feil melding
except ValueError:
    print('Feil: du må skrive inn et heltall.')
