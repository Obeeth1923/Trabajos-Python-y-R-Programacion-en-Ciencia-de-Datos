# -*- coding: utf-8 -*-
"""
Script 35: Agrupamiento con K-Means y Método del Codo
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. Generación de datos sintéticos no etiquetados usando `make_blobs`.
2. Entrenamiento de múltiples modelos de K-Means para diferentes valores de K.
3. Evaluación del rendimiento mediante la Inercia (Within-Cluster Sum of Squares - WCSS).
4. El Método del Codo para identificar el número óptimo de agrupaciones o clústeres.
"""

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# =====================================================================
# 1. PREPARACIÓN DE DATOS (DATASET NO SUPERVISADO)
# =====================================================================
# Generamos 300 muestras en un espacio bidimensional (2 características)
# agrupadas en torno a 4 centros verdaderos con cierta dispersión (ruido)
X, y_verdadero = make_blobs(
    n_samples=300, 
    centers=4, 
    cluster_std=0.60, 
    random_state=42
)

print("--- CLUSTERING CON K-MEANS ---")
print(f"Número total de muestras: {X.shape[0]}")
print(f"Número de características: {X.shape[1]}\n")

# =====================================================================
# 2. MÉTODO DEL CODO (IDENTIFICACIÓN DEL K ÓPTIMO)
# =====================================================================
# Evaluaremos la inercia para valores de K de 1 a 8.
# La inercia mide la suma de las distancias al cuadrado de las muestras 
# a su centro de clúster más cercano.
inercias = []
rango_k = range(1, 9)

print("--- Evaluando diferentes valores de K (Número de Clústeres) ---")
for k in rango_k:
    # Usamos n_init="auto" para evitar advertencias de versiones recientes de scikit-learn
    kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
    kmeans.fit(X)
    inercias.append(kmeans.inertia_)
    print(f"K = {k} | Inercia (WCSS): {kmeans.inertia_:.2f}")

print("\nAnálisis del Método del Codo:")
print("Buscamos el punto de inflexión donde la inercia deja de disminuir abruptamente.")
print("Para este dataset de prueba, la curva del 'codo' se sitúa claramente en K = 4.")

# =====================================================================
# 3. ENTRENAMIENTO DEL MODELO CON EL K ÓPTIMO
# =====================================================================
k_optimo = 4
modelo_kmeans = KMeans(n_clusters=k_optimo, random_state=42, n_init="auto")

# Ajuste y asignación de etiquetas de clústeres de forma directa
etiquetas_predichas = modelo_kmeans.fit_predict(X)

# Ubicación de los centroides finales en el espacio de características
centroides = modelo_kmeans.cluster_centers_

print(f"\n--- Resultados del Clústering Final (K = {k_optimo}) ---")
print("Ubicación de los Centroides Ajustados:")
for idx, centroide in enumerate(centroides):
    print(f"Centroide {idx}: X1 = {centroide[0]:.4f}, X2 = {centroide[1]:.4f}")

# Conteo de elementos asignados a cada grupo
conteo_grupos = np.bincount(etiquetas_predichas)
print("\nDistribución de observaciones por clúster:")
for i, count in enumerate(conteo_grupos):
    print(f"  Clúster {i}: {count} muestras")

print("\nNota Teórica: K-Means es altamente sensible a la escala de las características.")
print("En proyectos reales, siempre aplica una normalización (ej. StandardScaler)")
print("antes de realizar el agrupamiento.")
