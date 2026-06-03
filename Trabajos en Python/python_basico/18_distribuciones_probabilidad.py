# -*- coding: utf-8 -*-
"""
Script 18: Distribuciones de Probabilidad (Binomial y Normal)
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. Función de Masa de Probabilidad (PMF) para una Distribución Binomial (Discreta).
2. Función de Densidad de Probabilidad (PDF) para una Distribución Normal (Continua).
3. Implementación de las fórmulas matemáticas nativas utilizando las librerías matemáticas estándar de Python.
"""

import math

# =====================================================================
# 1. DISTRIBUCIÓN BINOMIAL (DISCRETA)
# =====================================================================
# Describe la probabilidad de tener exactamente 'k' éxitos en 'n' ensayos independientes,
# con una probabilidad de éxito 'p' en cada ensayo.
# Fórmula PMF: P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)
# Donde C(n, k) es el coeficiente binomial: n! / (k! * (n - k)!)

def coeficiente_binomial(n, k):
    """Calcula las combinaciones de n elementos tomados de k en k."""
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def binomial_pmf(k, n, p):
    """Calcula la probabilidad de obtener exactamente k éxitos."""
    combinaciones = coeficiente_binomial(n, k)
    probabilidad = combinaciones * (p ** k) * ((1 - p) ** (n - k))
    return probabilidad


# =====================================================================
# 2. DISTRIBUCIÓN NORMAL (CONTINUA / GAUSSIANA)
# =====================================================================
# Describe variables continuas que se agrupan simétricamente alrededor de la media (mu).
# Fórmula PDF: f(x) = (1 / (sigma * sqrt(2 * pi))) * e^( -0.5 * ((x - mu) / sigma)^2 )
# Donde sigma es la desviación estándar y mu es la media.

def normal_pdf(x, mu, sigma):
    """Calcula el valor de la función de densidad de probabilidad normal para un valor x."""
    coeficiente = 1 / (sigma * math.sqrt(2 * math.pi))
    exponente = -0.5 * (((x - mu) / sigma) ** 2)
    densidad = coeficiente * math.exp(exponente)
    return densidad


# =====================================================================
# PRUEBAS Y APLICACIONES PRÁCTICAS
# =====================================================================

print("--- 1. PRUEBA DE DISTRIBUCIÓN BINOMIAL ---")
# Supongamos que mandamos 10 correos electrónicos a clientes y la probabilidad histórica de apertura es del 30% (p = 0.3).
# Queremos saber la probabilidad de que exactamente 3 personas abran el correo.
n_ensayos = 10
k_exitos = 3
p_exito = 0.3

prob_binomial = binomial_pmf(k_exitos, n_ensayos, p_exito)
print(f"Número de ensayos (correos enviados): {n_ensayos}")
print(f"Probabilidad de éxito individual (apertura): {p_exito}")
print(f"Probabilidad de que abran exactamente {k_exitos} correos: {prob_binomial * 100:.4f}%\n")


print("--- 2. PRUEBA DE DISTRIBUCIÓN NORMAL ---")
# Supongamos que la altura promedio de una población es mu = 170 cm y la desviación estándar es sigma = 10 cm.
# Calcularemos la densidad de probabilidad para tres estaturas diferentes (170 cm, 185 cm, 150 cm).
mu_altura = 170.0
sigma_altura = 10.0

estaturas_evaluar = [170.0, 185.0, 150.0]

print(f"Parámetros de población: Media (mu) = {mu_altura}cm | Desviación (sigma) = {sigma_altura}cm")
for estatura in estaturas_evaluar:
    densidad = normal_pdf(estatura, mu_altura, sigma_altura)
    print(f"  Densidad de probabilidad para estatura {estatura} cm: {densidad:.6f}")
print("\nNota: La densidad más alta se encuentra siempre en el punto medio (la media, 170cm).")
