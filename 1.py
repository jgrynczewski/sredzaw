import collections

jack = ("Jack", 30, "male")
print(f"Tuple representation {jack}")

Person = collections.namedtuple('Person', 'name age gender')
# print(f"Type of Person: {type(Person)}")

jack = Person(name="Jack", age=30, gender="male")
print(f"Namedtuple representation {jack}")

print(f"Field by name: {jack.name}")

jane = Person(name="Jane", age=29, gender="female")
print(f"Field by age: {jane.age}")

