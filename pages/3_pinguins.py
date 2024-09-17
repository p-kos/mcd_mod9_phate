# penguins_streamlit.py
import streamlit as st
import pandas as pd
import phate
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Título de la aplicación
st.title("Análisis de Dimensionalidad con PHATE - Dataset de Pingüinos")

# Cargar el dataset
st.header("Cargar y Exploración del Dataset")
data_path = "penguins.csv"
penguins = pd.read_csv(data_path)

# Mostrar los primeros registros del dataset
st.write("Vista previa del dataset:")
st.dataframe(penguins.head())

# Limpiar y procesar los datos
st.header("Preprocesamiento de Datos")
penguins = penguins.dropna()  # Eliminamos los datos faltantes
st.write(f"Número de registros después de eliminar valores faltantes: {penguins.shape[0]}")

# Seleccionar solo las columnas numéricas para el análisis
numeric_cols = penguins.select_dtypes(include=['float64', 'int64']).columns
penguins_numeric = penguins[numeric_cols]

# Escalar los datos
scaler = StandardScaler()
penguins_scaled = scaler.fit_transform(penguins_numeric)

# Aplicar PHATE
st.header("Aplicación de PHATE")
phate_operator = phate.PHATE()
penguins_phate = phate_operator.fit_transform(penguins_scaled)

# Visualización del resultado de PHATE
st.subheader("Visualización de PHATE en 2D")
plt.figure(figsize=(8,6))
plt.scatter(penguins_phate[:, 0], penguins_phate[:, 1], c=penguins['species'], cmap='viridis', s=50)
plt.title('Reducción de Dimensionalidad con PHATE')
plt.xlabel('PHATE 1')
plt.ylabel('PHATE 2')
plt.colorbar(label='Especies')
st.pyplot(plt)

# Comparación con PCA
st.header("Comparación con PCA")
pca = PCA(n_components=2)
penguins_pca = pca.fit_transform(penguins_scaled)

plt.figure(figsize=(8,6))
plt.scatter(penguins_pca[:, 0], penguins_pca[:, 1], c=penguins['species'], cmap='plasma', s=50)
plt.title('Reducción de Dimensionalidad con PCA')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.colorbar(label='Especies')
st.pyplot(plt)

# Conclusiones
st.header("Conclusiones")
st.write("""
La visualización muestra cómo PHATE es capaz de capturar la estructura global y local de los datos de los pingüinos,
lo que puede no ser evidente en una reducción de dimensionalidad más lineal como PCA.
""")
