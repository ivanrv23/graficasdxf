import geopandas as gpd
import matplotlib.pyplot as plt
import mpld3

# Abrir el archivo DXF
plano = gpd.read_file('Surface.dxf')

# Crear el gráfico con ajuste de escala, líneas delgadas y colores diferenciados
fig, ax = plt.subplots(figsize=(8, 8))  # Tamaño de la figura ajustable según tus necesidades
plano.plot(ax=ax, linewidth=0.1, color='blue')

# Habilitar la funcionalidad de zoom y desplazamiento
ax.autoscale(enable=True, axis='both', tight=True)
ax.set(xlim=(plano.total_bounds[0], plano.total_bounds[2]), ylim=(plano.total_bounds[1], plano.total_bounds[3]))

# Convertir el gráfico en una figura interactiva mpld3
interactive_fig = mpld3.fig_to_html(fig)

# Guardar la figura interactiva en un archivo HTML
with open('interactiva.html', 'w') as file:
    file.write(interactive_fig)