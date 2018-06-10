'''
'''

# Importando as bibliotecas
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
import csv
import geopandas as gp
import pandas as pd
import numpy as np

def main(arg, arg2=None):

	# Shapefiles que vão gerar os limites territoriais.
	sc = 'analysis/cartopy/shapefiles/SC-POLYGON.shp'
	laguna = 'analysis/cartopy/shapefiles/DestaqueLaguna-POLYGON.shp'
	lagoas = 'analysis/cartopy/shapefiles/LagoasComplexoLagunar-POLYGON.shp'
	rios = gp.read_file('analysis/cartopy/shapefiles/RiosComplexoLagunar.shp')

	# Vamos fazer uma lista para iterar um loop com a função add_geometries()
	shapes = [sc, laguna, lagoas, rios]

	for key in arg:

		fig = plt.figure()

		# Iniciando a projeção e suas dimensões lat/lon
		ax = plt.axes(projection=ccrs.PlateCarree())
		coords = (-48.9, -48.7, -28.4, -28.55)
		ax.set_extent(coords)
		ax.gridlines(draw_labels=True)

		# Os pontos de coleta e os dados vêm de arquivos csv
		lats = arg[key][0].values
		lons = arg[key][1].values
		data = np.genfromtxt(arg[key][2], delimiter=',')
		# Assim como a data que vai aparecer no plot
		s = arg[key][2]
		d, m, y = s[9:11], s[11:13], '2017'
		dmy = '-'.join([d, m, y])

		# Imagem de background
		ax.stock_img()

		# Adicionando os shapes ao plot
		ax.add_geometries(Reader(sc).geometries(),
			ccrs.PlateCarree(),
			facecolor = 'beige', edgecolor = 'black')

		ax.add_geometries(Reader(lagoas).geometries(),
			ccrs.PlateCarree(),
			facecolor = 'skyblue')

		ax.text(-48.745, -28.41, dmy, zorder=9,
		 bbox = dict(facecolor='white', alpha=0.5))

		rios.plot(ax=ax, color = 'skyblue', edgecolor='black')

		plt.scatter(lons, lats, c=data, zorder=10, s=40)
		plt.colorbar(shrink=0.7, ticks=range(int(min(data))-1,int(max(data))+1,1), pad=0.125,
		).set_label('Temperature in C')

		if arg2:
			plt.savefig(arg2 + dmy + '_temperature', transparent=True)
		else:
			plt.show()

df = pd.read_csv('data/csv/coordenadas.csv', delimiter = ';')

all = {

'saida1' : (df.loc[df['Data'] == '25-Jan-17']['Lat'], df.loc[df['Data'] == '25-Jan-17']['Lon'], 'data/csv/2501_temp.csv'),
'saida2' : (df.loc[df['Data'] == '27-May-17']['Lat'], df.loc[df['Data'] == '27-May-17']['Lon'], 'data/csv/2705_temp.csv'),
'saida3' : (df.loc[df['Data'] == '08-Jul-17']['Lat'], df.loc[df['Data'] == '08-Jul-17']['Lon'], 'data/csv/0807_temp.csv'),
'saida4' : (df.loc[df['Data'] == '1-Oct-17']['Lat'], df.loc[df['Data'] == '1-Oct-17']['Lon'], 'data/csv/0110_temp.csv')

}

if __name__ == '__main__':
	main(all)
