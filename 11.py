# Zliczenia

text = "ala ma kota, a kot ma alę"

# DICTIONARY
my_dict = {}

for char in text.lower():
    if char in my_dict:
        my_dict[char] += 1
    else:
        my_dict[char] = 1

print(my_dict)

# DEFAULTDICT
from collections import defaultdict

my_dict2 = defaultdict(int)
for char in text:
    my_dict2[char] += 1

print(my_dict2)

from collections import Counter

# Counter v.1
cnt = Counter()
for char in text:
    cnt[char] += 1

print(cnt)

# Counter v.2
print(Counter(text))