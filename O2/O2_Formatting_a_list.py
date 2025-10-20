'''
Program: Formater liste + velg artikkel (en/ei/et)
----------------------------------------------------
Dette programmet lar brukeren skrive inn ett element (substantiv/frase).
Programmet:
  - normaliserer hvert input (fjerner tegn som ikke er bokstaver(inkl.ÆØÅ)/–/mellomrom)
  - fjerner evt. ledende artikkel (en/ei/et) fra input
  - velger artikkel automatisk: kjente nøytrale endelser er «et», ellers «en» (mulig feil).
  - formaterer FLERE elementer som "a, b og c"
  - skriver "Ingen data." hvis ingen gyldige elementer ble gitt

Eksempler på kjøring:
1,Vennligst skriv inn ett element om gangen (tom for å avslutte): eple
Vennligst skriv inn ett element om gangen (tom for å avslutte):
Elementet er et eple.

2,Vennligst skriv inn ett element om gangen (tom for å avslutte): banna
Vennligst skriv inn ett element om gangen (tom for å avslutte):
Elementet er en banna.

3,Vennligst skriv inn ett element om gangen (tom for å avslutte): eple
Vennligst skriv inn ett element om gangen (tom for å avslutte): banan
Vennligst skriv inn ett element om gangen (tom for å avslutte):
Elementene er eple og banan.

4,Vennligst skriv inn ett element om gangen (tom for å avslutte): eple
Vennligst skriv inn ett element om gangen (tom for å avslutte): banan
Vennligst skriv inn ett element om gangen (tom for å avslutte): appelsin
Vennligst skriv inn ett element om gangen (tom for å avslutte):
Elementene er eple, banan og appelsin.

5,Vennligst skriv inn ett element om gangen (tom for å avslutte): et eple
Vennligst skriv inn ett element om gangen (tom for å avslutte):
Elementet er et eple.

6,Vennligst skriv inn ett element om gangen (tom for å avslutte): grønt-eple!!!
Vennligst skriv inn ett element om gangen (tom for å avslutte):
Elementet er et grønt-eple.

7,Vennligst skriv inn ett element om gangen (tom for å avslutte):
Ingen data.

8,Vennligst skriv inn ett element om gangen (tom for å avslutte): 123!!!
Vennligst skriv inn ett element om gangen (tom for å avslutte):
Ingen data.


'''
import re

# Kjente nøytrale endelser
# NB: Dette er en forenkling for oppgaven, ikke en full grammatikk.
NEUTER_SUFFIXES = ('skap', 'hus', 'rom', 'verk',
                   'mål', 'navn', 'år', 'sted',
                   'språk', 'tema', 'eple', 'eri',
                   'tre'
                   )

'''Rens og normaliser input fra brukeren.
    - Fjerner ulovlige tegn (kun bokstaver inkl. ÆØÅ/ bindestrek / mellomrom beholdes)
    - Strip: fjerner mellomrom i starten/slutten
    - Fjerner ledende artikkel (en/ei/et) dersom den finnes
    - Returnerer en "ren" streng, eller '' hvis ingenting gjenstår
'''
def normalize_item(raw: str) -> str:
    cleaned = re.sub(r'[^A-Za-zÆØÅæøå\- ]+', '', raw).strip()
    if not cleaned:  # Bare symboler/whitespace er ikke gyldig
        return ''
    words = cleaned.split()
    # Hvis første ord er artikkel, fjern den. (Her håndteres kun norsk en/ei/et)
    if words and words[0].casefold() in {'en', 'ei', 'et'}:
        words = words[1:]
    # Hvis det kun var artikkel (ingenting igjen), returner tom streng
    if not words:
        return ''
    normalized = ' '.join(words).strip()  # liste til str
    return normalized  # Kan være '' (tom)


'''Hent siste "del" som styrer artikkel:
    - Først siste ord i frasen (delt på whitespace)
    - Deretter siste segment etter bindestrek (e-post → post)
'''
def last_token(noun: str) -> str:
    token = noun.strip()
    if not token:
        return ''
    # Siste ord, split uten argument, deler på alle typer whitespace
    last = token.split()[-1]
    # Siste segment etter bindestrek (om finnes)（e-post -> post）
    last = last.split('-')[-1]
    return last


'''
Velger artikkel automatisk: kjente nøytrale endelser er «et», ellers «en».
Merk: Dette er en enkelt måte i oppgaven, ikke full språkdekning.
'''
def choose_article(noun: str) ->str:
    # Normaliser først (renser og fjerner evt. ledende artikkel)
    noun = normalize_item(noun)
    # Hvis det ikke er noe igjen etter normalisering, bruk trygg default: 'en'
    if not noun:
        return 'en'
    # Finn siste segment for å bestemme artikkelen
    last = last_token(noun)
    if not last:
        return 'en'

    # Sammenlign på små bokstaver (case-insensitiv)
    last_lower = last.casefold()
    # Hvis ender med en av nøytrums-endelsene, velg 'et', ellers 'en'
    if any(last_lower.endswith(suf) for suf in NEUTER_SUFFIXES):
        return 'et'
    return 'en'


'''
Formater en liste til naturlig tekst:
    - 0 elementer → ''
    - 1 element  → 'a'
    - 2 elementer → 'a og b'
    - >=3 elementer → 'a, b og c'
'''
def format_list(items: list[str]) -> str:
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f'{items[0]} og {items[1]}'
    else:
        # head = items[:len(items) - 1]
        head = items[:-1]
        # tail = items[len(items) - 1]
        tail = items[-1]
        output_str = f"{', '.join(head)} og {tail}"
        return output_str


# Samler alle gyldige elementer her (uten ledende artikkel)
def main():
    list1 = []
    while True:
        # Brukeren skriver inn ETT element per linje; tom linje avslutter
        raw = input('Vennligst skriv inn ett element om gangen (tom for å avslutte): ').strip()
        if raw == '':
            break

        # Normaliser hvert input
        normalized = normalize_item(raw)
        if normalized != '':
            list1.append(normalized)
        else:
            # Hopper over input som bare var artikkel/symboler/whitespace
            continue

    # Ingen gyldige elementer registrert
    if not list1:
        print('Ingen data.')
    else:
        result = format_list(list1)
        if len(list1) == 1:
            # Velg artikkel kun for én enkelt ting (flertall skal ikke ha artikkel)
            article = choose_article(result)    # Alltid 'en' eller 'et'
            print(f'Elementet er {article} {result}.')
        else:
            print(f'Elementene er {result}.')


if __name__ == '__main__':
    main()
