# ==============================================================================
# 17_pronostico_series_temporales.R: Pronóstico de Series de Tiempo
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'forecast', ejecute: install.packages("forecast")
library(forecast)

# 2. Carga y exploración de la serie temporal
# Utilizaremos 'AirPassengers' (Pasajeros mensuales de aerolíneas internacionales, 1949-1960)
data("AirPassengers")
serie_tiempo <- AirPassengers

# 3. Descomposición y Ajuste de Modelos
# Descomposición clásica (Tendencia, Estacionalidad, Residuo)
descomposicion <- decompose(serie_tiempo, type = "multiplicative")
plot(descomposicion, col = "#2c3e50")

# Ajustar un modelo automático ARIMA (Autoregressive Integrated Moving Average)
modelo_arima <- auto.arima(serie_tiempo)
summary(modelo_arima)

# Ajustar un modelo de suavizado exponencial alternativo (ETS)
modelo_ets <- ets(serie_tiempo)
summary(modelo_ets)

# 4. Predicción (Forecast) e Visualización
# Pronóstico a 24 meses vista con el modelo ARIMA
pronostico_arima <- forecast(modelo_arima, h = 24)

# Visualizar el pronóstico usando ggplot2 integrado en forecast
autoplot(pronostico_arima) +
  theme_minimal() +
  labs(title = "Pronóstico de Pasajeros de Aerolíneas a 24 Meses (ARIMA)",
       x = "Año",
       y = "Número de Pasajeros (Miles)",
       subtitle = "Bandas de confianza del 80% y 95% en tonos azules")
