# -*- coding: utf-8 -*-
"""
Script 31: Regresión Lineal Múltiple con Scikit-Learn
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. Carga y división de un dataset de prueba para regresión.
2. Ajuste de un modelo de Regresión Lineal Múltiple usando `scikit-learn`.
3. Evaluación del rendimiento mediante Error Absoluto Medio (MAE), Error Cuadrático Medio (MSE) y Coeficiente de Determinación (R^2).
4. Inspección de coeficientes para interpretar el impacto de cada variable.
"""

import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# =====================================================================
# 1. PREPARACIÓN DE DATOS (DATASET SIMULADO)
# =====================================================================
# Generamos un dataset sintético de regresión:
# - n_samples: 150 registros (ej. viviendas)
# - n_features: 3 características (ej. metros cuadrados, n° habitaciones, edad de la casa)
# - noise: Ruido aleatorio para simular datos del mundo real.

X, y = make_regression(n_samples=150, n_features=3, noise=15.0, random_state=42)

# División en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("--- REGRESIÓN LINEAL MÚLTIPLE ---")
print(f"Tamaño del set de entrenamiento: {X_train.shape}")
print(f"Tamaño del set de prueba: {X_test.shape}\n")


# =====================================================================
# 2. ENTRENAMIENTO DEL MODELO
# =====================================================================
# Instanciamos el estimador de Regresión Lineal
modelo_reg = LinearRegression()

# Ajustamos el modelo a las características y etiquetas de entrenamiento
modelo_reg.fit(X_train, y_train)

print("--- Parámetros Ajustados por el Modelo ---")
print(f"Intercepto (b)    : {modelo_reg.intercept_:.4f}")
print(f"Coeficientes (w)  : {modelo_reg.coef_}\n")


# =====================================================================
# 3. PREDICCIÓN Y EVALUACIÓN DE MÉTRICAS
# =====================================================================
# Realizamos las predicciones sobre el conjunto de prueba
y_pred = modelo_reg.predict(X_test)

# Métricas principales de regresión:
# - MAE: Promedio de los errores absolutos. Indica la desviación promedio esperada.
# - MSE: Castiga con mayor fuerza los errores grandes debido a la potencia al cuadrado.
# - R^2: Porcentaje de la variabilidad del target explicado por las características (rango [0, 1]).
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
r2 = metrics.r2_score(y_test, y_pred)

print("--- Reporte de Desempeño del Modelo ---")
print(f"Error Absoluto Medio (MAE)      : {mae:.4f}")
print(f"Error Cuadrático Medio (MSE)     : {mse:.4f}")
print(f"Coeficiente de Determinación (R^2): {r2:.4f}")
print("Nota: Un R^2 cercano a 1.0 indica un excelente ajuste lineal del modelo a los datos.")
