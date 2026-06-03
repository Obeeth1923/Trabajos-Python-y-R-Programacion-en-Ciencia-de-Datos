# ==============================================================================
# 25_clustering_dbscan.R: Agrupamiento DBSCAN vs K-Means
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'dbscan', ejecute: install.packages("dbscan")
library(dbscan)

# 2. Simulación de datos con formas geométricas no lineales (Dos círculos concéntricos)
set.seed(111)
n_puntos <- 300

# Círculo interior
r1 <- 1
theta1 <- runif(n_puntos, 0, 2 * pi)
x1 <- r1 * cos(theta1) + rnorm(n_puntos, sd = 0.1)
y1 <- r1 * sin(theta1) + rnorm(n_puntos, sd = 0.1)

# Círculo exterior
r2 <- 3
theta2 <- runif(n_puntos, 0, 2 * pi)
x2 <- r2 * cos(theta2) + rnorm(n_puntos, sd = 0.15)
y2 <- r2 * sin(theta2) + rnorm(n_puntos, sd = 0.15)

datos <- tibble(
  X = c(x1, x2),
  Y = c(y1, y2)
)

# 3. Modelado
# Algoritmo A: K-Means (K = 2) - Fracasa en formas no esféricas
modelo_km <- kmeans(datos, centers = 2, nstart = 25)

# Algoritmo B: DBSCAN (basado en densidad)
# eps: distancia de vecindad, minPts: número mínimo de puntos en vecindad
modelo_dbscan <- dbscan(datos, eps = 0.4, minPts = 5)

# 4. Evaluación y Visualización Comparativa
datos_resultado <- datos %>%
  mutate(
    Cluster_KMeans = as.factor(modelo_km$cluster),
    # El valor 0 en DBSCAN indica ruido/outliers
    Cluster_DBSCAN = as.factor(modelo_dbscan$cluster)
  )

# Gráfico para K-Means
plot_km <- ggplot(datos_resultado, aes(x = X, y = Y, color = Cluster_KMeans)) +
  geom_point(size = 2, alpha = 0.8) +
  scale_color_brewer(palette = "Set1") +
  theme_minimal() +
  labs(title = "K-Means en Datos No Lineales (K = 2)",
       subtitle = "Divide el espacio linealmente fallando en identificar la estructura concéntrica")

# Gráfico para DBSCAN
plot_dbscan <- ggplot(datos_resultado, aes(x = X, y = Y, color = Cluster_DBSCAN)) +
  geom_point(size = 2, alpha = 0.8) +
  scale_color_brewer(palette = "Set1") +
  theme_minimal() +
  labs(title = "DBSCAN en Datos No Lineales (eps = 0.4)",
       subtitle = "Identifica correctamente los anillos concéntricos y el ruido (Cluster 0)")

# Imprimir los gráficos
print(plot_km)
print(plot_dbscan)
