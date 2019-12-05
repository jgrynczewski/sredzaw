# Zadanie 2

# 1. Utwórz dwie namedtuple:
# - 'Amount' z dwoma polami: kwota oraz skrót nazwy waluty
# - 'Currnency' z trzema polami: nazwa skrót nazwy oraz przelicznik na PLN

from collections import namedtuple

Amount = namedtuple("Amount", "kwota skrot")
Currency = namedtuple("Currency", "nazwa skrot przelicznik")

# 2. Utwórz cztery instsancje Currency:
# - EUR (z kursem 4.32)
# - USD (z kursem 3.93)
# - CHF (z kursem 3.95)
# - PLN (z kursem 1.00)

c1 = Currency('euro', "EUR", 4.32)
c2 = Currency('dolar', "USD", 4)
c3 = Currency('frank', "CHF", 3.95)
c4 = Currency('zloty', "PLN", 1.00)

print(c3)

a1  = Amount(30, 'PLN')
a2 = Amount(50, "USD")

print(a2)

# 3. Utwórz dataclass dla konta walutowego 'CurrencyAccount':
# - atrybuty: skrót waluty, stan konta oraz wartość debetu
# - property 'total_available' zwracające sumę stanu konta i dostępnego debetu
# - metody:
#   - 'pay_out(amount)' - sprawdza, czy na koncie jest dostepna kwota (suma stanu konta i
#     debetu) jeżeli tak, to zwraca obiekt namedtuple Amount (zdefiniowany w czesniej)
#   - 'pay_in(amount)' - dodaje kwotę do stanu konta (uwaga: amount jest liczbą - kwotą
#     w odpowiedniej walucie)

from dataclasses import dataclass

@dataclass
class CurrencyAccount:
    skrot: str
    stan: float
    debet: float

    @property
    def total_available(self):
        return Amount(self.stan + self.debet, self.skrot)

    def pay_out(self, amount):
        if amount < self.total_available.kwota:
            self.stan -= amount
            return Amount(amount, self.skrot)
        else:
            print("Sorry, amount not available.")

    def pay_in(self, amount):
        self.stan += amount

ca1 = CurrencyAccount("PLN", 1000, 1000)

print(ca1.total_available)
ca1.pay_out(500)
print(ca1.total_available)
ca1.pay_in(1000)
print(ca1.total_available)

# 4. Utwórz dataclass dla kantory ExchangeOffice:
# - atrybuty: wartość spreadu, dostepne waluty (domyslnie - wszystkie utworzone wczesniej)
# - metody - przeliczanie z uwzglednieniem spreadu:
#   'exchange_to_pln(amount)' - wymien kwote w innej walucie na PLN (użyj Amount)
#   'exchange_from_pln(amount, target)' - wymień kwotę w PLN na walutę 'target' (tu też użyj
#    Amount).

@dataclass
class ExchangeOffice:
    spread: float = 0.05
    waluty: tuple = (c1, c2, c3, c4)

    def _get_currency(self, abbr):
        return [currency for currency in self.waluty if currency.skrot==abbr][0]

    def exchange_to_pln(self, amount):
        currency = self._get_currency(amount.skrot)
        return Amount((currency.przelicznik-self.spread/2)*amount.kwota, 'PLN')

    def exchange_from_pln(self, amount, target):
        currency = self._get_currency(target)
        return Amount(1/(currency.przelicznik+self.spread/2)*amount.kwota, target)

eo1 = ExchangeOffice()

kwota_wplaty = Amount(1000, 'USD')
wyplata1 = eo1.exchange_to_pln(kwota_wplaty)
kwota_wplaty = Amount(1000, "PLN")
wyplata2 = eo1.exchange_from_pln(kwota_wplaty, "USD")

print(wyplata1)
print(wyplata2)
