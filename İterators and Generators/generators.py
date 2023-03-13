# generators are generally an iterator that does not occupy memory
#produces

def cube():
    for i in range(5):
        yield i**3 #calculates the value, doesn't store it in an address, you can't call it a second time

# generator = cube()
# iterator = iter(generator)
# iterator = cube()

# for i in iterator:
#     print(i)

for i in cube():
    print(i)
print(cube())

liste0 = [i**3 for i in range(5)]
print(liste0)

generator = (i**3 for i in range(5))
print(generator)
for i in generator:
    print(i)