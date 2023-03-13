import pandas as pd

dataframe = pd.read_csv("datasets/nba.csv")

#1 - Bring the first 10 records.
result1 = dataframe.head(10)
print(f"The first 10 record = {result1}")

#2 - How many records are there in total?
result2 = len(dataframe.index)
print(f"Total records in nba.csv = {result2}")

# 3- What is the average total salary of all players?
result3 = dataframe["Salary"].mean()
print(f"average total salary of all players = {result3}")

#4 What is the highest salary?
result4 = dataframe["Salary"].max()
print(f"The max salary = {result4}")

#5 - Who is the highest paid player?
result5 = dataframe[dataframe["Salary"]== dataframe["Salary"].max()]["Name"].iloc[0]
print(f"The highest paid player = {result5}")

# 6- Bring the names and teams of the players aged between 20-25 in descending order.
result6 = dataframe[(dataframe["Age"]>20) & (dataframe["Age"]<25)][["Name","Team","Age"]].sort_values("Age",ascending=False)
print(f"the names and teams of the players aged between 20-25 = \n{result6}")

#7- Which team does the player named "John Holland" play in?
result7 = dataframe[dataframe["Name"] == "John Holland"]["Team"].iloc[0]
print(f"Johm Holland's team = {result7}")

# 8- What is the average salary of the players according to the teams?
result8 = dataframe.groupby("Team").mean()["Salary"]   #groupby used for splitting
print(f"the average salary of the players according to the teams =\n{result8}")

#9- How many different teams are there?
#first usin len()
result9 = len(dataframe.groupby("Team"))
print(f"There are {result9} teams")
# second using nunique() which is a function counts number f distinct elements
result10 = dataframe["Team"].nunique()
print(f"There are {result10} teams")

#10- How many players play on each team?
result11 = dataframe["Team"].value_counts()
print(f"players play on each team = \n{result11}")

# 11- Find the records with "and" in the name.
#first
dataframe.dropna(inplace=True)
result12 = dataframe[dataframe["Name"].str.contains("and")]
print(f"the records with 'and' in the name = \n{result12}")
#second
def str_find(name):
    if "and" in name.lower():
        return True
    return False

result13 = dataframe[dataframe["Name"].apply(str_find)]
print(f"the records with 'and' in the name = \n{result13}")
