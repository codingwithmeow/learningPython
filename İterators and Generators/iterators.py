# Elements with _iter_ are an iterable object. you need to create an iterator to navigate through
"""
liste = [1,2,3,4,5]

iterator = iter(liste)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
"""

class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __next__(self):     
        return self

    def __next__(self):     
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(10,20)

for x in list:
    print(x)
 