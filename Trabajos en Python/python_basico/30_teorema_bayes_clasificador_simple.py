# -*- coding: utf-8 -*-
"""
Script 30: Clasificador Probabilístico Bayesiano Simple
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. El diseño computacional de un Clasificador Bayesiano Simple (Naive Bayes) para variables continuas.
2. Cálculo de verosimilitud usando la función de densidad de probabilidad Gaussiana (Normal PDF).
3. Cómo calcular y contrastar probabilidades a posteriori para asignar etiquetas de clasificación.
"""

import math
import numpy as np

# =====================================================================
# DISEÑO MATEMÁTICO DEL CLASIFICADOR
# =====================================================================
# Para clasificar un registro x (ej. temperatura de un servidor) en una clase C (ej. "Normal" o "Alerta"),
# calculamos la probabilidad a posteriori para cada clase usando Bayes:
# P(Clase | x) = ( P(x | Clase) * P(Clase) ) / P(x)
#
# Como P(x) es común para todas las clases, el clasificador decide comparando los numeradores:
# Decisión = argmax_c [ P(x | Clase_c) * P(Clase_c) ]
#
# Para una variable continua x, asumimos que sigue una distribución normal dentro de cada clase:
# P(x | Clase_c) = (1 / (sigma_c * sqrt(2 * pi))) * e^( -0.5 * ((x - mu_c) / sigma_c)^2 )

def evaluar_densidad_gaussiana(x, media, desviacion):
    """Calcula la probabilidad normal PDF (verosimilitud) de x dada una media y desviación."""
    coeficiente = 1.0 / (desviacion * math.sqrt(2.0 * math.pi))
    exponente = -0.5 * (((x - media) / desviacion) ** 2)
    return coeficiente * math.exp(exponente)


# =====================================================================
# DATOS DE ENTRENAMIENTO DEL MODELO (PARÁMETROS ESTIMADOS)
# =====================================================================
# Entrenamos el clasificador calculando las estadísticas de temperaturas de servidores:

# Clase 0: Servidor Estable ("Normal")
media_normal = 42.0       # Temperatura promedio 42°C
std_normal = 3.5          # Desviación
prob_prior_normal = 0.85  # El 85% de las veces los servidores están estables

# Clase 1: Servidor en Anomalía ("Alerta")
media_alerta = 65.0       # Temperatura promedio 65°C
std_alerta = 8.0          # Desviación
prob_prior_alerta = 0.15  # Solo el 15% de las veces hay problemas


# =====================================================================
# CLASIFICACIÓN DE UNA NUEVA LECTURA DE TEMPERATURA
# =====================================================================

temperatura_observada = 55.0

print("--- CLASIFICADOR BAYESIANO GAUSSIANO ---")
print(f"Temperatura a evaluar: {temperatura_observada}°C\n")

# Paso 1: Calcular verosimilitud de la observación para cada clase P(x | Clase)
verosimilitud_normal = evaluar_densidad_gaussiana(temperatura_observada, media_normal, std_normal)
verosimilitud_alerta = evaluar_densidad_gaussiana(temperatura_observada, media_alerta, std_alerta)

# Paso 2: Multiplicar por las probabilidades a priori P(x | Clase) * P(Clase) (Numerador de Bayes)
numerador_normal = verosimilitud_normal * prob_prior_normal
numerador_alerta = verosimilitud_alerta * prob_prior_alerta

# Paso 3: Evidencia total P(x) = Suma de todos los numeradores (para normalizar probabilidades)
evidencia_total = numerador_normal + numerador_alerta

# Paso 4: Calcular probabilidades a posteriori completas P(Clase | x)
prob_post_normal = numerador_normal / evidencia_total
prob_post_alerta = numerador_alerta / evidencia_total

print("--- RESULTADOS DEL CÁLCULO ---")
print(f"Verosimilitud clase Normal: {verosimilitud_normal:.6f}")
print(f"Verosimilitud clase Alerta: {verosimilitud_alerta:.6f}\n")

print(f"Probabilidad A Posteriori - ESTABLE (Normal): {prob_post_normal * 100:.2f}%")
print(f"Probabilidad A Posteriori - ANOMALÍA (Alerta): {prob_post_alerta * 100:.2f}%")

# Clasificación final
if prob_post_alerta > prob_post_normal:
    etiqueta = "ALERTA (Anomalía)"
else:
    etiqueta = "ESTABLE (Normal)"

print(f"\nDecisión final del clasificador Bayesiano: Clasificar como '{etiqueta}'")
