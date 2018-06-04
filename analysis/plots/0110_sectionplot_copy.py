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
Section plot 01-10
'''

# Plot dependencies
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
import geopandas as gp
import numpy as np

# Rio Tubarão section plot with salinity - DOUBLE CHECK THIS. COMPARE WITH MASTER BRANCH
s1, s2, s3 = np.array(st4['sal00:']), np.array(st5['sal00:']), np.array(st6['sal00:'])
z1, z2, z3 = np.array(st4['depSM:']), np.array(st5['depSM:']), np.array(st6['depSM:'])
sal_level = np.arange(1, 40.1, 1)

x = np.array([])
x = np.append(x, [0]*len(s1))
x = np.append(x, [1]*len(s2))
x = np.append(x, [2]*len(s3))

y = np.array([])
y = np.append(y, z1)
y = np.append(y, z2)
y = np.append(y, z3)

z = np.concatenate((s1, s2, s3))

plt.scatter(x, y, c=z)
plt.colorbar()
plt.show()

xi = np.linspace(np.min(x), np.max(x), 150)
yi = np.linspace(np.min(y), np.max(y), 150)
xi, yi = np.meshgrid(xi, yi)
zi = mlab.griddata(x, y, z, xi, yi)

plt.figure()
plt.pcolormesh(xi,yi,zi)
plt.contour(xi, yi, zi, colors='k') # desenha as linhas de gradiente.
plt.scatter(x,y,c=z)
plt.colorbar()
plt.axis([np.min(x), np.max(x), np.min(y), np.max(y)])
plt.gca().invert_yaxis()
plt.xlabel('Estacoes Rio Tubarao')
plt.show()

# Dados de clorofila

x, y, z, clo = [], [], [], []
clorofila = pd.read_csv('data/cc_nutrients/saida5cc.csv')
clorofila = clorofila[0:20] # valor da amostra de PP

for st in d:
     x.append(d[st]['LONG'][0])
     y.append(d[st]['LAT'][0])
     z.append(d[st]['sal00:'][0])

for item in clorofila['CC']:
    clo.append(item)

x.remove(x[2])
y.remove(y[2])
clo.remove(clo[2]) # remover valor NaN

plt.scatter(x, y, c=clo)
plt.colorbar()
plt.show()

import geopandas as gp
from mpl_toolkits.basemap import Basemap

# Importando shapefiles
sc = gp.read_file('analysis/cartopy/shapefiles/DestaqueSC-POLYGON.shp')
laguna = gp.read_file('analysis/cartopy/shapefiles/DestaqueLaguna-POLYGON.shp')
lagoas = gp.read_file('analysis/cartopy/shapefiles/LagoasComplexoLagunar-POLYGON.shp')
rios = gp.read_file('analysis/cartopy/shapefiles/RiosComplexoLagunar.shp')

xi = np.linspace(np.nanmin(x), np.nanmax(x), 2000)
yi = np.linspace(np.nanmin(y), np.nanmax(y), 2000)
zi = np.linspace(np.nanmin(z), np.nanmax(z), 2000)

xi, yi = np.meshgrid(xi, yi)
zi = mlab.griddata(x, y, z, xi, yi, interp='linear')


# Plot horizontal
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-48.9,-48.7)
ax.set_ylim(-28.55,-28.4)

sc.plot(ax=ax, color='gray',zorder=1)
laguna.plot(ax=ax, color = 'gray',zorder=2)
lagoas.plot(ax=ax, color = 'white', alpha = 1,zorder=3)
rios.plot(ax=ax, color = 'white',zorder=4)

#com grid
mesh = plt.pcolormesh(xi,yi,zi,zorder=5)
plt.colorbar()
plt.show()

#sem grid
plt.scatter(x,y,c=clo,zorder=6)
plt.colorbar()
plt.show()


# ODV importing
total = pd.concat(d)
cols = total.columns.tolist()
cols = cols[-3:] + cols[:-3]
total = total[cols]
total.insert(0, 'CRUISE', '01 oct')
# total.insert(1, 'Station ID', total.index) isso não funciona pq a coluna fica com o nome da estação E o index
total.insert(1, 'Station ID', range(1,len(total)+1))
# total.to_csv('odv_0110.csv')
