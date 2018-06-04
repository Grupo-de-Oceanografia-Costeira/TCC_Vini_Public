'''
Plot da localização de Laguna em SC, a ser usado na seção
de "Área de estudo"
'''

# Importando as bibliotecas
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
	coords = (-54, -47, -25.5, -30)
	ax.set_extent(coords)
	ax.gridlines(draw_labels=True)

	# Shapefiles que vão gerar os limites territoriais.
	brasil = 'analysis/cartopy/shapefiles/Brasil-POLYGON.shp'
	sc = 'analysis/cartopy/shapefiles/SC-POLYGON.shp'
	laguna = 'analysis/cartopy/shapefiles/DestaqueLaguna-POLYGON.shp'

	# Vamos fazer uma lista para iterar um loop com a função add_geometries()
	shapes = [brasil, sc, laguna]

	# ax.add_feature(cfeature.LAND)
	# ax.add_feature(cfeature.OCEAN)
	# ax.add_feature(cfeature.COASTLINE)
	ax.stock_img()

	# for loop para adicionar os shapes à figura
	for item in shapes:
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

if __name__ == '__main__':
	main()
