'''
'''

# Importando as bibliotecas
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader
import geopandas as gp
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
		lats = np.genfromtxt(arg[key][0], delimiter=',')
		lons = np.genfromtxt(arg[key][1], delimiter=',')
		data = np.genfromtxt(arg[key][2], delimiter=';')
		# Assim como a data que vai aparecer no plot
		s = arg[key][0]
		d, m, y = s[9:11], s[11:13], '2018'
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


all = {

'saida1' : ('data/csv/2501_lat.csv', 'data/csv/2501_lon.csv', 'data/cc_nutrients/saida1cc.csv')#,
#'saida2' : ('data/csv/2705_lat.csv', 'data/csv/2705_lon.csv', 'data/csv/2705_temp.csv'),
#'saida3' : ('data/csv/0807_lat.csv', 'data/csv/0807_lon.csv', 'data/csv/0807_temp.csv'),
#'saida4' : ('data/csv/0110_lat.csv', 'data/csv/0110_lon.csv', 'data/csv/0110_temp.csv')

}

if __name__ == '__main__':
	main(all)
