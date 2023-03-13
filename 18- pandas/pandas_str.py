import pandas as pd

data = pd.read_csv("datasets/nba.csv")

# NaN droping
data.dropna(inplace = True)

# # updating somevalues
# data["Name"] = data["Name"].str.upper() # data become upper letter
# data["Name"] = data["Name"].str.lower() # data become lower letter

# #finding something
# data["index"] = data["Name"].str.find('a') 
# data = data[data.Name.str.contains('Jordan')]

# # changing something to another thing
# data = data.Team.str.replace(' ','-')

# separating the name column into first and last name
data[['FirstName','LastName']] = data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand=True)

# printing just the first 10 data
print(data.head(10))