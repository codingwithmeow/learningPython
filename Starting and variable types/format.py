"""There are many uses, the most common being to make printing easier with the print function.
It is used to call a defined object to the print function."""
name = 'C'
surname = 'T'

#Format using
print('My name is {} {}' .format(name,surname))
print('My name is {1} {0}' .format(name,surname))
print('My name is {s} {n}' .format(n=name,s=surname))

age = 36
print('My name is {} {} and I am {} years old' .format(name,surname,age))


