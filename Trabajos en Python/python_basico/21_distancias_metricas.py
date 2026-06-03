# -*- coding: utf-8 -*-
"""
Script 21: Distancias Métricas (Euclidiana, Manhattan y Minkowski)
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. Implementación de la Distancia Euclidiana (Norma L2 de la diferencia).
2. Implementación de la Distancia Manhattan (Norma L1 de la diferencia).
3. Implementación de la Distancia Minkowski (Generalización paramétrica p).
4. El uso de estas métricas en algoritmos de machine learning basados en distancia (ej. KNN).
"""

import numpy as np

# Definición de dos puntos en un espacio tridimensional (ej. características de clientes: edad, ingresos, score)
punto_a = np.array([25.0, 50000.0, 4.2])
punto_b = np.array([30.0, 48000.0, 3.8])

print("--- Puntos de características evaluados ---")
print(f"Punto A: {punto_a}")
print(f"Punto B: {punto_b}\n")


# =====================================================================
# 1. DISTANCIA EUCLIDIANA (Métrica L2)
# =====================================================================
# Fórmula matemática:
# d_euclidiana = sqrt( sum( (x_i - y_i)^2 ) )

diferencia = punto_a - punto_b
dist_euclidiana = np.sqrt(np.sum(diferencia ** 2))
# Alternativa directa en NumPy: np.linalg.norm(punto_a - punto_b)

print("--- 1. DISTANCIA EUCLIDIANA ---")
print(f"Distancia Euclidiana calculada: {dist_euclidiana:.4f}\n")


# =====================================================================
# 2. DISTANCIA MANHATTAN (Métrica L1)
# =====================================================================
# Mide la distancia recorrida a lo largo de ejes perpendiculares (geometría de taxi).
# Fórmula matemática:
# d_manhattan = sum( |x_i - y_i| )

dist_manhattan = np.sum(np.abs(punto_a - punto_b))
# Alternativa directa en NumPy: np.linalg.norm(punto_a - punto_b, ord=1)

print("--- 2. DISTANCIA MANHATTAN ---")
print(f"Distancia Manhattan calculada: {dist_manhattan:.4f}\n")


# =====================================================================
# 3. DISTANCIA MINKOWSKI
# =====================================================================
# Es la generalización matemática que incluye a la Euclidiana y Manhattan.
# Fórmula matemática:
# d_minkowski = ( sum( |x_i - y_i|^p ) )^(1/p)
# - Si p = 1: Equivalente a la distancia Manhattan.
# - Si p = 2: Equivalente a la distancia Euclidiana.

def calcular_minkowski(x, y, p):
    """
    Calcula la distancia Minkowski paramétrica de orden p entre dos arreglos.
    """
    diferencia_abs = np.abs(x - y)
    suma_potencias = np.sum(diferencia_abs ** p)
    distancia = suma_potencias ** (1.0 / p)
    return distancia

# Evaluamos Minkowski con p=3 (espacio métrico de mayor orden)
parametro_p = 3
dist_minkowski_p3 = calcular_minkowski(punto_a, punto_b, p=parametro_p)
# Alternativa directa en NumPy: np.linalg.norm(punto_a - punto_b, ord=3)

print(f"--- 3. DISTANCIA MINKOWSKI (p={parametro_p}) ---")
print(f"Distancia Minkowski (p={parametro_p}) calculada: {dist_minkowski_p3:.4f}")
print("Nota: Las distancias son sensibles a la escala de las variables. En producción,")
print("los datos normalmente se normalizan antes de aplicar estas métricas.")
