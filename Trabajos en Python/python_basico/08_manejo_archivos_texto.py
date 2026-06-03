# -*- coding: utf-8 -*-
"""
Script 08: Manejo de Archivos de Texto
Profesor: Programación en Python para Ciencia de Datos

En este script aprenderás:
1. Cómo crear y abrir un archivo en modo de escritura ('w').
2. Cómo abrir un archivo en modo de lectura ('r').
3. El uso recomendado de la sentencia 'with open()' (Context Manager) para garantizar el cierre seguro de los archivos del sistema, incluso si ocurren excepciones.
"""

# Nombre del archivo que vamos a crear e interactuar
nombre_archivo = "registro_visitas.txt"

# =====================================================================
# 1. ESCRITURA EN UN ARCHIVO DE TEXTO
# =====================================================================
# El modo 'w' (write) crea el archivo si no existe. Si ya existe, lo sobrescribe por completo.
# Si quisiéramos agregar contenido al final sin borrar el anterior, usaríamos el modo 'a' (append).

datos_a_escribir = [
    "Ana Gomez,2026-06-01,Marketing\n",
    "Carlos Perez,2026-06-01,Ventas\n",
    "Maria Gomez,2026-06-02,Desarrollo\n",
    "Luis Delgado,2026-06-02,Soporte\n"
]

print(f"Creando y escribiendo en el archivo '{nombre_archivo}'...")

# La sintaxis 'with' maneja automáticamente la apertura y el cierre del archivo de forma interna.
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    for linea in datos_a_escribir:
        archivo.write(linea)

print("¡Escritura completada exitosamente!\n")


# =====================================================================
# 2. LECTURA DE UN ARCHIVO DE TEXTO
# =====================================================================
# Abrimos el mismo archivo creado anteriormente, pero esta vez en modo 'r' (read).

print(f"Abriendo y leyendo el contenido de '{nombre_archivo}':")

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    # Usamos readlines() para obtener todas las líneas del archivo estructuradas en una lista
    lineas = archivo.readlines()

# Mostramos cada línea limpia eliminando el salto de línea al final usando .strip()
for index, linea in enumerate(lineas, 1):
    linea_limpia = linea.strip()
    print(f"  Fila {index}: {linea_limpia}")

print("\nLectura finalizada correctamente.")
