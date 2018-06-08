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
hd1, hd2, variables, datapoints, df = load('data/ctd/stations_25-01-2017_processed.cnv')

# Loading metadata
metadata = pd.read_csv('data/csv/coordenadas_2501.csv', sep = ';')
stations, lat, lon = list(metadata['Ponto']), list(metadata['Lat']), list(metadata['Lon'])

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)


'''
Saída 2 - 27-05-2017
'''
# Loading the data
hd1, hd2, variables, datapoints, df = load('data/ctd/stations_27-05-2017_processed.cnv')

# Loading metadata
metadata = pd.read_csv('data/csv/coordenadas_2705.csv', sep = ';')
stations, lat, lon = list(metadata['Ponto']), list(metadata['Lat']), list(metadata['Lon'])

# This particular day (27-05) there was a test station before sampling.
stations, lat, lon = ['test'] + stations, ['test'] + lat, ['test'] + lon

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)

'''
Saída 3 - 08-07-2017
'''
# Loading the data
hd1, hd2, variables, datapoints, df = load('data/ctd/stations_08-07-2017_processed.cnv')

# Loading metadata
metadata = pd.read_csv('data/csv/coordenadas_0807.csv', sep = ';')
stations, lat, lon = list(metadata['Estacao']), list(metadata['Lat']), list(metadata['Lon'])

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)

'''
Saída 4 - 01-10-2017
'''
# Loading the data
hd1, hd2, variables, datapoints, df = load('data/ctd/stations_01-10-2017_processed.cnv')

# Loading metadata
metadata = pd.read_csv('data/csv/coordenadas_0110.csv', sep = ';')
stations, lat, lon = list(metadata['Ponto']), list(metadata['Lat']), list(metadata['Lon'])

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)
