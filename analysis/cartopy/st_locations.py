'''
Plot da localização das estações, a ser usado na seção de "Área de estudo".
'''

# Importando as bibliotecas
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
import geopandas as gp
import numpy as np

# Vamos definir a função main(), que vai gerar o plot.
def main():

	# Iniciando a projeção e suas dimensões lat/lon
	ax = plt.axes(projection=ccrs.PlateCarree())
	coords = (-48.9, -48.7, -28.4, -28.55)
	ax.set_extent(coords)
	ax.gridlines(draw_labels=True)

	# Shapefiles que vão gerar os limites territoriais.
	sc = 'analysis/cartopy/shapefiles/SC-POLYGON.shp'
	laguna = 'analysis/cartopy/shapefiles/DestaqueLaguna-POLYGON.shp'
	lagoas = 'analysis/cartopy/shapefiles/LagoasComplexoLagunar-POLYGON.shp'
	rios = gp.read_file('analysis/cartopy/shapefiles/RiosComplexoLagunar.shp')

	# Os pontos de coleta e os dados vêm de arquivos csv
	lons = np.genfromtxt('data/csv/0807_lon.csv', delimiter=',')
	lats = np.genfromtxt('data/csv/0807_lat.csv', delimiter=',')

	# Vamos fazer uma lista para iterar um loop com a função add_geometries()
	shapes = [sc, laguna, lagoas, rios]

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

	plt.scatter(lons, lats, color='black', zorder=10, s=40)

	plt.show()

if __name__ == '__main__':
	main()
