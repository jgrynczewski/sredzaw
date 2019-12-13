def fibonacci_decorator(fibonacci_function):  # nasza funkcja dekorująca, manipuluje na naszej funkcji, może np dodawać uprawnienia
    cache = {}
    print(f'Cześć nazwyam się {fibonacci_function.__name__}')

    def fibonacci_wrapper(fibonacci_param, *args, **kwargs):  # funkcja-wrapper przechwytuje paramaetry przekazywane do funkcji dekorujacej, podajemy tyle parametrów ile ma nasza funkcja
        print(f'jestem wewnątrz wrappera {fibonacci_function.__name__} {fibonacci_param}')
        if cache.get(fibonacci_param):
            return cache[fibonacci_param]
        cache[fibonacci_param] = fibonacci_function(fibonacci_param, *args, **kwargs)
        return fibonacci_function(fibonacci_param, *args, **kwargs)  # funkcja jest przekazyana do dekoratora

    return fibonacci_wrapper


# gdy mamy funkcję udekorowaną , to w mmencie jej wywolania jako pierwszy uruchamia sie dekorator, ktory jakby zawiera funkcję w srodku


@fibonacci_decorator
def fibonanacci2(n: int) -> int:
    if (n in (1, 2)):
        return 1
    return fibonanacci2(n - 2) + fibonanacci2(n - 1)  # zapisz do cache


# print(fiboncci(12))
for i in range(1, int(input('Podaj element ciagu: ')) + 1):
    print(fibonanacci2(i))
