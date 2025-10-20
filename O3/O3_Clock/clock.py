# -*- coding: utf-8 -*-
"""
Klasse: Clock (digital klokke med dato og tid)

Beskrivelse:
    Representerer en enkel digital klokke med år, måned, dag, time, minutt og sekund.
    Håndterer rulling ved økning (sekund → minutt → time → dag → måned → år) uten
    å bruke innebygde dato-/tidsbiblioteker.

Hovedregler:
    - Bruker private attributter (_year, _month, _day, _hour, _minute, _sec).
    - Alle settere validerer og korrigerer ugyldige verdier til nærmeste gyldige.
    - Når måned endres, revalideres dag automatisk (overstiger dag maks → settes til 1).
    - Skuddår: (år % 4 == 0 og år % 100 != 0) eller (år % 400 == 0).

Format:
    __str__ returnerer "YYYY-MM-DD HH:MM:SS" med null-padding.

Forfatter:
    Student, DTE2510
"""

from __future__ import annotations


class Clock:
    """Representerer en klokke med dato og tid (uten standardbibliotek).

    Konstruerer:
        year   (int): År (>= 0). Standard 0.
        month  (int): Måned (1–12). Standard 1.
        day    (int): Dag (1–28/29/30/31). Standard 1.
        hour   (int): Time (0–23). Standard 0.
        min    (int): Minutt (0–59). Standard 0.
        sec    (int): Sekund (0–59). Standard 0.

    Attributter (private):
        _year   (int): År (>= 0).
        _month  (int): Måned (1–12).
        _day    (int): Dag (1..days_in_month).
        _hour   (int): Time (0–23).
        _minute (int): Minutt (0–59).
        _sec    (int): Sekund (0–59).

    Klassekonstanter:
        MONTHS_31 (list[int]): Måneder med 31 dager.
        MONTHS_30 (list[int]): Måneder med 30 dager.
    """

    MONTHS_31 = [1, 3, 5, 7, 8, 10, 12]
    MONTHS_30 = [4, 6, 9, 11]

    def __init__(
        self,
        year: int = 0,
        month: int = 1,
        day: int = 1,
        hour: int = 0,
        min: int = 0,
        sec: int = 0,
    ) -> None:
        """Initialiserer klokken og sikrer gyldig starttilstand.

        Genererer:
            Validerer og korrigerer felt i rekkefølge:
            year → month → day → hour → min → sec.

        Args:
            year: År (>= 0).
            month: Måned (1–12).
            day: Dag (1–28/29/30/31).
            hour: Time (0–23).
            min: Minutt (0–59).
            sec: Sekund (0–59).

        Returns:
            None
        """
        # Bruk settere for å samle valideringslogikk ett sted.
        self._year = 0
        self._month = 1
        self._day = 1
        self._hour = 0
        self._minute = 0
        self._sec = 0

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.sec = sec

    # -------------------- Properties (gettere/settere) --------------------

    @property
    def year(self) -> int:
        """Henter år."""
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        """Setter år. Korrigerer til 0 hvis negativ.

        Args:
            value: År (int).

        Returns:
            None
        """
        if not isinstance(value, int):
            try:
                value = int(value)
            except Exception:
                value = 0
        self._year = max(0, value)
        # Etter år kan februar endre antall dager; revalider dag hvis nødvendig.
        maxd = self.days_in_month(self._month, self._year)
        if self._day > maxd:
            self._day = 1

    @property
    def month(self) -> int:
        """Henter måned."""
        return self._month

    @month.setter
    def month(self, value: int) -> None:
        """Setter måned. Korrigerer til [1, 12]. Revaliderer dag.

        Args:
            value: Måned (int).

        Returns:
            None
        """
        if not isinstance(value, int):
            try:
                value = int(value)
            except Exception:
                value = 1
        if value < 1:
            value = 1
        elif value > 12:
            value = 12
        self._month = value

        # Måned kan endre maksimal tillatt dag; revalider dag.
        maxd = self.days_in_month(self._month, self._year)
        if self._day > maxd:
            self._day = 1

    @property
    def day(self) -> int:
        """Henter dag."""
        return self._day

    @day.setter
    def day(self, value: int) -> None:
        """Setter dag. Korrigerer til 1 hvis utenfor gyldig intervall.

        Args:
            value: Dag (int).

        Returns:
            None
        """
        if not isinstance(value, int):
            try:
                value = int(value)
            except Exception:
                value = 1

        maxd = self.days_in_month(self._month, self._year)
        if 1 <= value <= maxd:
            self._day = value
        else:
            self._day = 1

    @property
    def hour(self) -> int:
        """Henter time."""
        return self._hour

    @hour.setter
    def hour(self, value: int) -> None:
        """Setter time. Korrigerer til [0, 23].

        Args:
            value: Time (int).

        Returns:
            None
        """
        if not isinstance(value, int):
            try:
                value = int(value)
            except Exception:
                value = 0
        if value < 0:
            value = 0
        elif value > 23:
            value = 23
        self._hour = value

    @property
    def min(self) -> int:
        """Henter minutt."""
        return self._minute

    @min.setter
    def min(self, value: int) -> None:
        """Setter minutt. Korrigerer til [0, 59].

        Args:
            value: Minutt (int).

        Returns:
            None
        """
        if not isinstance(value, int):
            try:
                value = int(value)
            except Exception:
                value = 0
        if value < 0:
            value = 0
        elif value > 59:
            value = 59
        self._minute = value

    @property
    def sec(self) -> int:
        """Henter sekund."""
        return self._sec

    @sec.setter
    def sec(self, value: int) -> None:
        """Setter sekund. Korrigerer til [0, 59].

        Args:
            value: Sekund (int).

        Returns:
            None
        """
        if not isinstance(value, int):
            try:
                value = int(value)
            except Exception:
                value = 0
        if value < 0:
            value = 0
        elif value > 59:
            value = 59
        self._sec = value

    # -------------------- Hjelpemetoder (stateless) --------------------

    @staticmethod
    def is_leapyear(year: int) -> bool:
        """Beregner om et år er skuddår.

        Regler:
            - Delelig med 400 → skuddår.
            - Ellers delelig med 100 → ikke skuddår.
            - Ellers delelig med 4 → skuddår.
            - Ellers → ikke skuddår.

        Args:
            year: År (int).

        Returns:
            bool: True hvis skuddår, ellers False.
        """
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return (year % 4) == 0

    @classmethod
    def days_in_month(cls, month: int, year: int) -> int:
        """Henter antall dager i en gitt måned/år.

        Args:
            month: Måned (1–12).
            year:  År (>= 0).

        Returns:
            int: Antall dager i måneden.
        """
        if month in cls.MONTHS_31:
            return 31
        if month in cls.MONTHS_30:
            return 30
        # Februar:
        return 29 if cls.is_leapyear(year) else 28

    # -------------------- Øk-metoder (rulling) --------------------

    def inc_sec(self) -> None:
        """Øker sekund med 1. Ruller til minutt ved 60.

        Returns:
            None
        """
        self._sec += 1
        if self._sec == 60:
            self._sec = 0
            self.inc_min()

    def inc_min(self) -> None:
        """Øker minutt med 1. Ruller til time ved 60.

        Returns:
            None
        """
        self._minute += 1
        if self._minute == 60:
            self._minute = 0
            self.inc_hour()

    def inc_hour(self) -> None:
        """Øker time med 1. Ruller til dag ved 24.

        Returns:
            None
        """
        self._hour += 1
        if self._hour == 24:
            self._hour = 0
            self.inc_day()

    def inc_day(self) -> None:
        """Øker dag med 1. Ruller til måned ved månedsslutt.

        Returns:
            None
        """
        self._day += 1
        if self._day > self.days_in_month(self._month, self._year):
            self._day = 1
            self.inc_month()

    def inc_month(self) -> None:
        """Øker måned med 1. Ruller til år ved 13.

        Returns:
            None
        """
        self._month += 1
        if self._month == 13:
            self._month = 1
            self.inc_year()
        # Etter månedsskifte er dag alltid 1 (via inc_day), så ingen revalidering her.

    def inc_year(self) -> None:
        """Øker år med 1.

        Returns:
            None
        """
        self._year += 1

    # -------------------- Andre metoder --------------------

    def set_clock(self, year: int, month: int, day: int, hour: int, min: int, sec: int) -> None:
        """Setter alle felter samlet og validerer automatisk.

        Rekkefølge:
            year → month → day → hour → min → sec

        Args:
            year: År (>= 0).
            month: Måned (1–12).
            day: Dag (1–28/29/30/31).
            hour: Time (0–23).
            min: Minutt (0–59).
            sec: Sekund (0–59).

        Returns:
            None
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.sec = sec

    def __str__(self) -> str:
        """Formaterer klokken som streng: 'YYYY-MM-DD HH:MM:SS'.

        Returns:
            str: Formatert dato og tid.
        """
        return f"{self._year:04d}-{self._month:02d}-{self._day:02d} " \
               f"{self._hour:02d}:{self._minute:02d}:{self._sec:02d}"
