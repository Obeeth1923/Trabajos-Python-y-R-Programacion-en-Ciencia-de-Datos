# -*- coding: utf-8 -*-
"""
Script 24: Regresión Lineal Analítica (Ecuación Normal)
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. El fundamento matemático de la Regresión Lineal por Mínimos Cuadrados Ordinarios (OLS).
2. Resolución analítica exacta de los parámetros (pesos/coeficientes) sin usar optimizadores numéricos directos.
3. Aplicación de la Ecuación Normal:
   beta = (X^T * X)^(-1) * X^T * y
4. Cálculo de predicciones sobre datos nuevos.
"""

import numpy as np

# =====================================================================
# CASO DE ESTUDIO: Predicción de Ingresos basada en Años de Experiencia
# =====================================================================

# Variable independiente (X): Años de experiencia
experiencia = np.array([1.0, 2.5, 3.0, 4.5, 6.0])

# Variable dependiente (y): Salario mensual (en miles de USD)
salario = np.array([2.5, 3.8, 4.0, 5.5, 7.2])

print("--- Datos del Experimento ---")
print(f"Años de experiencia (X): {experiencia}")
print(f"Salario mensual real (y): {salario}\n")


# =====================================================================
# IMPLEMENTACIÓN DE LA ECUACIÓN NORMAL
# =====================================================================
# Para ajustar el intercepto (b) en la ecuación de la recta (y = w*x + b),
# debemos agregar una columna de unos a nuestra matriz de características X.
# A esto se le conoce como la Matriz de Diseño.

# Generamos un arreglo bidimensional
X_matriz = experiencia.reshape(-1, 1)

# Creamos la columna de unos
unos = np.ones((len(experiencia), 1))

# Concatenamos horizontalmente para obtener la Matriz de Diseño
X_diseno = np.hstack((unos, X_matriz))

print("--- Matriz de Diseño X (Columna de Unos para Intercepto + Características) ---")
print(X_diseno)
print()

# Paso 1: Multiplicar transpuesta por X original: X^T * X
XT_X = X_diseno.T @ X_diseno

# Paso 2: Calcular la matriz inversa: (X^T * X)^(-1)
XT_X_inv = np.linalg.inv(XT_X)

# Paso 3: Multiplicar la inversa por la transpuesta de X y por y: (X^T * X)^(-1) * X^T * y
beta = XT_X_inv @ X_diseno.T @ salario

intercepto = beta[0]
pendiente = beta[1]

print("--- Coeficientes Estimados Analíticamente ---")
print(f"Intercepto (Beta 0) : {intercepto:.4f}")
print(f"Pendiente (Beta 1)  : {pendiente:.4f}")
print(f"Línea de Regresión  : Salario = {intercepto:.4f} + {pendiente:.4f} * Experiencia\n")


# =====================================================================
# MODELO PREDICATIVO
# =====================================================================
# Queremos predecir el salario de un nuevo empleado con 5 años de experiencia
nueva_experiencia = 5.0
salario_predicho = intercepto + pendiente * nueva_experiencia

print("--- Predicción de Datos Nuevos ---")
print(f"Para un empleado con {nueva_experiencia} años de experiencia,")
print(f"el salario estimado por el modelo analítico es: ${salario_predicho:.2f} k USD.")
