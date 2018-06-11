'''
Area chlorophyll plot.
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
		data = arg[key][2].values
		dmy = arg[key][3]

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

		rios.plot(ax=ax, color = 'skyblue', lw = 4.0)

		plt.scatter(lons, lats, c=data, zorder=10, s=40, cmap='Greens', vmin=1, vmax=20)
		plt.colorbar(shrink=0.7, pad=0.125,
		).set_label('Relative chl-a values')

		if arg2:
			plt.savefig(arg2 + dmy + '_chlorophyll', transparent=True)
		else:
			plt.show()

df = pd.read_csv('data/csv/coordenadas.csv', delimiter = ';')

all = {

'saida1' : (df.loc[df['Data'] == '25-Jan-17']['Lat'], df.loc[df['Data'] == '25-Jan-17']['Lon'], df.loc[df['Data'] == '25-Jan-17']['CC'], '25-Jan-2017'),
'saida3' : (df.loc[df['Data'] == '08-Jul-17']['Lat'], df.loc[df['Data'] == '08-Jul-17']['Lon'], df.loc[df['Data'] == '08-Jul-17']['CC'], '08-Jul-2017'),
'saida4' : (df.loc[df['Data'] == '01-Oct-17']['Lat'], df.loc[df['Data'] == '01-Oct-17']['Lon'], df.loc[df['Data'] == '01-Oct-17']['CC'], '01-Oct-2017')

}

if __name__ == '__main__':
	main(all)
