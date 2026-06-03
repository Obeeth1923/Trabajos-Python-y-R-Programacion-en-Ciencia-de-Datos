# ==============================================================================
# 10_evaluacion_comparativa.R: Comparación de Modelos mediante Validación Cruzada
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
library(rpart)
library(randomForest)

# 2. Carga y preprocesamiento de datos
data("iris")
datos <- as_tibble(iris)

# 3. Configuración de Validación Cruzada (10-Fold Cross-Validation)
set.seed(555)
k_folds <- 10

# Crear pliegues (folds) aleatorios balanceados
datos <- datos %>% sample_frac() # Mezclar datos aleatoriamente
pliegues <- cut(seq(1, nrow(datos)), breaks = k_folds, labels = FALSE)

# Vectores para almacenar las métricas de exactitud (accuracy) de cada modelo
exactitud_arbol <- numeric(k_folds)
exactitud_rf <- numeric(k_folds)

# Bucle de Validación Cruzada
for (i in 1:k_folds) {
  # Dividir en entrenamiento y validación para el pliegue actual
  indices_val <- which(pliegues == i, arr.ind = TRUE)
  val_fold <- datos[indices_val, ]
  train_fold <- datos[-indices_val, ]
  
  # Modelo A: Árbol de Decisión
  fit_arbol <- rpart(Species ~ ., data = train_fold, method = "class")
  pred_arbol <- predict(fit_arbol, newdata = val_fold, type = "class")
  exactitud_arbol[i] <- mean(pred_arbol == val_fold$Species)
  
  # Modelo B: Random Forest (con 50 árboles)
  fit_rf <- randomForest(Species ~ ., data = train_fold, ntree = 50)
  pred_rf <- predict(fit_rf, newdata = val_fold)
  exactitud_rf[i] <- mean(pred_rf == val_fold$Species)
}

# 4. Evaluación y Visualización Comparativa
# Construir dataframe con los resultados de exactitud de cada pliegue
resultados_cv <- tibble(
  Fold = rep(1:k_folds, 2),
  Modelo = c(rep("Árbol de Decisión", k_folds), rep("Random Forest", k_folds)),
  Exactitud = c(exactitud_arbol, exactitud_rf)
)

# Resumen de métricas
resumen_comparativo <- resultados_cv %>%
  group_by(Modelo) %>%
  summarise(
    Exactitud_Promedio = mean(Exactitud),
    Desviacion_Estandar = sd(Exactitud)
  )

print("Resumen de rendimiento comparativo:")
print(resumen_comparativo)

# Graficar la comparación de exactitudes usando diagramas de caja (Boxplots)
ggplot(resultados_cv, aes(x = Modelo, y = Exactitud, fill = Modelo)) +
  geom_boxplot(alpha = 0.7, outlier.shape = NA) +
  geom_jitter(width = 0.1, size = 2, color = "#2c3e50") +
  theme_minimal() +
  scale_fill_manual(values = c("Árbol de Decisión" = "#3498db", "Random Forest" = "#9b59b6")) +
  labs(title = "Comparativa de Modelos mediante 10-Fold Cross-Validation",
       subtitle = "Precisión promedio del modelo en cada iteración del pliegue",
       x = "Modelo Evaluado",
       y = "Exactitud (Accuracy)")
