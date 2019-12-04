import collections

#jack = ("Jack", 30, "male")
Person = collections.namedtuple('Person', 'name age gender')#klasa do generowania nazwanych krotek
print(f'Type of Person: {type(Person)}')

jack = Person(name='Jack', age=30, gender='male')#zachowuje sie jak krotka, ale mozna sie odwolywac przez parametry
print(f'Namedtuple representation {jack}')

print(f'Field by name: {jack.name}')

jane = Person(name='Jane', age=29, gender='female')

print(f'Field by name: {jane.age}')
print(jane[0]) #mozna tez sie odwolywac klasycznie
