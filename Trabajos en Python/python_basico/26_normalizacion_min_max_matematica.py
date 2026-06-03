# -*- coding: utf-8 -*-
"""
Script 26: Normalización y Estandarización de Datos
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. Implementación de la escala Min-Max para rango [0, 1].
2. Implementación de la estandarización Z-score (Media 0, Desviación Estándar 1).
3. Importancia matemática de estas técnicas para acelerar la convergencia en modelos de machine learning.
"""

import numpy as np

# =====================================================================
# 1. ESCALADO MIN-MAX
# =====================================================================
# Transforma los datos para que todos queden estrictamente dentro de un rango [0, 1] o [-1, 1].
# Fórmula matemática:
# X_escalado = ( X - X_min ) / ( X_max - X_min )

def normalizacion_min_max(datos):
    """
    Aplica el escalado Min-Max a un arreglo unidimensional o bidimensional de NumPy.
    """
    valor_min = np.min(datos, axis=0)
    valor_max = np.max(datos, axis=0)
    
    # Prevenir divisiones por cero si todas las características son iguales
    rango = valor_max - valor_min
    rango_limpio = np.where(rango == 0, 1.0, rango)
    
    datos_escalados = (datos - valor_min) / rango_limpio
    return datos_escalados, valor_min, valor_max


# =====================================================================
# 2. ESTANDARIZACIÓN Z-SCORE (STANDARD SCALER)
# =====================================================================
# Centra los datos en 0 y los escala según su variabilidad. No tiene límites fijos de salida.
# Fórmula matemática:
# X_estandarizado = ( X - mu ) / sigma
# Donde mu es la media y sigma es la desviación estándar.

def estandarizacion_z_score(datos):
    """
    Aplica la estandarización Z-score a un arreglo de NumPy.
    """
    media = np.mean(datos, axis=0)
    desviacion = np.std(datos, axis=0)
    
    # Prevenir divisiones por cero si la desviación es 0
    desviacion_limpia = np.where(desviacion == 0, 1.0, desviacion)
    
    datos_estandarizados = (datos - media) / desviacion_limpia
    return datos_estandarizados, media, desviacion


# =====================================================================
# APLICACIÓN PRÁCTICA
# =====================================================================

# Matriz de datos simulados (3 muestras y 2 características):
# Características: [Edad del cliente (en años), Salario anual (en miles USD)]
matriz_clientes = np.array([
    [20.0, 15.0],
    [40.0, 80.0],
    [60.0, 120.0]
])

print("--- Matriz de Características Original ---")
print("Fila 1: [Edad: 20, Salario: 15k]")
print("Fila 2: [Edad: 40, Salario: 80k]")
print("Fila 3: [Edad: 60, Salario: 120k]\n")

# A) Escalar Min-Max
datos_minmax, min_original, max_original = normalizacion_min_max(matriz_clientes)

print("--- 1. RESULTADOS MIN-MAX ---")
print(datos_minmax)
print("Nota: El valor mínimo de cada columna se convierte en 0.0 y el máximo en 1.0.\n")

# B) Estandarizar Z-Score
datos_zscore, media_original, std_original = estandarizacion_z_score(matriz_clientes)

print("--- 2. RESULTADOS Z-SCORE ---")
print(datos_zscore)
print(f"Medias calculadas de salida: {np.round(np.mean(datos_zscore, axis=0), 4)}")
print(f"Desviaciones calculadas de salida: {np.std(datos_zscore, axis=0)}")
print("Nota: La media es exactamente 0.0 y la desviación estándar de salida es 1.0.")
