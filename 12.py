# Iteratory

my_list = [1, 2, 3, 4]

for item in my_list:
    print(item)


my_iterator = iter(my_list)
while True:
    try:
        item = next(my_iterator)
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
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current-1

my_iterator = MyCounter(3, 6)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator)) -> StopIteration

my_counter = MyCounter(5, 100)
print(list(my_counter))

for item in my_counter:
    print(item)