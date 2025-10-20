'''
Program: Matrisesystem med tilfeldig utvalg
Beskrivelse:
    Dette programmet genererer en N x N matrise med tilfeldige heltall mellom 0 og 9.
    For hver rad velges et tilfeldig tall, og programmet lager en subliste fra
    dette tallet og ut til slutten av raden.

    Brukeren kan velge å lagre resultatene i en JSON-fil som inneholder metadata
    (matrisestørrelse, seed, og tidsstempel).

Argumenter:
    -n, --size   : Størrelse på matrisen (N)
    --seed       : Tilfeldighetsfrø for reproduserbare resultater
    --save       : Lagre automatisk uten å spørre
    -o, --output : Angi eget filnavn
    --debug      : Slå på detaljert logging


Eksempel på kjøring:
    Oppgi størrelse på matrisen (N): 5

    2025-10-20 15:01:04,634 - main - INFO - Generer matrise N=5
    === Resulater ===
    Rad0: [6, 9, 2, 2, 5],tilfeldig_tall = 2,start_index = 2,subliste = [2, 2, 5]
    Rad1: [0, 1, 7, 2, 0],tilfeldig_tall = 0,start_index = 0,subliste = [0, 1, 7, 2, 0]
    Rad2: [4, 2, 9, 2, 9],tilfeldig_tall = 9,start_index = 2,subliste = [9, 2, 9]
    Rad3: [9, 0, 0, 9, 6],tilfeldig_tall = 9,start_index = 0,subliste = [9, 0, 0, 9, 6]
    Rad4: [4, 7, 7, 5, 6],tilfeldig_tall = 7,start_index = 1,subliste = [7, 7, 5, 6]

    Vil du lagre resultatene til JSON? (y/N): y

    2025-10-20 15:01:08,191 - main - INFO - Resultater skrevet til /Users/yitongsun/PyCharmMiscProject/DTE_2510/results/resultater_20251020_150108.json
    Lagret: /Users/yitongsun/PyCharmMiscProject/DTE_2510/O3/results/resultater_20251020_150108.json
'''

import logging
import random
from datetime import datetime
from pathlib import Path
import argparse
import json
from typing import Any



# ---------- Logging ----------
def setup_logging(debug:bool=False) -> None:
    '''
    Konfigurerer logging for applikasjonen.

    Args:
        debug: Hvis True, settes loggnivå til DEBUG. Ellers brukes INFO.
    '''
    # Setter loggnivå basert på debug-modus
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',)
logger = logging.getLogger('main') # Hovedlogger for hele programmet


# ---------- Config ----------
DEFAULTS: dict[str, Any] = { #here can use dict instead of Dict if python 3.9 or later
    'size': None,   # None = ask interactively
    'seed': None,   # Optional[int], Frø for tilfeldige tall
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
        dict[str, any]: Et ordbokobjekt med innstillinger. Tomt dict hvis filen ikke finnes eller er ugyldig.

    Raises:
        json.JSONDecodeError: Hvis filen finnes men inneholder ugyldig JSON.
    '''
    p = Path(path)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        print(f'Ugyldig JSON i {path}: {e}. Ignorgerer filen.')
        return {}


# ---------- Flett Config ----------
def merge_config(cli: argparse.Namespace, cfg: dict[str, Any], defaults: dict[str, Any]) -> dict[str, Any]:
    '''
    Slår sammen innstillinger fra kommandolinje, konfigurasjonsfil og standardverdier.

    Prioritet: CLI > config.json > defaults.

    Args:
        cli: Argumenter fra kommandolinjen (argparse.Namespace).
        cfg: Verdier hentet fra konfigurasjonsfilen.
        defaults: Standardverdier som brukes hvis andre kilder mangler.

    Returns:
        dict[str, any]: Et ordbokobjekt med sammenslåtte innstillinger.
    '''
    def pick(key: str, cli_value: Any, cfg_value: Any, default_value: Any) -> Any:
        return (
            cli_value
            if cli_value is not None
            else (cfg_value if cfg_value is not None else default_value)
        )

    merged: dict[str, any] = {
        # .get() → Brukes når du ikke er sikker på om nøkkelen finnes.
        # [...] → Brukes når du er sikker på at nøkkelen finnes.
        'size': pick('size', cli.size, cfg.get('size'), defaults['size']),
        'seed': pick('seed', cli.seed, cfg.get('seed'), defaults['seed']),
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
    return [[random.randint(0, 9) for _ in range(N)] for _ in range(N)]



def behandle_rad(rad: list[int]) -> tuple[int, int, list[int]]:
    '''
    Velger et tilfeldig tall fra raden og lager en subliste fra og med dette tallet.

    Args:
        rad (list[int]): En rad med heltall.

    Returns:
        tuple[int, int, list[int]]: (tilfeldig_tall, start_index, subliste)
    '''
    tilfeldig_tall = random.choice(rad)
    start_index = rad.index(tilfeldig_tall)
    subliste = [rad[j] for j in range(len(rad)) if j >= start_index]
    return tilfeldig_tall, start_index, subliste



def behandle_matrise(matrise: list[list[int]]) -> list[dict]:
    '''
    Behandler matrisen og returnerer resultater for hver rad.

    Args:
        matrise: En liste av rader med heltall.

    Returns:
        En liste med resultater per rad.
    '''
    resultater = []
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


def skriv_resultater(resultater: list[dict]) -> None:
    '''
    Skriver resultatene til konsollen på en lesbar måte.

    Args:
        resultater: En liste med resultater fra behandle_matrise().
    '''
    for r in resultater:
        print(
            f"Rad{r['radnummer']}: {r['rad']},"
            f"tilfeldig_tall = {r['tilfeldig_tall']},"
            f"start_index = {r['start_index']},"
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


def lagre_til_json(resultater: list[dict], filnavn:str | Path, N: int, seed: int | None) -> Path :
    '''
    Lagrer resultatene i en JSON-fil med metadata (N, seed, timestamp).

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
            'seed': seed,
            'timestamp': datetime.now().strftime('%Y%m%d_%H%M%S'),
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
        description='Generer matrise og lag sublister for her rad.'
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

    return p



# ---------- Hovedfunksjon ----------
def main() -> None:
    '''
    Kjør hovedflyten: parse konfig, generer matrise, prosesser og (valgfritt) lagre.
    '''
    # 1) Parse og flett konfig (CLI > config.json > DEFAULTS)
    cli = build_parser().parse_args()
    cfg = merge_config(cli, load_config('config.json'), DEFAULTS)

    # 2) Logging og valgfri seed
    setup_logging(bool(cfg.get('debug')))
    logger.debug('Effektiv konfig: %r', cfg)

    # 3) Sett frø hvis gitt
    seed = cfg.get('seed')
    if seed is not None:
        random.seed(seed)
        logger.info('Bruker seed=%s', seed)

    # 4) Finn N (interaktivt hvis ikke oppgitt)
    size = cfg.get('size')
    if size is None:
        N = hent_brukerinput()
    else:
        N = int(size)
        if N <= 0:
            print('Ugyldig verdi! N må være et positivt heltall.')
            print("Oppgi en ny verdi interaktivt i stedet.\n")
            N = hent_brukerinput()

    # 5) Generer, behandle og skriv ut
    logger.info('Generer matrise N=%d', N)
    matrise = generer_matrise(N)
    resultater = behandle_matrise(matrise)

    print('\n=== Resulater ===')
    skriv_resultater(resultater)

    # 5) Valgfri lagring
    skal_lagre = bool(cfg.get('save'))
    if not skal_lagre:
        svar = input('\nVil du lagre resultatene til JSON? (y/N): ').strip().lower()
        skal_lagre = (svar == 'y')

    if not skal_lagre:
        print('\n(ikke lagret)')
        return

    # Opprett lagringsmappe
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)

    # Bruk angitt filnavn eller generer nytt
    if cfg.get('output'):
        filnavn = output_dir / cfg['output']
    else:
        filnavn = output_dir / lag_timestamp_navn(prefix='resultater', ext='.json')

    path = lagre_til_json(resultater, filnavn, N, seed)
    logger.info('Resultater skrevet til %s', path.resolve())
    print(f'\nLagret: {path.resolve()}')



if __name__ == '__main__':
    main()
