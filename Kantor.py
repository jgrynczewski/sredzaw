'''
Zadanie 21.
Utwórz dwie namedtuple:
- 'Amount' z dwoma polami: kwota oraz skrót nazwy waluty
- 'Currnency' z trzema polami: nazwa skrót nazwy oraz przelicznik na PLN2. Utwórz cztery instsancje Currency:
- EUR (z kursem 4.32)
- USD (z kursem 3.93)
- CHF (z kursem 3.95)
- PLN (z kursem 1.00).

Utwórz dataclass dla konta walutowego 'CurrencyAccount':
- atrybuty: skrót waluty, stan konta oraz wartość debetu
- property 'total_available' zwracające sumę stanu konta i dostępnego debetu
- metody:
- 'pay_out(amount)' - sprawdza, czy na koncie jest dostepna kwota (suma stanu konta i
debetu) jeżeli tak, to zwraca obiekt namedtuple Amount (zdefiniowany w czesniej)
- 'pay_in(amount)' - dodaje kwotę do stanu konta (uwaga: amount jest liczbą - kwotą
w odpowiedniej walucie

Utwórz dataclass dla kantory ExchangeOffice:
- atrybuty: wartość spreadu, dostepne waluty (domyslnie - wszystkie utworzone wczesniej)
- metody prywatne - przeliczanie z uwzglednieniem spreadu:
'exchange_to_pln(amount)' - wymien kwote w innej walucie na PLN (użyj Amount)
'exchange_from_pln(amount, target)' - wymień kwotę w PLN na walutę 'target' (tu też użyj Amount).
'''

from collections import namedtuple
from dataclasses import dataclass


Amount = namedtuple(("Amount","kwota nazwa_waluty"))
Currency = namedtuple(("Currency","nazwa skrot_nazwy przelicznik"))
eur = Currency('Euro','EUR',4.32)
usd = Currency('Dolar','USD',3.93)
chf = Currency('Frank','CHF',3.95)
pln = Currency('Złoty','PLN',1.00)


@dataclass
class CurrencyAccount:
    skrot_waluty: str
    stan_konta: int
    wartosc_debetu: int

    @property
    def total_available(self):
        return  self.stan_konta + self.wartosc_debetu

    def pay_out(self, amount):
        if self.total_available > 0:
            return amount #??????????????????

    def pay_in(self, amount):
        self.stan_konta += amount

@dataclass
class ExchangeOffice:
    wartosc_spreadu: float
    dostepne_waluty: ['EUR','PLN','USD','CHF']

    def _exchange_to_pln(self, amount):
        pass

    def _exchange_from_pln(amount, target):
        pass