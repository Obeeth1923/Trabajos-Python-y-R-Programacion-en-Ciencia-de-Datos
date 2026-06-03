# -*- coding: utf-8 -*-
"""
Script 06: Conjuntos y Operaciones Matemáticas de Conjuntos
Profesor: Programación en Python para Ciencia de Datos

En este script aprenderás:
1. Qué son los conjuntos (sets) en Python y sus propiedades principales (elementos únicos y no ordenados).
2. Eliminación eficiente de duplicados de una lista de datos.
3. Operaciones matemáticas fundamentales de conjuntos:
   - Unión
   - Intersección
   - Diferencia
   - Diferencia simétrica
"""

# =====================================================================
# 1. CONJUNTOS Y ELIMINACIÓN DE DUPLICADOS
# =====================================================================
print("--- 1. PROPIEDADES DE LOS SETS Y ELIMINACIÓN DE DUPLICADOS ---")

# Lista simulada de IDs de productos comprados en un sitio web (con duplicados)
compras_usuario_a = [101, 102, 103, 101, 104, 102, 105]

# Convertimos la lista a un conjunto para extraer de forma instantánea y eficiente los elementos únicos
set_usuario_a = set(compras_usuario_a)

print(f"Lista original con duplicados: {compras_usuario_a}")
print(f"Conjunto resultante (elementos únicos): {set_usuario_a}")

# Agregar y remover elementos individuales de un conjunto
set_usuario_a.add(106)
set_usuario_a.remove(103)
print(f"Conjunto después de agregar 106 y remover 103: {set_usuario_a}\n")


# =====================================================================
# 2. OPERACIONES DE CONJUNTOS PARA ANÁLISIS DE DATOS
# =====================================================================
# Supongamos que tenemos dos conjuntos de correos electrónicos de usuarios registrados
# en dos campañas de marketing distintas: Campaña de Redes Sociales y Campaña de Correo.

campaña_social = {"ana@mail.com", "pedro@mail.com", "carlos@mail.com", "sofia@mail.com"}
campaña_email = {"pedro@mail.com", "sofia@mail.com", "luis@mail.com", "marta@mail.com"}

print("--- 2. OPERACIONES MATEMÁTICAS ---")
print(f"Usuarios Campaña Social: {campaña_social}")
print(f"Usuarios Campaña Email: {campaña_email}\n")

# A) UNIÓN (|): Todos los usuarios únicos participantes en al menos una de las campañas
todos_los_usuarios = campaña_social.union(campaña_email)
# También se puede escribir: campaña_social | campaña_email
print(f"Unión (Todos los usuarios alcanzados): {todos_los_usuarios}")

# B) INTERSECCIÓN (&): Usuarios que participaron en ambas campañas (audiencia compartida)
usuarios_comunes = campaña_social.intersection(campaña_email)
# También se puede escribir: campaña_social & campaña_email
print(f"Intersección (Usuarios en ambas campañas): {usuarios_comunes}")

# C) DIFERENCIA (-): Usuarios que SOLO participaron en la campaña social pero NO en la de email
solo_social = campaña_social.difference(campaña_email)
# También se puede escribir: campaña_social - campaña_email
print(f"Diferencia (Solo Campaña Social): {solo_social}")

# D) DIFERENCIA SIMÉTRICA (^): Usuarios que estuvieron en una campaña o en la otra, pero NO en ambas
usuarios_exclusivos = campaña_social.symmetric_difference(campaña_email)
# También se puede escribir: campaña_social ^ campaña_email
print(f"Diferencia Simétrica (Usuarios exclusivos de una sola campaña): {usuarios_exclusivos}")
