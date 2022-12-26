students = {
    '120' : {
        'name' : 'Ali',
        'lastname' : 'Yılmaz',
        'phone' : '532 00 00 01'
    },
    '125' : {
        'name' : 'Can',
        'lastname' : 'Korkmaz',
        'phone' : '532 00 00 02'
    },
    '128' : {
        'name' : 'Volkan',
        'lastname' : 'Korkmaz',
        'phone' : '532 00 00 03'
    },
}
""" 1 - Store the given information in the dictionary with the information you receive from the user.
    2 - Get the student number from the user and show the relevant student information
"""
students = {}

number = input("student no: ")
name = input("student name: ")
surname = input("student lastname: ")
phone = input("student phone: ")

students.update ( {
    number : {
        'name' : name,
        'lastname' : surname,
        'phone' : phone
    },
})

print(students)