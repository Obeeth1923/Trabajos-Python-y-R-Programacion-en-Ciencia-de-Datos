# ==============================================================================
# 24_regresion_cuantilica.R: Regresión Cuantílica
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'quantreg', ejecute: install.packages("quantreg")
library(quantreg)

# 2. Simulación de datos con Heterocedasticidad (variabilidad no constante)
set.seed(987)
n <- 250
x_val <- runif(n, min = 1, max = 10)
# La varianza del error crece linealmente con X
errores <- rnorm(n, mean = 0, sd = 0.5 * x_val) 
y_val <- 2 + 1.5 * x_val + errores

datos <- tibble(X = x_val, Y = y_val)

# 3. Modelado
# Modelo A: Regresión Lineal Clásica por Mínimos Cuadrados Ordinarios (OLS)
modelo_ols <- lm(Y ~ X, data = datos)

# Modelo B: Regresión Cuantílica para los percentiles 0.10, 0.50 (mediana) y 0.90
modelo_rq_10 <- rq(Y ~ X, data = datos, tau = 0.10)
modelo_rq_50 <- rq(Y ~ X, data = datos, tau = 0.50)
modelo_rq_90 <- rq(Y ~ X, data = datos, tau = 0.90)

# 4. Evaluación y Visualización
# Generamos predicciones para graficar las rectas ajustadas
linea_x <- seq(1, 10, length.out = 100)
pred_df <- tibble(X = linea_x) %>%
  mutate(
    OLS = predict(modelo_ols, newdata = .),
    Q_10 = predict(modelo_rq_10, newdata = .),
    Q_50 = predict(modelo_rq_50, newdata = .),
    Q_90 = predict(modelo_rq_90, newdata = .)
  )

# Resumen de coeficientes estimados para el cuantil 50 (Mediana)
print("Resumen del modelo cuantitativo (mediana):")
print(summary(modelo_rq_50))

# Estructurar predicciones para graficar con ggplot2
pred_df_largo <- pred_df %>%
  pivot_longer(cols = -X, names_to = "Modelo", values_to = "Y_Pred")

# Graficar los puntos de datos y las diferentes rectas de regresión
ggplot() +
  geom_point(data = datos, aes(x = X, y = Y), color = "gray60", alpha = 0.7) +
  geom_line(data = pred_df_largo, aes(x = X, y = Y_Pred, color = Modelo, linetype = Modelo), size = 1.2) +
  scale_color_manual(values = c("OLS" = "#e74c3c", "Q_10" = "#2ecc71", "Q_50" = "#f1c40f", "Q_90" = "#3498db")) +
  scale_linetype_manual(values = c("OLS" = "dashed", "Q_10" = "solid", "Q_50" = "solid", "Q_90" = "solid")) +
  theme_minimal() +
  labs(title = "Comparación de Regresión Clásica (OLS) vs Regresión Cuantílica",
       subtitle = "Obsérvese la dispersión heterocedástica del error en el extremo derecho",
       x = "Variable Predictora (X)",
       y = "Variable Respuesta (Y)",
       color = "Modelo Ajustado",
       linetype = "Modelo Ajustado")
