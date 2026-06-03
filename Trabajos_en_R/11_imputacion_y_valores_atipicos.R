# ==============================================================================
# 11_imputacion_y_valores_atipicos.R: Datos Faltantes e Outliers
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'mice', ejecute: install.packages("mice")
library(mice)

# 2. Simulación de datos con valores atípicos y faltantes (NAs)
set.seed(123)
n <- 200
datos_sucios <- tibble(
  Edad = round(rnorm(n, mean = 35, sd = 10)),
  Ingresos = rnorm(n, mean = 50000, sd = 15000),
  Score = runif(n, min = 0, max = 100)
)

# Introducir valores faltantes artificialmente
datos_sucios$Edad[sample(1:n, 15)] <- NA
datos_sucios$Ingresos[sample(1:n, 10)] <- NA

# Introducir valores atípicos artificialmente (Outliers)
datos_sucios$Ingresos[sample(1:n, 5)] <- datos_sucios$Ingresos[sample(1:n, 5)] * 4
datos_sucios$Edad[sample(1:n, 3)] <- datos_sucios$Edad[sample(1:n, 3)] + 60

# 3. Tratamiento de Valores Faltantes (NA)
# Imputación predictiva media mediante MICE (Multivariate Imputation by Chained Equations)
datos_imputados_obj <- mice(datos_sucios, m = 1, method = "pmm", printFlag = FALSE)
datos_limpios <- complete(datos_imputados_obj)

# Verificar que ya no hay valores nulos
print("Resumen de datos tras imputación MICE:")
print(colSums(is.na(datos_limpios)))

# 4. Detección y Filtrado de Valores Atípicos (Outliers mediante IQR)
# Calculamos límites para la variable Ingresos
q1_ingresos <- quantile(datos_limpios$Ingresos, 0.25)
q3_ingresos <- quantile(datos_limpios$Ingresos, 0.75)
iqr_ingresos <- q3_ingresos - q1_ingresos

limite_inferior <- q1_ingresos - 1.5 * iqr_ingresos
limite_superior <- q3_ingresos + 1.5 * iqr_ingresos

# Clasificar observaciones como Normales o Outliers
datos_evaluados <- datos_limpios %>%
  mutate(Outlier = if_else(Ingresos < limite_inferior | Ingresos > limite_superior, "Outlier", "Normal"))

# Gráfico para visualizar los atípicos identificados
ggplot(datos_evaluados, aes(x = Edad, y = Ingresos, color = Outlier)) +
  geom_point(size = 3, alpha = 0.8) +
  scale_color_manual(values = c("Normal" = "#2ecc71", "Outlier" = "#e74c3c")) +
  theme_minimal() +
  labs(title = "Detección de Valores Atípicos mediante IQR en Ingresos",
       x = "Edad",
       y = "Ingresos")

# Filtrado definitivo de atípicos
datos_finales <- datos_evaluados %>% 
  filter(Outlier == "Normal") %>% 
  select(-Outlier)

print(paste("Observaciones originales:", nrow(datos_sucios)))
print(paste("Observaciones finales sin outliers:", nrow(datos_finales)))
