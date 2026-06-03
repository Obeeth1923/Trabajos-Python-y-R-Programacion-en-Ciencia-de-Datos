# -*- coding: utf-8 -*-
"""
Script 03: Ciclos y Control de Flujo (For y While)
Profesor: Programación en Python para Ciencia de Datos

En este script aprenderás:
1. Iteración sobre colecciones usando bucles 'for'.
2. El uso de la función range() para generar secuencias.
3. El bucle 'while' y cómo evitar bucles infinitos.
4. Las sentencias de control de flujo: 'break' y 'continue'.
5. Uso de acumuladores y contadores para analizar métricas.
"""

# =====================================================================
# 1. BUCLE 'FOR': Iterando sobre listas e índices
# =====================================================================
print("--- 1. BUCLE FOR CON LISTAS ---")
# Una lista de temperaturas de un sensor durante 5 horas
temperaturas = [21.5, 23.0, 24.8, 22.1, 20.3]
suma_temperaturas = 0.0

# Iteramos directamente sobre los elementos de la lista
for temp in temperaturas:
    suma_temperaturas += temp

promedio_temp = suma_temperaturas / len(temperaturas)
print(f"Temperaturas registradas: {temperaturas}")
print(f"Temperatura promedio: {promedio_temp:.2f}°C\n")

print("--- 2. BUCLE FOR CON range() ---")
# Supongamos que queremos simular el crecimiento de una población celular
# que se duplica cada ciclo durante 5 ciclos.
poblacion = 100
print(f"Población inicial: {poblacion}")

# range(inicio, fin_exclusivo)
for ciclo in range(1, 6):
    poblacion *= 2
    print(f"  Ciclo {ciclo}: {poblacion} células")
print()

# =====================================================================
# 2. BUCLE 'WHILE' Y ESTRUCTURAS DE CONTROL ('break' y 'continue')
# =====================================================================
print("--- 3. CONTROL DE FLUJO CON WHILE, BREAK Y CONTINUE ---")
# Simulamos un proceso de carga de datos en lotes (batches).
# Queremos procesar registros hasta que ocurra un error crítico o completemos la cuota.
registros_procesados = 0
limite_diario = 10
errores_detectados = [False, False, False, True, False, False] # El 4to registro tiene un error

while registros_procesados < limite_diario:
    # Simulamos avanzar al siguiente índice
    indice_actual = registros_procesados
    
    # Condición de salida de seguridad si excedemos los datos simulados
    if indice_actual >= len(errores_detectados):
        print("Se terminaron los datos disponibles para procesar.")
        break
        
    es_error = errores_detectados[indice_actual]
    
    if es_error:
        print(f"  [ADVERTENCIA] Registro {indice_actual + 1}: Error detectado. Omitiendo registro con 'continue'.")
        registros_procesados += 1
        continue  # Salta el resto del bloque de este ciclo e inicia la siguiente iteración
        
    print(f"  Registro {indice_actual + 1}: Procesado con éxito.")
    registros_procesados += 1

print(f"\nProceso finalizado. Total de registros evaluados: {registros_procesados}")
