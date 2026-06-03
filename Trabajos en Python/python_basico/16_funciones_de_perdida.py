# -*- coding: utf-8 -*-
"""
Script 16: Funciones de Pérdida (Loss Functions)
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. Programación y concepto del Error Cuadrático Medio (MSE) para problemas de Regresión.
2. Programación y concepto de la Entropía Cruzada Binaria (Binary Cross-Entropy / Log Loss) para problemas de Clasificación.
3. El uso de NumPy para vectorizar estos cálculos de forma altamente eficiente.
"""

import numpy as np

# =====================================================================
# 1. ERROR CUADRÁTICO MEDIO (MSE - MEAN SQUARED ERROR)
# =====================================================================
# Se usa en regresión para medir la diferencia promedio al cuadrado entre predicciones y valores reales.
# MSE = (1 / n) * sum( (y_real_i - y_pred_i)^2 )

def calcular_mse(y_real, y_pred):
    """
    Calcula el Error Cuadrático Medio entre valores reales y predicciones.
    """
    # Convertimos a arreglos de NumPy para aprovechar la resta vectorizada y potenciación directa
    arr_real = np.array(y_real)
    arr_pred = np.array(y_pred)
    
    diferencias = arr_real - arr_pred
    diferencias_al_cuadrado = diferencias ** 2
    mse = np.mean(diferencias_al_cuadrado)
    
    return mse


# =====================================================================
# 2. ENTROPÍA CRUZADA BINARIA (LOG LOSS)
# =====================================================================
# Se usa en clasificación binaria para castigar predicciones seguras pero incorrectas.
# Log Loss = -(1 / n) * sum( y_real_i * log(y_pred_i) + (1 - y_real_i) * log(1 - y_pred_i) )
# Nota: Añadimos un valor épsilon (muy pequeño) para evitar errores matemáticos al calcular log(0).

def calcular_log_loss(y_real, y_pred_prob):
    """
    Calcula la Entropía Cruzada Binaria (Log Loss).
    y_pred_prob debe ser una probabilidad entre 0 y 1.
    """
    arr_real = np.array(y_real)
    arr_pred = np.array(y_pred_prob)
    
    # Clip para evitar log(0) o log(1) que tienden a infinito
    eps = 1e-15
    arr_pred = np.clip(arr_pred, eps, 1 - eps)
    
    # Fórmula de entropía cruzada
    termino_1 = arr_real * np.log(arr_pred)
    termino_2 = (1 - arr_real) * np.log(1 - arr_pred)
    
    log_loss = -np.mean(termino_1 + termino_2)
    return log_loss


# =====================================================================
# EVALUACIÓN DE LAS FUNCIONES DE PÉRDIDA
# =====================================================================

print("--- EVALUACIÓN DE FUNCIONES DE PÉRDIDA ---")

# Caso A: Regresión (Precios de casas en miles de dólares)
precios_reales = [250.0, 310.0, 180.0, 420.0]
precios_predichos = [245.0, 318.0, 172.0, 410.0]

mse_resultado = calcular_mse(precios_reales, precios_predichos)
rmse_resultado = np.sqrt(mse_resultado)  # Raíz del MSE (mismas unidades de medida)

print("1. Métrica de Regresión (MSE y RMSE):")
print(f"   Valores reales     : {precios_reales}")
print(f"   Valores predichos  : {precios_predichos}")
print(f"   Error Cuadrático Medio (MSE)     : {mse_resultado:.2f}")
print(f"   Raíz del Error Cuadrático (RMSE)  : {rmse_resultado:.2f} (Error promedio de +/- ${rmse_resultado * 1000:.0f} USD)\n")


# Caso B: Clasificación (¿Es correo spam? 1 = Sí, 0 = No)
spam_reales = [1, 0, 1, 1, 0]
spam_probabilidades = [0.90, 0.15, 0.85, 0.40, 0.05] # El 4to es spam pero el modelo le dio baja probabilidad (0.40)

log_loss_resultado = calcular_log_loss(spam_reales, spam_probabilidades)

print("2. Métrica de Clasificación (Log Loss):")
print(f"   Clases reales (Spam)           : {spam_reales}")
print(f"   Probabilidades predichas       : {spam_probabilidades}")
print(f"   Entropía Cruzada Binaria (Loss): {log_loss_resultado:.5f}")
print("Nota: Un valor de Log Loss más cercano a 0 representa un modelo con predicciones más precisas y seguras.")
