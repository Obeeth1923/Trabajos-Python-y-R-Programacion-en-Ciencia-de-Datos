# ==============================================================================
# 33_bucles_y_control.R: Bucles y Estructuras de Control de Flujo
# ==============================================================================

# 1. Bucle 'for' con control 'next' (omitir iteraciones)
# Procesaremos un vector de números. Multiplicaremos por 2 solo los números pares.
# Los impares los ignoramos usando la palabra clave 'next'.
numeros <- c(10, 15, 22, 33, 40, 55, 68)
resultados_pares <- numeric()

print("Procesando números pares con bucle 'for':")
for (num in numeros) {
  # Si el residuo de la división por 2 es diferente de cero, es impar
  if (num %% 2 != 0) {
    next # Salta inmediatamente a la siguiente iteración del bucle
  }
  
  duplicado <- num * 2
  print(paste("Número par encontrado:", num, "-> Duplicado:", duplicado))
  resultados_pares <- c(resultados_pares, duplicado)
}

# 2. Bucle 'while' con control 'break' (detener ejecución prematuramente)
# Simularemos un sistema de ahorro. Sumamos aportaciones hasta superar los 1000 dólares.
# Si encontramos un valor negativo (anomalía), rompemos el ciclo con 'break'.
transacciones <- c(200, 150, 300, -50, 400, 100) # El -50 simula un retiro o error
saldo_acumulado <- 0
indice <- 1

print("Iniciando simulación de cuenta de ahorro:")
while (indice <= length(transacciones)) {
  monto <- transacciones[indice]
  
  if (monto < 0) {
    print(paste("Error: Transacción negativa detectada en la posición", indice, ". Abortando ciclo."))
    break # Finaliza el bucle while inmediatamente
  }
  
  saldo_acumulado <- saldo_acumulado + monto
  print(paste("Transacción:", monto, "| Saldo Actual:", saldo_acumulado))
  
  if (saldo_acumulado >= 500) {
    print("Meta mínima de ahorro de 500 alcanzada. Finalizando exitosamente.")
    break
  }
  
  indice <- indice + 1
}
