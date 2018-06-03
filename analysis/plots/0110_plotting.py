import pandas as pd
import matplotlib.pyplot as plt
from scripts.functions import *

# Load() function
hd1, hd2, variables, datapoints, df = load('sampling/01-10-17/1-10-2017_processed.cnv')

metadata = pd.read_csv('sampling/01-10-17/coordenadas_0110.csv', sep = ';')
stations = list(metadata['Ponto'])
#importing coordinates
lat = list(metadata['Lat'])
lon = list(metadata['Lon'])

d = split_stations(datapoints, stations, variables, lat, lon)

for st in d:
    d[st] = remove_upcast(d[st])

locals().update(d)

# Testando script do Arnaldo (scripts/plot_section.py)

import matplotlib.mlab as mlab

s1 = np.array(st4['sal00:'])
z1 = np.array(st4['depSM:'])
s2 = np.array(st5['sal00:'])
z2 = np.array(st5['depSM:'])
s3 = np.array(st6['sal00:'])
z3 = np.array(st6['depSM:'])
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

# Dados de coordenada

x, y, z, clo = [], [], [], []

clorofila = pd.read_csv('sampling/saida5cc.csv')
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
sc = gp.read_file('ShapeFiles/DestaqueSC.shp')
laguna = gp.read_file('ShapeFiles/DestaqueLaguna.shp')
lagoas = gp.read_file('ShapeFiles/LagoasComplexoLagunar.shp')
rios = gp.read_file('ShapeFiles/RiosComplexoLagunar.shp')

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
total.to_csv('odv_0110.csv')













plot(st1, '.')
plot(st2, '.')
plot(st3, '.')
plot(st4, '.')
plot(st5, '.')
plot(st6, '.')
plot(st7, '.')
plot(st9, '.')
plot(st8, '.')
plot(st10, '.')
plot(st11, '.')
plot(st12, '.')
plot(st13, '.')
plot(st16, '.')
plot(st15, '.')
plot(st18, '.')
plot(st19, '.')
plot(st20, '.')
plot(st17, '.')
plot(st14, '.')

for i in stations:
    print('plot' + '(' + i + ')')
