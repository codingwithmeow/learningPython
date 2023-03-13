import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

print("the database\n",df)

print("non-repeating values in column2\n",df["Column2"].unique())
print("the number of repeating values in column2\n",df["Column2"].value_counts())
print("the 2 times of the values in the column1",df["Column1"]*2)

def square(x):
    return x * x

print("the square of the values in the column1",df["Column1"].apply(square))
square2 = lambda x: x*x
print("the square of the values in the column1",df["Column1"].apply(square2))
print("the square of the values in the column1",df["Column1"].apply(lambda x: x*x))

print("the number of char in column3",df["Column3"].apply(len))

print("dataframe's columns", df.columns)
print("dataframe's columns lenght", len(df.columns))
print("dataframe's index", df.index)
print("dataframe's index lenght", len(df.index))
print("dataframe's info", df.info)

# allignment
print("For column2",df.sort_values("Column2"))
print("For column3",df.sort_values("Column3"))
print("For column3 in decreasing",df.sort_values("Column3", ascending = False))

# another example
data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

print(df.pivot_table(index="Ay",columns= "Kategori", values= "Gelir"))
