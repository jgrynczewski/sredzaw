import itertools


def primes():
    primes_found = set()
    primes_found.add(2)
    yield 2
    for i in itertools.count(1):
        candidate = i * 2 + 1
        if not all(candidate % prime for prime in primes_found):
            primes_found.add(candidate)
            yield candidate

def prime_products():
    primeiter = primes()
    prev = primeiter.next()
    for prime in primeiter:
        yield prime * prev
        prev = prime


def fib():
    first = 0
    second = 1
    #print(f"AThis is {first} and {second}")
    #yield #first
    #print(f"BThis is {first} and {second}")
    #yield second

    while 1:
        next = first + second
        #print(f"CThis is {next}")
        yield next
        first = second
        second = next

fibgen1 = fib()
print('This is',next(fibgen1))
fibgen2 = fib()
next(fibgen2)
next(fibgen2)
next(fibgen2)

print('This is',next(fibgen1))
print('This is',next(fibgen1))
print('This is',next(fibgen1))
print('This is',next(fibgen1))
print('This is',next(fibgen1))
print('This is',next(fibgen1))
next(fibgen1)

