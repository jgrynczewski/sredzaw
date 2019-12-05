import math
def pole_kola(r):
    return  math.pi * r *r


while(True):
    try:
        r = float(input('Podaj r:'))
        if r < 0:
            raise ValueError
        else:
            print(f'Pole kola o promieniu r = {r} wynosi {pole_kola(r)}')
    except:
        print(f'Podałeś niepoprawne dane')
    finally:
        print("Czy chcesz komentowac [t/n]", end='')
        answer = input()
        if answer.upper()=='N':
            break;