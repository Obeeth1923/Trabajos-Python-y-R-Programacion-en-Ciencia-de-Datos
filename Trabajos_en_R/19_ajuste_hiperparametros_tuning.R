# ==============================================================================
# 19_ajuste_hiperparametros_tuning.R: Grid Search Automatizado con Caret
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'caret', ejecute: install.packages("caret")
library(caret)

# 2. Carga y preprocesamiento de datos
data("iris")
datos <- as_tibble(iris)

# División en entrenamiento y prueba
set.seed(321)
indices_entreno <- createDataPartition(datos$Species, p = 0.8, list = FALSE)
entrenamiento <- datos[indices_entreno, ]
prueba <- datos[-indices_entreno, ]

# 3. Configuración del Grid Search
# Configuración del esquema de validación: 5-Fold Cross Validation repetida 3 veces
control_entrenamiento <- trainControl(
  method = "repeatedcv",
  number = 5,
  repeats = 3,
  search = "grid"
)

# Definición de la rejilla de parámetros a probar para el algoritmo KNN (k vecinos)
rejilla_parametros <- expand.grid(k = c(1, 3, 5, 7, 9, 11, 15, 21))

# 4. Ajuste del Modelo (Grid Search)
modelo_tunado <- train(
  Species ~ ., 
  data = entrenamiento, 
  method = "knn",
  trControl = control_entrenamiento,
  tuneGrid = rejilla_parametros,
  preProcess = c("center", "scale") # Escalado automático
)

# Resumen de resultados del Grid Search
print(modelo_tunado)

# 5. Evaluación y Visualización del Ajuste
# Gráfico del rendimiento (Accuracy) en función del hiperparámetro k
ggplot(modelo_tunado) +
  theme_minimal() +
  geom_line(color = "#3498db", size = 1) +
  geom_point(color = "#e74c3c", size = 3) +
  labs(title = "Optimización del Hiperparámetro k (KNN)",
       subtitle = "Precisión estimada por Validación Cruzada",
       x = "Cantidad de Vecinos Cercanos (k)",
       y = "Precisión (Accuracy)")

# Predicciones finales en el conjunto de prueba utilizando el mejor modelo
predicciones <- predict(modelo_tunado, newdata = prueba)
matriz_confusion <- confusionMatrix(predicciones, prueba$Species)
print(matriz_confusion)
