import pandas as pd
import numpy as np

# Pandas series is like Series([], dtype: float64)
pandas_series1 = pd.Series()
print(pandas_series1)

# making a things to pandas series
numbers = [20,30,40,50]
pandas_series2 = pd.Series(numbers)
print(f"The numbers list = {numbers}")
print(f"The numbers pandas series = \n{pandas_series2}")

letters = ['a','b','c','d']
pandas_series3 = pd.Series(letters)
print(f"The letters list = {letters}")
print(f"The letters pandas series = \n{pandas_series3}")

mix = ['a','b','c',20]
pandas_series4 = pd.Series(mix)
print(f"The mix list = {mix}")
print(f"The mix pandas series = \n{pandas_series4}")

dictionary = {'a':10,'b':20,'c':30,'d':40}
pandas_series5 = pd.Series(dictionary)
print(f"The dictionary list = {dictionary}")
print(f"The dictionary pandas series = \n{pandas_series5}")

scalar = 5
pandas_series6 = pd.Series(scalar)
print(f"The scalar = {dictionary}")
print(f"The scalar pandas series = \n{pandas_series6}")

# we can give our key names like
pandas_series7 = pd.Series(numbers, ['a','b','c','d'])
print(f"The number pandas series with keys ['a','b','c','d'] = \n{pandas_series7}")

pandas_series8 = pd.Series(scalar, letters)
print(f"The scalar pandas series with key letters= \n{pandas_series8}")

#pandas with numpy
random_numbers = np.random.randint(10,100)
pandas_series9 = pd.Series(random_numbers)
print(f"The random_numbers = {random_numbers}")
print(f"The random_numbers pandas series = \n{pandas_series9}")

numbers2 = np.array([20,30,40,50])
pandas_series10 = pd.Series(numbers2, ['a','b','c','d'])
print(f"The numbers2 = {numbers2}")
print(f"The numbers2 pandas series numbers2, ['a','b','c','d'] = \n{pandas_series10}")

#equations
print(f"The pandas series = \n{pandas_series10}")
print(f" pandas series[0] = {pandas_series10[0]}")
print(f" pandas series[-1] = {pandas_series10[-1]}")
print(f" pandas series first 2 elemans = \n{pandas_series10[:2]}")
print(f" pandas series last 2 elemans = \n{pandas_series10[-2:]}")
print(f" pandas series['a'] = {pandas_series10['a']}")
print(f" pandas series['d'] = {pandas_series10['d']}")
print(f" pandas series[['a','c']] = \n{pandas_series10[['a','c']]}")
# print(f" pandas series['e'] = {pandas_series10['e']}")   # error gives NaN
print(f"pandas series dimension is = {pandas_series10.ndim}")
print(f"pandas series data type is = {pandas_series10.dtype}")
print(f"pandas series shape is = {pandas_series10.shape}")
print(f"pandas series elemants total is = {pandas_series10.sum()}")
print(f"pandas series max elemants total is = {pandas_series10.max()}")
print(f"pandas series min elemants total is = {pandas_series10.min()}")
print(f"pandas series + pandas series = \n{pandas_series10+pandas_series10}")
print(f"pandas series + 50 = \n{pandas_series10+50}")
print(f"square root of pandas series  = \n{np.sqrt(pandas_series10)}")
print(f" is pandas series elemans >= 50 = \n{pandas_series10>=50}")
print(f" is pandas series elemans even numbers = \n{pandas_series10%2==0}")
print(f" is pandas series elemans even numbers = \n{pandas_series10[pandas_series10%2==0]}")

#example
opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total = opel2018 + opel2019
print(f"opel2018 + opel2019 = \n{total}")
print(f"astra brand total = {total['astra']}")
# print(f"combo brand total = {total['combo']}")   # gives error
