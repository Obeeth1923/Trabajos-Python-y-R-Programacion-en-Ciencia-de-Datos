# -*- coding: utf-8 -*-
"""
Script 15: Algoritmo de Descenso del Gradiente en 1D
Profesor: Matemáticas Aplicadas a la Ciencia de Datos en Python

En este script aprenderás:
1. El funcionamiento básico de optimización matemática por Descenso del Gradiente.
2. Cómo minimizar una función de pérdida (en este caso f(x) = x^2).
3. El rol de la Tasa de Aprendizaje (Learning Rate, alpha).
4. La regla de actualización del parámetro: x = x - alpha * f'(x)
"""

# =====================================================================
# DEFINICIÓN DEL PROBLEMA DE OPTIMIZACIÓN
# =====================================================================

# Queremos encontrar el mínimo global de la función cuadrática f(x) = x^2
def funcion_costo(x):
    return x ** 2

# Su derivada matemática (el gradiente en 1D) es f'(x) = 2*x
def gradiente(x):
    return 2 * x


# =====================================================================
# ALGORITMO DEL DESCENSO DEL GRADIENTE
# =====================================================================

# Parámetros iniciales
x_inicial = 8.0              # Punto de partida aleatorio
tasa_aprendizaje = 0.1       # Tamaño del paso (Learning Rate)
tolerancia = 1e-5            # Criterio de parada si el cambio es insignificante
max_iteraciones = 30         # Límite de seguridad de ciclos

x_actual = x_inicial

print("--- OPTIMIZACIÓN CON DESCENSO DEL GRADIENTE (1D) ---")
print(f"Buscando el valor mínimo de f(x) = x^2 partiendo desde x = {x_inicial}")
print(f"Tasa de aprendizaje (Learning Rate) = {tasa_aprendizaje}\n")

# Bucle de optimización
for paso in range(1, max_iteraciones + 1):
    grad = gradiente(x_actual)
    valor_costo = funcion_costo(x_actual)
    
    # Aplicamos la regla de actualización: nos movemos en dirección contraria al gradiente
    x_nuevo = x_actual - tasa_aprendizaje * grad
    
    # Mostrar el progreso de la optimización en este paso
    print(f"  Paso {paso:02d}: x = {x_actual:8.5f} | f(x) = {valor_costo:8.5f} | gradiente = {grad:8.5f}")
    
    # Comprobar criterio de parada (convergencia)
    # Si la distancia al mínimo es extremadamente pequeña, paramos el algoritmo
    if abs(x_nuevo - x_actual) < tolerancia:
        x_actual = x_nuevo
        print(f"\n[CONVERGENCIA] El algoritmo convergió en el paso {paso}.")
        break
        
    x_actual = x_nuevo

print("\n--- RESULTADO DE LA OPTIMIZACIÓN ---")
print(f"Mínimo aproximado encontrado en x = {x_actual:.6f}")
print(f"Valor de la función en el mínimo f(x) = {funcion_costo(x_actual):.12f}")
print("Nota: El mínimo real analítico se encuentra exactamente en x = 0.")
