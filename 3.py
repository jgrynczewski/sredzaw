from math import pi

def circle_area(r):
    """Return area pf the circle dor the given radius."""
    return pi * r**2

raw_r = input("Proszę, podaj mi promień koła:")
test_list = raw_r.split('.')
try:
    r = float(raw_r)
    area = circle_area(r)
    print(f"Pole koła o promieniu {r} wynosi {round(area, 2)}")
except ValueError:
    print("Cos poszlo nie tak!")