# -*- coding: utf-8 -*-
"""
Script 05: Diccionarios Estructurados
Profesor: Programación en Python para Ciencia de Datos

En este script aprenderás:
1. Creación de diccionarios (pares clave-valor).
2. Acceso seguro a llaves mediante el método .get().
3. Anidación de datos dentro de diccionarios.
4. Bucles eficientes para iterar sobre llaves, valores y pares clave-valor (.items()).
"""

# =====================================================================
# 1. CREACIÓN Y ESTRUCTURA DE UN DICCIONARIO
# =====================================================================
print("--- 1. ESTRUCTURA Y ACCESO BÁSICO ---")

# Los diccionarios se definen con llaves {} y representan registros mapeados por claves.
usuario = {
    "id": 101,
    "nombre": "Ana Gómez",
    "rol": "Analista de Datos",
    "pais": "México"
}

# Acceso directo usando corchetes []
print(f"Nombre del usuario: {usuario['nombre']}")

# Acceso seguro usando .get(clave, valor_por_defecto)
# Evita que el programa falle con un KeyError si la clave no existe.
telefono = usuario.get("telefono")  # Si no existe, devuelve None
correo = usuario.get("correo", "correo_no_registrado@empresa.com")  # Especifica un valor por defecto

print(f"Teléfono obtenido de forma segura: {telefono}")
print(f"Correo (con fallback por defecto): {correo}\n")


# =====================================================================
# 2. DICCIONARIOS ANIDADOS
# =====================================================================
print("--- 2. ANIDACIÓN DE ESTRUCTURAS ---")

# En Ciencia de Datos, los datos a menudo vienen en formatos complejos como JSON (que se traducen a diccionarios anidados).
dataset_metricas = {
    "proyecto_A": {
        "precision": 0.89,
        "sensibilidad": 0.85,
        "procesados": 1500
    },
    "proyecto_B": {
        "precision": 0.94,
        "sensibilidad": 0.91,
        "procesados": 2300
    }
}

# Acceso jerárquico a elementos anidados
precision_b = dataset_metricas["proyecto_B"]["precision"]
print(f"Precisión del Proyecto B: {precision_b * 100}%\n")


# =====================================================================
# 3. ITERACIÓN SOBRE DICCIONARIOS
# =====================================================================
print("--- 3. ITERACIÓN DE CLAVES Y VALORES ---")

info_ventas = {
    "Enero": 4500,
    "Febrero": 5200,
    "Marzo": 6100
}

# Iterar solo sobre las llaves (keys)
print("Meses evaluados:")
for mes in info_ventas.keys():
    print(f" - {mes}")

# Iterar solo sobre los valores (values)
print("\nMontos de ventas:")
for monto in info_ventas.values():
    print(f" $ {monto}")

# Iterar sobre el par clave-valor al mismo tiempo usando .items() (Muy recomendado en Ciencia de Datos)
print("\nReporte detallado de ventas:")
for mes, ventas in info_ventas.items():
    print(f"  En el mes de {mes} se facturaron ${ventas} USD.")
