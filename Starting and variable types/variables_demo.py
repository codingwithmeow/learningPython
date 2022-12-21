#string definitions
client_name = 'Cansu'
client_lastname= 'TAVUR'
client_adress = 'istanbul Beykoz' 
print("Client name: ",client_name,"\nClient lastname: ",client_lastname,"\nClient adress: ",client_adress)
print(type(client_name))
print(type(client_lastname))
print(type(client_adress))

#string addition
client_fullname = client_name + ' ' + client_lastname
print("Client fullname: ",client_fullname)
print(type(client_fullname))

#we can give int in string
client_ID = '12345678'
print(client_ID)
print(type(client_ID))
#we want to use int in string we can use
client_birtdayyear = int("1989")
client_age = 2022 - client_birtdayyear   #calculation

print(client_age)
print(type(client_age))

# we can use int + float and result will be float
order1 = 110
order2 = 11000.5
order3 = 356.95

total = order1 + order2 + order3

print("Total: ", total)
print(type(total))
