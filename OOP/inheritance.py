# inheritance (kalıtım) miras alma

#person => name ,lastname,age,eat(),run(),drink()
#student(person), teacher(person)

class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print('person created')
    def who_am_i(self):
        print('ı am a person')
    def eat (self):
        print('ı am eating')
    
class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber = number
        print('student created')
    #override
    def who_am_i(self):
        print('ı am a student')

    def sayHello(self):
        print('Hi ı am a student')

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch
    def who_am_i(self):
        print(f'ı am a {self.branch} teacher')
    

p1 = Person('Cansu','Tavur')
s1 = Student('Cansu','Tavur','16067018')
t1 = Teacher('Serkan','yılmaz','math')

print(p1.firstname+' '+p1.lastname)
print(s1.firstname+' '+s1.lastname+' '+s1.studentNumber)

s1.who_am_i()

print(t1.firstname+' '+t1.lastname)
t1.who_am_i()