'''
'''

# Importando as bibliotecas
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
import geopandas as gp
import numpy as np

def main(dict):

	# Shapefiles que vão gerar os limites territoriais.
	sc = 'analysis/cartopy/shapefiles/SC-POLYGON.shp'
	laguna = 'analysis/cartopy/shapefiles/DestaqueLaguna-POLYGON.shp'
	lagoas = 'analysis/cartopy/shapefiles/LagoasComplexoLagunar-POLYGON.shp'
	rios = gp.read_file('analysis/cartopy/shapefiles/RiosComplexoLagunar.shp')

	# Vamos fazer uma lista para iterar um loop com a função add_geometries()
	shapes = [sc, laguna, lagoas, rios]

	for key in dict:

		# Iniciando a projeção e suas dimensões lat/lon
		ax = plt.axes(projection=ccrs.PlateCarree())
		coords = (-48.9, -48.7, -28.4, -28.55)
		ax.set_extent(coords)
		ax.gridlines(draw_labels=True)

		# Os pontos de coleta e os dados vêm de arquivos csv
		lats = np.genfromtxt(dict[key][0], delimiter=',')
		lons = np.genfromtxt(dict[key][1], delimiter=',')
		data = np.genfromtxt(dict[key][2], delimiter=',')

		# Imagem de background
		ax.stock_img()

		# Adicionando os shapes ao plot
		ax.add_geometries(Reader(sc).geometries(),
			ccrs.PlateCarree(),
			facecolor = 'beige', edgecolor = 'black')

		ax.add_geometries(Reader(lagoas).geometries(),
			ccrs.PlateCarree(),
			facecolor = 'skyblue')

		rios.plot(ax=ax, color = 'skyblue', edgecolor='black')

		plt.scatter(lons, lats, c=data, zorder=10, s=40)
		plt.colorbar(shrink=0.7, ticks=range(int(min(data))-1,int(max(data))+1,1), pad=0.125,
		).set_label('Temperature in C')

		plt.show()


all = {
'saida1' : ('data/csv/2501_lat.csv', 'data/csv/2501_lon.csv', 'data/csv/2501_temp.csv'),
'saida2' : ('data/csv/2705_lat.csv', 'data/csv/2705_lon.csv', 'data/csv/2705_temp.csv'),
'saida3' : ('data/csv/0807_lat.csv', 'data/csv/0807_lon.csv', 'data/csv/0807_temp.csv'),
'saida4' : ('data/csv/0110_lat.csv', 'data/csv/0110_lon.csv', 'data/csv/0110_temp.csv')
}

if __name__ == '__main__':
	main(all)
