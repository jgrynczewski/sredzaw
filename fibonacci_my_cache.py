cache = {}


def fibonacci(n: int) -> int:
    if n in (1, 2):
        return 1

    try:
        return cache[n]
    except KeyError:
        cache[n] = fibonacci(n-2) + fibonacci(n-1)
        return cache[n]


if __name__ == '__main__':
    for i in range(1, int(input('Podaj element ciagu: ')) +1):
        print(fibonacci(i))