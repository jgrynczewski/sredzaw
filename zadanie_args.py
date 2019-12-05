def to_concatenate(*args, **kwargs):
    my_str=''
    for a in args:
        my_str += str(a)

    for b in kwargs.values():
        my_str += str(b)
    return my_str

print( to_concatenate(1, 2, 3, 'a', b=1, c='c'))

def funkcja(pozycyjne, *args, nazwane, **kwargs):
    pass

#funkcja(a, *args, n=1, **kwargs)
