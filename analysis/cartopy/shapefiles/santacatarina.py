'''
Plot da localização de Laguna em SC, a ser usado na seção
de "Área de estudo"
'''

# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
from cartopy.io.img_tiles import MapQuestOpenAerial
import matplotlib.patches as patches

# Vamos definir a função main(), que vai gerar o plot.
def main():

	# Iniciando a projeção e suas dimensões lat/lon
	ax = plt.axes(projection=ccrs.PlateCarree())
	# coords = (-54, -47, -25.8, -29.4)
	coords = (-50, -48, -26, -29.4)
	ax.set_extent(coords)
	# ax.set_yticks((-25.8, -27.0, -28.2, -29.4))
	ax.gridlines(draw_labels=True)

	# Shapefiles que vão gerar os limites territoriais.
	brasil = 'analysis/cartopy/shapefiles/Brasil-POLYGON.shp'
	sc = 'analysis/cartopy/shapefiles/SC-POLYGON.shp'
	laguna = 'analysis/cartopy/shapefiles/DestaqueLaguna-POLYGON.shp'
	lagoas = 'analysis/cartopy/shapefiles/LagoasComplexoLagunar-POLYGON.shp'

	# Vamos fazer uma lista para iterar um loop com a função add_geometries()
	shapes = [brasil, sc, laguna, lagoas]

	ax.stock_img()

	# for loop para adicionar os shapes à figura
	for item in shapes:
		if item is lagoas:
			ax.add_geometries(Reader(item).geometries(),
				ccrs.PlateCarree(),
				facecolor='skyblue', edgecolor='black')
		else:
			ax.add_geometries(Reader(item).geometries(),
				ccrs.PlateCarree(),
				facecolor='beige', edgecolor='black')

	# p = patches.Rectangle(
	# 	(-48.9, -28.55), 0.2, 0.15,
	# 	fill = False, color = 'red',
	# 	zorder = 6, lw = 3.0, ls = '-'
	# 	)

	# ax.add_patch(p)

	plt.show()
	# plt.savefig('img/santacatarina2.png', transparent=True)

if __name__ == '__main__':
	main()
