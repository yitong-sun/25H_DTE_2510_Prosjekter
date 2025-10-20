'''
Program: Matrisesystem med tilfeldig utvalg
Beskrivelse:
    Dette programmet genererer en N x N matrise med tilfeldige heltall mellom 0 og 9.
    For hver rad velges et tilfeldig tall, og programmet lager en subliste fra
    dette tallet og ut til slutten av raden.

    Brukeren kan velge å lagre resultatene i en JSON-fil som inneholder metadata
    (matrisestørrelse, random_seed, og tidsstempel).

Argumenter:
    -n, --size   : Størrelse på matrisen (N)
    --seed       : Tilfeldighetsfrø for reproduserbare resultater
    --save       : Lagre automatisk uten å spørre
    -o, --output : Angi eget filnavn
    --debug      : Slå på detaljert logging

Oppsummering av kjøringer：
1. Ren terminalinteraksjon + bekreftet lagring
2. Ikke-interaktiv kjøring lagrer direkte (-n 5 --save)
3. Ugyldig N → interaktiv korrigering
4. Ikke-interaktiv + ugyldig N → kontrollert avslutning
5. Relativt filnavn lagres i `results/`
6. Absolutt sti lagres uendret (f.eks. Desktop)


Eksempel 1 på kjøring:
    Oppgi størrelse på matrisen (N): 5

    2025-10-20 15:01:04,634 - main - INFO - Generer matrise N=5
    === Resultater ===
    Rad0: [6, 9, 2, 2, 5],tilfeldig_tall = 2,start_index = 2,subliste = [2, 2, 5]
    Rad1: [0, 1, 7, 2, 0],tilfeldig_tall = 0,start_index = 0,subliste = [0, 1, 7, 2, 0]
    Rad2: [4, 2, 9, 2, 9],tilfeldig_tall = 9,start_index = 2,subliste = [9, 2, 9]
    Rad3: [9, 0, 0, 9, 6],tilfeldig_tall = 9,start_index = 0,subliste = [9, 0, 0, 9, 6]
    Rad4: [4, 7, 7, 5, 6],tilfeldig_tall = 7,start_index = 1,subliste = [7, 7, 5, 6]

    Vil du lagre resultatene til JSON? (y/N): y

    2025-10-20 15:01:08,191 - main - INFO - Resultater skrevet til /Users/yitongsun/PyCharmMiscProject/DTE_2510/results/resultater_20251020_150108.json
    Lagret: /Users/yitongsun/PyCharmMiscProject/DTE_2510/O3/results/resultater_20251020_150108.json

Eksempel 2 på kjøring:
    (.venv) yitongsun@YitongdeMacBook-Air O3_Subliste % python O3_Subliste.py -n 5 --save
    2025-10-20 21:46:52,346 - main - INFO - Generer matrise N=5

    === Resultater ===
    Rad0: [0, 0, 5, 2, 2], tilfeldig_tall = 2, start_index = 3, subliste = [2, 2]
    Rad1: [2, 6, 4, 9, 7], tilfeldig_tall = 9, start_index = 3, subliste = [9, 7]
    Rad2: [2, 8, 4, 6, 3], tilfeldig_tall = 8, start_index = 1, subliste = [8, 4, 6, 3]
    Rad3: [3, 6, 2, 3, 7], tilfeldig_tall = 2, start_index = 2, subliste = [2, 3, 7]
    Rad4: [2, 2, 4, 2, 6], tilfeldig_tall = 2, start_index = 0, subliste = [2, 2, 4, 2, 6]
    2025-10-20 21:46:52,346 - main - INFO - Resultater skrevet til /Users/yitongsun/PyCharmMiscProject/25H_DTE_2510/O3/O3_Subliste/results/resultater_20251020_214652.json

    Lagret: /Users/yitongsun/PyCharmMiscProject/25H_DTE_2510/O3/O3_Subliste/results/resultater_20251020_214652.json

Eksempel 3 på kjøring:
    (.venv) yitongsun@YitongdeMacBook-Air O3_Subliste % python O3_Subliste.py -n 0
    Ugyldig verdi! N må være et positivt heltall.
    Oppgi en ny verdi interaktivt i stedet.

    Oppgi størrelse på matrisen (N):

    Kontinuering som Eksempel 1.

Eksempel 4 på kjøring:
    (.venv) yitongsun@YitongdeMacBook-Air O3_Subliste % python O3_Subliste.py -n 0 --no-interactive
    Ugyldig verdi! N må være et positivt heltall.
    Avslutter fordi interaktiv modus er deaktivert.

Eksempel 5 på kjøring:
    (.venv) yitongsun@YitongdeMacBook-Air O3_Subliste % python O3_Subliste.py -n 5 -o foo.json
    2025-10-20 21:53:05,414 - main - INFO - Generer matrise N=5

    === Resultater ===
    Rad0: [9, 3, 4, 3, 5], tilfeldig_tall = 5, start_index = 4, subliste = [5]
    Rad1: [3, 3, 3, 8, 8], tilfeldig_tall = 3, start_index = 0, subliste = [3, 3, 3, 8, 8]
    Rad2: [9, 6, 0, 3, 9], tilfeldig_tall = 0, start_index = 2, subliste = [0, 3, 9]
    Rad3: [3, 8, 6, 9, 2], tilfeldig_tall = 2, start_index = 4, subliste = [2]
    Rad4: [1, 5, 5, 0, 0], tilfeldig_tall = 1, start_index = 0, subliste = [1, 5, 5, 0, 0]

    Vil du lagre resultatene til JSON? (y/N): y
    2025-10-20 21:53:10,424 - main - INFO - Resultater skrevet til /Users/yitongsun/PyCharmMiscProject/25H_DTE_2510/O3/O3_Subliste/results/foo.json

    Lagret: /Users/yitongsun/PyCharmMiscProject/25H_DTE_2510/O3/O3_Subliste/results/foo.json

Eksempel 6 på kjøring:
    (.venv) yitongsun@YitongdeMacBook-Air O3_Subliste % python O3_Subliste.py -n 5 -o /Users/yitongsun/Desktop/foo.json
    2025-10-20 21:59:23,318 - main - INFO - Generer matrise N=5

    === Resultater ===
    Rad0: [1, 8, 4, 9, 0], tilfeldig_tall = 1, start_index = 0, subliste = [1, 8, 4, 9, 0]
    Rad1: [1, 9, 5, 1, 8], tilfeldig_tall = 5, start_index = 2, subliste = [5, 1, 8]
    Rad2: [8, 3, 2, 3, 1], tilfeldig_tall = 2, start_index = 2, subliste = [2, 3, 1]
    Rad3: [5, 1, 1, 3, 5], tilfeldig_tall = 1, start_index = 1, subliste = [1, 1, 3, 5]
    Rad4: [2, 7, 9, 9, 8], tilfeldig_tall = 9, start_index = 2, subliste = [9, 9, 8]

    Vil du lagre resultatene til JSON? (y/N): y
    2025-10-20 21:59:26,035 - main - INFO - Resultater skrevet til /Users/yitongsun/Desktop/foo.json

    Lagret: /Users/yitongsun/Desktop/foo.json
'''

import logging
import random as rnd
from random import randint, choice
from datetime import datetime
from pathlib import Path
import argparse
import json
from typing import Any


# Modulnavngitt logger. Bruker root-handlere konfigurert i setup_logging().
logger = logging.getLogger('main')

# ---------- Logging ----------
def setup_logging(debug: bool = False) -> None:
    """
    Konfigurerer logging for applikasjonen.

    Args:
        debug: Hvis True, settes loggnivå til DEBUG. Ellers brukes INFO.
    """
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        # Sikrer at tidligere handlere erstattes slik at vi ikke får duplisert logging.
        force=True
    )

# ---------- Config ----------
DEFAULTS: dict[str, Any] = { #here can use dict instead of Dict if python 3.9 or later
    'size': None,   # None = ask interactively
    'random_seed': None,   # Optional[int], Frø for tilfeldige tall
    'save': False,
    'output': None, # Filnavn genereres hvis None
    'debug': False  # Slår av debug som standard
}

# ---------- Last Config ----------
def load_config(path: str = 'config.json') -> dict[str, Any]:
    '''
    Leser konfigurasjon fra en JSON-fil hvis den finnes.

    Args:
        path: Filstien til konfigurasjonsfilen (standard er 'config.json').

    Returns:
        dict[str, Any]: Et ordbokobjekt med innstillinger.
        Hvis filen ikke finnes eller inneholder ugyldig JSON, returneres {}.
        Hendelsen logges som en advarsel, og programmet fortsetter.
    '''
    p = Path(path)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        logger.warning('Ugyldig JSON i %s: %s. Ignorerer filen.', path, e)
        return {}

# ---------- Flett Config ----------
def merge_config(cli: argparse.Namespace,
                 cfg: dict[str, Any],
                 defaults: dict[str, Any]) -> dict[str, Any]:
    '''
    Slår sammen innstillinger fra kommandolinje, konfigurasjonsfil og standardverdier.

    Prioritet: CLI > config.json > defaults.

    Args:
        cli: Argumenter fra kommandolinjen (argparse.Namespace).
        cfg: Verdier hentet fra konfigurasjonsfilen.
        defaults: Standardverdier som brukes hvis andre kilder mangler.

    Returns:
        dict[str, Any]: Et ordbokobjekt med sammenslåtte innstillinger.
    '''
    def pick(key: str, cli_value: Any, cfg_value: Any, default_value: Any) -> Any:
        return (
            cli_value
            if cli_value is not None
            else (cfg_value if cfg_value is not None else default_value)
        )

    merged: dict[str, Any] = {
        # .get() → Brukes når du ikke er sikker på om nøkkelen finnes.
        # [...] → Brukes når du er sikker på at nøkkelen finnes.
        'size': pick('size', cli.size, cfg.get('size'), defaults['size']),
        'random_seed': pick('random_seed',
                            getattr(cli, 'seed', None),
                            cfg.get('random_seed') or cfg.get('seed'),
                            defaults['random_seed']),
        'save': pick('save', cli.save, cfg.get('save'), defaults['save']),
        'output': pick('output', cli.output, cfg.get('output'), defaults['output']),
        'debug': pick('debug', cli.debug, cfg.get('debug'), defaults['debug']),
    }

    return merged


def generer_matrise(N: int) -> list[list[int]]:
    '''
    Generer en N x N matrise med tilfeldige heltall mellom 0 og 9.

    Args:
         N (int): Størrelsen på matrisen.

    Returns:
         list[list[int]]: En NxN matrise med tilfeldige heltall fra 0 til 9.
    '''
    return [[randint(0, 9) for _ in range(N)] for _ in range(N)]


def behandle_rad(rad: list[int]) -> tuple[int, int, list[int]]:
    '''
    Velger et tilfeldig tall fra raden og lager en subliste fra og med dette tallet.

    Args:
        rad (list[int]): En rad med heltall.

    Returns:
        tuple[int, int, list[int]]: (tilfeldig_tall, start_index, subliste)
    '''
    tilfeldig_tall = choice(rad)
    start_index = rad.index(tilfeldig_tall)
    subliste = [rad[j] for j in range(len(rad)) if j >= start_index]
    return tilfeldig_tall, start_index, subliste



def behandle_matrise(matrise: list[list[int]]) -> list[dict[str, Any]]:
    '''
    Behandler matrisen og returnerer resultater for hver rad.

    Args:
        matrise: En liste av rader med heltall.

    Returns:
        En liste med resultater per rad.
    '''
    resultater: list[dict[str, Any]] = []
    for i, rad in enumerate(matrise):
        # enumerate() gir (indeks, rad)
        t, idx, sub = behandle_rad(rad)
        logger.debug('Rad %d = %r, valgt = %s, start = %d, sub = %r',
                     i, rad, t, idx, sub)
        # Hvis variabelen er en kompleks struktur (list, dict, object) → bruk %r
        # Hvis variabelen er en enkel verdi (int, str) → bruk %s

        resultater.append({
            'radnummer': i,
            'rad': rad,
            'tilfeldig_tall': t,
            'start_index': idx,
            'subliste': sub
        })
    return resultater


def skriv_resultater(resultater: list[dict[str, Any]]) -> None:
    '''
    Skriver resultatene til konsollen på en lesbar måte.

    Args:
        resultater: En liste med resultater fra behandle_matrise().
    '''
    for r in resultater:
        print(
            f"Rad{r['radnummer']}: {r['rad']}, "
            f"tilfeldig_tall = {r['tilfeldig_tall']}, "
            f"start_index = {r['start_index']}, "
            f"subliste = {r['subliste']}"
        )


def lag_timestamp_navn(prefix:str = 'resultater', ext: str = '.json') -> str:
    '''
    Lager et unikt filnavn med tidsstempel.

    Args:
        prefix: Prefiks for filnavnet.
        ext: Filtype/utvidelse, f.eks. '.json'.

    Returns:
        Et filnavn på formatet 'prefix_YYYYMMDD_HHMMSS.ext'.
    '''
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f'{prefix}_{ts}{ext}'


def lagre_til_json(resultater: list[dict[str, Any]],
                   filnavn:str | Path,
                   N: int,
                   random_seed: int | None) -> Path :
    '''
    Lagrer resultatene i en JSON-fil med metadata (N, random_seed, timestamp).

    Args:
        resultater: Liste med resultater fra behandlingen.
        filnavn: Navnet på JSON-filen som skal opprettes.
        N: Størrelsen på matrisen.
        seed: Brukt tilfeldig frø (kan være None).

    Returns:
        Path: Stien til den lagrede filen.
    '''
    path = Path(filnavn)

    # Opprett katalogen hvis den ikke finnes
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)

    data = {
        'metadata': {
            'N': N,
            'random_seed': random_seed,
            # ISO 8601 med tidssone, sekundoppløsning
            'timestamp': datetime.now().astimezone().isoformat(timespec='seconds'),
        },
        'resultater': resultater
    }

    # Skriver JSON med norsk tegnstøtte og pen formatering
    path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding='utf-8')
    return path


# ---------- Interaktiv input ----------
def hent_brukerinput() -> int:
    '''
    Ber brukeren oppgi en gyldig heltallsverdi for N.

    Returns:
        Et positivt heltall som representerer matrisestørrelsen.
    '''
    while True:
        try:
            N = int(input('Oppgi størrelse på matrisen (N): '))
            if N <= 0:
                print('Ugyldig verdi! N må være et positivt heltall.\n')
            else:
                return N

        except ValueError:
            print('Ugyldig input! Du må skrive et heltall.\n')


# ----------Bygg CLI ----------
def build_parser() -> argparse.ArgumentParser:
    '''
    Bygger en argumentparser for kommandolinjegrensesnittet (CLI).

    Returns:
        argparse.ArgumentParser: Parser for programargumentene.
    '''
    p = argparse.ArgumentParser(
        description='Generer matrise og lag sublister for hver rad.'
    )

    p.add_argument(
        '-n', '--size',
        type=int,
        default=None,
        help='Størrelse N. Hvis ikke oppgitt, spørres brukeren interaktivt.'
    )

    p.add_argument(
        '--seed',
        type=int,
        help='Tilfeldighetsfrø for reproduserbarhet.'
    )

    p.add_argument(
        '--save',
        action='store_true',
        help='Lagre resultater til JSON uten å spørre.'
    )

    p.add_argument(
        '-o', '--output',
        help='Utdatafil (default: resultater_YYYYMMDD_HHMMSS.json).'
    )

    p.add_argument(
        '--debug',
        action='store_true',
        help='Vis debug-logging.'
    )

    p.add_argument(
        '--no-interactive',
        action='store_true',
        help='Deaktiver interaktiv input. Krever at -n/--size oppgis.'
    )

    return p


def run_pipeline(N: int, random_seed: int | None, logger: logging.Logger) -> dict[str, Any]:
    '''
    Kjør den rene beregningspipen: valgfritt sett RNG-frø, generer matrise og behandle.

    Args:
        N: Matrisestørrelse.
        random_seed: Frø for random (kan være None).
        logger: Logger for debug/info.

    Returns:
        dict med nøkler:
            'N': int,
            'random_seed': int | None,
            'matrise': list[list[int]],
            'resultater': list[dict[str, Any]]
    '''
    if random_seed is not None:
        rnd.seed(random_seed)
        logger.debug('Pipeline bruker random_seed=%s', random_seed)

    matrise = generer_matrise(N)
    resultater = behandle_matrise(matrise)

    return {
        'N': N,
        'random_seed': random_seed,
        'matrise': matrise,
        'resultater': resultater,
    }


# ---------- Hovedfunksjon ----------
def main() -> None:
    '''
    Kjør hovedflyten: parse konfig, generer matrise, prosesser og (valgfritt) lagre.
    '''
    # 1) Parse og flett konfig (CLI > config.json > DEFAULTS)
    cli = build_parser().parse_args()
    cfg = merge_config(cli, load_config('config.json'), DEFAULTS)

    # 2) Logging
    setup_logging(bool(cfg.get('debug')))
    logger.debug('Effektiv konfig: %r', cfg)

    # 3) Finn N (interaktivt hvis ikke oppgitt)
    size = cfg.get('size')
    no_interactive = bool(getattr(cli, 'no_interactive', False))

    if size is None:
        # Ikke tillat interaksjon hvis --no-interactive eller stdin ikke er TTY (teletypewriter)
        if no_interactive:
            raise SystemExit(
                'Størrelsen (N) mangler. Kjør med -n/--size eller fjern --no-interactive.'
            )
        try:
            N = hent_brukerinput()
        except (EOFError, OSError):
            raise SystemExit('Størrelsen (N) mangler, og interaktiv input er ikke tilgjengelig. Kjør med -n/--size.')
    else:
        N = int(size)
        if N <= 0:
            print('Ugyldig verdi! N må være et positivt heltall.')
            if no_interactive:
                raise SystemExit('Avslutter fordi interaktiv modus er deaktivert.')
            try:
                print('Oppgi en ny verdi interaktivt i stedet.\n')
                N = hent_brukerinput()
            except (EOFError, OSError):
                raise SystemExit('Interaktiv input er ikke tilgjengelig. Oppgi en gyldig -n/--size.')

    # 4) Les random_seed og kjør pipeline (REN beregning)
    random_seed = cfg.get('random_seed')
    logger.info('Generer matrise N=%d', N)
    pipe = run_pipeline(N, random_seed, logger)
    matrise = pipe['matrise']   # (ikke brukt videre nå, men greit å eksponere om ønskelig)
    resultater = pipe['resultater']

    # 5) Skriv ut
    print('\n=== Resultater ===')
    skriv_resultater(resultater)

    # 6) Valgfri lagring
    skal_lagre = bool(cfg.get('save'))
    if not skal_lagre:
        svar = input('\nVil du lagre resultatene til JSON? (y/N): ').strip().lower()
        skal_lagre = (svar == 'y')

    if not skal_lagre:
        print('\n(ikke lagret)')
        return

    # 7) Bestem utdatafil
    # Opprett lagringsmappe
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)
    # Bruk angitt filnavn eller generer nytt
    if cfg.get('output'):
        given = Path(cfg['output'])
        # Absolutt sti eller relativ sti som inneholder katalogdeler: bruk den som den er (respekter brukerens valg).
        if given.is_absolute() or len(given.parts) > 1:
            filnavn = given
        else:
            filnavn = output_dir / given
    else:
        filnavn = output_dir / lag_timestamp_navn(prefix='resultater', ext='.json')

    # 8) Lagre
    path = lagre_til_json(resultater, filnavn, N, random_seed)
    logger.info('Resultater skrevet til %s', path.resolve())
    print(f'\nLagret: {path.resolve()}')



if __name__ == '__main__':
    main()
