# -*- coding: utf-8 -*-
"""
Script 12: Álgebra Matricial
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. Definición y propiedades de matrices en Python usando listas de listas y arreglos de NumPy.
2. Multiplicación de matrices (producto matricial) paso a paso y con NumPy.
3. Transposición de una matriz (intercambio de filas por columnas).
4. Cálculo de la traza de una matriz (suma de elementos en la diagonal principal).
"""

import numpy as np

# Definición de dos matrices para el producto matricial.
# Nota: Para multiplicar matrices, las columnas de A deben ser iguales a las filas de B.
# Matriz A de dimensiones 2x3 (2 filas, 3 columnas)
A = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matriz B de dimensiones 3x2 (3 filas, 2 columnas)
B = [
    [7, 8],
    [9, 1],
    [2, 3]
]

print("--- Matrices Originales ---")
print("Matriz A (2x3):")
for fila in A:
    print(f"  {fila}")

print("\nMatriz B (3x2):")
for fila in B:
    print(f"  {fila}")
print()


# =====================================================================
# 1. MULTIPLICACIÓN DE MATRICES (PRODUCTO MATRICIAL)
# =====================================================================
# El elemento en la posición C[i][j] se calcula como el producto punto de la fila i de A por la columna j de B.

# Cálculo manual paso a paso desde cero
filas_A = len(A)
columnas_A = len(A[0])
columnas_B = len(B[0])

# Inicializamos la matriz de resultados C con dimensiones 2x2 llena de ceros
C_manual = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

for i in range(filas_A):
    for j in range(columnas_B):
        # Producto punto de la fila i de A con la columna j de B
        suma = 0
        for k in range(columnas_A):
            suma += A[i][k] * B[k][j]
        C_manual[i][j] = suma

# Con NumPy (operador @ o np.dot)
np_A = np.array(A)
np_B = np.array(B)
C_numpy = np_A @ np_B

print("--- 1. MULTIPLICACIÓN DE MATRICES ---")
print("Resultado manual (C = A x B):")
for fila in C_manual:
    print(f"  {fila}")
print(f"Resultado con NumPy:\n{C_numpy}\n")


# =====================================================================
# 2. TRANSPOSICIÓN DE UNA MATRIZ
# =====================================================================
# La matriz transpuesta A^T se obtiene convirtiendo cada fila en columna: (A^T)[i][j] = A[j][i]

# Transposición con NumPy (.T)
A_transpuesta = np_A.T

print("--- 2. MATRIZ TRANSPUESTA DE A (A^T) ---")
print(f"A original (2x3):\n{np_A}")
print(f"A^T transpuesta (3x2):\n{A_transpuesta}\n")


# =====================================================================
# 3. TRAZA DE UNA MATRIZ
# =====================================================================
# La traza se define solo en matrices cuadradas. Es la suma de los valores en la diagonal principal.
# trace(M) = M[0][0] + M[1][1] + ... + M[n][n]

# Matriz cuadrada resultante C (2x2)
traza_manual = C_manual[0][0] + C_manual[1][1]
traza_numpy = np.trace(C_numpy)

print("--- 3. TRAZA DE LA MATRIZ CUADRADA C ---")
print(f"Matriz cuadrada C:\n{C_numpy}")
print(f"Traza manual (C[0][0] + C[1][1] = {C_manual[0][0]} + {C_manual[1][1]}): {traza_manual}")
print(f"Traza calculada por NumPy: {traza_numpy}")
