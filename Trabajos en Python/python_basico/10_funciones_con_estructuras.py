# -*- coding: utf-8 -*-
"""
Script 10: Funciones y Retorno de Estructuras Complejas
Profesor: Programación en Python para Ciencia de Datos

En este script aprenderás:
1. Declaración de funciones y uso de parámetros con valores por defecto.
2. Pasar colecciones (listas y diccionarios) como argumentos a una función.
3. Limpieza de datos dentro del cuerpo de la función.
4. Cómo retornar múltiples valores estructurados (retornar tuplas o diccionarios).
"""

# =====================================================================
# DEFINICIÓN DE LA FUNCIÓN DE PROCESAMIENTO
# =====================================================================

def analizar_sensor_datos(lista_lecturas, valor_minimo_valido=0.0):
    """
    Función que limpia y analiza los datos de lecturas de sensores.
    
    Parámetros:
    - lista_lecturas: Lista de números (float o int) que contienen valores de temperatura/presión.
    - valor_minimo_valido: Límite por debajo del cual los datos se consideran erróneos (ruido del sensor).
    
    Retorna:
    Una tupla con tres valores:
    1. Lista de datos limpios (valores por encima del mínimo).
    2. Diccionario con estadísticas básicas (promedio, máximo, mínimo).
    3. Cantidad de valores ruidosos eliminados.
    """
    # 1. Limpieza de datos usando List Comprehension
    datos_limpios = [lectura for lectura in lista_lecturas if lectura >= valor_minimo_valido]
    
    # Calcular cantidad de datos eliminados
    datos_eliminados = len(lista_lecturas) - len(datos_limpios)
    
    # 2. Análisis y Cálculo de Estadísticas (Evitamos errores si la lista queda vacía)
    if len(datos_limpios) > 0:
        promedio = sum(datos_limpios) / len(datos_limpios)
        maximo = max(datos_limpios)
        minimo = min(datos_limpios)
    else:
        promedio = 0.0
        maximo = 0.0
        minimo = 0.0

    # Estructuramos el reporte de métricas en un diccionario
    estadisticas = {
        "promedio_lecturas": round(promedio, 2),
        "valor_maximo": round(maximo, 2),
        "valor_minimo": round(minimo, 2),
        "total_registros_validos": len(datos_limpios)
    }

    # 3. Retornamos múltiples valores estructurados como una tupla
    return datos_limpios, estadisticas, datos_eliminados


# =====================================================================
# APLICACIÓN DE LA FUNCIÓN CON DATOS REALES
# =====================================================================

# Lista de lecturas crudas del sensor. Hay algunos valores negativos que representan errores del sensor.
lecturas_crudas = [22.4, 25.1, -99.0, 24.3, 23.8, -99.9, 26.5]

print("--- ANÁLISIS DE SENSORES Y USO DE FUNCIONES ---")
print(f"Lecturas de sensor originales (crudas): {lecturas_crudas}")

# Llamamos a la función y desempaquetamos los tres valores de retorno
datos_filtrados, reporte_estadisticas, eliminados = analizar_sensor_datos(
    lista_lecturas=lecturas_crudas, 
    valor_minimo_valido=0.0
)

# Mostrar resultados finales procesados
print(f"\nDatos limpios obtenidos: {datos_filtrados}")
print(f"Cantidad de lecturas con ruido eliminadas: {eliminados}")

print("\nEstadísticas del Reporte Estructurado:")
for key, value in reporte_estadisticas.items():
    print(f"  * {key.replace('_', ' ').capitalize()}: {value}")
