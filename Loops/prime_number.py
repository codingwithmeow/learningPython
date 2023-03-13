number = int(input('sayi: '))
prime_number = True
if number == 1:
    print('number 1 is not a prime number')

for i in range (2,number):
    if(number %i == 0):
        prime_number= False
        break

if prime_number:
    print('Number is prime number')
else:
    print('Number is not prime number')