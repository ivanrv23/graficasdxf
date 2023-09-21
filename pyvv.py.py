import numpy as np
import pyvista as pv
from geopandas import read_file
from shapely.geometry import Polygon

# Cargar el archivo DXF
data = read_file('Surface.dxf')

# Calcular los límites de las coordenadas
xmin, ymin, zmin = float('inf'), float('inf'), float('inf')
xmax, ymax, zmax = float('-inf'), float('-inf'), float('-inf')

for geometry in data.ageometry:
    if geometry.geom_type == 'LineString':
        coords = geometry.coords
        for coord in coords:
            x, y, z = coord

            if x < xmin:
                xmin = x
            if y < ymin:
                ymin = y
            if z < zmin:
                zmin = z

            if x > xmax:
                xmax = x
            if y > ymax:
                ymax = y
            if z > zmax:
                zmax = z

# Crear el plotter
plotter = pv.Plotter(window_size=(800, 600))

# Graficar las geometrías válidas en el plotter
for geometry in data.geometry:
    if geometry.geom_type == 'LineString':
        points = np.array([coord for coord in geometry.coords])
        if len(points) % 2 != 0:
            points = points[:-1]  # Eliminar el último punto si es impar
        plotter.add_lines(points, color='black')
    elif geometry.geom_type == 'Polygon':
        polygon = Polygon(geometry)
        if polygon.is_valid:
            points = np.array([coord for coord in geometry.exterior.coords])
            plotter.add_mesh(pv.PolyData(points), color='red')

# Ajustar los límites de los ejes
plotter.view_vector((1, 1, 1))
plotter.reset_camera_clipping_range()

# Mostrar la visualización
plotter.show()