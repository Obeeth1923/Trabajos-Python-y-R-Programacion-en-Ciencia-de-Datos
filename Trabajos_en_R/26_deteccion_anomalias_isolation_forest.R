# ==============================================================================
# 26_deteccion_anomalias_isolation_forest.R: Detección con Isolation Forest
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'isotree', ejecute: install.packages("isotree")
library(isotree)

# 2. Simulación de datos
# Generamos 500 puntos de datos normales (comportamiento habitual)
set.seed(222)
n_normal <- 500
datos_normales <- tibble(
  Edad = rnorm(n_normal, mean = 40, sd = 5),
  Gastos = rnorm(n_normal, mean = 2000, sd = 300)
)

# Generamos 25 anomalías (valores atípicos aislados / fraudes)
n_anomalos <- 25
datos_anomalos <- tibble(
  Edad = c(runif(12, min = 18, max = 25), runif(13, min = 65, max = 80)),
  Gastos = c(runif(12, min = 4000, max = 5000), runif(13, min = 100, max = 300))
)

# Unimos los datasets
datos_completos <- bind_rows(datos_normales, datos_anomalos)

# 3. Entrenamiento de Isolation Forest
# Ajustar el bosque de aislamiento
modelo_iforest <- isolation.forest(
  data = datos_completos,
  ntrees = 100,
  sample_size = 256
)

# 4. Evaluación y Detección de Anomalías
# Calcular la puntuación de anomalía (rango entre 0 y 1; más cercano a 1 indica alta anomalía)
puntuaciones <- predict(modelo_iforest, newdata = datos_completos)

# Agregar puntuación e identificar las anomalías basadas en un umbral del percentil 95 (top 5%)
datos_evaluados <- datos_completos %>%
  mutate(
    Score = puntuaciones,
    Clasificacion = if_else(Score > quantile(Score, 0.95), "Anomalía", "Normal")
  )

# Resumen de resultados
print("Conteo de anomalías detectadas:")
print(table(datos_evaluados$Clasificacion))

# 5. Visualización
# Gráfico de dispersión coloreado por la clasificación de Isolation Forest
ggplot(datos_evaluados, aes(x = Edad, y = Gastos, color = Clasificacion, size = Score)) +
  geom_point(alpha = 0.7) +
  scale_color_manual(values = c("Normal" = "#3498db", "Anomalía" = "#e74c3c")) +
  scale_size_continuous(range = c(1.5, 4.5)) +
  theme_minimal() +
  labs(title = "Detección de Anomalías utilizando Isolation Forest",
       subtitle = "El 5% de observaciones con mayor score de aislamiento se clasifican como anomalías",
       x = "Edad",
       y = "Monto de Gastos Mensuales",
       color = "Estado",
       size = "Score de Anomalía")
