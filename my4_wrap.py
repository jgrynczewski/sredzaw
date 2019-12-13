from textwrap import wrap

def format_phone_number(number='000000000', area_code='+48', delimiter='-'): #argumenty bez wartości domyslnej == argumenty pozycyjne (czyli te z domyslnymi)
    wrapped_text = wrap(number, 3)
    phone_number = delimiter.join(wrapped_text)
    return f"{area_code} {phone_number}"


f = format_phone_number('111222333','+48','-')
print(f)
format_phone_number() #jak nei podano wartości domyślnych to mamy errora


