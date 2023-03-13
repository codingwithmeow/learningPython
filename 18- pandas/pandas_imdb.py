"""
From data.worl imbd top 250 lists and 500 plus IMDB records I will
make data analysis
"""
import pandas as pd
import numpy as np

#reading csv file
df = pd.read_csv("datasets/imdb.csv")

# Information about the file.
print("The dataframe = \n" , df)
print("The dataframes columns = \n", df.columns)
print("The dataframes info = \n",df.info)

# showing the first 5 records
print("The first 5 record of the dataframe is n", df.head())

# showing the first 10 records
print("The first 10 record of the dataframe is n", df.head(10))

# showing the last 5 records
print("The last 5 record of the dataframe is n", df.tail())

# showing the last 10 records
print("The last 10 record of the dataframe is n", df.tail(10))

# getting the Movie_Title column.
print("The Movie_Title column", df["Movie_Title"])

# Geting only the first 5 records containing the Movie_Title column.
print("The Movie_Title columns first 5 records", df["Movie_Title"].head())

# Geting only the first 5 records containing Movie_Title and 
# Rating column.
print("The Movie_Title and Ratings columns first 5 records", df[["Movie_Title","Rating"]].head())

# Geting only the last 7 records containing Movie_Title and 
# Rating column.
print("The Movie_Title and Ratings columns last 7 records", df[["Movie_Title","Rating"]].tail(7))

# getting the second 5 records containing Movie_Title and 
# Rating column.
print("The Movie_Title and Ratings columns the second 5 records", df[5:][["Movie_Title","Rating"]].head())
# or
print("The Movie_Title and Ratings columns the second 5 records", df[5:10][["Movie_Title","Rating"]])

# getting the first 50 records that only contain the Movie_Title 
# and Rating column and have an imdb score of 8.0 and above.
print("The irst 50 records that only contain the Movie_Title" +
      " and Rating column and have an imdb score of 8.0 and above ", 
      df[df["Rating"] >= 8.0][["Movie_Title","Rating"]].head(50))
    
# the names of the movies whose release date is between 2014 and 2015.
print("the names of the movies whose release date is between 2014 and 2015: \n", 
        df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <=2015) ])
# List the movies whose number of reviews (Num_Reviews) 
# is greater than 100,000 or whose imdb score is between 8 and 9.
print("List the movies whose number of reviews is greater than 100,000"+ 
    " or whose imdb score is between 8 and 9\n", 
        df[(df["Num_Reviews"] >= 100000) | (df["Rating"] >= 8) & (df["Rating"] <=9) ])

