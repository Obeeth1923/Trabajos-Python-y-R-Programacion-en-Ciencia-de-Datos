# -*- coding: utf-8 -*-
"""
Script 29: Teorema del Límite Central (Simulación)
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. El concepto del Teorema del Límite Central (TLC).
2. Simulación práctica generando múltiples muestras independientes de distribuciones no normales (Exponencial).
3. Cálculo y análisis de las medias de estas muestras.
4. Cómo la distribución de medias converge a una curva normal perfecta a medida que aumenta la muestra.
"""

import numpy as np

# =====================================================================
# TEORÍA DEL TEOREMA DEL LÍMITE CENTRAL (TLC)
# =====================================================================
# El TLC establece que, dada una población con cualquier tipo de distribución
# (incluso si no es normal, ej. uniforme, exponencial o sesgada), la distribución
# de las medias muestrales tenderá a seguir una Distribución Normal
# a medida que el tamaño de la muestra (n) se vuelve suficientemente grande (típicamente n >= 30).

# Fijamos semilla para reproducibilidad
np.random.seed(42)

# =====================================================================
# PARÁMETROS DE LA SIMULACIÓN
# =====================================================================
# Población base: Distribución Exponencial (altamente asimétrica y no normal)
# Escala (beta) = 10.0. Su media teórica es 10.
media_poblacional = 10.0

tamano_muestra = 50        # n = 50 (suficiente para que actúe el TLC)
cantidad_simulaciones = 1000  # Número de medias que vamos a promediar

medias_muestrales = []

print("--- SIMULACIÓN DEL TEOREMA DEL LÍMITE CENTRAL ---")
print(f"Población de origen: Distribución Exponencial (Media real = {media_poblacional})")
print(f"Tomaremos {cantidad_simulaciones} muestras de tamaño n = {tamano_muestra}.\n")

# Bucle de simulación
for i in range(cantidad_simulaciones):
    # Generamos n muestras aleatorias exponenciales
    muestra = np.random.exponential(scale=media_poblacional, size=tamano_muestra)
    
    # Calculamos la media de esta muestra individual y la registramos
    media_i = np.mean(muestra)
    medias_muestrales.append(media_i)

# Convertimos a arreglo de NumPy para análisis estadístico final
medias_muestrales = np.array(medias_muestrales)

# =====================================================================
# EVALUACIÓN DE CONVERGENCIA
# =====================================================================
media_de_medias = np.mean(medias_muestrales)
desviacion_de_medias = np.std(medias_muestrales)

# Según la teoría matemática del TLC:
# - La media de la distribución de medias debe ser casi idéntica a la media de la población.
# - La desviación estándar de las medias (Error Estándar, SE) debe ser: sigma / sqrt(n)
#   Para nuestra distribución exponencial, la desviación estándar poblacional (sigma) es igual a la media (10.0).
error_estandar_teorico = media_poblacional / np.sqrt(tamano_muestra)

print("--- RESULTADOS SIMULADOS VS TEÓRICOS ---")
print(f"Media real de la población original : {media_poblacional}")
print(f"Media de todas las muestras promediadas (S_t) : {media_de_medias:.4f}")
print(f"Desviación estándar de medias calculada (SE) : {desviacion_de_medias:.4f}")
print(f"Error estándar teórico esperado (sigma/sqrt(n)) : {error_estandar_teorico:.4f}")

print("\nInterpretación:")
print("A pesar de que las muestras individuales provienen de una curva exponencial asimétrica,")
print("el promedio de promedios se aproxima perfectamente a la media real y las variaciones")
print("de estas medias se ajustan al error estándar teórico, confirmando el comportamiento Gaussiano.")
