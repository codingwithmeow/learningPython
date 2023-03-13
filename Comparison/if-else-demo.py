"""
Asking the user for name, age and education information
Check your license status. 
"""
isim = input('name:')
age = int(input('your age:'))
education = input('aducation: ')

if age >= 18: 
    if education == 'higscholl'or education=='univercity':
        print('you can have your licence')
    else:
        print('you can not have it')
else:
    print('you cant have your license your young')


# Grade information according to grade range 
# with the average of 2 written and 1 oral grades?

exam1 = float(input('first exam:'))
exam2 = float(input('second exam:'))
exam3 = float(input('third exam:'))

average = ( exam1 + exam2 + exam3) / 3

if average >= 0 and average <25:
    print("0")
elif average >= 25 and average < 45:
    print("1")
elif average >= 45 and average < 55:
    print("2")
elif average >= 55 and average < 70:
    print("3")
elif average >= 70 and average < 85:
    print("4")
elif average >= 85 and average < 100:
    print("5")
else:
    print("somethings wrong")


# service time of a vehicle?

import datetime
 
date = input('what date was the vehicle trafficked(2019/8/9):')
date = date.split('/')

trafficOut = datetime.datetime(int(date[0]),int(date[1],int(date[2])))
current_time =datetime.datetime.now()
difference = current_time - trafficOut
days = difference.days

if days <= 365:
    print("1. service")
elif days > 365:
    print("2. service")
elif days > 365*2:
    print("3. service")
else :
    print("wrong")



# 1 - Is a number entered between 0-100
num1 = float(input("number:"))
result1 = num1 > 0 and num1 <100
print(f"number is between 0 and 100 {result1}")
