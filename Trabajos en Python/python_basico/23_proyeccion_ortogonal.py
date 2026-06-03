# -*- coding: utf-8 -*-
"""
Script 23: Proyección Ortogonal de Vectores
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. El concepto matemático de la proyección ortogonal.
2. Cómo proyectar un vector 'u' sobre la dirección de un vector 'v'.
3. Cálculo de la componente escalar y vectorial.
4. Aplicaciones en la descomposición de señales y reducción de dimensionalidad (ej. PCA).
"""

import numpy as np

# =====================================================================
# TEORÍA Y FÓRMULA MATEMÁTICA
# =====================================================================
# La proyección ortogonal de un vector 'u' sobre un vector 'v' se define como:
# proj_v(u) = ( (u · v) / ||v||^2 ) * v
#
# Donde:
# - (u · v) / ||v||^2  es un escalar (factor de escala).
# - proj_v(u) es un vector que apunta en la misma dirección que v.
#
# La parte residual (u - proj_v(u)) es ortogonal a v y representa la pérdida de información.

def calcular_proyeccion_ortogonal(u, v):
    """
    Calcula el vector proyección de u sobre la dirección de v.
    """
    producto_punto = np.dot(u, v)
    norma_v_cuadrada = np.sum(v ** 2)  # Equivalente a np.linalg.norm(v)**2
    
    # Factor escalar
    escalar_proyeccion = producto_punto / norma_v_cuadrada
    
    # Vector proyección
    vector_proyeccion = escalar_proyeccion * v
    return vector_proyeccion, escalar_proyeccion


# =====================================================================
# EJEMPLO PRÁCTICO
# =====================================================================

# Vector u (ej. Fuerza o tendencia combinada de dos variables del mercado)
u = np.array([4.0, 5.0])

# Vector v (ej. Eje principal de crecimiento económico sobre el que queremos proyectar)
v = np.array([3.0, 1.0])

print("--- Vectores Originales ---")
print(f"Vector u (a proyectar)      : {u}")
print(f"Vector v (dirección destino): {v}\n")

# Calcular proyección
proj_vectorial, proj_escalar = calcular_proyeccion_ortogonal(u, v)

# Componente residual (ortogonal)
residual = u - proj_vectorial

print("--- RESULTADOS DE LA PROYECCIÓN ---")
print(f"Componente Escalar de proyección (proporción): {proj_escalar:.4f}")
print(f"Vector Proyección proj_v(u)                  : {proj_vectorial}")
print(f"Vector Residual (Pérdida / Error)            : {residual}")

# Verificación matemática de ortogonalidad
# El producto punto entre el residuo y el vector de dirección v debe ser 0
verificacion_ortogonal = np.dot(residual, v)
print(f"\nVerificación matemática: Residuo · v = {verificacion_ortogonal:.15f}")
print("Nota: El resultado es prácticamente 0 (dentro de los límites de precisión numérica),")
print("lo que demuestra que el residuo y v son perfectamente perpendiculares.")
