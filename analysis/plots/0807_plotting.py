import pandas as pd
import matplotlib.pyplot as plt
from scripts.functions import *

# Load() function
hd1, hd2, variables, datapoints, df = load('sampling/cnv/stations_08-07-2017_processed.cnv')

# Defining 'stations', which will be arg2 for split_stations()
st_csv = pd.read_csv('sampling/08-07-17/coordenadas_0807.csv', sep = ';')
stations = list(st_csv['Estacao'])
lat = list(st_csv['Lat'])
lon = list(st_csv['Lon'])

# split_stations() function
d = split_stations(datapoints, stations, variables, lat, lon)

for st in d:
    d[st] = remove_upcast(d[st])

locals().update(d)

import matplotlib.mlab as mlab

x, y, z = [], [], []

for st in d:
     x.append(d[st]['LONG'][0])
     y.append(d[st]['LAT'][0])
     z.append(d[st]['t090:'][0])

plt.scatter(x, y, c=z)
plt.colorbar()
plt.show()

import geopandas as gp

# Importando shapefiles
sc = gp.read_file('ShapeFiles/DestaqueSC.shp')
laguna = gp.read_file('ShapeFiles/DestaqueLaguna.shp')
lagoas = gp.read_file('ShapeFiles/LagoasComplexoLagunar.shp')
rios = gp.read_file('ShapeFiles/RiosComplexoLagunar.shp')

xi = np.linspace(np.nanmin(x), np.nanmax(x), 2000)
yi = np.linspace(np.nanmin(y), np.nanmax(y), 2000)
zi = np.linspace(np.nanmin(z), np.nanmax(z), 2000)

xi, yi = np.meshgrid(xi, yi)
zi = mlab.griddata(x, y, z, xi, yi, interp='linear')

import csv

with open('0807_lon.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_NONNUMERIC, lineterminator = '\n')
    wr.writerow(x)

with open('0807_lat.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_NONNUMERIC, lineterminator = '\n')
    wr.writerow(y)

with open('0807_data.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_NONNUMERIC, lineterminator = '\n')
    wr.writerow(z)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-48.9,-48.7)
ax.set_ylim(-28.55,-28.4)

sc.plot(ax=ax, color='gray', zorder=1)
laguna.plot(ax=ax, color = 'gray', zorder=2)
lagoas.plot(ax=ax, color = 'white', alpha = 1,zorder=3)
rios.plot(ax=ax, color = 'white',zorder=4)

# plot com mesh
plt.pcolormesh(xi,yi,zi)
plt.show()

#plot sem mesh
plt.scatter(x, y, c=z,zorder=5)
plt.show()
