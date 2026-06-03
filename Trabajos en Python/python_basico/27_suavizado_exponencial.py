# -*- coding: utf-8 -*-
"""
Script 27: Suavizado Exponencial Simple (Filtro Móvil)
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. El concepto matemático de Suavizado Exponencial Simple (SES) para series de tiempo y datos secuenciales.
2. Cómo reducir el ruido de alta frecuencia (variaciones aleatorias) en una señal.
3. El rol del factor de suavizado alpha (ponderación de datos recientes frente a históricos).
4. La fórmula recursiva de actualización de la señal.
"""

import numpy as np

# =====================================================================
# TEORÍA Y FÓRMULA MATEMÁTICA
# =====================================================================
# El suavizado exponencial es un método recursivo para pronosticar y filtrar series de tiempo.
# Se le asigna pesos exponencialmente decrecientes a las observaciones pasadas.
#
# Fórmula matemática recursiva:
# S_t = alpha * Y_t + (1 - alpha) * S_(t-1)
#
# Donde:
# - S_t: Valor suavizado (estimación filtrada) en el periodo t.
# - Y_t: Valor real observado en el periodo t (entrada con ruido).
# - S_(t-1): Valor suavizado del periodo anterior.
# - alpha: Parámetro de suavizado (0 < alpha <= 1).
#   * Si alpha está cercano a 1: Da alta prioridad al valor más nuevo (reacciona rápido).
#   * Si alpha está cercano a 0: Da alta prioridad al historial (suaviza mucho, reacciona lento).

def suavizado_exponencial_simple(serie_temporal, alpha):
    """
    Aplica suavizado exponencial simple sobre una secuencia de datos numéricos.
    """
    n = len(serie_temporal)
    valores_suavizados = np.zeros(n)
    
    # Inicialización: El primer valor suavizado es igual a la primera observación real
    valores_suavizados[0] = serie_temporal[0]
    
    # Bucle recursivo
    for t in range(1, n):
        valores_suavizados[t] = alpha * serie_temporal[t] + (1 - alpha) * valores_suavizados[t - 1]
        
    return valores_suavizados


# =====================================================================
# APLICACIÓN PRÁCTICA
# =====================================================================
# Datos simulados de temperatura diaria con ruido del sensor
serie_ruido = np.array([22.1, 23.5, 21.8, 24.9, 23.1, 26.2, 22.8, 25.0])

# Aplicaremos dos niveles de suavizado para observar la sensibilidad de alpha
alpha_sensible = 0.8  # Reacciona rápido, filtra poco ruido
alpha_suave = 0.3     # Reacciona lento, filtra mucho ruido

suavizado_80 = suavizado_exponencial_simple(serie_ruido, alpha=alpha_sensible)
suavizado_30 = suavizado_exponencial_simple(serie_ruido, alpha=alpha_suave)

print("--- SUAVIZADO EXPONENCIAL SIMPLE ---")
print(f"Serie original (con ruido): {serie_ruido}\n")

print("--- Comparativa paso a paso ---")
print(f"{'Paso':<5} | {'Original':<10} | {'Suave (alpha=0.8)':<18} | {'Suave (alpha=0.3)':<18}")
print("-" * 60)
for t in range(len(serie_ruido)):
    print(f"{t+1:<5} | {serie_ruido[t]:<10.2f} | {suavizado_80[t]:<18.4f} | {suavizado_30[t]:<18.4f}")

print("\nConclusiones del Análisis:")
print("- Con alpha = 0.8, el filtro se ajusta de cerca a los cambios del sensor.")
print("- Con alpha = 0.3, la curva de salida es mucho más estable y tiene menos picos drásticos.")
