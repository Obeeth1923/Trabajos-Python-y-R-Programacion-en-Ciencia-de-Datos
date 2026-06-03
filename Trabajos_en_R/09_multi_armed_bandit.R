# ==============================================================================
# 09_multi_armed_bandit.R: Simulación del Bandido Multibrazo (Epsilon-Greedy)
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)

# 2. Configuración del Entorno de Simulación
# Definiremos 5 brazos con distintas probabilidades reales de dar recompensa (distribución de Bernoulli)
probabilidades_reales <- c(0.10, 0.30, 0.55, 0.80, 0.25) # El brazo 4 (0.80) es el óptimo
n_brazos <- length(probabilidades_reales)
n_pasos <- 1000

# Parámetros del agente
epsilon <- 0.1 # 10% de exploración, 90% de explotación

# Variables para guardar resultados históricos de la simulación
recompensa_acumulada <- numeric(n_pasos)
recompensa_promedio <- numeric(n_pasos)
brazos_elegidos <- integer(n_pasos)

# Variables de control del agente
contador_tiradas <- rep(0, n_brazos)
estimacion_valor <- rep(0.0, n_brazos) # Q(a): Valores estimados de cada brazo

# 3. Ejecución de la Simulación
set.seed(444)
for (t in 1:n_pasos) {
  # Decisión: Exploración o Explotación
  if (runif(1) < epsilon) {
    accion <- sample(1:n_brazos, 1) # Exploración aleatoria
  } else {
    # Explotación: Elegir el brazo con mayor valor estimado Q(a)
    max_valores <- estimacion_valor == max(estimacion_valor)
    accion <- sample(which(max_valores), 1) # Rompe empates de manera aleatoria
  }
  
  # Obtener recompensa del brazo elegido (1 si tiene éxito, 0 si no)
  recompensa <- ifelse(runif(1) < probabilidades_reales[accion], 1, 0)
  
  # Actualización incremental de la estimación del valor del brazo Q(accion)
  contador_tiradas[accion] <- contador_tiradas[accion] + 1
  n <- contador_tiradas[accion]
  estimacion_valor[accion] <- estimacion_valor[accion] + (1 / n) * (recompensa - estimacion_valor[accion])
  
  # Registro del paso
  brazos_elegidos[t] <- accion
  recompensa_acumulada[t] <- if (t == 1) recompensa else recompensa_acumulada[t - 1] + recompensa
  recompensa_promedio[t] <- recompensa_acumulada[t] / t
}

# 4. Evaluación y Visualización
print("Estimaciones Finales del Agente vs Probabilidades Reales:")
print(tibble(
  Brazo = 1:n_brazos,
  Probabilidad_Real = probabilidades_reales,
  Estimacion_Q = round(estimacion_valor, 3),
  Cantidad_Tiradas = contador_tiradas
))

# Estructurar resultados para graficar
resultados_df <- tibble(
  Paso = 1:n_pasos,
  Recompensa_Promedio = recompensa_promedio
)

# Gráfico del rendimiento promedio a lo largo de los ensayos
ggplot(resultados_df, aes(x = Paso, y = Recompensa_Promedio)) +
  geom_line(color = "#1abc9c", size = 1.2) +
  geom_hline(yintercept = max(probabilidades_reales), linetype = "dashed", color = "#e74c3c", size = 0.8) +
  theme_minimal() +
  labs(title = "Rendimiento Acumulado del Agente Epsilon-Greedy",
       subtitle = "Línea punteada roja representa el límite teórico óptimo (0.80)",
       x = "Paso / Ensayo",
       y = "Tasa de Recompensa Promedio")
