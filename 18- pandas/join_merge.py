import pandas as pd


customers = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

orders = {
    'OrderId': [10,11,12,13],
    'CustomerId': [1,2,5,7],
    'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
}

# making dataframe
df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

print(df_customers)
print(df_orders)

# using merge  function
print("Inner joint (just who has order)\n",pd.merge(df_customers,df_orders,how="inner"))
print("If there is no order becomes NaN\n",pd.merge(df_customers,df_orders,how="left"))
print("If there is a order but no owner\n",pd.merge(df_customers,df_orders,how="right"))
print("all records\n",pd.merge(df_customers,df_orders,how="outer"))

#second example
customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Turan","Yılmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA, columns = ["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns = ["CustomerId","FirstName","LastName"])

print(pd.concat([df_customersA,df_customersB])) # row
print(pd.concat([df_customersA,df_customersB],axis=1)) # column