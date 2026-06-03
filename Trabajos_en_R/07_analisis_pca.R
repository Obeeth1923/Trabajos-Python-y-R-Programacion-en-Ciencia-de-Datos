# ==============================================================================
# 07_analisis_pca.R: Análisis de Componentes Principales (PCA)
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)

# 2. Carga y preprocesamiento de datos
data("USArrests")
# El PCA requiere que las variables numéricas estén escaladas y centradas
datos <- USArrests

# 3. Entrenamiento (Cálculo del PCA)
pca_resultado <- prcomp(datos, center = TRUE, scale. = TRUE)

# Resumen de componentes
summary(pca_resultado)

# 4. Evaluación y Visualización
# Obtener la varianza explicada por cada componente
desviacion_estandar <- pca_resultado$sdev
varianza <- desviacion_estandar^2
porcentaje_varianza <- (varianza / sum(varianza)) * 100

# Dataframe de varianza explicada
varianza_df <- tibble(
  Componente = factor(1:length(porcentaje_varianza)),
  VarianzaExplicada = porcentaje_varianza,
  VarianzaAcumulada = cumsum(porcentaje_varianza)
)

# Gráfico de Varianza Explicada (Scree Plot) e Varianza Acumulada
ggplot(varianza_df, aes(x = Componente, y = VarianzaExplicada, group = 1)) +
  geom_bar(stat = "identity", fill = "#34495e", width = 0.5) +
  geom_line(aes(y = VarianzaAcumulada), color = "#e74c3c", size = 1) +
  geom_point(aes(y = VarianzaAcumulada), color = "#e74c3c", size = 3) +
  theme_minimal() +
  labs(title = "Gráfico del Sedimento (Scree Plot) y Varianza Acumulada",
       x = "Componentes Principales (PCs)",
       y = "Varianza Explicada % (Barras) / Acumulada % (Línea)")

# Visualización del Biplot usando R base
biplot(pca_resultado, 
       scale = 0, 
       cex = c(0.7, 1), 
       col = c("#2980b9", "#c0392b"),
       main = "Biplot del PCA (USArrests)")
