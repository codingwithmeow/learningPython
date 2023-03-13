list = ["1","2","5a","10b","abc","10","50"]
"""
# 1: Find numeric values in list elements

for x in list:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

# Make sure that every input you receive is a number 
#unless the user enters the 'q' value, otherwise write a g-error message

while True:
    number = input('Number: ')
    if number == 'q':
        break

    try:
        result1= float(number)
        print('entered number ', result1)
        break
    except ValueError:
        print('invalid number')
        continue
## 3: Give the error of Turkish characters in the entered password

def checkPassword(pasword):
    Turkish_charactersr = 'şçğüöi'

    for i in pasword:
        if i in Turkish_charactersr:
            raise TypeError('Password cannot contain Turkish characters')
        else:
            pass
    print('parola okey')

parola = input('Pasword: ')

try:
    checkPassword(password)
except TypeError as er:
    print(er)
"""
# 4: Error for the value that comes to the function after creating the factorial function
# give messages#

def faktoriyel(n):
    n = int(n)
    if n < 0:
        raise ValueError('Negative value')
    resullt2 = 1
    for i in range(1, n+1):
        resullt2 *= i
    return resullt2 

for x in [5,10,-3,'10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue

    print(y)
