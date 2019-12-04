# Zadanie 2

# 1. Utwórz dwie namedtuple:
# - 'Amount' z dwoma polami: kwota oraz skrót nazwy waluty
# - 'Currnency' z trzema polami: nazwa skrót nazwy oraz przelicznik na PLN

import collections

Amount = collections.namedtuple("Amount", "amount curr_short_name")
Currency = collections.namedtuple("Currency", "name curr_short_name to_pln_conv")

# 2. Utwórz cztery instsancje Currency:
# - EUR (z kursem 4.32)
# - USD (z kursem 3.93)
# - CHF (z kursem 3.95)
# - PLN (z kursem 1.00)

EUR = Currency(name='Euro', curr_short_name='EUR', to_pln_conv=4.32)
USD = Currency(name='United States Dollar', curr_short_name='USD', to_pln_conv=3.93)
CHF = Currency(name='Swiss Franc', curr_short_name='CHF', to_pln_conv=3.95)
PLN = Currency(name='Polish Zloty', curr_short_name='PLN', to_pln_conv=1.00)


# 3. Utwórz dataclass dla konta walutowego 'CurrencyAccount':
# - atrybuty: skrót waluty, stan konta oraz wartość debetu
# - property 'total_available' zwracające sumę stanu konta i dostępnego debetu
# - metody:
#   - 'pay_out(amount)' - sprawdza, czy na koncie jest dostepna kwota (suma stanu konta i
#     debetu) jeżeli tak, to zwraca obiekt namedtuple Amount (zdefiniowany w czesniej)
#   - 'pay_in(amount)' - dodaje kwotę do stanu konta (uwaga: amount jest liczbą - kwotą
#     w odpowiedniej walucie
from dataclasses import dataclass

@dataclass
class CurrencyAccount:
    curr_short_name: str
    account_value: float
    debit_value: float

    @property
    def total_available(self):
        return self.account_value+self.debit_value

    def pay_out(self, Amount):
        if self.total_available > 0:
            return Amount

    def pay_in(self, Amount):
        if Amount.amount > 0 and Amount.curr_short_name == self.curr_short_name:
            self.account_value += Amount.amount


# 4. Utwórz dataclass dla kantory ExchangeOffice:
# - atrybuty: wartość spreadu, dostepne waluty (domyslnie - wszystkie utworzone wczesniej)
# - metody prywatne - przeliczanie z uwzglednieniem spreadu:
#   'exchange_to_pln(amount)' - wymien kwote w innej walucie na PLN (użyj Amount)
#   'exchange_from_pln(amount, target)' - wymień kwotę w PLN na walutę 'target' (tu też użyj
#    Amount).

@dataclass
class ExchangeOffice:
    spread: float
    available_currencies: (USD, PLN, EUR, CHF)

    def __exchange_to_pln(self, Amount):
        pln_amount = Amount.amount * (Amount.cur_short_name.to_pln_conv + self.spread)
        return pln_amount

    def __exchange_from_pln(self, Amount):
        target_amount = Amount.amount / (Amount.cur_short_name.to_pln_conv + self.spread)
        return target_amount

# Amount = collections.namedtuple("Amount", "amount curr_short_name")
# Currency = collections.namedtuple("Currency", "name curr_short_name to_pln_conv")
