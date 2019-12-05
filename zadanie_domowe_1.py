from collections import namedtuple

Amount = namedtuple('Amount', 'kwota waluta')
Currency = namedtuple('Currency', 'nazwa skrot przelicznik')

a = Amount(100, 'PLN')
b = Amount(200, 'EUR')


c1=Currency('Euro', 'EUR', 4.32)
c2=Currency('Dolar', 'USD', 3.93)
c3=Currency('Frank', 'CHF', 3.95)
c4=Currency('Zloty', 'PLN', 1.00)

lista_walut = []
lista_walut.append((c1))
lista_walut.append((c2))
lista_walut.append((c3))
lista_walut.append((c4))

for c in lista_walut:
    print(f'{c.nazwa} {c.skrot} {c.przelicznik}')


'''
Utwórz dataclass dla konta walutowego 'CurrencyAccount':
- atrybuty: skrót waluty, stan konta oraz wartość debetu

- property 'total_available' zwracające sumę stanu konta i dostępnego debetu
- metody:
- 'pay_out(amount)' - sprawdza, czy na koncie jest dostepna kwota (suma stanu konta i
debetu) jeżeli tak, to zwraca obiekt namedtuple Amount (zdefiniowany w czesniej)

- 'pay_in(amount)' - dodaje kwotę do stanu konta (uwaga: amount jest liczbą - kwotą
w odpowiedniej walucie
'''
from dataclasses import  dataclass

@dataclass
class CurrencyAccount:
    waluta: str
    stan_konta: float
    debet: float

    @property
    def total_available(self):
        return  Amount( self.stan_konta + self.debet, self.waluta)

    def pay_out(self, amount):
        if self.total_available >= amount:
            self.stan_konta -= amount
            return Amount(amount, self.waluta)

    def pay_in(self, amount):
        if amount.waluta == self.waluta:
            self.stan_konta += amount.kwota
        else:
            for c in lista_walut:
                if c.skrot == amount.waluta:
                    self.stan_konta += (a.kwota * c.przelicznik)

'''
4. Utwórz dataclass dla kantory ExchangeOffice:
    - atrybuty: wartość spreadu, dostepne waluty (domyslnie - wszystkie utworzone wczesniej)
    - metody prywatne - przeliczanie z uwzglednieniem spreadu:
         'exchange_to_pln(amount)' - wymien kwote w innej walucie na PLN (użyj Amount)
         'exchange_from_pln(amount, target)' - wymień kwotę w PLN na walutę 'target' (tu też użyj Amount).

'''
@dataclass
class ExchangeOffice:
    spred: float
    waluty: []
    def __post_init__(self):
        waluty = lista_walut

    def exchange_to_pln(self, amount):
        c = self.get_currency(amount)
        val = c.przelicznik * amount.kwota
        return Amount(val, 'PLN')

    def exchange_from_pln(self, amount, target):
        a = self.get_currency(amount)
        t= self.get_currency(target)

        val = t.przelicznik * amount.kwota
        return Amount(val, t.waluta)

    def get_currency(self, amount):
        for c in lista_walut:
            if c.skrot == amount.waluta:
                return c

my_lista = [1, 2, 3, 4]
print( my_lista)
a = my_lista.pop()
print(a)
print(my_lista)
my_lista.append(a)
print(my_lista)