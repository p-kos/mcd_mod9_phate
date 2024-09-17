import streamlit as st

st.set_page_config(
    page_title="Slides",    
)

st.sidebar.success("Comenzamos")
st.title("Uso de PHATE")

st.subheader("1. Instalación")
st.write("Se instala usando pip")
st.markdown("""```pip install phate```""")

st.subheader("2. Ejemplo básico")
st.write("Supongamos que tienes un conjunto de datos en alta dimensionalidad. Puedes aplicar PHATE para reducir la dimensionalidad y visualizar los datos.")
st.markdown(
    """
```
import phate
import numpy as np
import matplotlib.pyplot as plt

# Simulación de un dataset en alta dimensionalidad
data = np.random.rand(100, 50)

# Crear el modelo PHATE
phate_operator = phate.PHATE()

# Aplicar PHATE al dataset
phate_embedding = phate_operator.fit_transform(data)

# Visualizar los datos en 2D
plt.scatter(phate_embedding[:, 0], phate_embedding[:, 1])
plt.title("Visualización de PHATE")
plt.show()

```
"""
)

import phate
# import numpy as np
# import matplotlib.pyplot as plt

# # Simulación de un dataset en alta dimensionalidad
# data = np.random.rand(100, 50)

# # Crear el modelo PHATE
# phate_operator = phate.PHATE()

# # Aplicar PHATE al dataset
# phate_embedding = phate_operator.fit_transform(data)

# # Visualizar los datos en 2D
# plt.scatter(phate_embedding[:, 0], phate_embedding[:, 1])
# plt.title("Visualización de PHATE")
# st.pyplot(plt)

st.subheader("3. Opciones avanzadas")
st.write("knn: Controla el número de vecinos más cercanos para la construcción del grafo de afinidad.")
st.write("t: Define la cantidad de difusión utilizada en el cálculo de la transición.")
st.write("mds_dist: Si True, utiliza la distancia MDS (Multidimensional Scaling) para la optimización.")

st.subheader("Ejemplo con parámetros ajustados:")
st.markdown(
    """
```
phate_operator = phate.PHATE(knn=10, t=50, mds_dist=True)
phate_embedding = phate_operator.fit_transform(data)
```
"""
)
