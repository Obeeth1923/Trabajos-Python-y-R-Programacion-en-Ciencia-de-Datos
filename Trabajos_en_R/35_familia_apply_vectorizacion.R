# ==============================================================================
# 35_familia_apply_vectorizacion.R: Vectorización con la Familia Apply
# ==============================================================================

# 1. Función apply(): Operaciones sobre márgenes de matrices (Filas = 1, Columnas = 2)
# Crear una matriz de 4x3 con registros de ventas mensuales de 4 vendedores
ventas <- matrix(c(1200, 1500, 1100, 1800, 2000, 1750, 900, 1150, 1300, 2500, 2400, 2600), 
                 nrow = 4, ncol = 3, 
                 dimnames = list(c("Pedro", "Ana", "Luis", "Sofía"), c("Ene", "Feb", "Mar")))

print("Matriz de Ventas:")
print(ventas)

# Calcular el promedio de ventas mensual de cada vendedor (operación por filas: 1)
promedio_vendedor <- apply(ventas, MARGIN = 1, FUN = mean)
print("Promedio de Ventas por Vendedor (apply por filas):")
print(promedio_vendedor)

# 2. Funciones lapply() y sapply(): Listas y simplificación de salidas
# lapply() aplica una función y retorna una Lista.
# sapply() intenta simplificar el resultado a un Vector o Matriz si es posible.
estudiantes_cursos <- list(
  Matematicas = c(90, 85, 95, 88),
  Fisica = c(70, 75, 80),
  Quimica = c(100, 95, 98, 92, 90)
)

# Obtener la calificación mínima por curso usando lapply
minimos_lista <- lapply(estudiantes_cursos, min)
print("Mínimos en formato Lista (lapply):")
print(minimos_lista)

# Obtener el promedio por curso usando sapply (retorna un vector con nombres)
promedios_vector <- sapply(estudiantes_cursos, mean)
print("Promedios en formato Vector (sapply):")
print(promedios_vector)

# 3. Función tapply(): Resumir datos agrupados por factores
# Similar a "GROUP BY" en SQL o "group_by() %>% summarise()" en tidyverse.
salarios <- c(2500, 3200, 4100, 2800, 3500, 4800)
departamento <- factor(c("TI", "Ventas", "TI", "Ventas", "Ventas", "TI"))

# Obtener la media salarial por departamento
media_salarial <- tapply(X = salarios, INDEX = departamento, FUN = mean)
print("Media Salarial por Departamento (tapply):")
print(media_salarial)
