# Detaljert README.md for O3_The_Rectangle2D_Class:
# https://github.com/yitong-sun/25H_DTE_2510_Prosjekter/blob/main/O3/O3_The_Rectangle2D_Class/README.md

'''
The_Rectangle2D_Class:
Programmet modellerer et aksejustert 2D-rektangel og skriver resultater i tabellform
for bedre lesbarhet. Alle relasjoner og mål presenteres i justerte kolonner.

Eksempel på kjøring:
Enter the center x-coordinate of r1: 0
Enter the center y-coordinate of r1: 0
Enter the width of r1: 20
Enter the height of r1: 10
Enter the center x-coordinate of r2: 4
Enter the center y-coordinate of r2: 4
Enter the width of r2: 10
Enter the height of r2: 5

=== Måltabell ===
+-----------+-------+------+
| Metric    | r1    | r2   |
+-----------+-------+------+
| Area      | 200.0 | 50.0 |
| Perimeter | 60.0  | 30.0 |
+-----------+-------+------+

=== Relasjonstabell ===
+-------------------------------+----------+
| Relasjon                      | Resultat |
+-------------------------------+----------+
| r1 contains the center of r2? | True     |
| r1 contains r2?               | False    |
| r2 in r1?                     | False    |
| r1 overlaps r2?               | True     |
| r1 < r2?                      | False    |
+-------------------------------+----------+

'''

from __future__ import annotations
import math
from dataclasses import dataclass


@dataclass
class _Tol:
    rel: float = 1e-9   #relative tolerance
    abs_tol: float = 1e-12  #absolute tolerance

_TOL = _Tol()

class Rectangle2D:
    '''Representerer et aksejustert rektangel i planet.'''

    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        '''Initialiserer rektangelet ved sentrum, bredde og høyde.

        Args:
            x:      Senterets x-koordinat.
            y:      Senterets y-koordinat.
            width:  Bredde (> 0).
            height: Høyde (> 0).

        '''
        self._x: float = float(x)
        self._y: float = float(y)
        self.width = width
        self.height = height

    @property
    def x(self) -> float:
        '''Henter senterets x-koordinat.

        Returns:
            Senterets x-koordinat.

        '''
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        '''Oppdaterer senterets x-koordinat.

        Args:
            value: Ny x-verdi.

        '''
        self._x = float(value)

    @property
    def y(self) -> float:
        '''Henter senterets y-koordinat.

        Returns:
            Senterets y-koordinat.

        '''
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        '''Oppdaterer senterets y-koordinat.

        Args:
            value: Ny y-verdi.

        '''
        self._y = float(value)

    @property
    def width(self) -> float:
        '''Henter bredden.

        Returns:
            Bredde.

        '''
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        '''Validerer og setter bredden.

        Args:
            value: Ny bredde (> 0).

        '''
        v = float(value)
        if not (v > 0.0):
            raise ValueError("Bredde må være > 0.")
        self._width = v

    @property
    def height(self) -> float:
        '''Henter høyden.

        Returns:
            Høyde.

        '''
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        '''Validerer og setter høyden.

        Args:
            value: Ny høyde (> 0).

        '''
        v = float(value)
        if not (v > 0.0):
            raise ValueError("Høyde må være > 0.")
        self._height = v

    @property
    def area(self) -> float:
        '''Beregner arealet.

        Returns:
            Areal.

        '''
        return self.width * self.height

    def get_area(self) -> float:
        '''Beregner arealet (metodevariant).

        Returns:
            Areal.

        '''
        return self.area

    @property
    def perimeter(self) -> float:
        '''Beregner omkretsen.

        Returns:
            Omkrets.

        '''
        return 2.0 * (self.width + self.height)

    def get_perimeter(self) -> float:
        '''Beregner omkretsen (metodevariant).

        Returns:
            Omkrets.

        '''
        return self.perimeter

    def contains_point(self, px: float, py: float) -> bool:
        '''Sjekker om et punkt ligger inne i rektangelet (inkl. kanter).

        Args:
            px: x-koordinat til punktet.
            py: y-koordinat til punktet.

        Returns:
            True hvis punktet er inne (inkl. kanter), ellers False.

        '''
        half_w = self.width / 2.0
        half_h = self.height / 2.0
        return (abs(px - self.x) <= half_w) and (abs(py - self.y) <= half_h)

    def contains(self, other: "Rectangle2D") -> bool:
        '''Sjekker om et annet rektangel er helt inne i dette (inkl. kanter).

        Args:
            other: Rektangelet som testes mot dette.

        Returns:
            True hvis other er helt inne (inkl. kanter), ellers False.

        '''
        if other.width > self.width or other.height > self.height:
            return False
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return (dx <= (self.width - other.width) / 2.0) and (
            dy <= (self.height - other.height) / 2.0
        )

    def overlaps(self, other: "Rectangle2D") -> bool:
        '''Sjekker om rektanglene overlapper (inkl. rand-berøring).

        Args:
            other: Rektangelet som testes mot dette.

        Returns:
            True hvis de overlapper (inkl. rand-berøring), ellers False.

        '''
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return (dx <= (self.width + other.width) / 2.0) and (
            dy <= (self.height + other.height) / 2.0
        )


    # --- Language interface methods (dunder methods) ---
    def __contains__(self, other: "Rectangle2D") -> bool:
        '''Sjekker om other er inne i dette rektangelet (for `other in self`).'''
        return self.contains(other)

    #1, self == other
    def __eq__(self, other: object) -> bool:
        '''Sammenligner likhet basert på areal (med toleranse).

        Args:
            other: Objektet som sammenlignes.

        Returns:
            True hvis arealene anses like, ellers False.

        '''
        if not isinstance(other, Rectangle2D):
            return NotImplemented
        return math.isclose(self.area, other.area, rel_tol=_TOL.rel, abs_tol=_TOL.abs_tol)

    #2, self < other
    def __lt__(self, other: object) -> bool:
        '''Sjekker om dette rektangelet har mindre areal enn other.

        Args:
            other: Objektet som sammenlignes.

        Returns:
            True hvis dette arealet er (strengt) mindre, ellers False.

        '''
        if not isinstance(other, Rectangle2D):
            return NotImplemented
        if math.isclose(self.area, other.area, rel_tol=_TOL.rel, abs_tol=_TOL.abs_tol):
            return False
        return self.area < other.area

    #3, self <= other
    def __le__(self, other: object) -> bool:
        '''Sjekker mindre-eller-lik basert på areal.

        Args:
            other: Objektet som sammenlignes.

        Returns:
            True hvis mindre-eller-lik, ellers False.

        '''
        if not isinstance(other, Rectangle2D):
            return NotImplemented
        return self < other or self == other

    #4, self > other
    def __gt__(self, other: object) -> bool:
        '''Sjekker om dette rektangelet har større areal enn other.

        Args:
            other: Objektet som sammenlignes.

        Returns:
            True hvis større, ellers False.

        '''
        if not isinstance(other, Rectangle2D):
            return NotImplemented
        return not (self <= other)

    #5, self != other
    def __ne__(self, other: object) -> bool:
        '''Sjekker ulikhet basert på areal (med toleranse).

        Args:
            other: Objektet som sammenlignes.

        Returns:
            True hvis arealene ikke anses like, ellers False.

        '''
        eq = self.__eq__(other)
        if eq is NotImplemented:
            return NotImplemented
        return not eq

    def __repr__(self) -> str:
        '''Genererer en kompakt strengrepresentasjon.

        Returns:
            Tekstlig representasjon.

        '''
        return f'Rectangle2D(x={self.x}, y={self.y}, width={self.width}, height={self.height})'


# ---------- tabellverktøy og hovedprogram med pen utskrift ----------

def print_table(headers: list[str], rows: list[list[str]]) -> None:
    '''Skriver en enkel ASCII-tabell med auto-justerte kolonner.

    Args:
        headers: Liste med kolonneoverskrifter.
        rows:    Rader som lister av strenger.

    Returns:
        Ingenting.

    '''
    # Beregn kolonnebredder fra header + rader
    widths = [len(h) for h in headers]
    for r in rows:
        for i, cell in enumerate(r):
            widths[i] = max(widths[i], len(cell))

    # Hjelpefunksjoner for linjer
    def sep(char_mid: str = '+') -> str:
        parts = ['-' * (w + 2) for w in widths]
        return char_mid + char_mid.join(parts) + char_mid

    def fmt_row(cells: list[str]) -> str:
        padded = [f' {c:<{w}} ' for c, w in zip(cells, widths)]
        return '|' + '|'.join(padded) + '|'

    # Skriv tabell
    print(sep('+'))
    print(fmt_row(headers))
    print(sep('+'))
    for r in rows:
        print(fmt_row(r))
    print(sep('+'))


def _b(value: bool) -> str:
    '''Formatterer bool som 'True'/'False' uten små bokstaver.

    Args:
        value: Boolsk verdi.

    Returns:
        Streng 'True' eller 'False'.

    '''
    return 'True' if value else 'False'




def main() -> None:
    '''Kjører interaktiv test og skriver resultat i tabellform.

    Returns:
        Ingenting.

    '''
    x1 = float(input('Enter the center x-coordinate of r1: '))
    y1 = float(input('Enter the center y-coordinate of r1: '))
    width1 = float(input('Enter the width of r1: '))
    height1 = float(input('Enter the height of r1: '))

    x2 = float(input('Enter the center x-coordinate of r2: '))
    y2 = float(input('Enter the center y-coordinate of r2: '))
    width2 = float(input('Enter the width of r2: '))
    height2 = float(input('Enter the height of r2: '))

    r1 = Rectangle2D(x1, y1, width1, height1)
    r2 = Rectangle2D(x2, y2, width2, height2)

    # Tabell 1: Mål (r1/r2)
    headers1 = ['Metric', 'r1', 'r2']
    rows1 = [
        ['Area',      f'{r1.get_area():.1f}',     f'{r2.get_area():.1f}'],
        ['Perimeter', f'{r1.perimeter:.1f}',      f'{r2.get_perimeter():.1f}'],
    ]
    print('\n=== Måltabell ===')
    print_table(headers1, rows1)

    # Tabell 2: Relasjoner (True/False)
    headers2 = ['Relasjon', 'Resultat']
    rows2 = [
        ['r1 contains the center of r2?', _b(r1.contains_point(r2.x, r2.y))],
        ['r1 contains r2?',               _b(r1.contains(r2))],
        ['r2 in r1?',                     _b(r2 in r1)],
        ['r1 overlaps r2?',               _b(r1.overlaps(r2))],
        ['r1 < r2?',                      _b(r1 < r2)],
    ]
    print('\n=== Relasjonstabell ===')
    print_table(headers2, rows2)

if __name__ == '__main__':
    main()
