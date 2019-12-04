import collections

jack = ("Jack", 30, "male")
Person = collections.namedtuple("Person", "name age gender") #funkcja namedtuple zwraca nam klasę Person
print(f'Type of Person: {type(Person)}')

jack = Person("Jack", 30, 'male')
print(f" Namedtuple representation {jack}")
print("Field by name", jack.name)


jane = Person("Jane", 29, "famele")
print("Field by age", jack.age)

print ("Field by index",jane[0])


NumberInfo = collections.namedtuple('NumberInfo', "number area_code delimiter")
n1 = NumberInfo('600600601','+48','-')
n2 = NumberInfo('600600602','+48','-')
n3 = NumberInfo('600600603','+48','-')
