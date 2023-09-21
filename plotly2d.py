import geopandas as gpd
import plotly.graph_objects as go

# Cargar el archivo DXF utilizando GeoPandas
archivo_dxf = "Surface.dxf"
datos = gpd.read_file(archivo_dxf)

# Crear una figura de Plotly
fig = go.Figure()

# Agregar las geometrías del archivo DXF a la figura
for geometry in datos.geometry:
    if geometry.geom_type == 'Polygon':
        fig.add_trace(go.Scatter(x=geometry.exterior.xy[0].tolist(), y=geometry.exterior.xy[1].tolist(), mode='lines'))
    elif geometry.geom_type == 'LineString':
        fig.add_trace(go.Scatter(x=geometry.xy[0].tolist(), y=geometry.xy[1].tolist(), mode='lines'))

# Mostrar la figura
fig.update_layout(width=800, height=600)
fig.show()