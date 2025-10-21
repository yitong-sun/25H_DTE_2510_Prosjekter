'''
Tester for Clock-klassen.

Beskrivelse:
    Verifiserer init, rulling (sek/min/time/dag/måned/år), skuddår,
    days_in_month, properties med validering og set_clock.
'''

import unittest
from O3_Clock import Clock
  # Koden som testes


class TestClock(unittest.TestCase):
    '''Tester Clock-funksjonalitet.'''

    def test_default_str(self):
        '''Sjekker standard konstruksjon og strengformat.'''
        c = Clock()
        self.assertEqual(str(c), "0000-01-01 00:00:00")

    def test_repr_stable(self):
        '''Sjekker at __repr__ er stabil og lesbar.'''
        self.assertEqual(repr(Clock(2025, 1, 1, 0, 0, 0)),
                         "Clock(2025, 1, 1, 0, 0, 0)")

    def test_inc_sec_simple(self):
        '''Sjekker enkel økning av sekund.'''
        c = Clock()
        c.inc_sec()
        self.assertEqual(str(c), "0000-01-01 00:00:01")

    def test_inc_min_rollover(self):
        '''Sjekker rulling fra 59 sek til nytt minutt.'''
        c = Clock(0, 1, 1, 0, 0, 59)
        c.inc_sec()
        self.assertEqual(str(c), "0000-01-01 00:01:00")

    def test_inc_hour_rollover(self):
        '''Sjekker rulling fra 59 min til ny time.'''
        c = Clock(0, 1, 1, 0, 59, 59)
        c.inc_sec()
        self.assertEqual(str(c), "0000-01-01 01:00:00")

    def test_inc_day_rollover(self):
        '''Sjekker rulling fra 23:59:59 til ny dag.'''
        c = Clock(2025, 1, 1, 23, 59, 59)
        c.inc_sec()
        self.assertEqual(str(c), "2025-01-02 00:00:00")

    def test_inc_month_rollover(self):
        '''Sjekker rulling ved månedsslutt (31. jan → 1. feb).'''
        c = Clock(2025, 1, 31, 23, 59, 59)
        c.inc_sec()
        self.assertEqual(str(c), "2025-02-01 00:00:00")

    def test_inc_year_rollover(self):
        '''Sjekker rulling ved årsslutt (31. des → 1. jan).'''
        c = Clock(2024, 12, 31, 23, 59, 59)
        c.inc_sec()
        self.assertEqual(str(c), "2025-01-01 00:00:00")

    def test_leap_year_rules(self):
        '''Sjekker skuddårsregler (2020/2021/1900/2000).'''
        self.assertTrue(Clock.is_leapyear(2020))
        self.assertFalse(Clock.is_leapyear(2021))
        self.assertFalse(Clock.is_leapyear(1900))  # 100-år, ikke 400 → ikke skuddår
        self.assertTrue(Clock.is_leapyear(2000))   # 400-år → skuddår

    def test_days_in_month(self):
        '''Sjekker days_in_month for ulike måneder og år.'''
        self.assertEqual(Clock.days_in_month(1, 2021), 31)
        self.assertEqual(Clock.days_in_month(4, 2021), 30)
        self.assertEqual(Clock.days_in_month(2, 2020), 29)  # skuddår
        self.assertEqual(Clock.days_in_month(2, 2021), 28)  # ikke skuddår

    def test_property_validation_month_day(self):
        '''Sjekker at dag revalideres når måned endres (februar 31 → 1).'''
        c = Clock(2025, 1, 31)
        c.month = 2
        self.assertEqual(c.day, 1)  # over maks → 1 i februar

    def test_property_set_invalid_day(self):
        '''Sjekker at ugyldig dag blir 1 i konstruktør og ved setting.'''
        c = Clock(2025, 2, 29)  # 2025 er ikke skuddår → dag=1
        self.assertEqual(c.day, 1)
        c.day = 31  # også ugyldig i februar → 1
        self.assertEqual(c.day, 1)

    def test_property_clamps(self):
        '''Sjekker at time/min/sek blir klampet til gyldig intervall.'''
        c = Clock(2025, 5, 10, -3, 99, 100)
        self.assertEqual(c.hour, 0)   # < 0 → 0
        self.assertEqual(c.min, 59)   # > 59 → 59
        self.assertEqual(c.sec, 59)   # > 59 → 59

    def test_set_clock(self):
        '''Sjekker set_clock rekkefølge og validering.'''
        c = Clock()
        c.set_clock(2020, 2, 29, 23, 59, 59)  # gyldig i skuddår
        self.assertEqual(str(c), "2020-02-29 23:59:59")
        c.set_clock(2025, 2, 29, 25, -1, 61)  # 2025: feb 29 → 1; time/min/sek klampes
        self.assertEqual(str(c), "2025-02-01 23:00:59")


if __name__ == '__main__':
    unittest.main()
