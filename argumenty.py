from textwrap import wrap
def format_phone_numer(number, area_code, delimter):
    wraped_text = wrap(number, 3)
    phone_numer = delimter.join( wraped_text)


    print(f'{area_code} {phone_numer}')

format_phone_numer('111222444', '+48', '-')


def method( start, stop):
    return range(start, stop)

def method( start, stop, bool):
    if bool == True:
        range(start, stop, 2)
    else:
        return  range(start, stop, 1)


print(method(1, 10, False))
print(method(1, 10, True))

from collections import Counter
litery = [1, 2, 4, 4 ]
result =  Counter(litery)
print(result)

def suma(a, b):
    return a+b
# *args pozycyjne argumenty waridyczne

def suma_wariadryczna(*args):
    len = len(args)
    print(len)

print(suma(10, 2))
#(1, 2, 3)

def f(*args):
    print(sum(args))

# ** kwargs [argumenty nazwane]
def ff(**kwargs):
    print(kwargs)


#def fff(*args, **kwargs) # (pozycyjne, nazwane)
    #pass
print('------------------------------')
f()
f(1)
f(1, 2)
f(1, 2, 3, 3)
ff(a=1, b=2, c=3)




def to_string(*args):
    my_str=''
    for a in args:
        str+=str(a)
    return my_str

print( to_string(1, 2, 3, 'a'))
