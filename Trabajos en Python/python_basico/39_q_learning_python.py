# -*- coding: utf-8 -*-
"""
Script 39: Algoritmo de Q-Learning con la Ecuación de Bellman
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. Implementación desde cero del algoritmo de Q-Learning clásico (libre de librerías externas complejas).
2. Estructuración e inicialización de la Q-Tabla para mapear pares Estado-Acción.
3. Actualización de la Q-Tabla basada en la Ecuación de Bellman Temporal-Difference (TD):
   Q(s, a) = Q(s, a) + alpha * [r + gamma * max_a' Q(s', a') - Q(s, a)]
4. Cómo un agente aprende a evitar penalizaciones y a trazar el camino óptimo hacia la meta.
"""

import numpy as np

# =====================================================================
# 1. DEFINICIÓN DEL ENTORNO INDEPENDIENTE
# =====================================================================
class RejillaSimple:
    """Entorno de rejilla de 3x3 para facilitar un aprendizaje rápido."""
    def __init__(self):
        self.filas = 3
        self.columnas = 3
        self.inicio = (0, 0)
        self.meta = (2, 2)
        self.obstaculo = (1, 1) # Da una penalización
        self.reset()
        
    def reset(self):
        self.agente_pos = self.inicio
        return self.agente_pos
    
    def step(self, accion):
        # 0: Arriba, 1: Abajo, 2: Izquierda, 3: Derecha
        r, c = self.agente_pos
        if accion == 0:    r = max(0, r - 1)
        elif accion == 1:  r = min(self.filas - 1, r + 1)
        elif accion == 2:  c = max(0, c - 1)
        elif accion == 3:  c = min(self.columnas - 1, c + 1)
        
        self.agente_pos = (r, c)
        
        # Determinar recompensa
        terminado = False
        if self.agente_pos == self.meta:
            recompensa = 20.0
            terminado = True
        elif self.agente_pos == self.obstaculo:
            recompensa = -5.0
        else:
            recompensa = -1.0  # Penalización de paso para incentivar rapidez
            
        return self.agente_pos, recompensa, terminado

# =====================================================================
# 2. CONFIGURACIÓN DEL AGENTE Y PARÁMETROS DE Q-LEARNING
# =====================================================================
env = RejillaSimple()

# Hiperparámetros de aprendizaje
ALPHA = 0.1      # Tasa de aprendizaje (Learning Rate)
GAMMA = 0.9      # Factor de descuento para recompensas futuras
EPSILON = 0.2    # Probabilidad de tomar una acción aleatoria (Exploración)
EPISODIOS = 500  # Cantidad de simulaciones completas para entrenar

# Inicializamos la Q-Tabla con ceros.
# Filas representan los estados posibles mapeados a un entero único: fila * 3 + col
# Columnas representan las 4 posibles acciones (Arriba, Abajo, Izquierda, Derecha)
n_estados = env.filas * env.columnas
n_acciones = 4
q_table = np.zeros((n_estados, n_acciones))

def pos_a_estado(pos):
    """Convierte la tupla de coordenadas (r, c) a un entero indexable en la tabla."""
    return pos[0] * env.columnas + pos[1]

# =====================================================================
# 3. PROCESO DE ENTRENAMIENTO (Q-LEARNING LOOP)
# =====================================================================
print("--- INICIANDO EL ENTRENAMIENTO DEL AGENTE ---")

for episodio in range(1, EPISODIOS + 1):
    pos = env.reset()
    estado = pos_a_estado(pos)
    terminado = False
    
    while not terminado:
        # Selección de acción usando Política Epsilon-Greedy
        if np.random.rand() < EPSILON:
            accion = np.random.randint(0, n_acciones) # Exploración
        else:
            accion = np.argmax(q_table[estado])       # Explotación
            
        # Ejecutar acción
        nueva_pos, recompensa, terminado = env.step(accion)
        nuevo_estado = pos_a_estado(nueva_pos)
        
        # Aplicación directa de la Ecuación de Bellman para TD-Learning
        mejor_accion_futura = np.argmax(q_table[nuevo_estado])
        target_q = recompensa + GAMMA * q_table[nuevo_estado, mejor_accion_futura]
        error_td = target_q - q_table[estado, accion]
        
        # Actualización de la Q-Tabla
        q_table[estado, accion] += ALPHA * error_td
        
        # Transición al siguiente estado
        estado = nuevo_estado

print(f"Entrenamiento terminado tras {EPISODIOS} episodios.")

# =====================================================================
# 4. EVALUACIÓN DE LA POLÍTICA APRENDIDA
# =====================================================================
print("\n--- Q-Tabla Final Entrenada (Redondeada a 2 decimales) ---")
print("Filas: Estados del 0 al 8 | Columnas: [Arriba, Abajo, Izquierda, Derecha]")
print(np.round(q_table, 2))

# Demostración de la ruta óptima aprendida (sin exploración)
print("\n--- Demostración de la Ruta Óptima ---")
pos = env.reset()
estado = pos_a_estado(pos)
terminado = False
ruta = [pos]

while not terminado:
    # Explotación pura para ver el camino óptimo
    accion = np.argmax(q_table[estado])
    pos, _, terminado = env.step(accion)
    estado = pos_a_estado(pos)
    ruta.append(pos)

print("Camino recorrido por el agente entrenado:")
print(" -> ".join(f"({r},{c})" for r, c in ruta))
