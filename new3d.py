import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Cargar el archivo DXF
data = gpd.read_file('TOPO.dxf')

# Calcular los límites de las coordenadas
xmin = ymin = zmin = float('inf')
xmax = ymax = zmax = float('-inf')

for geometry in data.geometry:
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

# Crear la figura 3D con el tamaño máximo
fig = plt.figure(figsize=(10, 6))  # Ajusta el tamaño de la figura según tus preferencias
ax = fig.add_subplot(111, projection='3d')

# Graficar las geometrías en la figura 3D
for geometry in data.geometry:
    if geometry.geom_type == 'LineString':
        x, y, z = zip(*geometry.coords)
        ax.plot(x, y, z,color='black')
    elif geometry.geom_type == 'Polygon':
        x, y, z = zip(*geometry.exterior.coords)
        ax.plot(x, y, z,color='red')

# Ajustar los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Ajustar los límites de los ejes
ax.set_xlim3d(xmin, xmax)
ax.set_ylim3d(ymin, ymax)
ax.set_zlim3d(zmin, zmax)

# Ajustar los márgenes de la figura para ocupar todo el espacio
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

# Mostrar la figura
plt.show()