import geopandas as gpd
import matplotlib.pyplot as plt

# Cargar el archivo DXF utilizando geopandas
data = gpd.read_file('s.dxf')

# Obtener el límite máximo y mínimo de las coordenadas X e Y
xmin, ymin, xmax, ymax = data.total_bounds

# Calcular el ancho y largo de la figura
width = xmax - xmin
height = ymax - ymin

# Configurar el diccionario de colores por tipo de geometría
color_dict = {
    'Point': 'red',
    'MultiPoint': 'blue',
    'LineString': 'black',
    'MultiLineString': 'green',
    'Polygon': 'orange',
    'MultiPolygon': 'purple',
    'GeometryCollection': 'gray',
    'Circle': 'yellow',
    'Rectangle': 'cyan',
    'Triangle': 'pink',
    'Ellipse': 'brown',
    'Arc': 'magenta',
    'Text': 'teal',
    # Agrega aquí los tipos de geometría adicionales que desees manejar
}

# Configurar la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

# Recorrer todas las geometrías del archivo DXF
for geometry in data['geometry']:
    # Obtener el tipo de geometría
    geom_type = geometry.geom_type
    
    # Obtener el color correspondiente al tipo de geometría del diccionario
    color = color_dict.get(geom_type, 'gray')  # Color gris como predeterminado
    
    # Dibujar la geometría con el color correspondiente
    if geom_type == 'Point':
        x, y = geometry.xy
        ax.plot(x, y, marker='o', markersize=3, color=color)
    elif geom_type == 'MultiPoint':
        for point in geometry:
            x, y = point.xy
            ax.plot(x, y, marker='o', markersize=3, color=color)
    elif geom_type == 'LineString':
        x, y = geometry.xy
        ax.plot(x, y, color=color, linewidth=0.1)
    elif geom_type == 'MultiLineString':
        for line in geometry:
            x, y = line.xy
            ax.plot(x, y, color=color, linewidth=0.1)
    elif geom_type == 'Polygon':
        x, y = geometry.exterior.xy
        ax.fill(x, y, color=color)
    elif geom_type == 'MultiPolygon':
        for polygon in geometry:
            x, y = polygon.exterior.xy
            ax.fill(x, y, color=color)
    elif geom_type == 'GeometryCollection':
        for sub_geometry in geometry:
            sub_geom_type = sub_geometry.geom_type
            sub_color = color_dict.get(sub_geom_type, 'gray')
            if sub_geom_type == 'Point':
                x, y = sub_geometry.xy
                ax.plot(x, y, marker='o', markersize=3, color=sub_color)
            elif sub_geom_type == 'LineString':
                x, y = sub_geometry.xy
                ax.plot(x, y, color=sub_color, linewidth=0.1)
            elif sub_geom_type == 'Polygon':
                x, y = sub_geometry.exterior.xy
                ax.fill(x, y, color=sub_color)
    elif geom_type == 'Circle':
        center_x, center_y = geometry.centroid.xy
        radius = geometry.radius
        circle = plt.Circle((center_x[0], center_y[0]), radius, color=color, fill=False)
        ax.add_artist(circle)
    elif geom_type == 'Rectangle':
        x, y = geometry.exterior.xy
        ax.fill(x, y, color=color)
    elif geom_type == 'Triangle':
        x, y = geometry.exterior.xy
        ax.fill(x, y, color=color)
    elif geom_type == 'Ellipse':
        center_x, center_y = geometry.centroid.xy
        width = geometry.major_axis
        height = geometry.minor_axis
        ellipse = plt.Ellipse((center_x[0], center_y[0]), width, height, color=color, fill=False)
        ax.add_artist(ellipse)
    elif geom_type == 'Arc':
        x, y, start_angle, end_angle = geometry.arc
        ax.plot(x, y, color=color, linewidth=0.1)
    elif geom_type == 'Text':
        x, y = geometry.xy
        text = geometry.text
        ax.text(x[0], y[0], text, color=color)
    # Agrega aquí los bloques de código adicionales para manejar otrosTipos de geometría adicionales que desees incluir.

# Mostrar la gráfica
plt.show()