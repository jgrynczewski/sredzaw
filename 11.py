# zliczenia

text = 'ala ma kota, a kot ma alę'

def zliczenia(text):
    lista = {}
    for char in text:
        if char not in lista.keys():
            lista[char] = 1
        else:
            lista[char] +=1
    print(lista)
    return lista

zliczenia(text)
#default dict
from collections import defaultdict

my_dict_2 = defaultdict(int)
for char in text:
    my_dict_2[char] += 1
print(my_dict_2)

# counter
from collections import Counter

cnt = Counter()

for char in text:
    cnt[char] += 1
print(cnt)

cnt2 = Counter(text)
print(cnt2)
print(counter)