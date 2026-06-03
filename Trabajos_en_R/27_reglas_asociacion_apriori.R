# ==============================================================================
# 27_regres_asociacion_apriori.R: Reglas de Asociación con el Algoritmo Apriori
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'arules', ejecute: install.packages("arules")
library(arules)

# 2. Carga e Inspección de datos
# Utilizaremos el dataset integrado 'Groceries' que contiene transacciones reales de supermercado
data("Groceries")

# Inspección básica de los datos transaccionales
print("Estructura de las transacciones:")
print(summary(Groceries))

# 3. Entrenamiento del algoritmo Apriori
# Buscar reglas de asociación con soporte mínimo de 0.005 y confianza mínima de 0.50
reglas <- apriori(
  Groceries, 
  parameter = list(support = 0.005, confidence = 0.50, minlen = 2)
)

# 4. Evaluación de las Reglas de Asociación
# Ordenar las reglas por nivel de sustentación/elevación (Lift)
reglas_ordenadas <- sort(reglas, by = "lift", decreasing = TRUE)

# Mostrar las 10 mejores reglas encontradas
print("Top 10 Reglas de Asociación Ordenadas por Lift:")
inspect(head(reglas_ordenadas, 10))

# Convertir las mejores reglas a Dataframe para visualización con ggplot2
reglas_df <- as(head(reglas_ordenadas, 15), "data.frame") %>% 
  as_tibble()

# 5. Visualización
# Gráfico de barras de las principales reglas por Lift
ggplot(reglas_df, aes(x = reorder(rules, lift), y = lift, fill = confidence)) +
  geom_bar(stat = "identity", width = 0.6) +
  scale_fill_gradient(low = "#3498db", high = "#e74c3c") +
  coord_flip() +
  theme_minimal() +
  labs(title = "Top 15 Reglas de Asociación en Supermercado",
       subtitle = "Ordenadas por Lift (Fuerza de Asociación) con color de Confianza",
       x = "Regla de Asociación (LHS => RHS)",
       y = "Lift (Elevación)",
       fill = "Confianza")
