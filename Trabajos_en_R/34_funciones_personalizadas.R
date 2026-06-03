# ==============================================================================
# 34_funciones_personalizadas.R: Funciones Propias con Control de Errores
# ==============================================================================

# 1. Definición de la función personalizada
# Esta función calcula estadísticas descriptivas de un vector numérico.
# Parámetros:
# - datos: vector numérico (requerido)
# - eliminar_na: lógico, indica si se deben omitir valores perdidos (por defecto TRUE)
calcular_metricas <- function(datos, eliminar_na = TRUE) {
  
  # Validación de tipos de datos de entrada
  if (!is.numeric(datos)) {
    stop("Error: El argumento 'datos' debe ser un vector estrictamente numérico.")
  }
  
  if (!is.logical(eliminar_na)) {
    stop("Error: El argumento 'eliminar_na' debe ser un valor lógico (TRUE/FALSE).")
  }
  
  # Tratamiento opcional de valores faltantes
  if (eliminar_na) {
    datos <- datos[!is.na(datos)]
  }
  
  # Validar que el vector no quede vacío tras eliminar NAs
  if (length(datos) == 0) {
    return(list(
      mensaje = "El vector no contiene elementos válidos para el cálculo.",
      media = NA, rango = NA, conteo = 0
    ))
  }
  
  # Cálculos aritméticos elementales
  suma <- sum(datos)
  conteo <- length(datos)
  media_calculada <- suma / conteo
  
  valor_min <- min(datos)
  valor_max <- max(datos)
  rango_calculado <- valor_max - valor_min
  
  # Retorno estructurado de resultados múltiples en una Lista
  resultados <- list(
    conteo_elementos = conteo,
    media = media_calculada,
    minimo = valor_min,
    maximo = valor_max,
    rango = rango_calculado
  )
  
  return(resultados)
}

# 2. Casos de Prueba de la Función
# Caso de éxito 1: Uso básico con argumentos por defecto
edades <- c(22, 25, 30, 28, 35, 40)
reporte_edades <- calcular_metricas(edades)
print("Estadísticas de Edades:")
print(reporte_edades)

# Caso de éxito 2: Procesamiento con presencia de NAs
temperaturas <- c(18.5, 20.2, NA, 22.1, 19.8, NA)
reporte_temp <- calcular_metricas(temperaturas, eliminar_na = TRUE)
print("Estadísticas de Temperaturas (con NAs imputados/removidos):")
print(reporte_temp)

# Caso de prueba 3: Captura de error controlado
# Intentar pasar un vector de tipo carácter (Descomentar para probar el error)
# calcular_metricas(c("A", "B", "C"))
