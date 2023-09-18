import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Cargar el archivo DXF utilizando geopandas
data = gpd.read_file('TAJO.dxf')

# Obtener las coordenadas X, Y y Z de las geometrías
x = []
y = []
z = []

for geometry in data['geometry']:
    coords = np.array(geometry.coords)
    x.extend(coords[:, 0])
    y.extend(coords[:, 1])
    z.extend(coords[:, 2])

# Configurar el diccionario de colores por tipo de geometría
color_dict = {
    'Point': 'red',
    'LineString': 'blue',
    'Polygon': 'green',
    'Circle': 'orange',
    'Rectangle': 'purple',
    'Triangle': 'gray',
    'Ellipse': 'brown',
    'Arc': 'magenta',
    'Text': 'cyan',
}

# Configurar la figura y los ejes 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Recorrer todas las geometrías del archivo DXF
for geometry in data['geometry']:
    # Obtener el tipo de geometría
    geom_type = geometry.geom_type
    
    # Obtener el color correspondiente al tipo de geometría del diccionario
    color = color_dict.get(geom_type, 'gray')  # Color gris como predeterminado
    
    # Dibujar la geometría con el color correspondiente
    if geom_type == 'Point':
        ax.scatter(x, y, z, c=color)
    elif geom_type == 'LineString':
        ax.plot(x, y, z, c=color, linewidth=0.1)
    elif geom_type == 'Polygon':
        ax.plot_surface([x], [y], [z], color=color)
    elif geom_type == 'Circle':
        center_x, center_y, center_z = geometry.centroid.coords[0]
        radius = geometry.radius
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = radius * np.outer(np.cos(u), np.sin(v)) + center_x
        y = radius * np.outer(np.sin(u), np.sin(v)) + center_y
        z = radius * np.outer(np.ones(np.size(u)), np.cos(v)) + center_z
        ax.plot_surface(x, y, z, color=color)
    elif geom_type == 'Rectangle':
        x, y, z = geometry.exterior.coords.xy
        ax.plot_surface([x], [y], [z], color=color)
    elif geom_type == 'Triangle':
        x, y, z = geometry.exterior.coords.xy
        ax.plot_trisurf(x, y, z, color=color)
    elif geom_type == 'Ellipse':
        center_x, center_y, center_z = geometry.centroid.coords[0]
        width = geometry.major_axis
        height = geometry.minor_axis
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = width/2 * np.outer(np.cos(u), np.sin(v)) + center_x
        y = width/2 * np.outer(np.sin(u), np.sin(v)) + center_y
        z = height/2 * np.outer(np.ones(np.size(u)), np.cos(v)) + center_z
        ax.plot_surface(x, y, z, color=color)
    elif geom_type == 'Arc':
        x, y, z = zip(*geometry.coords)
        ax.plot(x, y, z, c=color, linewidth=0.1)
    elif geom_type == 'Text':
        x, y, z = geometry.x, geometry.y, geometry.z
        text = geometry.text
        ax.text(x, y, z, text, color=color)

# Configurar los límites de los ejes
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_zlim(min(z), max(z))

# Mostrar el gráfico 3D
plt.show()