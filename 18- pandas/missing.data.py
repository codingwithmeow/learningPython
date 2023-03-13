import pandas as pd
import numpy as np

data = np.random.randint(10,1100,15).reshape(5,3)

df = pd.DataFrame(data, index = ['a','c','e','f','h'], columns = ['column1','column2','column3'])

df = df.reindex(['a','b','c','d','e','f','g','h'])

# adding column4
newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn

print(df)

# if you want the delete a row or a column 
print(df.drop("column1",axis=1))

print(df.drop(["column1","column2"],axis=1))

print(df.drop("a",axis=0))

print(df.drop(["a","b","h"],axis=0))

# if nan values exit
print("Is there a NaN value exit\n",df.isnull())
print("How many a NaN value exit = ",df.isnull().sum())

print("Is there not a NaN value\n",df.notnull())

print("In colum1 Is there a NaN value exit\n",df["column1"].isnull())
print("In colum1 how many Nan value exit",df["column1"].isnull().sum())

# Nan values
print(df[df["column1"].isnull()]["column1"])

#excapt the nan values
print(df[df["column1"].notnull()]["column1"])

# NaN values droping
# dropna If finds a NaN value it deletes all row
print("The dataset except NaN value \n", df.dropna()) # default axis = 0
print("The dataset except NaN value \n", df.dropna(axis=1))
print("The dataset except NaN value \n",df.dropna(how = "any"))

# if al the row NaN just deletes those rows
print(df.dropna(how = "all"))

print("",df.dropna(subset=["column1","column2"], how = "any"))
print("",df.dropna(subset=["column1","column2"], how = "all"))

print("et least 3 normal data",df.dropna(thresh = 2))

# NaN values filled
print("NaN values to no input\n", df.fillna(value = 'no input'))
print("NaN values to 1\n",df.fillna(value = 1))


def average(df):
    total = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return total / adet

# NaN values filled with average
print(df.fillna(value = average(df)))

print("The total of colunms", df.sum())
print("The total sum",df.sum().sum())
print("The size of the data", df.size)
print("The total of NaN values in colunms",df.isnull().sum())
print("The total of NaN values in the dataset",df.isnull().sum().sum())
