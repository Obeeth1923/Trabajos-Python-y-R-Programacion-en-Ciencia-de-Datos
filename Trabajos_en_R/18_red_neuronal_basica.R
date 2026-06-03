# ==============================================================================
# 18_red_neuronal_basica.R: Red Neuronal Simple (Perceptrón Multicapa)
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# 'nnet' está integrado en la instalación básica de R, por lo que no requiere instalación externa
library(nnet)

# 2. Carga y preprocesamiento de datos
data("iris")

# Estandarización de las variables independientes antes del entrenamiento
datos_preparados <- iris %>%
  mutate(across(where(is.numeric), ~ as.numeric(scale(.))))

# División en entrenamiento (80%) y prueba (20%)
set.seed(999)
indices <- sample(1:nrow(datos_preparados), size = 0.8 * nrow(datos_preparados))
entrenamiento <- datos_preparados[indices, ]
prueba <- datos_preparados[-indices, ]

# 3. Entrenamiento del modelo
# Red neuronal con 1 capa oculta de 5 neuronas (size = 5) para clasificar la especie
modelo_nnet <- nnet(Species ~ ., 
                    data = entrenamiento, 
                    size = 5, 
                    decay = 5e-4, 
                    maxit = 200, 
                    trace = FALSE)

# Resumen de pesos y estructura
summary(modelo_nnet)

# 4. Evaluación y Visualización
# Predicciones de clase en el conjunto de prueba
pred_clase <- predict(modelo_nnet, newdata = prueba, type = "class")

# Matriz de confusión
matriz_confusion <- table(Real = prueba$Species, Predicho = pred_clase)
print("Matriz de Confusión:")
print(matriz_confusion)

# Precisión final
exactitud <- mean(pred_clase == prueba$Species)
print(paste("Exactitud final de la Red Neuronal:", round(exactitud, 4)))

# Visualización: Probabilidades de clase asignadas para cada registro del conjunto de prueba
probabilidades <- predict(modelo_nnet, newdata = prueba, type = "raw") %>% 
  as_tibble() %>% 
  bind_cols(Real = prueba$Species) %>% 
  mutate(ID = row_number())

probabilidades %>%
  pivot_longer(cols = c(setosa, versicolor, virginica), names_to = "Clase_Predicha", values_to = "Probabilidad") %>%
  ggplot(aes(x = factor(ID), y = Probabilidad, fill = Clase_Predicha)) +
  geom_bar(stat = "identity", position = "fill") +
  facet_wrap(~ Real, scales = "free_x") +
  theme_minimal() +
  scale_fill_brewer(palette = "Pastel1") +
  labs(title = "Distribución de Probabilidades por Especie Real",
       x = "ID de Observación de Prueba",
       y = "Probabilidad Asignada por la Red Neuronal",
       fill = "Clase de Predicción")
