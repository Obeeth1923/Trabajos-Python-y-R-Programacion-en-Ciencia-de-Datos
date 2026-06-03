# ==============================================================================
# 28_reduccion_dimensionalidad_tsne.R: Reducción de Dimensionalidad con t-SNE
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'Rtsne', ejecute: install.packages("Rtsne")
library(Rtsne)

# 2. Carga y preprocesamiento de datos
data("iris")
datos <- as_tibble(iris)

# t-SNE es extremadamente sensible a duplicados exactos y requiere valores numéricos escalados.
# Eliminamos filas duplicadas para prevenir errores en la ejecución de t-SNE.
datos_unicos <- datos %>% distinct()

# Extraer y escalar variables numéricas
datos_num <- datos_unicos %>%
  select(where(is.numeric)) %>%
  scale()

# 3. Entrenamiento (Ejecución de t-SNE)
set.seed(444)
tsne_resultado <- Rtsne(
  datos_num, 
  dims = 2, 
  perplexity = 30, 
  verbose = FALSE, 
  max_iter = 500
)

# 4. Evaluación y Visualización
# Obtener las coordenadas resultantes del espacio bidimensional (Y)
coordenadas_tsne <- as_tibble(tsne_resultado$Y) %>%
  rename(tSNE1 = V1, tSNE2 = V2) %>%
  mutate(Especie = datos_unicos$Species)

# Gráfico de dispersión en 2D mapeando las especies a colores distintivos
ggplot(coordenadas_tsne, aes(x = tSNE1, y = tSNE2, color = Especie)) +
  geom_point(size = 3, alpha = 0.8) +
  theme_minimal() +
  scale_color_brewer(palette = "Set1") +
  labs(title = "Visualización de Datos de Iris Reducidos mediante t-SNE",
       subtitle = "Proyección bidimensional no lineal de características de 4 dimensiones",
       x = "Dimensión t-SNE 1",
       y = "Dimensión t-SNE 2")
