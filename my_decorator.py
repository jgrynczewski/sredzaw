def fibonacci_decorator(fibonacci_function): # funkcja przechwytuje funkcje na której bedzie działac
    cache = {}
    print(f'Nazywam sie {fibonacci_function.__name__}')
    def fibonacci_wrapper(fibonacci_param, *args, **kwargs):  # funkcja przechwytuje parametry z funkcji na której działamy
        if cache.get(fibonacci_param):
            return cache[fibonacci_param]

        cache[fibonacci_param] = fibonacci_function(fibonacci_param, *args, **kwargs)
        return cache[fibonacci_param]

    return fibonacci_wrapper

@fibonacci_decorator
def fibonacci(n: int) -> int:
    if n in (1, 2):
        return 1

    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    for i in range(1, int(input('Podaj element ciagu: ')) +1):
        print(fibonacci(i))