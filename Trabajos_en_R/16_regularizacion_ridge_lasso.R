# ==============================================================================
# 16_regularizacion_ridge_lasso.R: Regularización Ridge y Lasso
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'glmnet', ejecute: install.packages("glmnet")
library(glmnet)

# 2. Carga y preprocesamiento de datos
data("mtcars")
# Preparar matrices para glmnet (requiere matriz de predictores X y vector respuesta y)
X <- mtcars %>% select(-mpg) %>% as.matrix()
y <- mtcars$mpg

# 3. Entrenamiento de los modelos (Ridge y Lasso)
# Alpha = 0 representa Ridge Regression. Alpha = 1 representa Lasso Regression.
set.seed(888)

# Validación Cruzada para buscar el lambda óptimo
cv_ridge <- cv.glmnet(X, y, alpha = 0)
cv_lasso <- cv.glmnet(X, y, alpha = 1)

# Mejores valores de lambda
lambda_optimo_ridge <- cv_ridge$lambda.min
lambda_optimo_lasso <- cv_lasso$lambda.min

print(paste("Lambda óptimo Ridge:", round(lambda_optimo_ridge, 4)))
print(paste("Lambda óptimo Lasso:", round(lambda_optimo_lasso, 4)))

# 4. Evaluación y Visualización
# Gráfico del proceso de optimización del error según lambda
par(mfrow = c(1, 2))
plot(cv_ridge, main = "Ridge (Alpha = 0)")
plot(cv_lasso, main = "Lasso (Alpha = 1)")
par(mfrow = c(1, 1))

# Coeficientes resultantes con el mejor lambda para comparar la selección de variables
coef_ridge <- as.matrix(coef(cv_ridge, s = "lambda.min"))
coef_lasso <- as.matrix(coef(cv_lasso, s = "lambda.min"))

comparativa_coef <- tibble(
  Caracteristica = rownames(coef_ridge),
  Ridge = as.numeric(coef_ridge),
  Lasso = as.numeric(coef_lasso)
) %>% filter(Caracteristica != "(Intercept)")

# Gráfico de barras comparativo de coeficientes estimados usando ggplot2
comparativa_coef %>%
  pivot_longer(cols = c(Ridge, Lasso), names_to = "Modelo", values_to = "Coeficiente") %>%
  ggplot(aes(x = reorder(Caracteristica, Coeficiente), y = Coeficiente, fill = Modelo)) +
  geom_bar(stat = "identity", position = "dodge", alpha = 0.8) +
  scale_fill_manual(values = c("Ridge" = "#2980b9", "Lasso" = "#e67e22")) +
  theme_minimal() +
  coord_flip() +
  labs(title = "Comparación de Coeficientes: Ridge vs Lasso",
       subtitle = "Lasso tiende a anular coeficientes (selección automática de características)",
       x = "Variables Predictoras",
       y = "Coeficiente Estimado")
