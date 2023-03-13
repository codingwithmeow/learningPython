import pandas as pd
from numpy.random import randn

dataframe = pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
print(dataframe)

result1 = dataframe["Column1"]
print(f"First column of dataframe = \n{result1} \nand datatype = {type(result1)}")

result2 = dataframe[["Column1","Column2"]]
print(f"dataframes column1 and column2 = \n{result2}")

#loc["row","column"] , loc["row"] , loc[:,"column"]
result3 = dataframe.loc["A"]
print(f"dataframes A index = \n{result3} \nand datatype = {type(result3)}")

result4 = dataframe.loc[:,"Column1"]
print(f"First column of dataframe = \n{result4}")

result5 = dataframe.loc[:,["Column1","Column2"]]
print(f"dataframes column1 and column2 = \n{result5}")

result6 = dataframe.loc[:,"Column1":"Column3"]
print(f"dataframes columns = \n{result6}")

result7 = dataframe.loc[:,:"Column2"]
print(f"dataframes throug column2 = \n{result7}")

result8 = dataframe.loc["A":"B",:"Column2"]
print(f"data frame column2 A and B index = {result8}")

result9 = dataframe.loc[:"B",:"Column2"]
print(f"data frame column2 through B index = {result9}")

result10 = dataframe.loc["A","Column2"]
print(f"data frame column2 A index = {result10}")

result11 = dataframe.loc["C","Column1"]
print(f"data frame column1 C index = {result11}")

result12 = dataframe.loc[["A","B"],["Column1","Column2"]]
print(f"data frame column1 column2 A and B index = {result12}")

#resulting index
result13 = dataframe.iloc[2]
print(f"dataframe 2. index = {result13}")

# adding column
dataframe["Column4"] = pd.Series(randn(3),["A","B","C"])
print(f"after adding column4 new dataframe = \n{dataframe}")

dataframe["Column5"] = dataframe["Column1"] + dataframe["Column3"]
print(f"after adding column5 new dataframe = \n{dataframe}")

# delete column
result14 = dataframe.drop("Column5",axis=1, inplace=False)   # axis=0 for x axis=1 for y
print(f"after deleting column5 new dataframe = \n{result14} \nold dataframe = \n{dataframe}")

dataframe.drop("Column5",axis=1, inplace=True)   # axis=0 for x axis=1 for y
print(f"after deleting column5 new dataframe = \n{dataframe} \nold dataframe = \n{dataframe}")
