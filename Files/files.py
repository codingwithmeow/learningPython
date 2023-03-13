"""
The open() function is used to open and create files.
open(file_name,file_access_method)
file_access_method-->
"w" : write write mode. creates the file at the location.
deletes file content and re-adds
"a" : append append. If the file is not in my command, create it.
"x" : create create. gives an error if the file already exists.
"r" : read rejection. default. If the file does not exist, it will throw an error.
"""

file = open("newfile.txt","w")
file.close() # to close the file

file2 = open("C:/Users/Casper/Desktop/newfile.txt","w")
print(file2)
file2.close()

file = open("newfile.txt","w",encoding='utf-8')
file.write("abc")
file.close()

file = open("newfile.txt","a",encoding='utf-8')
file.write("\ngalp")
file.close()

file = open("newfile2.txt","x",encoding='utf-8')

try:
    file = open("newfile.txt","r")
    print(file)
except FileNotFoundError:
    print("file read error")
finally:
    print("file closes")
    file.close()

file = open("newfile.txt","r", encoding="utf-8")
for i in file:
    print(i, end="")
    file.close()

""" READ() FUNCTION"""

file = open("newfile.txt","r", encoding="utf-8")
content = file.read()
content2 = file.read()
file.close()

print(content)
print(content2) # read before file close
# because it is done first, the cursor stays at the end and there is nothing to read

file = open("newfile.txt","r", encoding="utf-8")
content0 = file.read(5) # 5 bytes means 5 characters here
content1 = file.read(3)
print(content0)
print(content1)
file.close()

""" READLINE() FUNCTION"""
file = open("newfile.txt","r", encoding="utf-8")
content = file.readline()
print(content)
file.close()

""" READLINEs() FUNCTION"""

file = open("newfile.txt","r", encoding="utf-8")
list = file.readlines()
print(list[0])
print(list[1])
print(list[2])
file.close()