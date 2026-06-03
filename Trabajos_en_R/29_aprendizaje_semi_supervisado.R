# ==============================================================================
# 29_aprendizaje_semi_supervisado.R: Aprendizaje Semi-Supervisado (Self-Training)
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
library(rpart)

# 2. Simulación de datos semi-supervisados (Clasificación Binaria)
set.seed(555)
n <- 600

# Variables independientes
x1 <- rnorm(n, mean = 0, sd = 1.5)
x2 <- rnorm(n, mean = 0, sd = 1.5)
# Frontera de clase real
y_real <- factor(if_else(x1 + x2 > 0, "Clase_A", "Clase_B"))

# Crear dataset inicial
datos <- tibble(X1 = x1, X2 = x2, Real = y_real, Etiqueta = y_real)

# Ocultar etiquetas (hacerlas NA) para el 85% de los datos (Simulamos un entorno real semi-supervisado)
indices_ocultos <- sample(1:n, size = 0.85 * n)
datos$Etiqueta[indices_ocultos] <- NA

print("Distribución de etiquetas iniciales (Supervisadas vs No Etiquetadas):")
print(table(datos$Etiqueta, useNA = "always"))

# 3. Algoritmo de Auto-Entrenamiento (Self-Training Loop)
max_iteraciones <- 10
umbral_confianza <- 0.90 # El modelo solo adoptará nuevas etiquetas si está muy seguro

for (iter in 1:max_iteraciones) {
  # Filtrar datos etiquetados (para entrenar) y no etiquetados (para predecir)
  etiquetados <- datos %>% filter(!is.na(Etiqueta))
  no_etiquetados <- datos %>% filter(is.na(Etiqueta))
  
  if (nrow(no_etiquetados) == 0) {
    print("Se han etiquetado todos los registros.")
    break
  }
  
  # Entrenar clasificador base con los datos disponibles actualmente
  modelo_base <- rpart(Etiqueta ~ X1 + X2, data = etiquetados, method = "class")
  
  # Obtener predicciones probabilísticas para los registros no etiquetados
  pred_prob <- predict(modelo_base, newdata = no_etiquetados, type = "prob")
  pred_clase <- predict(modelo_base, newdata = no_etiquetados, type = "class")
  
  # Encontrar el nivel máximo de confianza de predicción para cada registro
  max_prob <- apply(pred_prob, 1, max)
  
  # Seleccionar registros que superan el umbral de confianza para pseudo-etiquetado
  candidatos <- no_etiquetados %>%
    mutate(
      Confianza = max_prob,
      PseudoEtiqueta = pred_clase,
      ID = indices_ocultos[is.na(datos$Etiqueta[indices_ocultos])]
    ) %>%
    filter(Confianza >= umbral_confianza)
  
  if (nrow(candidatos) == 0) {
    print(paste("Convergencia alcanzada en la iteración", iter, "- No hay más predicciones de alta confianza."))
    break
  }
  
  # Incorporar las pseudo-etiquetas al dataset de trabajo
  datos$Etiqueta[candidatos$ID] <- candidatos$PseudoEtiqueta
  
  print(paste("Iteración", iter, "- Pseudo-etiquetados:", nrow(candidatos), "| Pendientes:", sum(is.na(datos$Etiqueta))))
}

# 4. Evaluación y Visualización
# Comparar el resultado del pseudo-etiquetado con las clases reales
datos_finales <- datos %>%
  mutate(
    Tipo_Dato = case_when(
      !is.na(Etiqueta) & !((1:n) %in% indices_ocultos) ~ "Etiquetado Inicial",
      !is.na(Etiqueta) ~ "Pseudo-Etiquetado",
      TRUE ~ "No Etiquetado / Incierto"
    )
  )

ggplot(datos_finales, aes(x = X1, y = X2, color = Etiqueta, shape = Tipo_Dato)) +
  geom_point(size = 2.5, alpha = 0.8) +
  scale_color_manual(values = c("Clase_A" = "#3498db", "Clase_B" = "#e74c3c"), na.value = "gray") +
  theme_minimal() +
  labs(title = "Auto-Entrenamiento Semi-Supervisado (Self-Training)",
       subtitle = "Los puntos circulares son el 15% inicial etiquetado; los triángulos son deducidos del modelo",
       x = "Característica X1",
       y = "Característica X2",
       color = "Clase",
       shape = "Tipo de Dato")
