# -*- coding: utf-8 -*-
"""
Script 38: Simulación de Entorno Interactivo (GridWorld) desde Cero
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. Cómo construir un entorno de Reinforcement Learning (Aprendizaje por Refuerzo) personalizado.
2. Definición del Espacio de Estados y Espacio de Acciones en un mundo de rejilla (GridWorld).
3. Ciclo de interacción clásica: reset, step (acción, recompensa, nuevo estado, término del episodio) y render.
4. Simulación del movimiento de un Agente que toma decisiones aleatorias en el entorno.
"""

import numpy as np

class EntornoRejilla:
    """
    Simulación de un entorno de cuadrícula (GridWorld) de 4x4.
    El agente inicia en la esquina superior izquierda (0,0) y busca llegar a la meta (3,3).
    Hay un obstáculo peligroso en (1,1) que da penalizaciones y una trampa en (2,2).
    """
    def __init__(self):
        self.filas = 4
        self.columnas = 4
        self.estado_inicio = (0, 0)
        self.estado_meta = (3, 3)
        self.obstaculo = (1, 1)
        self.trampa = (2, 2)
        
        # Espacio de acciones: 0: Arriba, 1: Abajo, 2: Izquierda, 3: Derecha
        self.acciones = {
            0: "ARRIBA",
            1: "ABAJO",
            2: "IZQUIERDA",
            3: "DERECHA"
        }
        self.reset()
        
    def reset(self):
        """Reinicia el entorno devolviendo al agente al punto de partida."""
        self.posicion_agente = self.estado_inicio
        return self.posicion_agente
    
    def step(self, accion):
        """
        Ejecuta la acción en el entorno y actualiza su estado.
        Devuelve: (nuevo_estado, recompensa, terminado, info)
        """
        fila, col = self.posicion_agente
        
        # Movimiento tentativo
        if accion == 0:    # ARRIBA
            fila = max(0, fila - 1)
        elif accion == 1:  # ABAJO
            fila = min(self.filas - 1, fila + 1)
        elif accion == 2:  # IZQUIERDA
            col = max(0, col - 1)
        elif accion == 3:  # DERECHA
            col = min(self.columnas - 1, col + 1)
            
        nueva_posicion = (fila, col)
        self.posicion_agente = nueva_posicion
        
        # Evaluar recompensa y fin de episodio
        terminado = False
        if nueva_posicion == self.estado_meta:
            recompensa = 10.0
            terminado = True
        elif nueva_posicion == self.obstaculo:
            recompensa = -5.0  # Penalización menor por pisar obstáculo
        elif nueva_posicion == self.trampa:
            recompensa = -10.0 # Penalización grave
            terminado = True
        else:
            recompensa = -1.0  # Penalización por cada paso transcurrido (fomenta rutas cortas)
            
        return nueva_posicion, recompensa, terminado, {}

    def render(self):
        """Muestra de manera visual en consola el estado actual de la cuadrícula."""
        grid = np.full((self.filas, self.columnas), ".", dtype=str)
        grid[self.estado_meta] = "M"     # Meta
        grid[self.obstaculo] = "O"       # Obstáculo
        grid[self.trampa] = "T"          # Trampa
        grid[self.posicion_agente] = "A" # Agente
        
        print("\n=== Estado del Tablero ===")
        for fila in grid:
            print(" ".join(fila))
        print("==========================")


# =====================================================================
# SIMULACIÓN CON UN AGENTE ALEATORIO
# =====================================================================
if __name__ == "__main__":
    np.random.seed(42)
    env = EntornoRejilla()
    estado = env.reset()
    
    print("--- INICIO DE LA SIMULACIÓN DEL ENTORNO ---")
    env.render()
    
    pasos = 0
    max_pasos = 10
    total_recompensa = 0.0
    terminado = False
    
    while not terminado and pasos < max_pasos:
        # Selección de una acción aleatoria (Exploración pura)
        accion = np.random.choice([0, 1, 2, 3])
        accion_nombre = env.acciones[accion]
        
        # El agente realiza la acción y recibe feedback del entorno
        nuevo_estado, recompensa, terminado, _ = env.step(accion)
        total_recompensa += recompensa
        pasos += 1
        
        print(f"\nPaso {pasos} | Acción tomada: {accion_nombre}")
        print(f"Nuevo Estado: {nuevo_estado} | Recompensa: {recompensa}")
        env.render()
        
        if terminado:
            if nuevo_estado == env.estado_meta:
                print("\n¡Éxito! El agente ha llegado a la Meta (M).")
            else:
                print("\n¡Derrota! El agente ha caído en una Trampa (T).")
                
    print(f"\nResumen de la simulación:")
    print(f"Pasos ejecutados : {pasos}")
    Total_recompensa = total_recompensa
    print(f"Recompensa Total : {total_recompensa}")
