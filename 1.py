import collections
#krotka
jack = ('Jack', 30, 'male')

#nazwana krotka
Person = collections.namedtuple('Person', 'name age gender') #fabryka klas
#print(f'Type of Person:{type(Person)}')
person = Person( name='Piotr', age=50,  gender='male')
print(f'Nazywam się {person.name} mam lat {person.age}')
print(f'Nazywam się {person[0]} mam lat {person[2]}')

print(person)

TelNumer = collections.namedtuple('TelNumber', 'area_code, number delimiter')
tel1 = TelNumer(area_code='+48', delimiter='-', number='111111111')
tel2 = TelNumer(area_code='+48', delimiter='-', number='222222222')
tel3 = TelNumer(area_code='+48', delimiter='-', number='333333333')
print(f'{tel1.area_code}{tel1.delimiter}{tel1.number}')
print(f'{tel2.area_code}{tel2.delimiter}{tel2.number}')
print(f'{tel3.area_code}{tel3.delimiter}{tel3.number}')
