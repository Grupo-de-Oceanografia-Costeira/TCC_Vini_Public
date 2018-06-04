'''
Section plot 01-10

Load data template.
'''
# Importing libraries
import pandas as pd
from code.functions import *

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

'''
Section plot 01-10 - salinity
'''

# Plot dependencies
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import geopandas as gp
import numpy as np

def sectionplot(arg):
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
    zi = mlab.griddata(x, y, z, xi, yi)

    # Plotting the gridded data
    plt.figure() # Starting the figure object
    plt.pcolormesh(xi,yi,zi) # Adding the colour mesh
    plt.contour(xi, yi, zi, colors='k') # Contour lines
    plt.scatter(x,y,c=z) # Adding the scatter points
    plt.colorbar()
    plt.axis([np.min(x), np.max(x), np.min(y), np.max(y)])
    plt.gca().invert_yaxis()
    plt.show()


if __name__ == '__main__':
    arg = [st4, st5, st6] # Test this with other stations
    sectionplot(arg)
