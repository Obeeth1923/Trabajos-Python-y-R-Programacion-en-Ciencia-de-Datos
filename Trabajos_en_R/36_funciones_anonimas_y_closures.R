# ==============================================================================
# 36_funciones_anonimas_y_closures.R: Funciones de Orden Superior e Closures
# ==============================================================================

# 1. Funciones Anónimas (Lambda Functions)
# Funciones sin nombre explícito declaradas al vuelo. Muy útiles dentro de la familia apply.
valores <- c(10, 20, 30, 40, 50)

# Aplicar una transformación lineal f(x) = (x * 1.8) + 32 a un vector
# Definimos la función directamente dentro del argumento FUN de sapply
valores_transformados <- sapply(valores, function(x) (x * 1.8) + 32)
print("Valores originales:")
print(valores)
print("Valores transformados con función anónima:")
print(valores_transformados)

# 2. Closures (Funciones que retornan funciones)
# Un closure es una función que encapsula un entorno con variables locales persistentes.
# Creamos un generador de funciones de potencias
crear_potenciador <- function(exponente) {
  # El argumento 'exponente' se mantiene en el entorno de la función retornada
  function(base) {
    return(base ^ exponente)
  }
}

# Generar funciones específicas a partir del closure creador
elevar_al_cuadrado <- crear_potenciador(2)
elevar_al_cubo <- crear_potenciador(3)

# Evaluar las funciones generadas
print(paste("5 elevado al cuadrado:", elevar_al_cuadrado(5)))
print(paste("5 elevado al cubo:", elevar_al_cubo(5)))

# 3. Aplicación Práctica: Generador de Normalizadores de Rango
# Retorna una función adaptada a los límites de un dataset particular
crear_escalador_minmax <- function(vector_referencia) {
  minimo <- min(vector_referencia)
  maximo <- max(vector_referencia)
  
  function(x) {
    return((x - minimo) / (maximo - minimo))
  }
}

# Inicializar un escalador basado en un vector de entrenamiento
escalador_edades <- crear_escalador_minmax(c(18, 60))

# Escalar nuevos valores usando la función persistente creada
print("Edad 39 normalizada:")
print(escalador_edades(39)) # Debe dar 0.5 (exactamente a la mitad del rango 18-60)
