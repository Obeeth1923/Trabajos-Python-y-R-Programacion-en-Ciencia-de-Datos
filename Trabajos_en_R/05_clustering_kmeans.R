# ==============================================================================
# 05_clustering_kmeans.R: Agrupamiento por K-Means y Método del Codo
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)

# 2. Carga y preprocesamiento de datos
data("iris")
# Para clustering no supervisado, removemos la variable etiqueta (Species) y escalamos
datos_num <- iris %>% 
  select(-Species) %>% 
  scale() %>% 
  as_tibble()

# 3. Selección de K: Método del Codo (Elbow Method)
set.seed(222)
wcss <- numeric()
valores_k <- 1:10

for (k in valores_k) {
  modelo_km <- kmeans(datos_num, centers = k, nstart = 20)
  wcss[k] <- modelo_km$tot.withinss
}

# Crear dataframe para el gráfico del codo
datos_codo <- tibble(K = valores_k, WCSS = wcss)

# Gráfico del método del codo
ggplot(datos_codo, aes(x = K, y = WCSS)) +
  geom_line(color = "#7f8c8d", size = 1) +
  geom_point(color = "#e67e22", size = 3) +
  scale_x_continuous(breaks = valores_k) +
  theme_minimal() +
  labs(title = "Método del Codo para Selección de K óptimo",
       x = "Número de Clústeres (K)",
       y = "Suma de Cuadrados Intra-Clúster (WCSS)")

# 4. Entrenamiento del modelo final con K óptimo (K = 3)
k_optimo <- 3
modelo_final <- kmeans(datos_num, centers = k_optimo, nstart = 25)

# Visualización de los Clústeres
datos_grafico <- iris %>% 
  mutate(Cluster = as.factor(modelo_final$cluster))

ggplot(datos_grafico, aes(x = Petal.Length, y = Petal.Width, color = Cluster)) +
  geom_point(size = 3, alpha = 0.8) +
  theme_minimal() +
  scale_color_brewer(palette = "Set1") +
  labs(title = "Agrupamiento por K-Means (K = 3)",
       x = "Longitud del Pétalo",
       y = "Ancho del Pétalo")
