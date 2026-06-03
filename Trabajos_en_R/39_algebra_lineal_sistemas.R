# ==============================================================================
# 39_algebra_lineal_sistemas.R: Resolución de Sistemas de Ecuaciones Lineales
# ==============================================================================

# 1. Planteamiento del problema (Sistema de Ecuaciones 3x3)
# Vamos a resolver el siguiente sistema de ecuaciones lineales:
#  3x + 2y - z  = 1
#  2x - 2y + 4z = -2
# -x + 0.5y - z = 0

# 2. Representación Matricial (A * X = B)
# Matriz de coeficientes (A)
matriz_coeficientes <- matrix(c(
  3,  2, -1,
  2, -2,  4,
 -1, 0.5, -1
), nrow = 3, ncol = 3, byrow = TRUE)

# Vector de términos independientes (B)
vector_independientes <- c(1, -2, 0)

print("Matriz de Coeficientes (A):")
print(matriz_coeficientes)

print("Vector de Términos Independientes (B):")
print(vector_independientes)

# 3. Validación: Comprobar si existe solución única
# El sistema tiene solución única si el determinante de la matriz A es diferente de cero (det(A) != 0)
determinante <- det(matriz_coeficientes)
print(paste("Determinante de A:", round(determinante, 4)))

if (determinante == 0) {
  stop("El determinante es cero; el sistema no tiene solución única (es indeterminado o incompatible).")
}

# 4. Solución del Sistema (Método de la Matriz Inversa usando solve())
# solve(A, B) resuelve directamente el sistema lineal A * X = B
vector_solucion <- solve(matriz_coeficientes, vector_independientes)

# Asignar nombres a los componentes del vector solución
names(vector_solucion) <- c("x", "y", "z")

print("Valores calculados de las variables (X):")
print(vector_solucion)

# 5. Verificación Matemática de la Solución
# Comprobamos que A %*% X es exactamente igual a B
verificacion <- matriz_coeficientes %*% vector_solucion
print("Comprobación final (Multiplicación A %*% X):")
print(as.numeric(verificacion))
print("¿Es idéntica al vector B original?:")
print(all.equal(as.numeric(verificacion), vector_independientes))
