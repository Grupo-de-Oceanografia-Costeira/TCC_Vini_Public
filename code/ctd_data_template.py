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

'''
Saída 1 - 25-01-2017
'''

# Loading the data
hd1, hd2, variables, datapoints, alldata = load('data/ctd/stations_25-01-2017_processed.cnv')

# Loading metadata
df = pd.read_csv('data/csv/coordenadas.csv', sep = ';')
stations = list(df.loc[df['Data'] == '25-Jan-17']['Ponto'])
lat = list(df.loc[df['Data'] == '25-Jan-17']['Lat'])
lon = list(df.loc[df['Data'] == '25-Jan-17']['Lon'])

[i.insert(3,i[2]) for i in [stations, lat, lon]]


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
    top.append(i['t090:'][0])
    bot.append(i['t090:'][len(i)-1])
    names.append(i['STATION'][0])

top, bot, names = pd.Series(top), pd.Series(bot), pd.Series(names)

df = pd.DataFrame([top, bot, names])
df = df.transpose()
df.to_csv('./25-jan-temp.csv')

'''
Saída 2 - 27-05-2017
'''
# Loading the data
hd1, hd2, variables, datapoints, df2 = load('data/ctd/stations_27-05-2017_processed.cnv')

# Loading metadata
df = pd.read_csv('data/csv/coordenadas.csv', sep = ';')
stations = list(df.loc[df['Data'] == '27-May-17']['Ponto'])
lat = list(df.loc[df['Data'] == '27-May-17']['Lat'])
lon = list(df.loc[df['Data'] == '27-May-17']['Lon'])
#stations, lat, lon = list(metadata['Ponto']), list(metadata['Lat']), list(metadata['Lon'])

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
    top.append(i['t090:'][0])
    bot.append(i['t090:'][len(i)-1])
    names.append(i['STATION'][0])

top, bot, names = pd.Series(top), pd.Series(bot), pd.Series(names)

df = pd.DataFrame([top, bot, names])
df = df.transpose()
df.to_csv('./27-may-temp.csv')

'''
Saída 3 - 08-07-2017
'''
# Loading the data
hd1, hd2, variables, datapoints, df = load('data/ctd/stations_08-07-2017_processed.cnv')

# Loading metadata
df = pd.read_csv('data/csv/coordenadas.csv', sep = ';')
stations = list(df.loc[df['Data'] == '08-Jul-17']['Ponto'])
lat = list(df.loc[df['Data'] == '08-Jul-17']['Lat'])
lon = list(df.loc[df['Data'] == '08-Jul-17']['Lon'])

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)

top, bot, names = [], [], []

for i in st_list:
    top.append(i['t090:'][0])
    bot.append(i['t090:'][len(i)-1])
    names.append(i['STATION'][0])

top, bot, names = pd.Series(top), pd.Series(bot), pd.Series(names)

df = pd.DataFrame([top, bot, names])
df = df.transpose()

df.to_csv('./07-jul-temp.csv')

'''
Saída 4 - 01-10-2017
'''
# Loading the data
hd1, hd2, variables, datapoints, df = load('data/ctd/stations_01-10-2017_processed.cnv')

# Loading metadata
df = pd.read_csv('data/csv/coordenadas.csv', sep = ';')
stations = list(df.loc[df['Data'] == '01-Oct-17']['Ponto'])
lat = list(df.loc[df['Data'] == '01-Oct-17']['Lat'])
lon = list(df.loc[df['Data'] == '01-Oct-17']['Lon'])

[i.insert(3,i[2]) for i in [stations, lat, lon]]

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)

top, bot, names = [], [], []

for i in st_list:
    top.append(i['t090:'][0])
    bot.append(i['t090:'][len(i)-1])
    names.append(i['STATION'][0])

top, bot, names = pd.Series(top), pd.Series(bot), pd.Series(names)

df = pd.DataFrame([top, bot, names])
df = df.transpose()

df.to_csv('./01-oct-temp.csv')
