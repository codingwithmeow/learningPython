import pandas as pd
import numpy as np

staf = {
    'Employe': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Department': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Age': [30,25,45,50,23,34,42],
    'Place': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Salary': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(staf)

print("Total salary = ", df["Salary"].sum())

# grouping
print("The groups are for department = ", df.groupby("Department").groups)

print("The groups are for department and living place  = ", df.groupby(["Department","Place"]).groups)

places = df.groupby("Place")
for name, group in places:
    print(name)
    print(group)

for name, group in df.groupby("Department"):
    print(name)
    print(group)


print("The groups are for places at Kadiköy/n", df.groupby("Place").get_group("Kadıköy"))

print("The groups are for deparment at muhasebe/n", df.groupby("Department").get_group("Muhasebe"))

print("the sum of departmet",df.groupby("Department").sum())

print("the mean of departmet",df.groupby("Department").mean())

print("the mean of departmets salary",df.groupby("Department")["Salary"].mean())

print("the mean of places age",df.groupby("Place")["Age"].mean())

print("the mean of places salary",df.groupby("Place")["Salary"].mean())

print("the number of employes for places",df.groupby("Place")["Employe"].count())

print("the max of departmon for age",df.groupby("Department")["Age"].max())

print("the min of departmon for salary",df.groupby("Department")["Salary"].min())


result = df.groupby("Department")["Salary"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]
print(result)
