# ==============================================================================
# 01_regresion_lineal.R: Regresión Lineal Múltiple
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)

# 2. Carga y preprocesamiento de datos
data("mtcars")
datos <- as_tibble(mtcars)

# División en entrenamiento (80%) y prueba (20%)
set.seed(123)
indices <- sample(1:nrow(datos), size = 0.8 * nrow(datos))
entrenamiento <- datos[indices, ]
prueba <- datos[-indices, ]

# 3. Entrenamiento del modelo
# Predicción de millas por galón (mpg) en función del peso (wt), caballos de fuerza (hp) y aceleración (qsec)
modelo <- lm(mpg ~ wt + hp + qsec, data = entrenamiento)

# Resumen del modelo
summary(modelo)

# 4. Evaluación y Visualización
# Predicciones
predicciones <- predict(modelo, newdata = prueba)

# Métricas de evaluación
real <- prueba$mpg
mse <- mean((real - predicciones)^2)
rmse <- sqrt(mse)
r2 <- cor(real, predicciones)^2

print(paste("MSE:", round(mse, 4)))
print(paste("RMSE:", round(rmse, 4)))
print(paste("R2:", round(r2, 4)))

# Visualización: Valores reales vs Predichos
resultados <- tibble(Real = real, Predicho = predicciones)

ggplot(resultados, aes(x = Real, y = Predicho)) +
  geom_point(color = "#3498db", size = 3) +
  geom_abline(slope = 1, intercept = 0, color = "#e74c3c", linetype = "dashed", size = 1) +
  theme_minimal() +
  labs(title = "Regresión Lineal Múltiple: MPG Real vs Predicho",
       x = "Millas por Galón Reales",
       y = "Millas por Galón Predichas")
