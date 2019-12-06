# Zliczena

text = "ala ma kota, a kot ma alę"

slownik = {}
def counter(text):
    for char in text.lower():
        if char in slownik:
            slownik[char] += 1
        else:
            slownik[char] = 1
        return slownik

print(slownik)

# DEFaultDict
from collections import defaultdict

my_dict = defaultdict(int)
for char in text:
    my_dict[char] += 1

print(my_dict)

# counter
from collections import Counter

cnt = Counter()

for char in text:
    cnt[char] += 1

print(cnt)