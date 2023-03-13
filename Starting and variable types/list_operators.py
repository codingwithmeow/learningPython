numbers1 = [x for x in range(10)]
print(numbers1)

numbers2 = [x**2 for x in range(10)]
print(numbers2)

numbers3 = [x**2 for x in range(10)if x%3==0]
print(numbers3)

#string printing
mysrting = 'hello'
mylist = []

for letter in mysrting:
    mylist.append(letter)
print(mylist)

mylist = [letter for letter in mylist]
print(mylist)

# we can calculations like
years =[1983, 1999, 2008, 1956, 1986]
ages = [2019-year for year in years]
print(f"years = {years}")
print(f"2019 - years = {ages}")

results = [ x if x%2==0 else 'TEK' for x in range(1,10)]
print(results)

result=[]

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers = [ (x,y) for x in range(3)for y in range(3)]
print(numbers)

numbers = [ (x,y,z) for x in range(3)for y in range(3) for z in range(3)]
print(numbers)