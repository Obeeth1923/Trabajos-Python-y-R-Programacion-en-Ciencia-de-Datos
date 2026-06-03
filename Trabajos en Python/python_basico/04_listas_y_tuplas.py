# -*- coding: utf-8 -*-
"""
Script 04: Listas y Tuplas
Profesor: Programación en Python para Ciencia de Datos

En este script aprenderás:
1. Las diferencias fundamentales entre listas (mutables) y tuplas (inmutables).
2. Métodos comunes de listas: append, extend, pop y sort.
3. El concepto de clonación (copiado) de listas frente a referencias.
4. Comprensión de listas (List Comprehensions): una técnica poderosa y limpia en Python.
"""

# =====================================================================
# 1. LISTAS (MUTABLES) VS TUPLAS (INMUTABLES)
# =====================================================================
print("--- 1. MUTABILIDAD VS INMUTABILIDAD ---")

# Las listas se definen con corchetes [] y son ideales para colecciones de datos dinámicos.
lista_frutas = ["manzana", "banana", "naranja"]
print(f"Lista original: {lista_frutas}")
lista_frutas[1] = "pera"  # Modificación permitida (mutabilidad)
print(f"Lista modificada: {lista_frutas}")

# Las tuplas se definen con paréntesis () y son excelentes para datos estructurados fijos (ej. coordenadas, registros base).
coordenadas_gps = (4.7110, -74.0721)  # (Latitud, Longitud) de Bogotá
print(f"Tupla de coordenadas: {coordenadas_gps}")
# Intentar hacer: coordenadas_gps[0] = 4.7120 generaría un TypeError (inmutabilidad).
print("Nota: Las tuplas protegen la integridad de los datos evitando cambios accidentales.\n")


# =====================================================================
# 2. MÉTODOS CLAVE DE LISTAS Y CLONACIÓN
# =====================================================================
print("--- 2. MÉTODOS DE LISTAS ---")
valores = [10, 5, 8]

# Agregar un elemento al final (append)
valores.append(20)

# Agregar múltiples elementos al final (extend)
valores.extend([15, 3])
print(f"Lista después de append y extend: {valores}")

# Eliminar y obtener el último elemento (pop)
ultimo = valores.pop()
print(f"Elemento extraído con pop: {ultimo}")
print(f"Lista después del pop: {valores}")

# Ordenar la lista en su lugar (sort)
valores.sort()
print(f"Lista ordenada de menor a mayor: {valores}")

# Clonación correcta de listas
# En Python, si haces 'copia = valores', ambas variables apuntan al mismo objeto en memoria.
# Para crear una copia independiente (clon), usamos .copy() o el slicing [:]
valores_clonados = valores.copy()
valores_clonados.append(999)
print(f"Lista original sin alterar: {valores}")
print(f"Lista clonada modificada: {valores_clonados}\n")


# =====================================================================
# 3. COMPRENSIÓN DE LISTAS (LIST COMPREHENSIONS)
# =====================================================================
print("--- 3. COMPRENSIÓN DE LISTAS (LIST COMPREHENSIONS) ---")
# Una sintaxis elegante para crear nuevas listas a partir de iteraciones.

# Supongamos que tenemos precios en dólares y queremos convertirlos a euros (tasa: 0.92)
precios_usd = [10.0, 25.5, 100.0, 5.75]

# Enfoque tradicional con bucle for:
precios_eur_tradicional = []
for p in precios_usd:
    precios_eur_tradicional.append(p * 0.92)

# Enfoque moderno y rápido con List Comprehension:
precios_eur_comprension = [p * 0.92 for p in precios_usd]

# List Comprehension con filtrado condicional:
# Solo queremos los precios mayores a 20 USD en la conversión
precios_altos_eur = [p * 0.92 for p in precios_usd if p > 20.0]

print(f"Precios USD: {precios_usd}")
print(f"Precios EUR (List Comp.): {precios_eur_comprension}")
print(f"Precios altos EUR (>20 USD): {precios_altos_eur}")
