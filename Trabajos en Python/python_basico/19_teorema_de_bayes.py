# -*- coding: utf-8 -*-
"""
Script 19: Teorema de Bayes
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. La fórmula matemática de la probabilidad condicional y el Teorema de Bayes.
2. Cómo interpretar los conceptos de Probabilidad A Priori, Sensibilidad (Verdadero Positivo), Tasa de Falsos Positivos y Probabilidad A Posteriori.
3. Un caso práctico clásico en medicina y detección de anomalías.
"""

# =====================================================================
# TEORÍA Y FÓRMULA MATEMÁTICA
# =====================================================================
# El Teorema de Bayes calcula la probabilidad de que ocurra un evento A dado que ocurrió B:
# P(A | B) = ( P(B | A) * P(A) ) / P(B)
# Donde:
# - P(A | B): Probabilidad a posteriori (lo que queremos calcular).
# - P(B | A): Probabilidad condicional conocida de observar B dado A.
# - P(A): Probabilidad a priori del evento A.
# - P(B): Probabilidad total de observar B.
#         P(B) = P(B | A)*P(A) + P(B | no A)*P(no A)

def calcular_bayes(p_prior_A, p_B_dado_A, p_B_dado_no_A):
    """
    Aplica el Teorema de Bayes para retornar la probabilidad condicional P(A | B).
    
    Parámetros:
    - p_prior_A: Probabilidad a priori de que ocurra A. (P(A))
    - p_B_dado_A: Probabilidad de observar el síntoma/evidencia B si ocurre A. (P(B|A) - Sensibilidad)
    - p_B_dado_no_A: Probabilidad de observar B si NO ocurre A. (P(B|no A) - Falso Positivo)
    """
    # 1. Calcular probabilidad de no A
    p_no_A = 1.0 - p_prior_A
    
    # 2. Calcular la probabilidad total de observar la evidencia B (Ley de Probabilidad Total)
    p_total_B = (p_B_dado_A * p_prior_A) + (p_B_dado_no_A * p_no_A)
    
    # 3. Aplicar fórmula de Bayes
    p_A_dado_B = (p_B_dado_A * p_prior_A) / p_total_B
    
    return p_A_dado_B, p_total_B


# =====================================================================
# CASO PRÁCTICO: Detección de Enfermedades Raras por Pruebas Clínicas
# =====================================================================
# Supongamos que una enfermedad rara afecta al 1% de la población (P(A) = 0.01).
# Existe una prueba clínica para detectarla con las siguientes características:
# - Sensibilidad (Verdadero Positivo): 95% de los enfermos dan positivo (P(B | A) = 0.95).
# - Falso Positivo: 5% de las personas sanas dan positivo de todos modos (P(B | no A) = 0.05).
#
# Queremos saber: Si un paciente da positivo en la prueba, ¿cuál es la probabilidad real de que tenga la enfermedad?

prob_prior_enfermedad = 0.01
sensibilidad = 0.95
falso_positivo = 0.05

prob_real_enfermo, prob_positivo_total = calcular_bayes(
    p_prior_A=prob_prior_enfermedad,
    p_B_dado_A=sensibilidad,
    p_B_dado_no_A=falso_positivo
)

print("--- ANÁLISIS DE PROBABILIDAD CONDICIONAL (TEOREMA DE BAYES) ---")
print(f"Probabilidad a priori de estar enfermo: {prob_prior_enfermedad * 100}%")
print(f"Sensibilidad del test (Verdadero Positivo): {sensibilidad * 100}%")
print(f"Tasa de falso positivo del test: {falso_positivo * 100}%")

print("\n--- RESULTADOS ---")
print(f"Probabilidad de que cualquier persona dé positivo en el test P(B): {prob_positivo_total * 100:.2f}%")
print(f"Probabilidad de estar realmente enfermo si el test dio positivo P(A|B): {prob_real_enfermo * 100:.2f}%")

print("\nInterpretación:")
print("Aunque la prueba es 95% precisa, como la enfermedad es muy rara, la mayoría de los positivos")
print("serán falsos positivos de la población sana. Por eso la probabilidad real de estar enfermo")
print("al dar positivo es de solo 16.10%. Esto justifica el uso de una segunda prueba confirmatoria.")
