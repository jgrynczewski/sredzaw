import collections

jack = ("Jack")

Person = collections.namedtuple('Person', 'name age gender')
print(f"type of person: {type(Person)}")

jack = Person(name = "Jack", age=30, gender="male")
print(f"Named Tuple representation:  {jack}")

print(f'field by name: {jack.name}')

jane = Person(name="Jane", age=29, gender="female")
print(f'Field by age : {jane.age}')


