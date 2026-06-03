# -*- coding: utf-8 -*-
"""
Script 01: Tipos de Datos y Operaciones
Profesor: Programación en Python para Ciencia de Datos

En este script aprenderás:
1. Manipulación de números enteros (int) y decimales (float).
2. Operaciones aritméticas fundamentales en Python.
3. Métodos esenciales para manipular cadenas de texto (strings).
"""

# =====================================================================
# 1. NÚMEROS Y OPERACIONES ARITMÉTICAS
# =====================================================================

# Definición de variables numéricas para análisis de datos básico
ventas_mensuales = 1500  # Tipo entero (int)
precio_unidad = 29.99    # Tipo decimal/punto flotante (float)

# Operaciones aritméticas básicas
ingreso_total = ventas_mensuales * precio_unidad
costo_operativo = 12500.50
ganancia_neta = ingreso_total - costo_operativo

# División entera (//) y residuo/módulo (%)
# Ejemplo: Queremos empacar productos en cajas de 12 unidades
total_productos = 157
unidades_por_caja = 12
cajas_completas = total_productos // unidades_por_caja
productos_restantes = total_productos % unidades_por_caja

# Potenciación (**)
# Ejemplo: Cálculo de interés compuesto simple
capital_inicial = 1000
tasa_interes = 0.05
años = 3
capital_final = capital_inicial * (1 + tasa_interes) ** años

print("--- 1. RESULTADOS NUMÉRICOS ---")
print(f"Ingreso Total: ${ingreso_total:.2f}")
print(f"Ganancia Neta: ${ganancia_neta:.2f}")
print(f"Cajas completas a enviar: {cajas_completas}")
print(f"Productos sueltos/restantes: {productos_restantes}")
print(f"Capital final estimado a 3 años: ${capital_final:.2f}\n")


# =====================================================================
# 2. MANIPULACIÓN DE CADENAS DE TEXTO (STRINGS)
# =====================================================================

# En Ciencia de Datos es muy común recibir texto sucio que debemos limpiar
reporte_sucio = "   REPORTE Mensual: Análisis De Ventas_Sector_Norte   "

# Métodos de limpieza de texto (eliminación de espacios en blanco al inicio y final)
reporte_limpio = reporte_sucio.strip()

# Convertir a mayúsculas (upper) y minúsculas (lower)
mayusculas = reporte_limpio.upper()
minusculas = reporte_limpio.lower()

# Reemplazar caracteres (replace)
# Cambiamos los guiones bajos por espacios simples
reporte_formateado = reporte_limpio.replace("_", " ")

# Dividir texto basado en un delimitador (split)
# Esto genera una lista con las palabras resultantes
palabras = reporte_limpio.split("_")

# Slicing (rebanado) de cadenas
# Sintaxis: cadena[inicio:fin_exclusivo]
primeros_15_caracteres = reporte_limpio[:15]
codigo_sector = reporte_limpio[-5:]  # Toma los últimos 5 caracteres

print("--- 2. RESULTADOS DE CADENAS (STRINGS) ---")
print(f"Texto original sucio: '{reporte_sucio}'")
print(f"Texto limpio (.strip()): '{reporte_limpio}'")
print(f"Mayúsculas (.upper()): '{mayusculas}'")
print(f"Minúsculas (.lower()): '{minusculas}'")
print(f"Reemplazo (.replace()): '{reporte_formateado}'")
print(f"División (.split()): {palabras}")
print(f"Slicing (primeros 15 caracteres): '{primeros_15_caracteres}'")
print(f"Slicing (últimos 5 caracteres): '{codigo_sector}'")
