from textwrap import wrap

def format_phone_number(number="000000000", area_code="+48", delimiter=" "):
    wrapped_text = wrap(number, 3)
    phone_number = delimiter.join(wrapped_text)
    return f"{area_code} {phone_number}"


my_phone_number = format_phone_number('111222333', '+48', '-')
print(my_phone_number)
print(format_phone_number())


def func(a, b=4, c=0):
    print(a)
    print(b)
    print(c)


func(2, 3)
