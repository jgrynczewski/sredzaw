from textwrap import wrap

def format_phone_number(number='555666777', area_code='+48', delimeter='-'):
    wrapped_text = wrap(number, 3)
    phone_number = delimeter.join(wrapped_text)
    return f'{area_code} {phone_number}'

format_phone_number('123456789', '+48', '-')
format_phone_number()

def func(a, b, c=0):
    print(a)
    print(b)
    print(c)

func(1, 2)