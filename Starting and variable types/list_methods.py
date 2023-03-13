numbers = [1,10,5,16,4,9,10]
letters = ['a', 'g','s','b','y','a','s']

# finding min and max values
val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val= numbers[3:6]
numbers.append(49) # adds end of the list
numbers.insert(3,78) # adss 78 to third of the list
numbers.insert(-1,52) # adds 52 to before thee last element

numbers.pop()
print(numbers)
numbers.pop(0)
# numbers.remove(59) # looks for 59 and deleetes
numbers.sort() # alligns
letters.sort() 
numbers.reverse() # reverse order 
letters.reverse()

print(numbers.count(10)) # counts how many are 10
numbers.clear() # clears the list
print(letters)
print(numbers)





