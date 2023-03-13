# 1- Which of the 2 numbers entered is greater
num1 = int(input("first number"))
num2 = int(input("second number"))

result1 = num1 > num2
print(f"number 1 :{num1} number 2 {num2}: {result1} ")

# Get 2 midterm 60% and final 40% grades from the user and calculate the average
# passed if average is above 50
mid1 = int(input("first midterm"))
mid2 = int(input("second midterm"))
final = int(input("final exam"))

average = ((mid1+mid2)/2) * 0.6 + final * 0.4
result2 = average > 50
print(f"You passed  {result2} ")

# print whether a number entered is odd or even
num3 = int(input("first number"))
result3 = (num3 % 2 == 0)
print(f"Sayi cift {result3} ")

# entered number is positive or negative
num4 = int(input("first number"))
result3 = (num4 > 0)
print(f"number positive {result3} ")

# ask for password and email information and check it is correct
email = 'abc@gmail.com'
pasword = 'abc123'

entered_email = input("email")
entered_pasword = input("pasword")

result4 = email == entered_email
result5 = pasword == entered_pasword
print(f"email is correct :{result4} pasword is correct:{result5} ")
