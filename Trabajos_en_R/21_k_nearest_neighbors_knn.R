# ==============================================================================
# 21_k_nearest_neighbors_knn.R: Clasificación por KNN y Selección de K
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# 'class' contiene la implementación clásica del algoritmo KNN
library(class)

# 2. Carga y preprocesamiento de datos
data("iris")
datos <- as_tibble(iris)

# Normalizar variables independientes (KNN es sensible a la escala de distancia)
normalizar <- function(x) {
  return((x - min(x)) / (max(x) - min(x)))
}

datos_norm <- datos %>%
  mutate(across(where(is.numeric), normalizar))

# División en entrenamiento (70%) y prueba (30%)
set.seed(123)
indices <- sample(1:nrow(datos_norm), size = 0.7 * nrow(datos_norm))
entrenamiento <- datos_norm[indices, ]
prueba <- datos_norm[-indices, ]

X_entreno <- entrenamiento %>% select(-Species)
y_entreno <- entrenamiento$Species
X_prueba <- prueba %>% select(-Species)
y_prueba <- prueba$Species

# 3. Búsqueda del hiperparámetro K óptimo
valores_k <- seq(1, 15, by = 2)
exactitudes <- numeric(length(valores_k))

for (i in seq_along(valores_k)) {
  k_actual <- valores_k[i]
  pred_knn <- knn(train = X_entreno, test = X_prueba, cl = y_entreno, k = k_actual)
  exactitudes[i] <- mean(pred_knn == y_prueba)
}

# Consolidar los resultados del tuning
resultados_tuning <- tibble(K = valores_k, Exactitud = exactitudes)

# Gráfico de afinación de hiperparámetro
ggplot(resultados_tuning, aes(x = K, y = Exactitud)) +
  geom_line(color = "#34495e", size = 1) +
  geom_point(color = "#e67e22", size = 3) +
  scale_x_continuous(breaks = valores_k) +
  theme_minimal() +
  labs(title = "Búsqueda de K Óptimo para KNN",
       x = "Número de Vecinos (K)",
       y = "Exactitud (Accuracy)")

# 4. Evaluación del mejor modelo (K = 5 o similar según gráfica)
k_optimo <- valores_k[which.max(exactitudes)]
print(paste("Mejor valor de K encontrado:", k_optimo))

prediccion_final <- knn(train = X_entreno, test = X_prueba, cl = y_entreno, k = k_optimo)

# Matriz de confusión
matriz_confusion <- table(Real = y_prueba, Predicho = prediccion_final)
print("Matriz de Confusión Final:")
print(matriz_confusion)
