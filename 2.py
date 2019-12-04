'''
'''
from dataclasses import dataclass #wymagane przy użyciu


#defaultdict przechowują dane i reprezentują typ danych
class Number:

    def __init__(self, value):
        self.value = value


one = Number(1)
print(one.value)


@dataclass
class NumberDC:
    value: int=4

one_dc = NumberDC(2)
print(one_dc.value)

two_dc = NumberDC()
print(two_dc.value)
print(repr(two_dc.value))

# <, >, ==, <=, >=

