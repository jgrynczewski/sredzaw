from math import pi
def circle_area(r):
    return pi*r**2

raw_r = input(f'Wprowadź promien koła: ')
try:
    r = float(raw_r)
    area = circle_area(r)
    print(f'Pole koła o promieniu {r} wynosi {round(area, 2)}')
except:
    print('Coś poszło  nie tak')
