def nwd_decorator(function):
    def wrapper(a, b):
        try:
            return function(a,b)
        except RecursionError:
            print('Ale aż tyle to ja nie policzę')
            exit(1)
    return wrapper

@nwd_decorator
def nwd(a, b):
    if a == b:
        return a
    elif a > b:
        return nwd(a-b, b)

    return nwd(a, b-a)

if __name__ == '__main__':
    print(nwd(75,14))