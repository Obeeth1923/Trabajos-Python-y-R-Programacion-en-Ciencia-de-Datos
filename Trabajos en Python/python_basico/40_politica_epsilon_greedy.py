# -*- coding: utf-8 -*-
"""
Script 40: Estrategia Épsilon-Greedy (Exploración vs. Explotación)
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. El dilema central de Reinforcement Learning: Exploración vs. Explotación.
2. Cómo implementar la política Épsilon-Greedy de forma matemática y computacional.
3. El decaimiento exponencial de Épsilon (Epsilon Decay) para transicionar de exploración pura a explotación pura.
4. Simulación interactiva que muestra el conteo de decisiones aleatorias frente a decisiones optimizadas a lo largo del tiempo.
"""

import numpy as np

# =====================================================================
# 1. PARÁMETROS DE LA ESTRATEGIA ÉPSILON-GREEDY
# =====================================================================
# Épsilon inicial: 1.0 (exploración del 100%)
epsilon_inicial = 1.0
# Épsilon mínimo: 0.05 (mantiene un 5% de exploración residual para entornos dinámicos)
epsilon_minimo = 0.05
# Tasa de decaimiento: velocidad a la que epsilon disminuye en cada episodio
tasa_decaimiento = 0.015

print("--- ESTRATEGIA ÉPSILON-GREEDY ---")
print(f"Épsilon Inicial : {epsilon_inicial}")
print(f"Épsilon Mínimo  : {epsilon_minimo}")
print(f"Decay Rate      : {tasa_decaimiento}\n")

# =====================================================================
# 2. DEFINICIÓN DE LA FUNCIÓN DE DECISIÓN ÉPSILON-GREEDY
# =====================================================================
def seleccionar_accion(q_valores, epsilon, n_acciones=4):
    """
    Selecciona una acción basada en la política Epsilon-Greedy.
    - Con probabilidad Epsilon: se toma una acción aleatoria (Exploración).
    - Con probabilidad 1 - Epsilon: se toma la mejor acción conocida (Explotación).
    """
    probabilidad = np.random.rand()
    
    if probabilidad < epsilon:
        # Acción aleatoria (Exploración)
        accion = np.random.randint(0, n_acciones)
        es_exploracion = True
    else:
        # Acción codiciosa/óptima (Explotación)
        accion = np.argmax(q_valores)
        es_exploracion = False
        
    return accion, es_exploracion

# =====================================================================
# 3. SIMULACIÓN A LO LARGO DE MÚLTIPLES EPISODIOS
# =====================================================================
# Simulamos un agente entrenando durante 300 episodios.
# Simularemos valores Q de ejemplo para un estado determinado.
q_valores_estado = np.array([2.5, 0.1, -1.2, 5.0]) # La mejor acción es la 3 (valor 5.0)
n_episodios = 300

epsilon_actual = epsilon_inicial
historial_decisiones = []

print("--- Progreso del decaimiento y tipo de decisiones ---")
print(f"{'Episodio':<10} | {'Epsilon':<10} | {'Decisión Seleccionada'}")
print("-" * 50)

for episodio in range(1, n_episodios + 1):
    # Seleccionamos la acción basándonos en la probabilidad epsilon actual
    accion, es_exploracion = seleccionar_accion(q_valores_estado, epsilon_actual)
    historial_decisiones.append(es_exploracion)
    
    # Imprimimos logs periódicos de la evolución del agente
    if episodio in [1, 50, 100, 150, 200, 250, 300]:
        tipo_decision = "EXPLORACIÓN (Acción aleatoria)" if es_exploracion else "EXPLOTACIÓN (Mejor Acción)"
        print(f"Episodio {episodio:<2} | {epsilon_actual:.4f}   | {tipo_decision}")
        
    # Decaimiento exponencial de Epsilon
    # En cada paso, disminuimos la tasa de exploración para confiar más en los conocimientos adquiridos.
    epsilon_actual = max(epsilon_minimo, epsilon_inicial * np.exp(-tasa_decaimiento * episodio))

# =====================================================================
# 4. MÉTRICAS Y ANÁLISIS DE LA SIMULACIÓN
# =====================================================================
# Analizamos los primeros 50 episodios vs los últimos 50 episodios
primeros_50 = historial_decisiones[:50]
ultimos_50 = historial_decisiones[-50:]

pct_exploracion_inicio = (sum(primeros_50) / 50) * 100
pct_explotacion_inicio = 100 - pct_exploracion_inicio

pct_exploracion_fin = (sum(ultimos_50) / 50) * 100
pct_explotacion_fin = 100 - pct_exploracion_fin

print("\n--- Análisis de la Política de Aprendizaje ---")
print(f"Primeros 50 Episodios:")
print(f"  - Acciones de Exploración: {pct_exploracion_inicio:.1f}%")
print(f"  - Acciones de Explotación: {pct_explotacion_inicio:.1f}%")
print(f"Últimos 50 Episodios:")
print(f"  - Acciones de Exploración: {pct_exploracion_fin:.1f}% (Límite inferior ~5%)")
print(f"  - Acciones de Explotación: {pct_explotacion_fin:.1f}%")

print("\nNota Teórica: Al principio del aprendizaje, el agente no sabe nada del entorno,")
print("por lo que es fundamental explorar (epsilon alto). A medida que el tiempo avanza,")
print("el agente aprovecha el conocimiento recopilado en su tabla (explotación) y decae epsilon.")
