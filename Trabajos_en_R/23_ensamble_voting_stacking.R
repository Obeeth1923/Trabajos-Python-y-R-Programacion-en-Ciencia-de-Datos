# ==============================================================================
# 23_ensamble_voting_stacking.R: Modelo de Ensamble (Voting Classifier)
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
library(rpart)
library(randomForest)
# Nota: Si no tiene instalado 'e1071', ejecute: install.packages("e1071")
library(e1071) # Para el clasificador Naive Bayes

# 2. Carga y preprocesamiento de datos
data("iris")
datos <- as_tibble(iris)

# División en entrenamiento (70%) y prueba (30%)
set.seed(432)
indices <- sample(1:nrow(datos), size = 0.7 * nrow(datos))
entrenamiento <- datos[indices, ]
prueba <- datos[-indices, ]

# 3. Entrenamiento de los modelos base (Clasificadores Diversos)
# Modelo 1: Árbol de Decisión
modelo_arbol <- rpart(Species ~ ., data = entrenamiento, method = "class")

# Modelo 2: Random Forest
modelo_rf <- randomForest(Species ~ ., data = entrenamiento, ntree = 50)

# Modelo 3: Naive Bayes
modelo_nb <- naiveBayes(Species ~ ., data = entrenamiento)

# 4. Predicciones individuales en el conjunto de prueba
pred_arbol <- predict(modelo_arbol, newdata = prueba, type = "class")
pred_rf <- predict(modelo_rf, newdata = prueba)
pred_nb <- predict(modelo_nb, newdata = prueba)

# 5. Combinación por Votación Mayoritaria (Voting)
# Unir predicciones en una matriz
matriz_predicciones <- tibble(
  Arbol = pred_arbol,
  RF = pred_rf,
  NB = pred_nb
)

# Función para obtener la moda (voto mayoritario) por fila
voto_mayoritario <- function(fila) {
  tabla_frec <- table(fila)
  ret <- names(tabla_frec)[which.max(tabla_frec)]
  return(ret)
}

prediccion_ensamble <- apply(matriz_predicciones, 1, voto_mayoritario) %>% 
  factor(levels = levels(prueba$Species))

# 6. Evaluación Comparativa
exactitud_arbol <- mean(pred_arbol == prueba$Species)
exactitud_rf <- mean(pred_rf == prueba$Species)
exactitud_nb <- mean(pred_nb == prueba$Species)
exactitud_ensamble <- mean(prediccion_ensamble == prueba$Species)

# Dataframe de comparación
comparativa <- tibble(
  Modelo = c("Árbol de Decisión", "Random Forest", "Naive Bayes", "Ensamble (Votación)"),
  Exactitud = c(exactitud_arbol, exactitud_rf, exactitud_nb, exactitud_ensamble)
)

print(comparativa)

# Gráfico comparativo de rendimientos
ggplot(comparativa, aes(x = reorder(Modelo, Exactitud), y = Exactitud, fill = Modelo)) +
  geom_bar(stat = "identity", width = 0.5, alpha = 0.8) +
  geom_text(aes(label = round(Exactitud, 3)), vjust = -0.3, size = 4) +
  theme_minimal() +
  scale_fill_brewer(palette = "Set2") +
  theme(legend.position = "none") +
  labs(title = "Comparación de Modelos: Modelos Individuales vs Ensamble",
       x = "Modelo",
       y = "Exactitud (Accuracy)")
