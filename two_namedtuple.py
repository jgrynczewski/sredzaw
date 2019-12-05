# Zadanie 2

# 1. Utwórz dwie namedtuple:
# - 'Amount' z dwoma polami: kwota oraz skrót nazwy waluty
# - 'Currnency' z trzema polami: nazwa skrót nazwy oraz przelicznik na PLN

# 2. Utwórz cztery instsancje Currency:
# - EUR (z kursem 4.32)
# - USD (z kursem 3.93)
# - CHF (z kursem 3.95)
# - PLN (z kursem 1.00)

# 3. Utwórz dataclass dla konta walutowego 'CurrencyAccount':
# - atrybuty: skrót waluty, stan konta oraz wartość debetu
# - property 'total_available' zwracające sumę stanu konta i dostępnego debetu
# - metody:
#   - 'pay_out(amount)' - sprawdza, czy na koncie jest dostepna kwota (suma stanu konta i
#     debetu) jeżeli tak, to zwraca obiekt namedtuple Amount (zdefiniowany w czesniej)
#   - 'pay_in(amount)' - dodaje kwotę do stanu konta (uwaga: amount jest liczbą - kwotą
#     w odpowiedniej walucie

# 4. Utwórz dataclass dla kantory ExchangeOffice:
# - atrybuty: wartość spreadu, dostepne waluty (domyslnie - wszystkie utworzone wczesniej)
# - metody prywatne - przeliczanie z uwzglednieniem spreadu:
#   'exchange_to_pln(amount)' - wymien kwote w innej walucie na PLN (użyj Amount)
#   'exchange_from_pln(amount, target)' - wymień kwotę w PLN na walutę 'target' (tu też użyj
#    Amount).

import collections
from dataclasses import dataclass

Amount = collections.namedtuple('Amount', 'amount symbol')
Currenency = collections.namedtuple('Currenency', 'name symbol converter')

c_1 = Currenency('euro', 'EUR',  4.32)
c_2 = Currenency('dolar', 'USD', 3.93)
c_3 = Currenency('frank', 'CHF', 3.95)
c_4 = Currenency('zloty', 'PLN', 1.00)

a_1 = Amount(amount = , symbol= '')
a_2 = Amount(amount = , symbol= '')

@dataclass
class CurrencyAccount:
    symbol: str
    balance: float
    debet: float

    @property
    def total_available(self):
        return Amount(self.balance + self.debet, self.symbol)

    def pay_out(self, amount):
        if amount < self.total_available.balance:
            self.balance -= amount
            return Amount(amount, self.symbol)
        else:
            return 'Nie masz dostępnych środków'

    def pay_in(self, amount):
        self.balance += amount

@dataclass
class ExchangeOffice:
    speed_spead: float = 0.05
    waluty: tuple = (c_1, c_2, c_3, c_4)

    def find_currency(self, amount):
        for currency in self.waluty:
            if currency.symbol == abbr:
                return currency

    def _get_currency(self, abbr):
        return [currency for currency in self.waluty if currency.symbol == abbr][0]

    def exchange_to_pln(self, amount):
        #znajdź przelicznik
       # waluta_wplaty = amount.symbol
        #przelicz
        currency = self._get_currency(amount.symbol)
        return Amount((przelicznik - self.speed_spead/2)*amount.amount, 'PLN')

    def exchange_from_pln(self, amount, target):
        currency = self._get_currency(target)
        return Amount(1/(currency.przelicznik + self.speed_spead/2) * amount.amount, target)




ca_1 = CurrencyAccount('PLN', 1000, 1000)
eo_1 = ExchangeOffice()

kwota_wplaty = Amount(1000, 'USD')
wyplata_1 = eo_1.exchange_to_pln(kwota_wplaty)
kwota_wplaty = Amount(1000, 'PLN')
wyplata_2 = eo_1.exchange_from_pln(kwota_wplaty)