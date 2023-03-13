numbers = [1,3,5,7,9,12,19,21]

# printing numbers
i = 0
while i < len(numbers):
    print(numbers[i])
    i+=1
#print odd numbers from start and end given
start = int(input('Starting number:'))
final = int(input('final number:'))
i = start
while i < final:
    if i % 2 == 1:
        print(i)
    i += 1 

# Print 1-100 in descending order
i = 100
while i > 0:
    i -= 1
    print(i)

# print 5 numbers received from user sequentially
numbers = []

i = 0

while i <= 5:
    sayi = int(input(f'{i}. Sayi:'))
    numbers.append(sayi)
    i += 1
numbers.sort()
print(numbers)

# Unlimited product information you will receive from the user is stored in the list of products
# ask the user for the number of products
# make a distributionary list (name,price)
# print the products on the screen when the product adding process is finished
products = []

piece = int(input(('how many products do you want to add')))

i = 0

while i < piece:
    name = input('products name: ')
    price = input("products price: ")
    products.append({
        'name' : name,
        'price' : price,
    })
    i += 1

for product in products:
    print(f'products name {product["name"]} ve products price {product["price"]} ')