# ==============================================================================
# 08_q_learning_basico.R: Algoritmo Q-Learning en un Laberinto de Rejilla (4x4)
# ==============================================================================

# 1. Carga de librerías
# Usaremos únicamente R base para asegurar portabilidad y un enfoque puramente algorítmico

# 2. Configuración del entorno
# Representaremos una rejilla 4x4 donde las posiciones representan estados del 1 al 16.
# Posición (1,1) es el Estado 1 (Inicio). Posición (4,4) es el Estado 16 (Meta/Goal).
# Hay un obstáculo (pared) en la posición (2,2) -> Estado 6, y en (3,2) -> Estado 10.

ancho <- 4
alto <- 4
n_estados <- ancho * alto
n_acciones <- 4 # 1: Arriba, 2: Abajo, 3: Izquierda, 4: Derecha

# Matriz de recompensa (inicializada en -1 por cada paso para penalizar retrasos)
recompensas <- rep(-1, n_estados)
recompensas[16] <- 100 # Recompensa máxima al llegar a la meta
obstaculos <- c(6, 10)
recompensas[obstaculos] <- -100 # Penalización por chocar con obstáculos

# Función para obtener las coordenadas (x, y) de un número de estado
estado_a_coordenadas <- function(estado) {
  y <- ceiling(estado / ancho)
  x <- estado - (y - 1) * ancho
  return(c(x, y))
}

# Función para obtener el número de estado a partir de coordenadas (x, y)
coordenadas_a_estado <- function(coords) {
  return(coords[1] + (coords[2] - 1) * ancho)
}

# Función de transición
dar_paso <- function(estado_actual, accion) {
  coords <- estado_a_coordenadas(estado_actual)
  x <- coords[1]
  y <- coords[2]
  
  if (accion == 1) y <- max(1, y - 1)      # Arriba
  else if (accion == 2) y <- min(alto, y + 1) # Abajo
  else if (accion == 3) x <- max(1, x - 1)  # Izquierda
  else if (accion == 4) x <- min(ancho, x + 1) # Derecha
  
  nuevo_estado <- coordenadas_a_estado(c(x, y))
  
  # Si es un obstáculo, el agente rebota y se queda en su estado actual, recibiendo penalización
  if (nuevo_estado %in% obstaculos) {
    return(list(s_siguiente = estado_actual, recompensa = recompensas[nuevo_estado]))
  }
  
  return(list(s_siguiente = nuevo_estado, recompensa = recompensas[nuevo_estado]))
}

# 3. Entrenamiento (Algoritmo Q-Learning)
# Inicializar la Q-Table con ceros
Q <- matrix(0, nrow = n_estados, ncol = n_acciones)

# Parámetros del algoritmo
alpha <- 0.1     # Tasa de aprendizaje
gamma <- 0.9     # Factor de descuento
epsilon <- 0.2   # Tasa de exploración
episodios <- 1000

set.seed(333)
for (ep in 1:episodios) {
  estado <- 1 # Iniciar siempre en el Estado 1
  
  while (estado != 16) {
    # Estrategia Epsilon-Greedy
    if (runif(1) < epsilon) {
      accion <- sample(1:n_acciones, 1) # Exploración
    } else {
      # Explotación: elegir la mejor acción (rompiendo empates aleatoriamente)
      max_valores <- Q[estado, ] == max(Q[estado, ])
      accion <- sample(which(max_valores), 1)
    }
    
    # Ejecutar acción
    resultado <- dar_paso(estado, accion)
    s_siguiente <- resultado$s_siguiente
    recompensa <- resultado$recompensa
    
    # Actualizar Q-Table utilizando la ecuación de Bellman
    max_futuro <- max(Q[s_siguiente, ])
    Q[estado, accion] <- Q[estado, accion] + alpha * (recompensa + gamma * max_futuro - Q[estado, accion])
    
    estado <- s_siguiente
  }
}

# 4. Evaluación y Visualización del Camino Óptimo
print("Q-Table Finalizada:")
print(round(Q, 2))

# Simular el camino óptimo aprendido por el agente
camino <- 1
estado <- 1
limite_pasos <- 15
pasos <- 0

while (estado != 16 && pasos < limite_pasos) {
  accion <- which.max(Q[estado, ])
  resultado <- dar_paso(estado, accion)
  estado <- resultado$s_siguiente
  camino <- c(camino, estado)
  pasos <- pasos + 1
}

print("Camino Óptimo Encontrado (Historial de Estados):")
print(camino)
