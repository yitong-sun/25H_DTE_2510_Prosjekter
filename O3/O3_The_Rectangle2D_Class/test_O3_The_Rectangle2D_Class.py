
"""
Kort introduksjon:
Testfil for O3_The_Rectangle2D_Class. Verifiserer areal/omkrets, punkt/rek­tangel-
relasjoner (inneholder/overlapper), operatorer (__contains__, sammenligning),
samt validering av bredde/høyde. Testene bruker unittest og følger enkle,
lesbare sjekkpunkter med subTest der det er hensiktsmessig.
"""

from __future__ import annotations

import math
import unittest

# Anta at klassen ligger i O3_The_Rectangle2D_Class.py i samme mappe:
from O3_The_Rectangle2D_Class import Rectangle2D  # noqa: E402


_TOL_REL = 1e-9
_TOL_ABS = 1e-12


def _close(a: float, b: float) -> bool:
    """Sjekker om to flyttall er tilnærmet like.

    Args:
        a: Første verdi.
        b: Andre verdi.

    Returns:
        True hvis verdiene er tilnærmet like gitt toleranse, ellers False.

    """
    return math.isclose(a, b, rel_tol=_TOL_REL, abs_tol=_TOL_ABS)


class TestRectangle2D(unittest.TestCase):
    """Samler enhetstester for Rectangle2D."""

    def setUp(self) -> None:
        """Forbereder standard rektangler brukt i flere tester.

        Returns:
            Ingenting.

        """
        # Symmetrisk “basis”-rektangel 4x4 i origo
        self.r_base = Rectangle2D(0.0, 0.0, 4.0, 4.0)
        # Mindre rektangel 2x2 i origo (helt inne i r_base)
        self.r_small = Rectangle2D(0.0, 0.0, 2.0, 2.0)
        # Samme størrelse som r_base men forskjøvet på x slik at de berører i kanten
        self.r_touch = Rectangle2D(4.0, 0.0, 4.0, 4.0)  # høyrekant r_base møter venstrekant r_touch
        # Et rektangel som ikke overlapper med r_base
        self.r_far = Rectangle2D(10.0, 0.0, 2.0, 2.0)

    # ------------------- Grunnleggende mål -------------------

    def test_area_and_perimeter(self) -> None:
        """Beregner og verifiserer areal og omkrets.

        Returns:
            Ingenting.

        """
        self.assertTrue(_close(self.r_base.get_area(), 16.0))
        self.assertTrue(_close(self.r_base.area, 16.0))
        self.assertTrue(_close(self.r_base.get_perimeter(), 16.0))
        self.assertTrue(_close(self.r_base.perimeter, 16.0))

        self.assertTrue(_close(self.r_small.area, 4.0))
        self.assertTrue(_close(self.r_small.perimeter, 8.0))

    # ------------------- Punkt-inkludering -------------------

    def test_contains_point_center_and_edges(self) -> None:
        """Sjekker punkt-inkludering for sentrum, kanter og utenfor.

        Returns:
            Ingenting.

        """
        r = self.r_base  # 4x4 rundt (0,0): halv-bredde/-høyde = 2
        # Sentrum
        self.assertTrue(r.contains_point(0.0, 0.0))
        # Midt på kanter (inkluderer kanter → True)
        with self.subTest("Edge right"):
            self.assertTrue(r.contains_point(2.0, 0.0))
        with self.subTest("Edge left"):
            self.assertTrue(r.contains_point(-2.0, 0.0))
        with self.subTest("Edge top"):
            self.assertTrue(r.contains_point(0.0, 2.0))
        with self.subTest("Edge bottom"):
            self.assertTrue(r.contains_point(0.0, -2.0))
        # Like utenfor kanten
        with self.subTest("Outside"):
            self.assertFalse(r.contains_point(2.0000001, 0.0))

    # ------------------- Rektangel-inkludering -------------------

    def test_contains_rectangle_true_and_false(self) -> None:
        """Verifiserer at et rektangel kan inneholde et annet (inkl. kanter).

        Returns:
            Ingenting.

        """
        # r_base inneholder r_small
        self.assertTrue(self.r_base.contains(self.r_small))
        # r_small inneholder ikke r_base
        self.assertFalse(self.r_small.contains(self.r_base))
        # Når de kun berører i kanten: r_base inneholder ikke r_touch (ikke helt inne)
        self.assertFalse(self.r_base.contains(self.r_touch))

    # ------------------- Overlapp -------------------

    def test_overlaps_cases_inclusive_edges(self) -> None:
        """Sjekker overlapp i ulike scenarier (inkl. rand-berøring som overlapp).

        Returns:
            Ingenting.

        """
        # Fullt overlapp (det lille inni det store)
        self.assertTrue(self.r_base.overlaps(self.r_small))
        # Rand-berøring regnes som overlapp i vår definisjon
        self.assertTrue(self.r_base.overlaps(self.r_touch))
        # Tydelig separasjon
        self.assertFalse(self.r_base.overlaps(self.r_far))

    # ------------------- __contains__ (in-operator) -------------------

    def test_in_operator_matches_contains(self) -> None:
        """Sjekker at `other in self` samsvarer med contains(self, other).

        Returns:
            Ingenting.

        """
        # r_small er inne i r_base
        self.assertTrue(self.r_small in self.r_base)
        # r_base er ikke inne i r_small
        self.assertFalse(self.r_base in self.r_small)
        # Berøring i kant → ikke “inne”
        self.assertFalse(self.r_touch in self.r_base)

    # ------------------- Sammenligning på areal -------------------

    def test_area_comparisons(self) -> None:
        """Sammenligner rektangler på areal med toleranse.

        Returns:
            Ingenting.

        """
        # areal(r_base)=16, areal(r_small)=4
        self.assertTrue(self.r_base > self.r_small)
        self.assertTrue(self.r_small < self.r_base)
        self.assertTrue(self.r_base >= self.r_small)
        self.assertTrue(self.r_small <= self.r_base)
        self.assertTrue(self.r_base != self.r_small)
        self.assertFalse(self.r_base == self.r_small)

        # Like areal: lag et nytt rektangel med samme areal som r_base
        r_same_area = Rectangle2D(1.0, 1.0, 8.0, 2.0)  # 16.0 areal
        self.assertTrue(self.r_base == r_same_area)
        self.assertFalse(self.r_base < r_same_area)
        self.assertFalse(self.r_base > r_same_area)
        self.assertTrue(self.r_base <= r_same_area)
        self.assertTrue(self.r_base >= r_same_area)
        self.assertFalse(self.r_base != r_same_area)

    # ------------------- Validering av input -------------------

    def test_invalid_dimensions_raise(self) -> None:
        """Validerer at bredde/høyde må være > 0.

        Returns:
            Ingenting.

        """
        with self.assertRaises(ValueError):
            Rectangle2D(0.0, 0.0, 0.0, 1.0)
        with self.assertRaises(ValueError):
            Rectangle2D(0.0, 0.0, 1.0, 0.0)
        # Setter via properties skal også feile for ikke-positive verdier
        r = Rectangle2D(0.0, 0.0, 1.0, 1.0)
        with self.assertRaises(ValueError):
            r.width = -3.0
        with self.assertRaises(ValueError):
            r.height = 0.0


if __name__ == "__main__":
    # Kjør alle tester
    unittest.main(verbosity=2)
