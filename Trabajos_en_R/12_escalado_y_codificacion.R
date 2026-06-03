# ==============================================================================
# 12_escalado_y_codificacion.R: Escalado Numérico y Codificación Categórica
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)

# 2. Carga y Simulación de datos
data("iris")
datos_crudos <- as_tibble(iris)

# Añadir una variable categórica arbitraria para ilustrar One-Hot Encoding
set.seed(42)
datos_crudos <- datos_crudos %>%
  mutate(Region = sample(c("Norte", "Sur", "Este"), size = nrow(datos_crudos), replace = TRUE))

# 3. Escalado Numérico (Min-Max y Z-score)
# Función para Min-Max Escalado [0, 1]
min_max_scale <- function(x) {
  return((x - min(x)) / (max(x) - min(x)))
}

# Aplicar estandarización (Z-score) y escalado Min-Max
datos_escalados <- datos_crudos %>%
  mutate(
    # Z-score: Resta de la media y división por la desviación estándar (función scale de R base)
    Sepal.Length_Z = as.numeric(scale(Sepal.Length)),
    Sepal.Width_Z  = as.numeric(scale(Sepal.Width)),
    # Min-Max: Escala en rango estricto entre 0 y 1
    Petal.Length_MinMax = min_max_scale(Petal.Length),
    Petal.Width_MinMax  = min_max_scale(Petal.Width)
  )

# Visualizar la diferencia del escalado mediante boxplot comparativo
datos_escalados %>%
  select(Sepal.Length, Sepal.Length_Z, Petal.Length, Petal.Length_MinMax) %>%
  pivot_longer(cols = everything(), names_to = "Metodo", values_to = "Valor") %>%
  ggplot(aes(x = Metodo, y = Valor, fill = Metodo)) +
  geom_boxplot() +
  theme_minimal() +
  theme(legend.position = "none") +
  labs(title = "Comparación de Escalas: Valores Crudos vs Escalados",
       x = "Variable y Método de Escalado",
       y = "Valor")

# 4. Codificación Categórica (One-Hot Encoding usando R base y model.matrix)
# Creamos las variables binarias ficticias (dummy variables) para 'Region'
dummies <- model.matrix(~ Region - 1, data = datos_escalados) %>% as_tibble()

# Unir las variables numéricas escaladas con las dummies codificadas
datos_preprocesados <- datos_escalados %>%
  select(Species, Sepal.Length_Z, Sepal.Width_Z, Petal.Length_MinMax, Petal.Width_MinMax) %>%
  bind_cols(dummies)

print("Estructura final del dataset tras preprocesamiento:")
print(head(datos_preprocesados))
