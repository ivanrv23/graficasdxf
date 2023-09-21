
import geopandas as gpd
import matplotlib.pyplot as plt

# Carga el archivo DXF usando GeoPandas
gdf = gpd.read_file('Surface.dxf')

# Crea la figura y los ejes
fig, ax = plt.subplots()

# Calcula el rango de coordenadas para ajustar el tamaño de la figura
x_min, y_min, x_max, y_max = gdf.total_bounds
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Configura las características de las líneas
line_width = 0.5 # Ancho de línea en puntos
line_color = 'black' # Color de línea en formato de cadena

# Grafica cada geometría del archivo DXF con sus propiedades personalizadas
for geom in gdf['geometry']:
    if geom.geom_type == 'LineString':
        ax.plot(*geom.xy, linewidth=line_width, color=line_color)
    elif geom.geom_type == 'Polygon':
        ax.fill(*geom.exterior.xy, linewidth=line_width, edgecolor=line_color, facecolor=line_color, alpha=0.5)

# Muestra la gráfica
plt.show()

