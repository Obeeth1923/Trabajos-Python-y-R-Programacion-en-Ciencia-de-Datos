# -*- coding: utf-8 -*-
"""
Script 11: Operaciones Vectoriales (Álgebra Lineal)
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. Cómo definir vectores usando listas nativas y arreglos de NumPy.
2. Cálculo de la Norma L2 (magnitud de un vector) de forma matemática paso a paso y con NumPy.
3. Cálculo del Producto Punto (dot product) desde cero y con NumPy.
4. Interpretación geométrica de estas operaciones.
"""

import math
import numpy as np

# Definición de dos vectores simulando características de dos productos (ej. calificación y precio normalizado)
v1 = [4.0, 3.0, 1.5]
v2 = [2.0, 5.0, 0.5]

print("--- Vectores Originales (Listas de Python) ---")
print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}\n")


# =====================================================================
# 1. NORMA DE UN VECTOR (NORMA L2)
# =====================================================================
# Formula matemática de la Norma L2 (Distancia Euclidiana desde el origen):
# ||v|| = sqrt( v_1^2 + v_2^2 + ... + v_n^2 )

# Cálculo manual desde cero
suma_cuadrados = sum(x**2 for x in v1)
norma_manual = math.sqrt(suma_cuadrados)

# Cálculo eficiente con NumPy
np_v1 = np.array(v1)
norma_numpy = np.linalg.norm(np_v1)

print("--- 1. CÁLCULO DE LA NORMA L2 (VECTOR 1) ---")
print(f"Norma calculada manualmente: {norma_manual:.4f}")
print(f"Norma calculada con NumPy: {norma_numpy:.4f}\n")


# =====================================================================
# 2. PRODUCTO PUNTO (DOT PRODUCT)
# =====================================================================
# El producto punto mide la proyección de un vector sobre otro y se define como:
# v1 · v2 = (v1_1 * v2_1) + (v1_2 * v2_2) + ... + (v1_n * v2_n)

# Cálculo manual desde cero usando zip para iterar sobre ambos vectores al mismo tiempo
producto_punto_manual = sum(x * y for x, y in zip(v1, v2))

# Cálculo eficiente con NumPy
np_v2 = np.array(v2)
producto_punto_numpy = np.dot(np_v1, np_v2)  # O también: np_v1 @ np_v2

print("--- 2. CÁLCULO DEL PRODUCTO PUNTO ---")
print(f"Fórmula: v1 · v2 = (4*2) + (3*5) + (1.5*0.5) = 8 + 15 + 0.75 = 23.75")
print(f"Producto punto manual: {producto_punto_manual:.4f}")
print(f"Producto punto con NumPy: {producto_punto_numpy:.4f}\n")


# =====================================================================
# 3. INTERPRETACIÓN: CÁLCULO DE SIMILITUD COSENO
# =====================================================================
# En ciencia de datos, la similitud coseno mide qué tan alineados están dos vectores:
# cos(theta) = (v1 · v2) / (||v1|| * ||v2||)

norma_v2 = np.linalg.norm(np_v2)
coseno_theta = producto_punto_numpy / (norma_numpy * norma_v2)

print("--- 3. SIMILITUD COSENO ---")
print(f"Similitud Coseno calculada: {coseno_theta:.4f}")
print("Nota: Un valor cercano a 1 indica que los vectores apuntan en direcciones muy similares.")
