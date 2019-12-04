from math import pi
# exceptions
def circle_area(r):
    return pi * r**2
raw_r = input('Podaj promień koła')
try:
    r = float(raw_r)
    area = circle_area(r)
    print(f'Pole koła o promieniu {r} wynosi {round(area, 2)}')

except ValueError:
    print('Nieprawidłowe dane')

print('--------------as a class:------------------')


class ObliczPoleKola:
    def __init__(self):
        self.radius = input('podaj promień koła')
        self.result = 0

    def validate(self):
        try:
            number = float(self.radius)
            return number
        except ValueError:
            return False

    def calculate(self):
        if not self.validate():
            return 'Podano nieprawidłową wartość'
        else:
            r = self.validate()
            result = pi * r**2
            return f'Pole koła o promieniu {r} wynosi {round(result, 2)}'

walidacja = ObliczPoleKola().validate()
print(f'Walidacja: {walidacja}')
oblicz_pole1 = ObliczPoleKola().calculate()
print(f'Wynik: {oblicz_pole1}')



