# -*- coding: utf-8 -*-
"""
Script 14: Derivadas y Tasas de Cambio Numéricas
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. El concepto matemático de la derivada como límite de la tasa de cambio.
2. Cómo aproximar numéricamente la derivada en un punto usando el método de Diferencias Finitas (Diferencia Central).
3. Comparar el cálculo numérico aproximado frente al resultado analítico exacto.
"""

# =====================================================================
# 1. FUNCIÓN MATEMÁTICA Y DERIVADA ANALÍTICA (EXACTA)
# =====================================================================
# Definimos la función f(x) = 3*x^2 + 2*x + 5
def f(x):
    return 3 * (x ** 2) + 2 * x + 5

# Matemáticamente, aplicando reglas de derivación, la derivada de f(x) es:
# f'(x) = 6*x + 2
def f_derivada_analitica(x):
    return 6 * x + 2


# =====================================================================
# 2. APROXIMACIÓN NUMÉRICA (DIFERENCIAS FINITAS CENTRALES)
# =====================================================================
# La fórmula de la diferencia central para aproximar la derivada en un punto x es:
# f'(x) ≈ ( f(x + h) - f(x - h) ) / ( 2 * h )
# Donde 'h' es un incremento infinitesimalmente pequeño.

def aproximar_derivada(funcion, x, h=1e-5):
    """
    Calcula la derivada numérica en el punto 'x' usando diferencias finitas centrales.
    """
    cambio_superior = funcion(x + h)
    cambio_inferior = funcion(x - h)
    
    # Pendiente de la recta secante aproximada
    derivada_aproximada = (cambio_superior - cambio_inferior) / (2 * h)
    return derivada_aproximada


# =====================================================================
# 3. VERIFICACIÓN Y TASAS DE CAMBIO
# =====================================================================
# Evaluaremos la derivada (pendiente de la curva) en diferentes valores de x

puntos_evaluacion = [1.0, 0.0, -2.5]
h_paso = 1e-6  # Un valor muy pequeño para una alta precisión

print("--- APROXIMACIÓN DE DERIVADAS POR DIFERENCIAS FINITAS ---")
print(f"Función evaluada: f(x) = 3*x^2 + 2*x + 5")
print(f"Derivada exacta teórica: f'(x) = 6*x + 2\n")

for x in puntos_evaluacion:
    derivada_exacta = f_derivada_analitica(x)
    derivada_num = aproximar_derivada(f, x, h=h_paso)
    
    # Calcular el error absoluto de la aproximación
    error = abs(derivada_exacta - derivada_num)
    
    print(f"Para x = {x}:")
    print(f"  > Derivada Analítica (Exacta)  : {derivada_exacta:.6f}")
    print(f"  > Derivada Numérica (Aprox h)  : {derivada_num:.6f}")
    print(f"  > Error absoluto de estimación : {error:.1e}")
    print("-" * 50)
