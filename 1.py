import collections
import math import pi
import math import *

jack = ('Jack', 30, 'male')
print(f'Tuple representation {jack}')

Person = collections.namedtuple('Person', 'name age gender')
print(f'Type of person: {type(Person)}')
jack = Person(name = 'Jake', age = 30, gender = 'male')
print(f'Nametuple representation: {jack}')

print(f'Field by name: {jack.name}')

jane = Person(name = 'Jane', age = 23, gender = 'female')
print(f'Field by age: {jane.age}')

Telephone = collections.namedtuple('Telephone', 'number area_code delimiter')
nr_magda = Telephone(number = '694939941', area_code = '+48', delimiter = '-')
print(f'Numer Magdy: {nr_magda.area_code}{nr_magda.delimiter}{nr_magda.number}')

nr_niemca = Telephone(number = '666939881', area_code = '+44', delimiter = '-')
print(f'Numer Niemca: {nr_niemca.area_code}{nr_niemca.delimiter}{nr_niemca.number}')


