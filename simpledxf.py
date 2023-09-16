import geopandas as gpd
import matplotlib.pyplot as plt

# Abrir el archivo DXF
plano = gpd.read_file('Curvas.dxf')

# Crear el gráfico
ax = plano.plot()

# Mostrar el gráfico en Visual Studio
plt.show()