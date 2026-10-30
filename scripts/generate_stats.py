import os
import matplotlib.pyplot as plt

# Asegurarse de que el directorio de salida existe
os.makedirs("assets", exist_ok=True)

# Configuración de los datos de ejemplo (puedes adaptarlos o hacerlos dinámicos)
labels = ['Commits', 'Pull Requests', 'Issues', 'Repositorios']
values = [32, 8, 2, 8]  # Métricas basadas en tu actividad actual

# Crear la figura con estilo oscuro acorde al perfil de GitHub
fig, ax = plt.subplots(figsize=(6, 3), facecolor='#0d1117')
ax.set_facecolor('#161b22')

# Dibujar las barras horizontales con colores llamativos
bars = ax.barh(labels, values, color='#58a6ff', edgecolor='#30363d')

# Personalizar el diseño para que quede limpio y estético
ax.set_xlabel('Cantidad', color='#c9d1d9', fontsize=10)
ax.set_title('Estadísticas de Actividad - IlloquediC', color='#FFD600', fontsize=12, fontweight='bold')
ax.tick_params(colors='#c9d1d9', which='both')

# Quitar los bordes innecesarios (spines)
for spine in ax.spines.values():
    spine.set_color('#30363d')

# Añadir los valores numéricos al final de las barras
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Desplazamiento horizontal
                textcoords="offset points",
                ha='left', va='center',
                color='#c9d1d9', fontsize=9, fontweight='bold')

plt.tight_layout()

# Guardar la imagen generada en la carpeta assets en formato SVG
output_path = 'assets/stats.svg'
plt.savefig(output_path, format='svg', bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
print(f"¡Gráfica generada con éxito en {output_path}!")
