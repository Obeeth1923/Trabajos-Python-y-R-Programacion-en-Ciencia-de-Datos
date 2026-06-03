# ==============================================================================
# 38_estadistica_desde_cero.R: Media, Mediana y Moda sin Funciones Nativas
# ==============================================================================

# 1. Cálculo de la Media Aritmética
calcular_media <- function(x) {
  # Validación de entrada
  if (length(x) == 0) return(NA)
  
  suma_acumulada <- 0
  contador <- 0
  
  # Sumar recursivamente y contar los elementos de forma explícita
  for (valor in x) {
    suma_acumulada <- suma_acumulada + valor
    contador <- contador + 1
  }
  
  return(suma_acumulada / contador)
}

# 2. Cálculo de la Mediana
calcular_mediana <- function(x) {
  if (length(x) == 0) return(NA)
  
  # Ordenar el vector numérico usando ordenamiento nativo
  x_ordenado <- sort(x)
  n <- length(x_ordenado)
  
  if (n %% 2 != 0) {
    # Caso impar: Tomamos el elemento exactamente a la mitad
    indice_medio <- (n + 1) / 2
    mediana <- x_ordenado[indice_medio]
  } else {
    # Caso par: Promedio de los dos elementos centrales
    indice_medio_1 <- n / 2
    indice_medio_2 <- (n / 2) + 1
    mediana <- (x_ordenado[indice_medio_1] + x_ordenado[indice_medio_2]) / 2
  }
  
  return(mediana)
}

# 3. Cálculo de la Moda (el valor más repetido)
calcular_moda <- function(x) {
  if (length(x) == 0) return(NA)
  
  # Obtener los elementos únicos
  valores_unicos <- unique(x)
  
  # Contar las repeticiones de cada elemento único manualmente
  frecuencias <- numeric(length(valores_unicos))
  
  for (i in seq_along(valores_unicos)) {
    val_u <- valores_unicos[i]
    conteo <- 0
    for (item in x) {
      if (item == val_u) {
        conteo <- conteo + 1
      }
    }
    frecuencias[i] <- conteo
  }
  
  # Identificar la frecuencia máxima
  max_frecuencia <- max(frecuencias)
  
  # Encontrar cuáles valores tienen esa frecuencia máxima
  indices_moda <- which(frecuencias == max_frecuencia)
  modas <- valores_unicos[indices_moda]
  
  # Si todos los elementos se repiten igual número de veces, no hay moda real
  if (length(modas) == length(valores_unicos)) {
    return("No existe moda (distribución uniforme)")
  }
  
  return(modas)
}

# 4. Verificación de los Algoritmos con un Vector de Muestra
muestra_datos <- c(10, 15, 20, 20, 25, 30, 35, 40, 20, 15)

print(paste("Vector evaluado:", paste(muestra_datos, collapse = ", ")))
print(paste("Media calculada desde cero:", calcular_media(muestra_datos)))
print(paste("Mediana calculada desde cero:", calcular_mediana(muestra_datos)))
print("Moda calculada desde cero:")
print(calcular_moda(muestra_datos))
