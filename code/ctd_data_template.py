'''
Load data template. Includes load(), metadata, split_stations(),
remove_upcast() and locals().update().

Inputs:

load() - data/ctd/<DATE>.cnv
metadata() - data/csv/coordenadas_<DATE>.csv

'''
# Dependencies
import pandas as pd
from code.functions import *

saida1 = 'data/ctd/stations_25-01-2017_processed.cnv'
saida2 = 'data/ctd/stations_27-05-2017_processed.cnv'
saida3 = 'data/ctd/stations_08-07-2017_processed.cnv'
saida4 = 'data/ctd/stations_01-10-2017_processed.cnv'
df = pd.read_csv('data/csv/coordenadas.csv', sep=';')
dates = set(df['Data'])
dates = list(dates)

'''
Saída 1 - 25-01-2017
'''

# Loading the data
hd1, hd2, variables, datapoints, alldata = load(saida1)

# Loading metadata
today = dates[2]
stations = list(df.loc[df['Data'] == today]['Ponto'])
lat = list(df.loc[df['Data'] == today]['Lat'])
lon = list(df.loc[df['Data'] == today]['Lon'])


[i.insert(3, i[2]) for i in [stations, lat, lon]]


# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)

# Let's put them all into lists
st_list = list(d.values())

# Picking out surface and bottom temperatures
top, bot, names = [], [], []

for i in st_list:
    top.append(i['sal00:'][0])
    bot.append(i['sal00:'][len(i)-1])
    names.append(i['STATION'][0])

top, bot, names = pd.Series(top), pd.Series(bot), pd.Series(names)

df2 = pd.DataFrame([top, bot, names])
df2 = df2.transpose()
df2.to_csv('./25-jan-sal.csv')

'''
Saída 2 - 27-05-2017
'''
# Loading the data
hd1, hd2, variables, datapoints, alldata = load(saida2)

# Loading metadata
today = dates[0]
stations = list(df.loc[df['Data'] == today]['Ponto'])
lat = list(df.loc[df['Data'] == today]['Lat'])
lon = list(df.loc[df['Data'] == today]['Lon'])

# This particular day (27-05) there was a test station before sampling.
stations, lat, lon = ['test'] + stations, ['test'] + lat, ['test'] + lon

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)

# Let's put them all into lists
st_list = list(d.values())

top, bot, names = [], [], []

for i in st_list:
    top.append(i['sal00:'][0])
    bot.append(i['sal00:'][len(i)-1])
    names.append(i['STATION'][0])

top, bot, names = pd.Series(top), pd.Series(bot), pd.Series(names)

df2 = pd.DataFrame([top, bot, names])
df2 = df2.transpose()
df2.to_csv('./27-may-sal.csv')

'''
Saída 3 - 08-07-2017
'''
# Loading the data
hd1, hd2, variables, datapoints, alldata = load(saida3)

# Loading metadata
today = dates[3]
stations = list(df.loc[df['Data'] == today]['Ponto'])
lat = list(df.loc[df['Data'] == today]['Lat'])
lon = list(df.loc[df['Data'] == today]['Lon'])

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)

st_list = list(d.values())

top, bot, names = [], [], []

for i in st_list:
    top.append(i['sal00:'][0])
    bot.append(i['sal00:'][len(i)-1])
    names.append(i['STATION'][0])

top, bot, names = pd.Series(top), pd.Series(bot), pd.Series(names)

df2 = pd.DataFrame([top, bot, names])
df2 = df2.transpose()

df2.to_csv('./08-jul-sal.csv')

'''
Saída 4 - 01-10-2017
'''
# Loading the data
hd1, hd2, variables, datapoints, alldata = load(saida4)

# Loading metadata
today = dates[1]
stations = list(df.loc[df['Data'] == today]['Ponto'])
lat = list(df.loc[df['Data'] == today]['Lat'])
lon = list(df.loc[df['Data'] == today]['Lon'])

[i.insert(3, i[2]) for i in [stations, lat, lon]]

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)

st_list = list(d.values())

top, bot, names = [], [], []

for i in st_list:
    top.append(i['sal00:'][0])
    bot.append(i['sal00:'][len(i)-1])
    names.append(i['STATION'][0])

top, bot, names = pd.Series(top), pd.Series(bot), pd.Series(names)

df2 = pd.DataFrame([top, bot, names])
df2 = df2.transpose()

df2.to_csv('./01-oct-sal.csv')
