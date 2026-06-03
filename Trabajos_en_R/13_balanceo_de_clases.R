# ==============================================================================
# 13_balanceo_de_clases.R: Balanceo de Datos en Clases Desequilibradas
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'ROSE', ejecute: install.packages("ROSE")
library(ROSE)

# 2. Carga y Simulación de un dataset desbalanceado
set.seed(456)
n_muestras <- 1000
datos_desbalanceados <- tibble(
  V1 = rnorm(n_muestras, mean = 5, sd = 2),
  V2 = rnorm(n_muestras, mean = 10, sd = 3),
  # Clase objetivo binaria con desbalance del 90% (Clase 0) y 10% (Clase 1)
  Clase = as.factor(c(rep(0, 900), rep(1, 100)))
)

print("Distribución inicial de clases:")
print(table(datos_desbalanceados$Clase))

# 3. Aplicación de técnicas de balanceo utilizando el paquete ROSE
# Opción A: Submuestreo (Under-sampling)
datos_sub <- ovun.sample(Clase ~ ., data = datos_desbalanceados, method = "under", N = 200, seed = 1)$data

# Opción B: Sobremuestreo (Over-sampling)
datos_sobre <- ovun.sample(Clase ~ ., data = datos_desbalanceados, method = "over", N = 1800, seed = 1)$data

# Opción C: Síntesis de datos artificiales (ROSE)
datos_rose <- ROSE(Clase ~ ., data = datos_desbalanceados, seed = 1)$data

# 4. Evaluación y Visualización
# Comparar distribuciones resultantes en un dataframe consolidado
comparativa_distribucion <- tibble(
  Metodo = c(rep("Original", nrow(datos_desbalanceados)), 
             rep("Submuestreo", nrow(datos_sub)), 
             rep("Sobremuestreo", nrow(datos_sobre)), 
             rep("ROSE", nrow(datos_rose))),
  Clase = c(datos_desbalanceados$Clase, datos_sub$Clase, datos_sobre$Clase, datos_rose$Clase)
)

# Gráfico de barras comparativo de las distribuciones
ggplot(comparativa_distribucion, aes(x = Clase, fill = Clase)) +
  geom_bar(width = 0.5) +
  facet_wrap(~ Metodo, scales = "free_y") +
  theme_minimal() +
  scale_fill_manual(values = c("0" = "#34495e", "1" = "#e74c3c")) +
  labs(title = "Comparación de Técnicas de Balanceo de Clases",
       x = "Clase",
       y = "Frecuencia / Cantidad")
