x = 5
y = 25

x = y

y = 10

print(x,y)

# references types => list

a = ["apple", "banana"]
b = ["apple", "banana"]

a = b # Since the reference is assignment, the address of b is assigned to a. The change in b also affects a, even if it happens later.

b[0] = "grape"

print(a)
print(b)
