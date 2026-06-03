# ==============================================================================
# 30_q_learning_politica_aproximada.R: Aprendizaje por Refuerzo con Aproximación Lineal
# ==============================================================================

# 1. Carga de librerías
# Usaremos R base para asegurar la legibilidad matemática y algorítmica
library(tidyverse)

# 2. Definición del Entorno Dinámico (Línea Continua)
# Estado: posición continua x en el rango [0, 10].
# Meta (Goal): llegar a x >= 10.
# Acciones: -1 (Izquierda), 1 (Derecha)

estado_inicial <- 1.0
meta <- 10.0

# 3. Aproximación de la Función de Valor de Acción Q(s, a)
# En lugar de una tabla Q, aproximamos Q(s, a) usando una función lineal:
# Q(s, a) = w0 + w1*s + w2*a + w3*s*a
# Representamos esto con un vector de pesos w de dimensión 4.

pesos_w <- c(0.0, 0.0, 0.0, 0.0) # Pesos iniciales

# Función para extraer características del par (estado, acción)
obtener_caracteristicas <- function(s, a) {
  return(c(1, s, a, s * a))
}

# Función para estimar el valor Q
estimar_q <- function(s, a, w) {
  phi <- obtener_caracteristicas(s, a)
  return(sum(phi * w))
}

# Elegir acción usando Epsilon-Greedy basada en la aproximación de Q
elegir_accion <- function(s, w, epsilon) {
  acciones_posibles <- c(-1, 1)
  if (runif(1) < epsilon) {
    return(sample(acciones_posibles, 1)) # Exploración
  } else {
    # Explotación: evaluar Q para cada acción y elegir la mejor
    q_valores <- sapply(acciones_posibles, function(a) estimar_q(s, a, w))
    return(acciones_posibles[which.max(q_valores)])
  }
}

# Función de transición del entorno
ejecutar_accion <- function(s, a) {
  # Agregar ruido dinámico al movimiento del agente
  nuevo_s <- s + a + rnorm(1, mean = 0, sd = 0.2)
  # Prevenir salirse del límite inferior
  nuevo_s <- max(0, nuevo_s)
  
  # Sistema de Recompensas
  if (nuevo_s >= meta) {
    recompensa <- 100 # Recompensa por alcanzar la meta
  } else {
    recompensa <- -1 # Penalización por paso de tiempo transcurrido
  }
  
  return(list(s_siguiente = nuevo_s, recompensa = recompensa))
}

# 4. Entrenamiento del Agente (Approximate Q-Learning)
alpha <- 0.01   # Tasa de aprendizaje de los pesos w
gamma <- 0.95   # Factor de descuento
epsilon <- 0.2  # Tasa de exploración
episodios <- 200

historial_pasos <- numeric(episodios)

set.seed(777)
for (ep in 1:episodios) {
  s <- estado_inicial
  pasos <- 0
  
  while (s < meta && pasos < 100) {
    a <- elegir_accion(s, pesos_w, epsilon)
    
    # Transición
    resultado <- ejecutar_accion(s, a)
    s_siguiente <- resultado$s_siguiente
    recompensa <- resultado$recompensa
    
    # Calcular objetivo temporal (TD-Target)
    if (s_siguiente >= meta) {
      max_q_siguiente <- 0.0 # No hay estado futuro al llegar a la meta
    } else {
      max_q_siguiente <- max(sapply(c(-1, 1), function(a_sig) estimar_q(s_siguiente, a_sig, pesos_w)))
    }
    
    td_target <- recompensa + gamma * max_q_siguiente
    td_error <- td_target - estimar_q(s, a, pesos_w)
    
    # Actualización de los pesos mediante gradiente descendente
    phi <- obtener_caracteristicas(s, a)
    pesos_w <- pesos_w + alpha * td_error * phi
    
    s <- s_siguiente
    pasos <- pasos + 1
  }
  
  historial_pasos[ep] <- pasos
}

print("Pesos de la función de aproximación finalizados:")
print(pesos_w)

# 5. Visualización del Rendimiento
eval_df <- tibble(
  Episodio = 1:episodios,
  Pasos = historial_pasos
)

# Gráfico de convergencia del entrenamiento
ggplot(eval_df, aes(x = Episodio, y = Pasos)) +
  geom_line(color = "#8e44ad", size = 1) +
  geom_smooth(method = "loess", color = "#2ecc71", se = FALSE, size = 1.2) +
  theme_minimal() +
  labs(title = "Convergencia de Q-Learning con Aproximación de Función",
       subtitle = "La línea verde muestra la tendencia de reducción de pasos para llegar al objetivo",
       x = "Episodio de Entrenamiento",
       y = "Número de Pasos hasta Meta")
