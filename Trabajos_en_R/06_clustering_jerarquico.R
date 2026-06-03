# ==============================================================================
# 06_clustering_jerarquico.R: Clústering Jerárquico y Dendrograma
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)

# 2. Carga y preprocesamiento de datos
data("USArrests")
# Escalamos los datos debido a las diferencias en magnitudes de las variables
datos_escalados <- scale(USArrests)

# 3. Entrenamiento del modelo
# Calcular la matriz de distancias euclidianas
matriz_distancias <- dist(datos_escalados, method = "euclidean")

# Realizar clustering jerárquico usando el método de Ward
modelo_hclust <- hclust(matriz_distancias, method = "ward.D2")

# 4. Evaluación y Visualización
# Visualizar el dendrograma en R base
plot(modelo_hclust, 
     main = "Dendrograma de Clústering Jerárquico (USArrests)",
     xlab = "Estados", 
     ylab = "Distancia de Ward",
     sub = "", 
     labels = rownames(USArrests),
     cex = 0.7)

# Cortar el árbol en 4 clústeres representativos
grupos <- cutree(modelo_hclust, k = 4)

# Dibujar rectángulos rojos alrededor de los 4 grupos identificados en el dendrograma
rect.hclust(modelo_hclust, k = 4, border = "#e74c3c")

# Visualizar la asignación del clúster a nivel de tabla
arrests_grupos <- USArrests %>%
  mutate(Cluster = as.factor(grupos))

print("Primeras filas con asignación de clústeres:")
print(head(arrests_grupos))
