# -*- coding: utf-8 -*-
"""
Script 36: Clustering Jerárquico Aglomerativo (Agglomerative Clustering)
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. Generación de un conjunto de datos simulado.
2. Uso de `scipy` para calcular la matriz de enlace (Linkage Matrix) usando la distancia Euclidiana y el método de Ward.
3. Simulación de la estructura del Dendrograma que muestra las divisiones y fusiones jerárquicas.
4. Ajuste del modelo de clasificación con `AgglomerativeClustering` de `scikit-learn`.
5. Métricas de evaluación para clustering sin etiquetas verdaderas: Coeficiente de Silueta.
"""

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage, dendrogram

# =====================================================================
# 1. PREPARACIÓN DE DATOS
# =====================================================================
# Generamos 100 observaciones aleatorias distribuidas en 3 agrupaciones
X, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.70, random_state=42)

print("--- CLUSTERING JERÁRQUICO AGLOMERATIVO ---")
print(f"Número de observaciones a agrupar: {X.shape[0]}\n")

# =====================================================================
# 2. CONSTRUCCIÓN DE LA MATRIZ DE ENLACE (LINKAGE) CON SCIPY
# =====================================================================
# El método de Ward minimiza la varianza total dentro del grupo en cada fusión.
# Calculamos la matriz de enlace basándonos en la distancia euclidiana.
Z = linkage(X, method='ward', metric='euclidean')

print("--- Matriz de Enlace (Primeras 5 uniones) ---")
# Columnas en Z: [Índice de Clúster 1, Índice de Clúster 2, Distancia, Tamaño del Clúster fusionado]
for idx, union in enumerate(Z[:5]):
    print(f"Paso {idx+1}: Fusiona Clúster {int(union[0])} con Clúster {int(union[1])} a una distancia de {union[2]:.4f} (Contiene {int(union[3])} puntos)")
print("...")

# =====================================================================
# 3. ENTRENAMIENTO DEL MODELO DE CLUSTERING CON SCIKIT-LEAR
# =====================================================================
# Definimos el número de clústeres a formar
n_clusters = 3

# Instanciamos el clasificador de Clustering Jerárquico Aglomerativo
# - linkage: 'ward' (minimiza la varianza de los clústeres que se fusionan)
# - metric: 'euclidean' (métrica de distancia)
modelo_jerarquico = AgglomerativeClustering(
    n_clusters=n_clusters,
    metric='euclidean',
    linkage='ward'
)

# Ajuste del modelo y obtención de etiquetas de pertenencia
etiquetas_predichas = modelo_jerarquico.fit_predict(X)

# =====================================================================
# 4. EVALUACIÓN CON MÉTRICA DE COEFICIENTE DE SILUETA
# =====================================================================
# El Coeficiente de Silueta mide cuán similar es un objeto a su propio clúster (cohesión) 
# en comparación con otros clústeres (separación). Rango de -1 a 1.
# Un valor alto indica que el objeto está bien emparejado con su clúster y mal con los vecinos.
score_silueta = silhouette_score(X, etiquetas_predichas)

print(f"\n--- Reporte de Desempeño ---")
print(f"Número final de clústeres: {n_clusters}")
print(f"Coeficiente de Silueta   : {score_silueta:.4f}")

# Conteo de observaciones por clúster asignado
conteo_grupos = np.bincount(etiquetas_predichas)
for i, count in enumerate(conteo_grupos):
    print(f"  Clúster {i}: {count} observaciones")

print("\nNota Teórica: A diferencia de K-Means, el clustering jerárquico no requiere")
print("definir el número de clústeres a priori para construir el árbol (Dendrograma),")
print("pero sí para particionar los resultados finales a una altura determinada del corte.")
