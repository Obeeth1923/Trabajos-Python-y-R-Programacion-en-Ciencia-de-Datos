# ==============================================================================
# 31_manipulacion_vectores_matrices.R: Filtrado e Operaciones Matriciales
# ==============================================================================

# 1. Vectores: Creación, Indexación y Operaciones Lógicas
# Crear un vector de calificaciones simuladas
calificaciones <- c(85, 92, 58, 74, 90, 60, 45, 100, 88, 79)

# Filtrado avanzado usando indexación lógica (calificaciones aprobatorias >= 70)
aprobados <- calificaciones[calificaciones >= 70]
print("Calificaciones Aprobatorias:")
print(aprobados)

# Obtener posiciones de los alumnos con calificación sobresaliente (>= 90)
posiciones_sobresalientes <- which(calificaciones >= 90)
print("Índices de alumnos sobresalientes:")
print(posiciones_sobresalientes)

# 2. Matrices: Creación y Propiedades Básicas
# Crear una matriz de 4x3 con números del 1 al 12 (llenada por filas)
matriz_A <- matrix(1:12, nrow = 4, ncol = 3, byrow = TRUE)
print("Matriz A (4x3):")
print(matriz_A)

# Acceder a subsecciones (Fila 2 completa, y el elemento en posición [3,2])
fila_2 <- matriz_A[2, ]
elemento_3_2 <- matriz_A[3, 2]

# 3. Álgebra Matricial: Transposición y Multiplicación
# Para multiplicar matrices A (4x3) y B, B debe tener 3 filas. Creamos B (3x2).
matriz_B <- matrix(c(2, 1, 0, 3, -1, 4), nrow = 3, ncol = 2)
print("Matriz B (3x2):")
print(matriz_B)

# Multiplicación matricial (Operador %*%) -> Resultado será de dimensión (4x2)
matriz_producto <- matriz_A %*% matriz_B
print("Producto Matricial (A %*% B):")
print(matriz_producto)

# Transposición de la matriz producto (dimensión pasa a ser 2x4)
transpuesta_producto <- t(matriz_producto)
print("Transpuesta del Producto Matricial:")
print(transpuesta_producto)
