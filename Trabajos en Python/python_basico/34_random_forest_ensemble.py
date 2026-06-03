# -*- coding: utf-8 -*-
"""
Script 34: Random Forest para Clasificación (Ensamble de Árboles)
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. Qué es el aprendizaje por ensamble (Ensemble Learning) y la técnica de Bagging (Bootstrap Aggregating).
2. Cómo entrenar un clasificador de Random Forest utilizando `scikit-learn`.
3. El papel de la aleatoriedad en las observaciones y en la selección de características para reducir el sobreajuste.
4. Evaluación del modelo con métricas de clasificación y extracción de la importancia de las características (Feature Importance).
"""

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# =====================================================================
# 1. CARGA Y PREPARACIÓN DE DATOS
# =====================================================================
# Usamos el dataset integrado Breast Cancer (Clasificación binaria)
datos = load_breast_cancer()
X, y = datos.data, datos.target
nombres_caracteristicas = datos.feature_names

# División en entrenamiento (80%) y prueba (20%) con estratificación para mantener balance
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("--- CLASIFICACIÓN CON RANDOM FOREST ---")
print(f"Dimensiones de entrenamiento: {X_train.shape}")
print(f"Dimensiones de prueba       : {X_test.shape}")
print(f"Clases a clasificar         : {datos.target_names}\n")

# =====================================================================
# 2. ENTRENAMIENTO DEL MODELO DE ENSAMBLE
# =====================================================================
# Instanciamos el RandomForestClassifier.
# Parámetros clave:
# - n_estimators: Número de árboles de decisión independientes que se construirán.
# - max_depth: Límite de profundidad de cada árbol (ayuda a controlar el sobreajuste).
# - random_state: Semilla aleatoria para asegurar la reproducibilidad.
# - bootstrap: Si es True (por defecto), entrena cada árbol en una submuestra aleatoria con reemplazo.
# - max_features: Subconjunto aleatorio de características a evaluar en cada división.
modelo_rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42,
    bootstrap=True,
    max_features="sqrt"
)

# Ajuste del ensamble a los datos de entrenamiento
modelo_rf.fit(X_train, y_train)

print("--- Entrenamiento Completado ---")
print(f"Número de estimadores (árboles): {len(modelo_rf.estimators_)}")
print(f"Criterio de división utilizado : {modelo_rf.criterion}\n")

# =====================================================================
# 3. PREDICCIÓN Y EVALUACIÓN MÉTRICA
# =====================================================================
# Realizamos la predicción en el conjunto de prueba
y_pred = modelo_rf.predict(X_test)
y_pred_proba = modelo_rf.predict_proba(X_test)[:, 1]

# Métricas de evaluación
exactitud = metrics.accuracy_score(y_test, y_pred)
matriz_confusion = metrics.confusion_matrix(y_test, y_pred)
reporte = metrics.classification_report(y_test, y_pred, target_names=datos.target_names)
auc_roc = metrics.roc_auc_score(y_test, y_pred_proba)

print("--- Reporte de Desempeño ---")
print(f"Exactitud Global (Accuracy): {exactitud:.4f}")
print(f"Área Bajo la Curva ROC (AUC): {auc_roc:.4f}\n")
print("Matriz de Confusión:")
print(matriz_confusion)
print("\nReporte de Clasificación Detallado:")
print(reporte)

# =====================================================================
# 4. EXTRACCIÓN DE LA IMPORTANCIA DE LAS CARACTERÍSTICAS
# =====================================================================
# Random Forest calcula la importancia basándose en la reducción de impureza (Gini) en las divisiones
importancias = modelo_rf.feature_importances_
indices_ordenados = np.argsort(importancias)[::-1]

print("--- Características Más Influyentes (Top 5) ---")
for i in range(5):
    idx = indices_ordenados[i]
    print(f"{i+1}. {nombres_caracteristicas[idx]:<25}: {importancias[idx]:.4f}")

print("\nNota Teórica: El ensamble de árboles mitiga la varianza individual de cada árbol.")
print("Al promediar las predicciones (soft/hard voting), la variabilidad se cancela de forma efectiva,")
print("haciendo que el modelo sea significativamente más estable frente al ruido de los datos.")
