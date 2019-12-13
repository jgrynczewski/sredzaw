#program ktory zliczy wystąpienia lister w tekscie

def zlicz_litery(word):
    letters_counter={};

    for ind in word.lower():
        if ind in letters_counter:
            letters_counter[ind] +=1
        else:
            letters_counter[ind] = 1
    print(letters_counter)


word = input("Podaj inwokację: ")
zlicz_litery(word)

print("używamy struktury danych defaultdict z modułu collections")
from collections import defaultdict

#jesli klucz nie ustneije to go utworzy z wartością domyślną
counter = defaultdict(int)
for char in word.lower():
    counter[char] += 1

print(counter)


print("używamy obiektu Counter z modułu collections")
from collections import Counter

#counter v1
cnt = Counter()

for char in word.lower():
    cnt[char] += 1
print(cnt)

#counter v2
#już w ogole najprościej w 1 linijce
print(Counter(word))

