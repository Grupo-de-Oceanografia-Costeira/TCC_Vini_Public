'''
Plot da localização das estações, a ser usado na seção de "Área de estudo".
'''

# Importando as bibliotecas
import geopandas as gp
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader


def main():
	# Iniciando a projeção e suas dimensões
	ax = plt.axes(projection=ccrs.PlateCarree())
	coords = (-48.9, -48.63, -28.2, -28.6)
	ax.set_extent(coords)
	ax.gridlines(draw_labels=True)

	# Shapefiles que vão gerar os limites territoriais.
	sc = 'analysis/cartopy/shapefiles/SC-POLYGON.shp'
	laguna = 'analysis/cartopy/shapefiles/DestaqueLaguna-POLYGON.shp'
	lagoas = 'analysis/cartopy/shapefiles/LagoasComplexoLagunar-POLYGON.shp'
	rios = gp.read_file('analysis/cartopy/shapefiles/RiosComplexoLagunar.shp')

	# Os pontos de coleta e os dados vêm de arquivos csv
	# lons = list(df.loc[df['Data'] == '25-Jan-17']['Lon'])
	# lats = list(df.loc[df['Data'] == '25-Jan-17']['Lat'])

	ax.stock_img()

	# Adicionando os shapes ao plot
	ax.add_geometries(
		Reader(sc).geometries(),
		ccrs.PlateCarree(),
		facecolor='beige',
		edgecolor='black'
	)

	ax.add_geometries(
		Reader(lagoas).geometries(),
		ccrs.PlateCarree(),
		facecolor='skyblue'
	)

	rios.plot(ax=ax, color='skyblue', lw=4.0)

	plt.show()


if __name__ == '__main__':
	main()
