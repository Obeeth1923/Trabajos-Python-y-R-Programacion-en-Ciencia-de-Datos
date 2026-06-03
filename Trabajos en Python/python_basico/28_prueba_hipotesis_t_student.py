# -*- coding: utf-8 -*-
"""
Script 28: Prueba de Hipótesis T de Student (Una muestra)
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. El concepto matemático del contraste de hipótesis estadística.
2. Formulación de Hipótesis Nula (H0) e Hipótesis Alternativa (H1).
3. Cálculo manual de la estadística T para una muestra.
4. Toma de decisiones basada en el valor crítico de T de Student y la interpretación estadística.
"""

import math
import numpy as np

# =====================================================================
# CASO DE ESTUDIO
# =====================================================================
# Un fabricante afirma que sus baterías duran en promedio 50 horas (mu_afirmada = 50.0).
# Para validar la afirmación, tomamos una muestra aleatoria de 9 baterías.
# Queremos evaluar si el promedio real es menor y el fabricante miente.

muestra_baterias = np.array([48.5, 49.0, 51.2, 47.0, 48.0, 50.5, 46.5, 49.5, 48.2])

# Configuración del test
mu_afirmada = 50.0
n = len(muestra_baterias)
grados_libertad = n - 1

print("--- PRUEBA DE HIPÓTESIS (T DE STUDENT) ---")
print(f"Baterías de muestra analizadas: {muestra_baterias}")
print(f"Tamaño de muestra (n): {n}")
print(f"Grados de libertad (df): {grados_libertad}\n")


# =====================================================================
# FORMULACIÓN DE HIPÓTESIS
# =====================================================================
# H0 (Hipótesis Nula): mu >= 50 (La duración promedio es igual o mayor a la que dice el fabricante)
# H1 (Hipótesis Alternativa): mu < 50 (La duración promedio real es significativamente menor)
# Nivel de significancia (alpha) = 0.05 (Confianza del 95%)


# =====================================================================
# CÁLCULO ESTADÍSTICO MANUAL
# =====================================================================
# 1. Media de la muestra (X_barra)
media_muestral = np.mean(muestra_baterias)

# 2. Desviación estándar muestral (s) con corrección de Bessel
desviacion_muestral = np.std(muestra_baterias, ddof=1)

# 3. Error estándar de la media (SE)
# SE = s / sqrt(n)
error_estandar = desviacion_muestral / math.sqrt(n)

# 4. Estadístico T
# T = ( X_barra - mu_afirmada ) / SE
t_estadistico = (media_muestral - mu_afirmada) / error_estandar

print("--- Estadísticas Calculadas ---")
print(f"Media Muestral (X_barra)   : {media_muestral:.4f} horas")
print(f"Desviación Estándar (s)    : {desviacion_muestral:.4f}")
print(f"Error Estándar (SE)        : {error_estandar:.4f}")
print(f"Estadístico T calculado    : {t_estadistico:.4f}\n")


# =====================================================================
# TOMA DE DECISIONES CON VALOR CRÍTICO TEÓRICO
# =====================================================================
# Para df = 8 (9 - 1) y un test de una cola hacia la izquierda con alpha = 0.05,
# el valor crítico teórico de la tabla T de Student es -1.8595.
# Criterio de rechazo: Rechazamos H0 si T_calculado < T_critico

t_critico = -1.8595

print("--- DECISIÓN ESTADÍSTICA ---")
print(f"Valor crítico de la tabla T (df=8, alpha=0.05, unilateral): {t_critico}")

if t_estadistico < t_critico:
    conclusion = "RECHAZAR la Hipótesis Nula (H0). Hay suficiente evidencia estadística" \
                 "\npara concluir que el promedio de duración real de las baterías es menor a 50 horas."
else:
    conclusion = "NO RECHAZAR la Hipótesis Nula (H0). No hay pruebas suficientes para " \
                 "\ndecir que el fabricante miente."

print(f"Resultado: {conclusion}")
