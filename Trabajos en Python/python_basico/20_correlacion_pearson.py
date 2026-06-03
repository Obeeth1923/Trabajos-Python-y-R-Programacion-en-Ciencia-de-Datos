# -*- coding: utf-8 -*-
"""
Script 20: Coeficiente de Correlación de Pearson
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. El concepto matemático de la correlación lineal y covarianza.
2. Programación manual paso a paso del coeficiente de correlación de Pearson (r).
3. Verificación rápida de la solución usando la función np.corrcoef de NumPy.
"""

import math
import numpy as np

# =====================================================================
# TEORÍA Y FÓRMULA MATEMÁTICA
# =====================================================================
# El coeficiente de correlación de Pearson (r) se calcula como:
# r = Covarianza(X, Y) / ( Desviacion_Estandar(X) * Desviacion_Estandar(Y) )
#
# Fórmula matemática expandida:
# r = sum( (x_i - mean_x) * (y_i - mean_y) ) / sqrt( sum( (x_i - mean_x)^2 ) * sum( (y_i - mean_y)^2 ) )
#
# Rangos de r:
# - r = 1: Correlación lineal positiva perfecta.
# - r = -1: Correlación lineal negativa perfecta.
# - r = 0: No existe relación lineal entre las variables.

def calcular_correlacion_pearson(x, y):
    """
    Calcula manualmente el coeficiente de correlación de Pearson entre dos listas.
    """
    n = len(x)
    if n != len(y):
        raise ValueError("Los vectores x e y deben tener la misma longitud.")
    
    # 1. Calcular las medias
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # 2. Calcular los términos de la fórmula
    numerador = 0.0
    denominador_x = 0.0
    denominador_y = 0.0
    
    for xi, yi in zip(x, y):
        diff_x = xi - mean_x
        diff_y = yi - mean_y
        
        numerador += diff_x * diff_y
        denominador_x += diff_x ** 2
        denominador_y += diff_y ** 2
        
    denominador = math.sqrt(denominador_x * denominador_y)
    
    # Evitar divisiones por cero si la varianza de alguna variable es cero
    if denominador == 0:
        return 0.0
        
    return numerador / denominador


# =====================================================================
# APLICACIÓN PRÁCTICA CON DATOS SIMULADOS
# =====================================================================
# Supongamos que analizamos la relación entre las Horas de Estudio (X)
# y la Calificación Obtenida (Y) de un grupo de estudiantes.

horas_estudio = [2, 5, 8, 10, 15, 12, 6, 9]
calificacion = [55, 65, 75, 80, 95, 90, 70, 78]

print("--- ANÁLISIS DE CORRELACIÓN DE PEARSON ---")
print(f"Horas de estudio (X) : {horas_estudio}")
print(f"Calificación (Y)     : {calificacion}\n")

# Cálculo manual
r_manual = calcular_correlacion_pearson(horas_estudio, calificacion)

# Cálculo usando NumPy (corrcoef retorna una matriz de correlación)
matriz_correlacion = np.corrcoef(horas_estudio, calificacion)
r_numpy = matriz_correlacion[0, 1]

print("--- RESULTADOS ---")
print(f"Coeficiente r calculado manualmente: {r_manual:.6f}")
print(f"Coeficiente r obtenido con NumPy    : {r_numpy:.6f}\n")

# Interpretación estadística del resultado
if r_manual > 0.7:
    interpretacion = "Correlación positiva fuerte (A mayor horas de estudio, mayor calificación)"
elif r_manual < -0.7:
    interpretacion = "Correlación negativa fuerte"
else:
    interpretacion = "Correlación débil o nula"

print(f"Interpretación: {interpretacion}")
