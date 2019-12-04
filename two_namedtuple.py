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

Amount = collections.namedtuple('Amount', 'sum symbol')
Currenency = collections.namedtuple('Currenency', 'name symbol converter')

EUR = Currenency(name = 'euro', symbol = 'EUR', converter = 4.32)
USD = Currenency(name = 'dolar', symbol = 'USD', converter = 3.93)
CHF = Currenency(name = 'frank', symbol = 'CHF', converter = 3.95)
PLN = Currenency(name = 'zloty', symbol = 'PLN', converter = 1.00)

@dataclass
class CurrencyAccount:
    symbol: str
    account_balance: float
    debet: float

    @property
    def total_available(self):
        return sum(self.account_balance, self.debet)

    def pay_out(self, amount):
        if total_available() > 0:
            return Amount
        else:
            return 'Nie masz dostępnych środków'

    def pay_in(self, amount):
        if Amount.symbol == Currenency.symbol:
            amount = Amount.sum * Currenency.converter
            return amount



