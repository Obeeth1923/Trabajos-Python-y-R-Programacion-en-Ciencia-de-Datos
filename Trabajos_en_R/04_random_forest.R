# ==============================================================================
# 04_random_forest.R: Random Forest para Clasificación
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'randomForest', ejecute: install.packages("randomForest")
library(randomForest)

# 2. Carga y preprocesamiento de datos
data("iris")
datos <- as_tibble(iris)

# División en entrenamiento (70%) y prueba (30%)
set.seed(111)
indices <- sample(1:nrow(datos), size = 0.7 * nrow(datos))
entrenamiento <- datos[indices, ]
prueba <- datos[-indices, ]

# 3. Entrenamiento del modelo
# Clasificación de la especie (Species) utilizando todos los predictores
modelo_rf <- randomForest(Species ~ ., data = entrenamiento, ntree = 100, importance = TRUE)

# Resumen del modelo
print(modelo_rf)

# 4. Evaluación y Visualización
# Predicciones en el conjunto de prueba
predicciones <- predict(modelo_rf, newdata = prueba)

# Matriz de confusión
matriz_confusion <- table(Real = prueba$Species, Predicho = predicciones)
print("Matriz de Confusión:")
print(matriz_confusion)

# Importancia de variables
importancia <- as.data.frame(importance(modelo_rf))
importancia$Variable <- rownames(importancia)

# Graficar la importancia de variables usando ggplot2 (Mean Decrease Gini)
ggplot(importancia, aes(x = reorder(Variable, MeanDecreaseGini), y = MeanDecreaseGini)) +
  geom_bar(stat = "identity", fill = "#8e44ad", width = 0.6) +
  coord_flip() +
  theme_minimal() +
  labs(title = "Importancia de Variables (Random Forest)",
       x = "Variables",
       y = "Disminución Media de Gini (Importancia)")
