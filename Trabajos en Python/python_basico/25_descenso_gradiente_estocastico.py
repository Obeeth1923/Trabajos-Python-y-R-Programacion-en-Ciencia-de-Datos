# -*- coding: utf-8 -*-
"""
Script 25: Descenso de Gradiente Estocástico (SGD)
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. El fundamento del Descenso de Gradiente Estocástico (SGD).
2. Diferencia matemática con el Descenso de Gradiente en Lotes (Batch Gradient Descent).
3. Simulación de la optimización paso a paso actualizando parámetros registro por registro.
4. Cómo la estocasticidad (aleatoriedad) ayuda a escapar de mínimos locales y reduce costos en grandes bases de datos.
"""

import numpy as np

# =====================================================================
# DIFERENCIA TEÓRICA
# =====================================================================
# - Batch Gradient Descent: Calcula el gradiente usando TODOS los datos
#   en cada paso. Es muy costoso con millones de registros.
# - Stochastic Gradient Descent (SGD): Elige UN SOLO registro aleatorio
#   en cada iteración para calcular el gradiente y actualizar el parámetro.
#   Introduce ruido en la trayectoria de optimización, pero es sumamente rápido.

# Datos del problema: Ajustaremos un modelo simple de regresión y = w * x (sin intercepto)
# Características (X) y Etiquetas (y) correspondientes
X = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.2, 3.9, 6.1, 8.0, 10.2])  # Relación real cercana a y = 2.0 * x

# Función de pérdida cuadrática para un único registro (i):
# Loss_i = (w * x_i - y_i)^2
# Su derivada respecto al peso w (Gradiente para el registro i):
# dLoss_i / dw = 2 * (w * x_i - y_i) * x_i

def gradiente_individual(w, x_i, y_i):
    """Calcula el gradiente de la pérdida respecto al peso w para una única muestra."""
    return 2 * (w * x_i - y_i) * x_i


# =====================================================================
# ALGORITMO SGD
# =====================================================================

# Inicialización
peso_actual = 0.0          # Peso inicial
tasa_aprendizaje = 0.01    # Learning Rate constante
epocas = 4                 # Cantidad de veces que recorreremos todo el conjunto de datos
n_muestras = len(X)

# Semilla aleatoria fija para reproducibilidad
np.random.seed(42)

print("--- OPTIMIZACIÓN MEDIANTE SGD ---")
print(f"Relación aproximada buscada: y = 2 * x")
print(f"Peso inicial w = {peso_actual}\n")

# Bucle principal de entrenamiento
for epoca in range(1, epocas + 1):
    print(f"ÉPOCA {epoca}:")
    
    # En SGD, ordenamos aleatoriamente los índices al inicio de cada época para romper sesgos
    indices_mezclados = np.random.permutation(n_muestras)
    
    for paso, idx in enumerate(indices_mezclados, 1):
        x_i = X[idx]
        y_i = y[idx]
        
        # Calcular gradiente solo para esta muestra elegida
        grad_i = gradiente_individual(peso_actual, x_i, y_i)
        
        # Guardar valor previo para el print
        peso_anterior = peso_actual
        
        # Actualización del parámetro
        peso_actual = peso_actual - tasa_aprendizaje * grad_i
        
        # Calcular la pérdida en toda la muestra solo para monitoreo
        perdida_promedio = np.mean((peso_actual * X - y) ** 2)
        
        print(f"  Paso {paso}: Muestra index {idx} (x={x_i}, y={y_i}) | "
              f"Gradiente={grad_i:6.2f} | w_prev={peso_anterior:5.2f} -> w_nuevo={peso_actual:5.2f} | "
              f"Pérdida Global={perdida_promedio:6.4f}")
    print("-" * 85)

print(f"\nPeso óptimo final estimado w: {peso_actual:.4f}")
print("Nota: El modelo óptimo converge rápidamente hacia w ≈ 2.0.")
