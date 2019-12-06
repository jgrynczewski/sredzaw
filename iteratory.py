# Iteratory

my_list = [1,2,3,4]
for item in my_list:
    print(item)

for item in 'asd"':
    print(item)

alist= [1,2,3 ,4]
my_iterator  = iter(alist)
while True:
    try:
        item = (next(my_iterator))
        print(item)
    except StopIteration:
        break


class MyCounter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current -1

my_iterator_2 = MyCounter(5,100)
print(list(my_iterator_2))

for item in my_iterator_2:
    print(list(item))
