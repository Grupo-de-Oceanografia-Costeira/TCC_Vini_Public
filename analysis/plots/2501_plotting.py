import pandas as pd
import matplotlib.pyplot as plt

from scripts.functions import *

# Load() function
hd1, hd2, variables, datapoints, df = load('sampling/cnv/stations_25-01-2017_processed.cnv')

# Defining 'stations', which will be arg2 for split_stations()
st_csv = pd.read_csv('sampling/25-01-17/coordenadas_2501.csv', sep = ';')
stations = list(st_csv['Ponto'])
lat = list(st_csv['Lat'])
lon = list(st_csv['Lon'])

# split_stations() function
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
plt.xlabel('Estações Rio Tubarão')
plt.show()

# Dados de coordenada

x, y, z = [], [], []

for st in d:
     x.append(d[st]['LONG'][0])
     y.append(d[st]['LAT'][0])
     z.append(d[st]['t090:'][0])

plt.scatter(x, y, c=z)
plt.colorbar()
plt.show()


# Criando plot superficial baseado no localhost.py
import geopandas as gp
from mpl_toolkits.basemap import Basemap

# Importando shapefiles
sc = gp.read_file('ShapeFiles/DestaqueSC.shp')
laguna = gp.read_file('ShapeFiles/DestaqueLaguna.shp')
lagoas = gp.read_file('ShapeFiles/LagoasComplexoLagunar.shp')
rios = gp.read_file('ShapeFiles/RiosComplexoLagunar.shp')

# Removing data from station with NaN values for lat and long (não fazer isso)
# # se há dados de lat long para todas as estações USAR NANMIN AQUI
x.remove(x[3])
y.remove(y[3])
z.remove(z[3])

from shapely.geometry import Point

a, b, n = [], [], []

#Só lagoa de santo antônio
for pt in list(lagoas.loc[1]['geometry'].exterior.coords):
    a.append(pt[0])
    b.append(pt[1])

#
# todas as lagoas

# a, b, n = [], [], []
#
# for index, row in lagoas.iterrows():
#      for pt in list(row['geometry'].exterior.coords):
#         a.append(pt[0])
#         b.append(pt[1])

# salvando em um Arquivo
import csv

with open('ShapeFiles/lagoaslon.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_NONNUMERIC, lineterminator = '\n')
    wr.writerow(a)

with open('ShapeFiles/lagoaslat.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_NONNUMERIC, lineterminator = '\n')
    wr.writerow(b)

# teste
# x = x[6:10]
# y = y[6:10]
# z = z[6:10]

with open('2501_lon.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_NONNUMERIC, lineterminator = '\n')
    wr.writerow(x)

with open('2501_lat.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_NONNUMERIC, lineterminator = '\n')
    wr.writerow(y)

with open('2501_data.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting = csv.QUOTE_NONNUMERIC, lineterminator = '\n')
    wr.writerow(z)

n.append([np.nan]*len(a))

xi = np.linspace(np.nanmin(x), np.nanmax(x), 2000)
yi = np.linspace(np.nanmin(y), np.nanmax(y), 2000)
zi = np.linspace(np.nanmin(z), np.nanmax(z), 2000)

xi, yi = np.meshgrid(xi, yi)
zi = mlab.griddata(x, y, z, xi, yi, interp='linear')

# teste
# ar = np.array(a)
# br = np.array(b)
# zr = np.linspace(np.nanmin(z), np.nanmax(z), 452)
# ar, br = np.meshgrid(ar,br)
# zr = mlab.griddata(x, y, z, ar, br, interp='linear')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-48.9,-48.7)
ax.set_ylim(-28.55,-28.4)

sc.plot(ax=ax, color='gray')
laguna.plot(ax=ax, color = 'gray')
lagoas.plot(ax=ax, color = 'white', alpha = 1)
rios.plot(ax=ax, color = 'white')

# from scipy.interpolate import griddata # experimentar com isto)

mesh = plt.pcolormesh(xi,yi,zi)

plt.show()

# Tentando extrair coordenadas do shapefile



# Arquivo antigo:

# def export_ODV(arg, arg2):
#     arg['CRUISE'] = arg2
#     arg['Station ID'] = arg.index
#     arg = arg[['CRUISE', 'Station ID', 'STATION', 'LAT', 'LONG', 't090:', 'c0S/m:', 'pr:', 'timeJ:', 'potemp090C:', 'sal00:', 'depSM:', 'sigma-t00:', 'flag:']]
#
# st10 = st10[['CRUISE', 'Station ID', 'STATION', 'LAT', 'LONG', 't090:', 'c0S/m:', 'pr:', 'timeJ:', 'potemp090C:', 'sal00:', 'depSM:', 'sigma-t00:', 'flag:']]
#
# st10.to_csv('st10.csv', sep=',')
#
# cd 'sampling/plots/2501/fig'
#
# plot(st2, '.')
# plot(st5, '.')
# plot(st4, '.')
# plot(st3, '.')
# plot(st6, '.')
# plot(st7, '.')
# plot(st8, '.')
# plot(st9, '.')
# plot(st10, '.')
# plot(st11, '.')
# plot(st12, '.')
# plot(st14, '.')
# plot(st15, '.')
# plot(st16, '.')
# plot(st17, '.')
# plot(st18, '.')
# plot(st19, '.')
# plot(st20, '.')
