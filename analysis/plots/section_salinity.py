'''
Load data template.
'''
# Importing libraries
import pandas as pd
from code.functions import *

saida1 = 'data/ctd/stations_25-01-2017_processed.cnv'
saida2 = 'data/ctd/stations_27-05-2017_processed.cnv'
saida3 = 'data/ctd/stations_08-07-2017_processed.cnv'
saida4 = 'data/ctd/stations_01-10-2017_processed.cnv'

# Loading the data
hd1, hd2, variables, datapoints, alldata = load(saida3)

# Loading metadata
df = pd.read_csv('data/csv/coordenadas.csv', sep = ';')
dates = set(df['Data'])
dates = list(dates)
today = dates[3]
stations = list(df.loc[df['Data'] == today]['Ponto'])
lat = list(df.loc[df['Data'] == today]['Lat'])
lon = list(df.loc[df['Data'] == today]['Lon'])


# [i.insert(3,'test') for i in [stations, lat, lon]] # saida1 e saida4
# stations, lat, lon = ['test'] + stations, ['test'] + lat, ['test'] + lon # saida2

# Splitting data into different stations
d = split_stations(datapoints, stations, variables, lat, lon)

# Removing upcasts
for st in d:
    d[st] = remove_upcast(d[st])

# Creating variables with stations from the dictionary
locals().update(d)

# Plot dependencies
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import geopandas as gp
import numpy as np

def sectionplot(arg, arg2 = None, arg3 = None):
    # Arrays storing salinity data in sals list
    sals = []
    for i in arg:
        sals.append(np.array(i['sal00:']))

    # Setting salinity range for colorbar
    sal_range = np.arange(1, 40.1, 1)

    # Arrays storing depth data in deps list
    deps = []
    for i in arg:
        deps.append(np.array(i['depSM:']))

    # Setting the x axis values for salinity
    x = np.array([])
    ix = 0
    for i in sals:
        x = np.append(x, [ix]*len(i))
        ix += 1

    # Setting the y axis values for depth
    y = np.array([])
    ix = 0
    for i in deps:
        y = np.append(y, i)
        ix += 1

    # Setting the color values
    z = np.concatenate(tuple(sals))

    # Generating the gridded data
    xi = np.linspace(np.min(x), np.max(x), 200)
    yi = np.linspace(np.min(y), np.max(y), 200)
    xi, yi = np.meshgrid(xi, yi)
    zi = mlab.griddata(x, y, z, xi, yi, interp='linear') #interp = 'linear' se der erro no Natgrid

    # Plotting the gridded data
    plt.figure() # Starting the figure object
    plt.pcolormesh(xi,yi,zi, vmin = z.min(), vmax = z.max()) # Adding the colour mesh
    plt.contour(xi, yi, zi, colors='k') # Contour lines
    plt.scatter(x,y,c=z, vmin = z.min(), vmax = z.max()) # Adding the scatter points
    plt.xticks(range(0, len(arg)+1), ["Estacao " + i['STATION'][0][2:] for i in arg])
    plt.colorbar().set_label('Salinidade')
    plt.axis([np.min(x), np.max(x), np.min(y), np.max(y)])
    plt.gca().invert_yaxis()
    plt.ylabel('Profundidade (m)')

    if arg2:
        plt.title(arg2)

    if arg3:
        plt.savefig(arg3+arg2.split()[0].strip()+'_section_', transparent=True)
    else:
        plt.show()


if __name__ == '__main__':
    arg = [st1, st7, st11, st14] # Test this with other stations
    sectionplot(arg, 'Canal da margem leste')

if __name__ == '__main__':
    arg = [st4, st5, st6] # Test this with other stations
    sectionplot(arg, 'Rio Tubarao')
