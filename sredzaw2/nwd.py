#dekaorator można definiować tylko ponad funkcją
# łapiemy błąd zbyt wielu rekurencji  w naszej funkcji
def nwd_decorator(function):
    def wrapper(a, b):
        try:
            return function(a, b)

        except RecursionError:
            print("Aż tyle to ja nie policzę")
            exit(1) # jest jakis blad
    return wrapper


def nwd (a:int, b:int) -> int:
    '''
    implementujemy algorytmu Euklidesa
    :param a:
    :param b:
    :return:
    '''

    while b != 0:
          c = a % b
          a = b
          b = c
         # można to zapisać krócej: a , b = b , c
    return a


def  nwd_rekurencyjnie(a: int, b: int) -> int:

    if b == 0:
        return a
    else:
        return nwd_rekurencyjnie(b, a % b)


#@ostatnie - może być więcej dekoratorów wykonywane są od tych najbardziej zagnieżdzonych do tyh na wierzchu
#@srodkowe
@nwd_decorator
def nwd_rekurencyjnie2(a : int, b:int) -> int:
    if a == b:
        return a
    if a > b :
        return nwd(a - b, b)
    else:
        return nwd(a, b - a)


if __name__ == '__main__':

    a, b = input ("Podaj a i b po przecinku: ").split(',')
    #print(nwd(int(a),int(b)))
    #print(nwd_rekurencyjnie(int(a), int(b)))
    print(nwd_rekurencyjnie2(int(a),int(b)))