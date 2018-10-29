'''
Plot da localização de Laguna no Brasil, a ser usado na seção
de "Área de estudo"
'''

# Importando as bibliotecas
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.patches as patches


# Vamos definir a função main(), que vai gerar o plot.
def main():

	# Iniciando a projeção e suas dimensões lat/lon
    ax = plt.axes(projection=ccrs.Orthographic(-50, -10))

    # Adicionand cfeatures
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.RIVERS)
    ax.add_feature(cfeature.BORDERS)

    # Não botamos LAND ou OCEANS para poder usar o stock_img()
    ax.stock_img()

    ax.set_global()
    ax.gridlines()

    plt.savefig('img/brasil.png', transparent=True)


if __name__ == '__main__':
    main()
