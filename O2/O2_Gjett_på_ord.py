'''
Program: Gjett på ord
----------------------------------------------------
Dette programmet velger et ord tilfeldig fra en standard(default) ordliste
eller en txt. fil, og lar brukeren gjette bokstaver til hele ordet er avslørt.
Programmet:
  - viser ordet som '*' for hver bokstav (f.eks. '***')
  - godtar kun én bokstav av gangen (inkl. norske æ/ø/å)
  - avslører ALLE forekomster av en riktig gjettet bokstav
  - behandler gjentatte/ulovlige innput og ber om ny bokstav
  - avslutter når hele ordet er gjettet
I debug-modus (main(debug=True)) settes random.seed(0) for forutsigbarhet.


Eksempel på kjøring: (forutsigbart)
Gjett ordet: ***
Skriv inn en bokstav: u
Riktig!

Gjett ordet: u**
Skriv inn en bokstav: q
Ingen treff.

Gjett ordet: u**
Skriv inn en bokstav: q
Du har allerede gjettet den bokstaven.

Gjett ordet: u**
Skriv inn en bokstav: 3
Vennligst skriv inn en enkelt bokstav.

Gjett ordet: u**
Skriv inn en bokstav: i
Riktig!

Gjett ordet: ui*
Skriv inn en bokstav: t
Riktig!

Gjett ordet: uit
Gratulerer! Du har gjettet ordet.
'''
import random
import re
import os

# Standard ordliste brukt når fil ikke finnes/er tom eller etter lengdefilter
default_words = [
    'java', 'python', 'matlab', 'golang', 'c', 'javascript',
    'uit', 'datateknikk', 'først', 'år', 'student',
    'kode', 'algoritme', 'program', 'lekser', 'lærer',
    'matrise', 'liste', 'streng', 'funksjon', 'klasse',
    'løkken', 'fil', 'server', 'modell', 'system'
]

# Regex som definerer gyldige bokstaver (inkludert ÆØÅ/æøå)
words_re = re.compile(r'^[A-Za-zÆØÅæøå]+$')


'''
Leser ord fra fil 'path', filtrerer på [A-Za-zÆØÅæøå]+ og lengde [min_len,max_len],
normaliserer til små bokstaver og returnerer sortert liste uten duplikater.
'''
def build_wordlists_from_file(path: str, min_len=3, max_len=4):
    wordlist = set() #sett, ingen duplikater
    try:
        # 'utf-8' inkluderer ÆØÅ/æøå    #'open' lukker filer automatisk
        with open(path, encoding='utf-8') as wordfile:
            for line in wordfile:
                #Finn alle ord i linjen
                for token in re.findall('[A-Za-zÆØÅæøå]+', line):
                    word_found = token.lower()
                    # Lengdefilter # bokstavsjekk
                    if min_len <= len(word_found) <= max_len and words_re.fullmatch(word_found):
                        wordlist.add(word_found)
    # Varsel, og faller tilbake til tom liste (som senere gir default_words)
    except (OSError, UnicodeDecodeError) as e:
        print(f"[WARNING] Lesefeil for {path}: {e}")
        return []

    return sorted(wordlist)  #wordlist er en sett og sorteres til en liste uten duplikater


'''
Returnerer en sortert liste med ord:
1) fra fil (hvis den finnes, returneres det filtrerte innholdet)
I dette eksemplet er det ingen fil, men man kan legge til filene man vil senere.
2) Ellers, fra standardord (default_word) (filtrert etter lengde).
'''
def get_wordlist(min_len=3, max_len=4, filename: str = 'ordliste.txt'):
    if os.path.exists(filename):
        wordlist = build_wordlists_from_file(filename, min_len, max_len)
        if wordlist:
            return wordlist

    return sorted({w for w in default_words if min_len <= len(w) <= max_len})


'''
Gitt ordet, den nåværende maskeringen (f.eks. '**a*') og en bokstav,  
returner en ny maskering der bokstaven vises på alle riktige plasser.
'''
def update_guessed_word(chosen_word: str, guessed: str, letter: str) -> str:
    result = []
    for i in range(len(chosen_word)):
        if chosen_word[i] == letter:
            result.append(chosen_word[i]) # avslør korrekt bokstav
        else:
            result.append(guessed[i]) # behold eksisterende maskering
    return ''.join(result)


'''
Kjører selve gjette-loopen. Hvis chosen_word er None, 
velges et tilfeldig ord fra en fil eller default_words.
Viser maskert ord, validerer input, håndterer duplikate bokstaver og gir tilbakemeldinger.
'''
def check_guess(chosen_word: str | None = None):
    if chosen_word is None:
        wordlist = get_wordlist()
        chosen_word = random.choice(wordlist)

    guessed = '*' * len(chosen_word) # start med full maskering
    seen = set()                    # bokstaver som allerede er gjettet

    while '*' in guessed:           # fortsett til hele ordet er avslørt
        print(f'Gjett ordet: {guessed}')
        letter = input('Skriv inn en bokstav: ').strip().lower()

        # Avvis alt som ikke er nøyaktig én bokstav
        if not words_re.fullmatch(letter) or len(letter) != 1:
            print('Vennligst skriv inn en enkelt bokstav.\n')
            continue
        # Avvis gjentatt bokstav
        if letter in seen:
            print('Du har allerede gjettet den bokstaven.\n')
            continue

        seen.add(letter)            # Registrer ny bokstav
        count = guessed.count('*') # antall skjulte før oppdatering
        guessed = update_guessed_word(chosen_word, guessed, letter)

        # Tilbakemelding basert på endring i antall skjulte
        if guessed.count('*') < count:
            print('Riktig!\n')
        else:
            print('Ingen treff.\n')

    # Hele ordet er gjettet
    print(f'Gjett ordet: {guessed}')
    print('Gratulerer! Du har gjettet ordet.\n')


'''
main program
I debug-modus settes seed for forutsigbar kjøring.
chosen_word kan settes som et fast ord.
'''
def main(debug: bool = False):
    # Hvis debug=True er det alltid samme "tilfeldige" resultat
    if debug:
        random.seed(0)  # gjør resultatet forutsigbart (nyttig for testing)
        # check_guess(chosen_word='java')
    # else:
    #     check_guess()
    check_guess()


if __name__ == "__main__":
    # Velg om du vil ha forutsigbart eller ekte tilfeldig
    main(debug=True)  # fast resultat
    # main(debug=False)  # ekte tilfeldig
