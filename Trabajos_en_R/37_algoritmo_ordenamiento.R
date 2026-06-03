# ==============================================================================
# 37_algoritmo_ordenamiento.R: Algoritmo Bubble Sort desde Cero
# ==============================================================================

# 1. Definición del Algoritmo de Ordenamiento Burbuja (Bubble Sort)
# Recorre repetidamente el vector, compara elementos adyacentes e los intercambia si están en el orden incorrecto.
bubble_sort <- function(vector_numerico) {
  # Validar que el argumento sea numérico
  if (!is.numeric(vector_numerico)) {
    stop("El vector a ordenar debe ser puramente numérico.")
  }
  
  n <- length(vector_numerico)
  
  # Si el vector tiene 0 o 1 elementos, ya está ordenado
  if (n <= 1) {
    return(vector_numerico)
  }
  
  # Bucle externo: controla cuántas pasadas realizamos
  for (i in 1:(n - 1)) {
    # Bandera para optimización: si no hay intercambios en una pasada, el vector ya está ordenado
    intercambio <- FALSE
    
    # Bucle interno: realiza las comparaciones de elementos adyacentes
    # Los últimos 'i' elementos ya están en su posición correcta, por lo que no es necesario compararlos
    for (j in 1:(n - i)) {
      # Comparar el elemento actual con el siguiente
      if (vector_numerico[j] > vector_numerico[j + 1]) {
        # Intercambiar elementos usando una variable temporal
        temporal <- vector_numerico[j]
        vector_numerico[j] <- vector_numerico[j + 1]
        vector_numerico[j + 1] <- temporal
        
        # Activar la bandera de intercambio
        intercambio <- TRUE
      }
    }
    
    # Optimización: salir temprano si el vector ya está ordenado
    if (!intercambio) {
      break
    }
  }
  
  return(vector_numerico)
}

# 2. Prueba y Simulación de ejecución del algoritmo
# Simular un vector desordenado aleatorio
set.seed(77)
vector_desordenado <- sample(1:50, 10)

print("Vector original (Desordenado):")
print(vector_desordenado)

# Ejecutar ordenamiento burbuja
vector_ordenado <- bubble_sort(vector_desordenado)

print("Vector ordenado desde cero (Bubble Sort):")
print(vector_ordenado)

# Verificación de integridad con la función de ordenamiento nativa de R
print("¿El ordenamiento coincide con sort() de R?:")
print(identical(vector_ordenado, sort(vector_desordenado)))
