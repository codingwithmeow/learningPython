import json
import os

class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRespository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        #load user from. json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user['username'],password=user['password'],email=user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self,user : User):
        self.users.append(user)
        self.savetoFile()
        print("User created")

    def login(self,username,password):
        for user in self.users: 
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Logged in.")
                break

    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('users.json','w') as file:
            json.dump(list, file)

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Logged out.")

    def identity(self):
        if self.isLoggedIn:
            print(f'username : {self.currentUser.username}')
        else:
            print("There is no logged in person")

respository = UserRespository()

while True:
    print("Menü".center(50,"*"))
    print("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit")
    choose = input("Your Choose:")
    if choose == '5':
        break
    else:
        if choose == '1':
            username = input("Username: ")
            password = input("Passwoord: ")
            email = input("email: ")
            user = User(username=username,password=password,email=email)
            respository.register(user)

        elif choose == '2':
            if respository.isLoggedIn:
                print("Your are already logged in")
            else:
                username = input("Username: ")
                password = input("Passwoord: ")
                respository.login(username,password)

        elif choose == '3':
            respository.logout()

        elif choose == '4':
            respository.identity()