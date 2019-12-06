#zliczenia

text ='ala ma kota, a kot ma ale'

def f(text):
    my_dict = dict()
    for char in text:
        if char not in my_dict.keys():
            my_dict[char] = 1
        else:
            my_dict[char] = my_dict[char]+1
    print(my_dict)

f(text)


from collections import  defaultdict
my_defauldict = defaultdict(int)
for char in text:
    my_defauldict[char]+=1
print(my_defauldict)


from collections import  Counter
print(Counter(text))



class A:
    pass

class B:
    pass

object_a = A()
object_b = B()
object_list = [object_a, object_b, object_b]
print(Counter(object_list))