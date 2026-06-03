# ==============================================================================
# 22_naive_bayes_clasificacion.R: Clasificador Naive Bayes
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'e1071', ejecute: install.packages("e1071")
library(e1071)

# 2. Carga y preprocesamiento de datos
# Utilizaremos el dataset histórico de sobrevivientes del Titanic (categorizado)
data("Titanic")
datos_titanic <- as.data.frame(Titanic) %>% 
  uncount(Freq) %>% # Expandir el conteo a registros individuales
  as_tibble()

# Conversión a factores
datos_titanic <- datos_titanic %>%
  mutate(across(everything(), as.factor))

# División en entrenamiento (80%) y prueba (20%)
set.seed(321)
indices <- sample(1:nrow(datos_titanic), size = 0.8 * nrow(datos_titanic))
entrenamiento <- datos_titanic[indices, ]
prueba <- datos_titanic[-indices, ]

# 3. Entrenamiento del modelo Naive Bayes
# Predecir si sobrevivió (Survived) basándonos en Clase, Sexo y Edad
modelo_nb <- naiveBayes(Survived ~ Class + Sex + Age, data = entrenamiento)

# Resumen del modelo (Probabilidades condicionales e a priori)
print(modelo_nb)

# 4. Evaluación y Visualización
# Predicciones de clase y probabilidades asociadas
predicciones <- predict(modelo_nb, newdata = prueba)
probabilidades <- predict(modelo_nb, newdata = prueba, type = "raw")

# Matriz de confusión
matriz_confusion <- table(Real = prueba$Survived, Predicho = predicciones)
print("Matriz de Confusión:")
print(matriz_confusion)

# Exactitud (Accuracy)
exactitud <- mean(predicciones == prueba$Survived)
print(paste("Exactitud (Accuracy):", round(exactitud, 4)))

# Visualización de la distribución de predicciones correctas por Género
resultados <- prueba %>%
  mutate(Predicho = predicciones,
         Correcto = Survived == Predicho)

ggplot(resultados, aes(x = Sex, fill = Correcto)) +
  geom_bar(position = "fill", width = 0.6) +
  scale_fill_manual(values = c("TRUE" = "#2ecc71", "FALSE" = "#e74c3c")) +
  theme_minimal() +
  labs(title = "Tasa de Predicción Correcta de Naive Bayes por Género",
       x = "Género",
       y = "Proporción",
       fill = "¿Predicción Correcta?")
