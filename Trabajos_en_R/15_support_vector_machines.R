# ==============================================================================
# 15_support_vector_machines.R: Máquinas de Vector de Soporte (SVM)
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'e1071', ejecute: install.packages("e1071")
library(e1071)

# 2. Carga y preprocesamiento de datos
data("iris")
# Para facilitar la visualización en 2D, seleccionamos 2 variables y 2 especies (clasificación binaria)
datos <- iris %>%
  filter(Species %in% c("versicolor", "virginica")) %>%
  select(Petal.Length, Petal.Width, Species) %>%
  mutate(Species = factor(Species)) # Re-ajustar niveles del factor

# 3. Entrenamiento del modelo
# Modelo A: Kernel Lineal
svm_lineal <- svm(Species ~ ., data = datos, kernel = "linear", cost = 1)

# Modelo B: Kernel Radial (RBF)
svm_radial <- svm(Species ~ ., data = datos, kernel = "radial", cost = 1, gamma = 1)

# 4. Evaluación y Visualización de Fronteras de Decisión con ggplot2
# Crear una cuadrícula densa para predecir las fronteras
rango_longitud <- seq(min(datos$Petal.Length) - 0.5, max(datos$Petal.Length) + 0.5, length.out = 100)
rango_ancho <- seq(min(datos$Petal.Width) - 0.5, max(datos$Petal.Width) + 0.5, length.out = 100)
cuadricula <- expand.grid(Petal.Length = rango_longitud, Petal.Width = rango_ancho)

# Predicciones de la cuadrícula
cuadricula$Pred_Lineal <- predict(svm_lineal, newdata = cuadricula)
cuadricula$Pred_Radial <- predict(svm_radial, newdata = cuadricula)

# Graficar frontera del Kernel Lineal
plot_lineal <- ggplot() +
  geom_tile(data = cuadricula, aes(x = Petal.Length, y = Petal.Width, fill = Pred_Lineal), alpha = 0.3) +
  geom_point(data = datos, aes(x = Petal.Length, y = Petal.Width, color = Species), size = 3) +
  scale_fill_manual(values = c("versicolor" = "#3498db", "virginica" = "#9b59b6")) +
  scale_color_manual(values = c("versicolor" = "#2980b9", "virginica" = "#8e44ad")) +
  theme_minimal() +
  labs(title = "SVM: Kernel Lineal",
       x = "Longitud del Pétalo",
       y = "Ancho del Pétalo",
       fill = "Clase Predicha",
       color = "Clase Real")

# Graficar frontera del Kernel Radial
plot_radial <- ggplot() +
  geom_tile(data = cuadricula, aes(x = Petal.Length, y = Petal.Width, fill = Pred_Radial), alpha = 0.3) +
  geom_point(data = datos, aes(x = Petal.Length, y = Petal.Width, color = Species), size = 3) +
  scale_fill_manual(values = c("versicolor" = "#3498db", "virginica" = "#9b59b6")) +
  scale_color_manual(values = c("versicolor" = "#2980b9", "virginica" = "#8e44ad")) +
  theme_minimal() +
  labs(title = "SVM: Kernel Radial (RBF)",
       x = "Longitud del Pétalo",
       y = "Ancho del Pétalo",
       fill = "Clase Predicha",
       color = "Clase Real")

# Mostrar gráficos
print(plot_lineal)
print(plot_radial)
