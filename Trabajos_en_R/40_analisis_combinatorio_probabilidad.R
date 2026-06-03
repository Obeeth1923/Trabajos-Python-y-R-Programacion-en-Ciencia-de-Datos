# ==============================================================================
# 40_analisis_combinatorio_probabilidad.R: Técnicas de Conteo en Probabilidad
# ==============================================================================

# 1. Definición de Funciones para Permutaciones y Combinaciones
# Factorial manual (demostrando lógica sin depender únicamente de factorial() nativa)
calcular_factorial <- function(n) {
  if (n < 0) stop("El factorial solo está definido para enteros no negativos.")
  if (n == 0 || n == 1) return(1)
  
  resultado <- 1
  for (i in 2:n) {
    resultado <- resultado * i
  }
  return(resultado)
}

# Permutaciones: Importa el orden de colocación (P(n, r) = n! / (n - r)!)
calcular_permutaciones <- function(n, r) {
  if (r > n) stop("El tamaño de selección 'r' no puede superar el tamaño de población 'n'.")
  return(calcular_factorial(n) / calcular_factorial(n - r))
}

# Combinaciones: No importa el orden de los elementos seleccionados (C(n, r) = n! / (r! * (n - r)!))
calcular_combinaciones <- function(n, r) {
  if (r > n) stop("El tamaño de selección 'r' no puede superar el tamaño de población 'n'.")
  return(calcular_factorial(n) / (calcular_factorial(r) * calcular_factorial(n - r)))
}

# 2. Resolución de Casos de Estudio de Probabilidad
# Caso A: Permutaciones
# Tenemos un comité de 10 personas y queremos saber cuántas formas diferentes hay de seleccionar 
# un Presidente, un Secretario y un Tesorero (el orden del cargo importa).
n_personas <- 10
r_cargos <- 3

formas_comite <- calcular_permutaciones(n_personas, r_cargos)
print(paste("Caso A (Permutaciones): Formas de asignar cargos a", n_personas, "personas para", r_cargos, "puestos:", formas_comite))

# Caso B: Combinaciones (Juego de Lotería)
# En una lotería, debes elegir 6 números de un total de 49. ¿Cuál es el espacio muestral (combinaciones posibles)?
n_numeros_totales <- 49
r_numeros_elegidos <- 6

combinaciones_loteria <- calcular_combinaciones(n_numeros_totales, r_numeros_elegidos)
print(paste("Caso B (Combinaciones): Total de combinaciones posibles en la lotería (6 de 49):", combinaciones_loteria))

# Caso C: Cálculo de Probabilidad Clásica
# Si compras una única boleta de lotería, ¿cuál es la probabilidad de ganar (casos favorables / casos totales)?
probabilidad_ganar <- 1 / combinaciones_loteria
print(paste("Probabilidad exacta de ganar la lotería:", format(probabilidad_ganar, scientific = FALSE)))
