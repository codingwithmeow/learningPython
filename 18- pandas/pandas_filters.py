import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])

print(df.head()) # gives first 5 data
print(df.head(10)) # gives first 10 data

print(df.tail()) # gives last 5 data
print(df.tail(10)) # gives first 10 data

print(df["Column1"].head()) #gives column1's 5 first data
print(df.Column1.head()) #gives first column1's 5 data

print(df["Column1"].tail()) #gives column1's 5 last data
print(df.Column1.tail()) #gives column1's last 5 data

print(df[["Column1","Column2"]].head()) #gives column1's and columns'2 first 5 data
print(df[["Column1","Column2"]].tail()) #gives column1's and columns'2 last 5 data

print(df[5:15]) #gives between 5 and 15
print(df[5:15][["Column1","Column2"]].head()) #gives column1's and column2's between 5 and 15 first 5 data
print(df[5:15][["Column1","Column2"]].tail()) #gives column1's and column2's between 5 and 15 last 5 data

print(df > 50) # gives true if bigger than 50 else false
print(df[df > 50]) # gives data if bigger than 50 else Nan

print(df[df % 2 == 0]) # gives data if even else Nan
print(df[df["Column1"] > 50]) # gives data if bigger than 50 for column1 

print(df[df["Column1"] > 50][["Column1","Column2"]]) # gives data if bigger than 50 for just column1 and column2
print(df[(df["Column1"] > 50) & (df["Column1"] <= 70)]) # gives data if condition true for just column1
print(df[(df["Column1"] > 50) & (df["Column2"] <= 70)]) # gives data if and condition true and the data
print(df[(df["Column1"] > 50) | (df["Column2"] > 50)]) # gives data if or condition true and the data
print(df[(df["Column1"] > 50) | (df["Column2"] > 50)][["Column1","Column2"]]) # gives data if condition true for just column1 and column2

# query function used for condition as above
print(df.query("Column1 >= 50 & Column1 % 2 == 0"))
print(df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]])
