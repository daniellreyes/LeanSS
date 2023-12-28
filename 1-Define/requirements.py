import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

# Cargar datos desde el archivo CSV (asegúrate de tener la ruta correcta al archivo)
ruta_archivo = './Kano_Model.csv'
datos = pd.read_csv(ruta_archivo)

# Mostrar las primeras filas para comprobar que se han cargado correctamente
print(datos.head())

# Supongamos que queremos analizar la frecuencia de una columna específica llamada 'columna_de_interes'
columna_de_interes = 'nombre_de_la_columna'

# Calcular la frecuencia de los valores en la columna seleccionada
frecuencias = datos[columna_de_interes].value_counts()

# Crear un gráfico de barras (puedes elegir otros tipos de gráficos según tu preferencia)
plt.figure(figsize=(10, 6))  # Tamaño del gráfico
sns.barplot(x=frecuencias.index, y=frecuencias.values, palette='viridis')
plt.title(f'Frecuencia de valores en la columna {columna_de_interes}')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)  # Rotar etiquetas en el eje x para mejor visualización
plt.tight_layout()
plt.show()