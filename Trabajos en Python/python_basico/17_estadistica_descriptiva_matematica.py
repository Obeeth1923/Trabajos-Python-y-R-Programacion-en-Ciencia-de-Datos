# -*- coding: utf-8 -*-
"""
Script 17: Estadística Descriptiva Matemática
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. El cálculo matemático y diferencia conceptual entre la Varianza Poblacional (sigma^2) y la Varianza Muestral (s^2).
2. Cálculo de la Desviación Estándar.
3. Programación manual paso a paso de estas fórmulas y verificación directa con NumPy.
"""

import math
import numpy as np

# Datos simulados: Puntajes de rendimiento de 8 servidores en una red de cómputo
datos = [85, 90, 88, 92, 78, 85, 94, 80]

print("--- Conjunto de Datos Original ---")
print(f"Datos: {datos}")
print(f"Cantidad de elementos (N): {len(datos)}\n")


# =====================================================================
# 1. CÁLCULO DE LA MEDIA (PROMEDIO)
# =====================================================================
# mu = (1 / N) * sum( x_i )
media = sum(datos) / len(datos)
print(f"Media matemática (promedio): {media:.2f}\n")


# =====================================================================
# 2. VARIANZA POBLACIONAL (sigma^2)
# =====================================================================
# Se usa cuando tenemos los datos de la población entera de estudio.
# formula: var_p = (1 / N) * sum( (x_i - mu)^2 )
suma_desviaciones_cuadrado = sum((x - media)**2 for x in datos)

varianza_poblacional_manual = suma_desviaciones_cuadrado / len(datos)

# Con NumPy (por defecto calcula varianza poblacional)
varianza_poblacional_numpy = np.var(datos)

print("--- 2. VARIANZA POBLACIONAL (Población completa) ---")
print(f"Varianza Poblacional manual: {varianza_poblacional_manual:.4f}")
print(f"Varianza Poblacional NumPy: {varianza_poblacional_numpy:.4f}\n")


# =====================================================================
# 3. VARIANZA MUESTRAL (s^2)
# =====================================================================
# Se usa cuando los datos son una muestra representativa de una población mayor.
# Se aplica la corrección de Bessel dividiendo entre (N - 1) para corregir el sesgo.
# formula: var_m = (1 / (N - 1)) * sum( (x_i - mu)^2 )

varianza_muestral_manual = suma_desviaciones_cuadrado / (len(datos) - 1)

# Con NumPy, forzamos la corrección de grados de libertad (ddof=1)
varianza_muestral_numpy = np.var(datos, ddof=1)

print("--- 3. VARIANZA MUESTRAL (Muestra extraída) ---")
print(f"Varianza Muestral manual (grados de libertad N-1): {varianza_muestral_manual:.4f}")
print(f"Varianza Muestral NumPy (ddof=1): {varianza_muestral_numpy:.4f}\n")


# =====================================================================
# 4. DESVIACIÓN ESTÁNDAR (std)
# =====================================================================
# Representa la dispersión de los datos en las mismas unidades originales (raíz cuadrada de la varianza).
# std = sqrt( varianza )

desviacion_muestral_manual = math.sqrt(varianza_muestral_manual)
desviacion_muestral_numpy = np.std(datos, ddof=1)

print("--- 4. DESVIACIÓN ESTÁNDAR MUESTRAL ---")
print(f"Desviación Estándar manual: {desviacion_muestral_manual:.4f}")
print(f"Desviación Estándar NumPy: {desviacion_muestral_numpy:.4f}")
print("Nota: Indica que en promedio, los puntajes varían aproximadamente +/- 5.53 puntos de la media.")
