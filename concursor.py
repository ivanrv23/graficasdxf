import geopandas as gpd
import matplotlib.pyplot as plt
import mplcursors

# Abrir el archivo DXF
plano = gpd.read_file('s.dxf')

# Crear el gráfico con ajuste de escala, líneas delgadas y colores diferenciados
fig, ax = plt.subplots(figsize=(8, 8))  # Tamaño de la figura ajustable según tus necesidades
plano.plot(ax=ax, linewidth=0.1, color='blue')

# Habilitar la funcionalidad de zoom
ax.autoscale(enable=True, axis='both', tight=True)

# Configurar mplcursors para la interactividad
cursor = mplcursors.cursor(ax, hover=True)

@cursor.connect("add")
def on_add(sel):
    # Obtener la información del punto seleccionado
    x, y = sel.target
    info = f'Coordenadas: ({x:.2f}, {y:.2f})'  # Aquí puedes personalizar el formato de visualización

    # Agregar una etiqueta con la información
    sel.annotation.set(text=info, position=(0, 10), anncoords='axes points')

# Mostrar el gráfico interactivo
plt.show()