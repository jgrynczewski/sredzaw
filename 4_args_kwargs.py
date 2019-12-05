from textwrap import wrap

def format_phone_number(number="000000000", area_code="+48", delimiter="-"):
    wrapped_text = wrap(number, 3) # string number na 3 substringi o dlugosci nie dluzsze niz 3
    phone_number = delimiter.join(wrapped_text)
    return f'{area_code} {phone_number}'

my = format_phone_number('111222333', '+48', '-')
print(my)
print(format_phone_number())


def func(a="0",b="0", c="0"):
    #(a="0", b, c="0") is invalid
    print(a)
    print(b)
    print(c)

func()