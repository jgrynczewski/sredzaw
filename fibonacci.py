from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n: int) -> int:
    if n in (1, 2):
        return 1

    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    for i in range(1, int(input('Podaj element ciagu: ')) +1):
        print(fibonacci(i))