# ==============================================================================
# 02_regresion_logistica.R: Regresión Logística para Clasificación Binaria
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'pROC', ejecute: install.packages("pROC")
library(pROC)

# 2. Carga y preprocesamiento de datos
data("mtcars")
# Usaremos 'am' (Tipo de transmisión: 0 = automático, 1 = manual) como variable objetivo
datos <- as_tibble(mtcars) %>%
  select(am, mpg, hp, wt)

# División en entrenamiento (70%) y prueba (30%)
set.seed(456)
indices <- sample(1:nrow(datos), size = 0.7 * nrow(datos))
entrenamiento <- datos[indices, ]
prueba <- datos[-indices, ]

# 3. Entrenamiento del modelo
modelo <- glm(am ~ mpg + hp + wt, data = entrenamiento, family = binomial)

# Resumen del modelo
summary(modelo)

# 4. Evaluación y Visualización
# Predicción probabilística
probabilidades <- predict(modelo, newdata = prueba, type = "response")
# Clasificación con umbral de 0.5
predicciones <- ifelse(probabilidades > 0.5, 1, 0)

# Matriz de confusión
matriz_confusion <- table(Real = prueba$am, Predicho = predicciones)
print("Matriz de Confusión:")
print(matriz_confusion)

# Precisión (Accuracy)
precision <- sum(diag(matriz_confusion)) / sum(matriz_confusion)
print(paste("Precisión (Accuracy):", round(precision, 4)))

# Curva ROC y AUC
curva_roc <- roc(prueba$am, probabilidades)
auc_valor <- auc(curva_roc)
print(paste("AUC (Área bajo la curva):", round(auc_valor, 4)))

# Visualización de la curva ROC con ggplot2
ggroc(curva_roc, color = "#2ecc71", size = 1.2) +
  theme_minimal() +
  geom_abline(slope = 1, intercept = 1, linetype = "dashed", color = "gray") +
  labs(title = paste("Curva ROC (AUC =", round(auc_valor, 2), ")"),
       x = "Especificidad",
       y = "Sensibilidad")
