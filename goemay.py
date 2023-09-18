import geopandas as gpd
from mayavi import mlab

# Paso 1: Carga del archivo DXF en Geopandas
archivo_dxf = 's.dxf'
gdf = gpd.read_file(archivo_dxf)

mlab.figure(bgcolor=(1, 1, 1))  # Configura el fondo blanco

for geometria in gdf.geometry:
    if geometria.geom_type == 'LineString':
        coords = geometria.coords[:]
        x, y, z = zip(*coords)
        mlab.plot3d(x, y, z, color=(0, 0, 1), tube_radius=None)
    elif geometria.geom_type == 'Polygon':
        coords = geometria.exterior.coords[:]
        x, y, z = zip(*coords)
        mlab.plot3d(x, y, z, color=(0, 1, 0), tube_radius=None)

mlab.show()