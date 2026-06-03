# -*- coding: utf-8 -*-
"""
Script 13: Determinante e Inversa de una Matriz
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. El concepto matemático de determinante y matriz inversa.
2. Cálculo de la inversa y determinante utilizando el módulo lineal de NumPy (`np.linalg`).
3. Por qué la inversa es crítica para la solución de la ecuación normal de mínimos cuadrados:
   beta = (X^T * X)^(-1) * X^T * y
"""

import numpy as np

# Definición de una matriz de características correlacionadas en un experimento
# Nota: La matriz debe ser cuadrada y no singular (determinante distinto de cero) para tener inversa.
X_features = np.array([
    [2, 1],
    [1, 3]
])

print("--- Matriz Original (X_features) ---")
print(X_features)
print()


# =====================================================================
# 1. DETERMINANTE DE LA MATRIZ
# =====================================================================
# Para una matriz 2x2: A = [[a, b], [c, d]], det(A) = a*d - b*c
# Si det(A) = 0, la matriz se llama "singular" y no posee inversa.

det_manual = (X_features[0, 0] * X_features[1, 1]) - (X_features[0, 1] * X_features[1, 0])
det_numpy = np.linalg.det(X_features)

print("--- 1. CÁLCULO DEL DETERMINANTE ---")
print(f"Determinante calculado manualmente: {det_manual}")
print(f"Determinante calculado con NumPy: {det_numpy:.4f}\n")


# =====================================================================
# 2. INVERSA DE LA MATRIZ
# =====================================================================
# La matriz inversa X^(-1) satisface: X * X^(-1) = I (donde I es la matriz identidad)
# Para una matriz 2x2: X^(-1) = (1 / det(X)) * [[d, -b], [-c, a]]

try:
    X_inversa = np.linalg.inv(X_features)
    print("--- 2. CÁLCULO DE LA MATRIZ INVERSA (X^-1) ---")
    print(X_inversa)
    
    # Verificación matemática: X * X^-1 debe ser igual a la matriz identidad
    identidad_aprox = X_features @ X_inversa
    print("\nVerificación (X @ X^-1) ~ Matriz Identidad:")
    print(np.round(identidad_aprox, 4))
    print()
except np.linalg.LinAlgError:
    print("[ERROR] La matriz es singular y no se puede invertir.\n")


# =====================================================================
# 3. APLICACIÓN PRÁCTICA: ECUACIÓN NORMAL (MÍNIMOS CUADRADOS)
# =====================================================================
# En la regresión lineal, estimamos los coeficientes óptimos (beta) usando la ecuación:
# beta = (X^T * X)^(-1) * X^T * y

# Datos simulados: matriz de diseño X y vector de etiquetas/objetivos y
X = np.array([
    [1, 1],  # Fila 1: intercepto y característica 1
    [1, 2],  # Fila 2
    [1, 3]   # Fila 3
])
y = np.array([1.5, 2.5, 3.5])

# Cálculo paso a paso de la regresión por mínimos cuadrados
XT_X = X.T @ X               # Multiplicamos la transpuesta por la matriz original
XT_X_inv = np.linalg.inv(XT_X) # Invertimos la matriz cuadrada resultante
beta = XT_X_inv @ X.T @ y    # Multiplicamos por la transpuesta y por y

print("--- 3. ESTIMACIÓN POR MÍNIMOS CUADRADOS ---")
print(f"Matriz de diseño X:\n{X}")
print(f"Valores reales y: {y}")
print(f"Coeficientes Beta estimados (Intercepto y Pendiente): {beta}")
print("Nota: El primer valor representa el intercepto y el segundo representa la pendiente.")
