"""
key - value
41=> kocaeli 34=> İstanbul
"""
plaka = {'kocaeli' : 41 ,'istanbul' : 34}

# accessing key variables values
print(f"Plaka dictionary [kocel] key = {plaka['kocaeli']}")
print(f"Plaka dictionary [istanbul] key = {plaka['istanbul']}")

# can change values with
plaka['ankara'] = 6
plaka['koceli'] = 12

#printing dictionary
print(f"the new plaka dictionary = {plaka}")

users = {
    'cansutavur' :{
        'age' : 26,
        'roles' : ['admin','user'],
        'email': '@gmail.com',
        'adres' : 'istanbul',
        'phone' : 123543
    }
}

print(f"Users cansutavur information = {users['cansutavur']}")
print(f"Users cansutavur age information = {users['cansutavur']['age']}")
print(f"Users cansutavur roles information = {users['cansutavur']['roles'][0]}")
