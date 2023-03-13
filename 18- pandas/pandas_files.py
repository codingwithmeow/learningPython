import sqlite3
import pandas as pd

# csv file reading
dataframe1 = pd.read_csv('datasets\samples.csv')
print(dataframe1)

# json file reading
dataframe2 = pd.read_json('datasets\sample.json',encoding="UTF-8")
print(dataframe2)

# xlsx file reading(should be downloaded pip install xlrd or pip install openpyxl)
dataframe3 = pd.read_excel('datasets\sample.xlsx')
print(dataframe3)

# db file reading( should be downloaded pip install pysqlite3 )
connection =sqlite3.connect('datasets\sample.db') 
dataframe4 = pd.read_sql_query("SELECT * FROM students",connection)
print(dataframe4)

