'''
Plotting Santa Catarina maps with Cartopy using Google Maps,
GSHHS and OpenStreetMap data.
From https://ocefpaf.github.io/python4oceanographers/blog/2015/06/22/osm/
'''

# Dependencies
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io import shapereader
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

# Plot function
def make_map(projection=ccrs.PlateCarree()):
    fig, ax = plt.subplots(figsize=(9, 13),
                           subplot_kw=dict(projection=projection))
    gl = ax.gridlines(draw_labels=True)
    gl.xlabels_top = gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    return fig, ax

# Google Maps Tiles
def gmaps():
    fig, ax = make_map(projection=request.crs)
    extent = [-50, -47.4, -30.5, -25]
    ax.set_extent(extent)
    ax.add_image(request, 10)

    plt.show()

if __name__ == '__main__':
    gmaps()

# GSHHS data
def gshhs():
    fig, ax = make_map(projection=ccrs.PlateCarree())
    request = cimgt.GoogleTiles()
    extent = [-50.5, -47.4, -31, -25]
    ax.set_extent(extent)

    shp = shapereader.Reader('./analysis/cartopy/shapefiles/santacatarina.shp')
    for record, geometry in zip(shp.records(), shp.geometries()):
        ax.add_geometries([geometry], ccrs.PlateCarree(), facecolor = 'lightgray',
                          edgecolor = 'black')

    plt.show()

if __name__ == '__main__':
    gshhs()

# Open Street Map
def osm():
    fig, ax = make_map(projection=ccrs.PlateCarree())
    extent = [-50.5, -47.4, -31, -25]
    ax.set_extent(extent)

    shp = shapereader.Reader('../osm/coastlines-split-4326/lines.shp')
    for record, geometry in zip(shp.records(), shp.geometries()):
        ax.add_geometries([geometry], ccrs.PlateCarree(), facecolor='w',
                          edgecolor='black')

if __name__ == '__main__':
    osm()
