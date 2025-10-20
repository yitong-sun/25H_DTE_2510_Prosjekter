import math
import time

def beregn_avstand():
    print('Beregn avstand mellom to punkter på jordens overflate!')
    time.sleep(1)

    #gjennomsnittlig radius av jorden i kilometer
    R = 6371.01

    # Tillat maks 3 forsøk
    for i in range(3):
        try:
            # Les inn bredde- og lengdegrader som flyttall (float)
            t1 = float(input('Skriv inn breddegrad for punkt 1 (i grader): '))
            g1 = float(input('Skriv inn lengdegrad for punkt 1 (i grader): '))
            t2 = float(input('Skriv inn breddegrad for punkt 2 (i grader): '))
            g2 = float(input('Skriv inn lengdegrad for punkt 2 (i grader): '))
        except ValueError:
            # Hvis brukeren skriver noe som ikke kan konverteres til tall，liksom str'aaaaa'
            print('Feil: du må skrive inn tall.\n')
            if i < 2: # Hvis ikke siste forsøk
                print('Prøv igjen!')
            continue # Hopp til neste forsøk


        # Sjekk om verdiene gyldige
        if -90 <= t1 <= 90 and -90 <= t2 <= 90 and -180 <= g1 <= 180 and -180 <= g2 <= 180:
            # Konverter grader til radianer
            t1, g1, t2, g2 = map(math.radians, (t1, g1, t2, g2))
            # Beregn avstanden
            avstand = R * math.acos(
                math.sin(t1) * math.sin(t2) +
                math.cos(t1) * math.cos(t2) * math.cos(g1 - g2)
            )
            # Skriv ut resultatet med to desimaler
            print(f'Avstanden mellom punktene er {avstand:.2f} kilometer.')
            return # Avslutt funksjonen hvis beregning var vellykket

        else:
            # Feilmelding hvis verdiene er ugyldige
            print('Feil melding: breddegrad må være mellom -90 og 90, lengdegrad mellom -180 og 180.\n')
            if i < 2: # Ikke siste forsøk
                print('Prøv igjen!')

    # Hvis alle tre forsøk feiler
    print("For mange feilforsøk. Programmet avsluttes.")

beregn_avstand()






