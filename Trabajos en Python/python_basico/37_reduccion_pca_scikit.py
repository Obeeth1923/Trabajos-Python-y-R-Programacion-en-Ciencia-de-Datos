# -*- coding: utf-8 -*-
"""
Script 37: Reducción de Dimensionalidad con PCA (Principal Component Analysis)
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. Por qué es necesario escalar o estandarizar los datos antes de aplicar PCA.
2. Cómo proyectar un conjunto de datos de alta dimensionalidad (30 variables) a solo 2 componentes principales.
3. El concepto de Varianza Explicada Acumulada para entender cuánta información del dataset original se retiene.
4. Interpretación de los pesos (loadings) de los componentes.
"""

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# =====================================================================
# 1. CARGA Y PREPARACIÓN DE DATOS (CON ALTA DIMENSIONALIDAD)
# =====================================================================
# El dataset Breast Cancer tiene 30 características originales
datos = load_breast_cancer()
X, y = datos.data, datos.target

print("--- REDUCCIÓN DE DIMENSIONALIDAD CON PCA ---")
print(f"Dimensiones del dataset original: {X.shape} (30 características)")

# PCA calcula las direcciones de máxima varianza espacial.
# Si no escalamos los datos, las variables con escalas grandes dominarán artificialmente las componentes.
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)

print("Datos escalados exitosamente (Media = 0, Desviación Estándar = 1).\n")

# =====================================================================
# 2. APLICACIÓN DE PCA (REDUCCIÓN A 2 COMPONENTES)
# =====================================================================
# Instanciamos PCA fijando el número de componentes en 2
pca = PCA(n_components=2, random_state=42)

# Ajustamos PCA y transformamos los datos a la nueva base ortogonal
X_pca = pca.fit_transform(X_escalado)

print("--- Proyección PCA ---")
print(f"Dimensiones de los datos reducidos: {X_pca.shape} (2 componentes principales)")

# =====================================================================
# 3. EVALUACIÓN DE LA VARIANZA EXPLICADA
# =====================================================================
# La razón de varianza explicada indica qué porcentaje de la variabilidad total de los
# datos es explicada por cada uno de los componentes principales individuales.
varianza_explicada = pca.explained_variance_ratio_
varianza_acumulada = np.sum(varianza_explicada)

print("\n--- Reporte de Información Retenida ---")
print(f"Varianza explicada por el Componente Principal 1: {varianza_explicada[0]*100:.2f}%")
print(f"Varianza explicada por el Componente Principal 2: {varianza_explicada[1]*100:.2f}%")
print(f"Varianza acumulada retenida (2 componentes)      : {varianza_acumulada*100:.2f}%")

print("\nNota de Interpretación:")
print(f"Con solo 2 componentes principales, logramos resumir el {varianza_acumulada*100:.2f}% de la varianza")
print("total del conjunto original de 30 variables. Esto facilita enormemente la visualización")
print("y acelera el entrenamiento de algoritmos supervisados al evitar la maldición de la dimensionalidad.")

# Muestra de los primeros registros transformados
print("\nPrimeras 5 observaciones en el espacio PCA:")
for i in range(5):
    print(f"Muestra {i+1}: PC1 = {X_pca[i, 0]:.4f}, PC2 = {X_pca[i, 1]:.4f}")
