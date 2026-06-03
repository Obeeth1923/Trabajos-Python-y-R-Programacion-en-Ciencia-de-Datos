# ==============================================================================
# 03_arbol_decision.R: Árbol de Decisión para Clasificación
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'rpart', ejecute: install.packages("rpart")
library(rpart)

# 2. Carga y preprocesamiento de datos
data("iris")
datos <- as_tibble(iris)

# División en entrenamiento (80%) y prueba (20%)
set.seed(789)
indices <- sample(1:nrow(datos), size = 0.8 * nrow(datos))
entrenamiento <- datos[indices, ]
prueba <- datos[-indices, ]

# 3. Entrenamiento del modelo
# Clasificación de la especie (Species) en función de las medidas de la flor
modelo_arbol <- rpart(Species ~ ., data = entrenamiento, method = "class")

# 4. Evaluación y Visualización
# Predicciones
predicciones <- predict(modelo_arbol, newdata = prueba, type = "class")

# Matriz de confusión
matriz_confusion <- table(Real = prueba$Species, Predicho = predicciones)
print("Matriz de Confusión:")
print(matriz_confusion)

# Precisión (Accuracy)
precision <- sum(diag(matriz_confusion)) / sum(matriz_confusion)
print(paste("Precisión (Accuracy):", round(precision, 4)))

# Visualización del árbol de decisión (Usando R base)
plot(modelo_arbol, margin = 0.1, main = "Árbol de Decisión - Especies de Iris")
text(modelo_arbol, use.n = TRUE, all = TRUE, cex = 0.8, col = "#2c3e50")

# Visualización de predicciones correctas vs incorrectas con ggplot2
prueba_resultados <- prueba %>%
  mutate(Predicho = predicciones,
         Correcto = Species == Predicho)

ggplot(prueba_resultados, aes(x = Petal.Length, y = Petal.Width, color = Correcto, shape = Species)) +
  geom_point(size = 3, alpha = 0.8) +
  scale_color_manual(values = c("TRUE" = "#2ecc71", "FALSE" = "#e74c3c")) +
  theme_minimal() +
  labs(title = "Predicciones del Árbol de Decisión en Iris",
       x = "Longitud del Pétalo",
       y = "Ancho del Pétalo",
       color = "¿Predicción Correcta?")
