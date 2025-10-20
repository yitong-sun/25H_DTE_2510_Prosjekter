'''
Program: Bestem årstid

Beskrivelse:
Dette programmet ber brukeren om å skrive inn en måned (som tekst) og en dag (som tall).
Programmet sjekker om input er gyldig, og bestemmer hvilken årstid datoen tilhører
basert på faste startdatoer for vår, sommer, høst og vinter.

Funksjoner:
- Validerer månedsnavn og dag
- Håndterer ugyldige inndata (feilmeldinger ved feil måned eller dag)
- Returnerer korrekt årstid

Eksempel på kjøring:
    Brukerinput:
        måned → "mars"
        dag   → "19"
    Output:
        "Årstiden er: Vinter"
'''

from datetime import date

def bestem_årstid():
    # Ordbok som konverterer månedsnavn til månedsnummer (bruker dictionary)
    dict_month_number = {
        'januar': 1,
        'februar': 2,
        'mars': 3,
        'april': 4,
        'mai': 5,
        'juni': 6,
        'juli': 7,
        'august': 8,
        'september': 9,
        'oktober': 10,
        'november': 11,
        'desember': 12
    }

    # Datoer for sesongstart, også dictionary
    sesong_grenser = {
        'Vår': date(2000, 3, 20),
        'Sommer': date(2000, 6, 21),
        'Høst': date(2000, 9, 22),
        'Vinter': date(2000, 12, 21)
    }

    # Les inn måned fra brukeren med ubegrensede forsøk
    while True:
        month = input('Skriv inn månedens navn: ').strip().lower()
        number = dict_month_number.get(month)

        if number is None:
            print('Feil: ugyldig månedsnavn.')
            continue # Be om ny måned hvis noe er feil

        # Les inn dag for valgt måned
        while True:
            day = input('Skriv inn dag i måneden: ').strip()

            try:
                dato_input = date(2000, number, int(day))
            except ValueError:
                print('Feil: Ugyldig dag.')

            else:
                # Bestem årstid ut fra dato
                if sesong_grenser['Vår'] <= dato_input < sesong_grenser['Sommer']:
                    return 'Vår'
                elif sesong_grenser['Sommer'] <= dato_input < sesong_grenser['Høst']:
                    return 'Sommer'
                elif sesong_grenser['Høst'] <= dato_input < sesong_grenser['Vinter']:
                    return 'Høst'
                else:
                    return 'Vinter'


# Kjør funksjonen og skriv ut resultatet
# Funksjonen bestem_årstid() har et returverdi som kan brukes på nytt
årstid = bestem_årstid()
print(f'Årstiden er: {årstid}')
