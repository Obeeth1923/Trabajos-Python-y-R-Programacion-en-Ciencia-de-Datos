# -*- coding: utf-8 -*-
"""
Script 32: Regresión Logística para Clasificación Binaria
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. Preparación de datos y división de entrenamiento/prueba para clasificación binaria.
2. Entrenamiento de un clasificador de Regresión Logística.
3. Evaluación usando Matriz de Confusión y reporte detallado (Precisión, Exhaustividad, F1-Score).
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# =====================================================================
# 1. GENERACIÓN Y PREPARACIÓN DE DATOS
# =====================================================================
# Generamos datos sintéticos binarios (0 o 1):
# - n_samples: 200 registros (ej. transacciones de tarjetas de crédito)
# - n_features: 4 características de comportamiento de la transacción
# - weights: Proporción balanceada [0.5, 0.5]

X, y = make_classification(
    n_samples=200, 
    n_features=4, 
    n_classes=2, 
    weights=[0.5, 0.5], 
    random_state=42
)

# División entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("--- CLASIFICACIÓN BINARIA (REGRESIÓN LOGÍSTICA) ---")
print(f"Instancias de entrenamiento: {X_train.shape[0]}")
print(f"Instancias de prueba       : {X_test.shape[0]}\n")


# =====================================================================
# 2. ENTRENAMIENTO DEL MODELO
# =====================================================================
# La regresión logística modela la probabilidad de la clase positiva usando la función sigmoide:
# P(y=1 | x) = 1 / (1 + e^(-z)) donde z = w*x + b
modelo_log = LogisticRegression(random_state=42)
modelo_log.fit(X_train, y_train)


# =====================================================================
# 3. EVALUACIÓN MÉTRICA
# =====================================================================
# Predicciones de etiquetas de clase
y_pred = modelo_log.predict(X_test)

# Predicciones de probabilidad (necesarias para curvas ROC/AUC o calibración de umbrales)
y_prob = modelo_log.predict_proba(X_test)[:, 1]

# A) Matriz de Confusión
# Estructura: [[Verdaderos Negativos (TN), Falsos Positivos (FP)],
#              [Falsos Negativos (FN), Verdaderos Positivos (VP)]]
matriz_confusion = metrics.confusion_matrix(y_test, y_pred)

# B) Reporte de Clasificación
reporte = metrics.classification_report(y_test, y_pred)

# C) Área bajo la Curva ROC (ROC AUC)
roc_auc = metrics.roc_auc_score(y_test, y_prob)

print("--- MATRIZ DE CONFUSIÓN ---")
print(matriz_confusion)
print("\n--- REPORTE DE CLASIFICACIÓN ---")
print(reporte)
print(f"Área Bajo la Curva ROC (ROC AUC): {roc_auc:.4f}")
print("Nota: Un ROC AUC cercano a 1.0 indica un excelente balance de sensibilidad frente a especificidad.")
