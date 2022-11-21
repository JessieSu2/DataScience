from urllib.request import urlretrieve
import pandas as pd

url = 'https://data.cityofnewyork.us/resource/pvqr-7yc4.csv'
urlretrieve(url, 'pvqr-7yc4.csv')

df = pd.read_csv('pvqr-7yc4.csv', sep=';')

print(df.head(3))