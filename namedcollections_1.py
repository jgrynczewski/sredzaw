import math

print(dir(math))

import collections

jack = ("Jack", 30, "male")
print(f"Tuple representation {jack}")

Person = collections.namedtuple('Person', 'name age gender')
# generuje klase z polami nazwanymi
print(f"Type of Person: {type(Person)}")

jack = Person(name="Jack", age=30, gender="male")
print(f"Tuple representation {jack}")

print(f'Field by name: {jack.name}')

jane = Person(name="jane", age=29, gender="female")
print(jane)
print(f'Field by age: {jane.age}')

Number = collections.namedtuple('Number', 'number area_code delimiter')
num1 = Number(number='343678234', area_code="+48", delimiter="-")
num2 = Number(number='999998233', area_code="+44", delimiter="-")
num3 = Number(number='121879311', area_code="+42", delimiter="-")
print(f'{num1} {num2} {num3}')
print(f'nr telefonu: {num1.area_code}{num1.delimiter}{num1.number}')
