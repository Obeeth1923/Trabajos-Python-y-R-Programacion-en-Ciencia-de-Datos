# -*- coding: utf-8 -*-
"""
Script 07: Operaciones Combinadas (Listas, Diccionarios y Conjuntos)
Profesor: Programación en Python para Ciencia de Datos

En este script resolveremos un caso práctico completo:
- Gestión y análisis de un registro de alumnos.
- Utilizaremos listas para almacenar datos ordenados, diccionarios para estructurar la información individual de cada alumno, y conjuntos para extraer categorías únicas y calcular estadísticas agregadas limpiamente.
"""

# =====================================================================
# CASO PRÁCTICO: Registro y Análisis de Estudiantes de un Bootcamp
# =====================================================================

# 1. Entrada de datos simulados en una lista de diccionarios
alumnos = [
    {
        "id": 1,
        "nombre": "Carlos Perez",
        "edad": 22,
        "materias": {"Python", "SQL", "Estadística"},
        "notas": [85, 90, 78]
    },
    {
        "id": 2,
        "nombre": "María Gómez",
        "edad": 29,
        "materias": {"Python", "Machine Learning", "Visualización"},
        "notas": [95, 88, 92]
    },
    {
        "id": 3,
        "nombre": "Luis Delgado",
        "edad": 25,
        "materias": {"SQL", "Visualización", "Estadística"},
        "notas": [70, 75, 80]
    },
    {
        "id": 4,
        "nombre": "Sofía Martínez",
        "edad": 24,
        "materias": {"Python", "SQL", "Visualización"},
        "notas": [90, 92, 94]
    }
]

print("--- REGISTRO DE ALUMNOS CARGADO ---")
print(f"Total de alumnos en el sistema: {len(alumnos)}\n")


# 2. Análisis e Iteración de Datos
# A) Encontrar todas las materias únicas dictadas en el Bootcamp
todas_las_materias = set()

for alumno in alumnos:
    # Agregamos todas las materias del alumno actual usando la unión en el set acumulativo
    todas_las_materias = todas_las_materias.union(alumno["materias"])

print(f"Materias dictadas en el Bootcamp (sin duplicados): {todas_las_materias}\n")


# B) Calcular el promedio de notas de cada alumno y estructurar un reporte final
# Usaremos una lista para guardar los diccionarios con el reporte de desempeño individual
reporte_desempeño = []

for alumno in alumnos:
    nombre = alumno["nombre"]
    notas = alumno["notas"]
    
    # Calcular promedio numérico
    promedio = sum(notas) / len(notas)
    
    # Decidir estatus según la calificación promedio (jerarquía condicional)
    if promedio >= 90:
        estatus = "Excelente"
    elif promedio >= 80:
        estatus = "Aprobado Sobresaliente"
    elif promedio >= 70:
        estatus = "Aprobado"
    else:
        estatus = "Requiere Tutoría"
        
    # Crear un diccionario para este alumno y agregarlo a la lista de reportes
    resumen_alumno = {
        "estudiante": nombre,
        "promedio_calificaciones": round(promedio, 2),
        "estatus": estatus,
        "cantidad_materias": len(alumno["materias"])
    }
    reporte_desempeño.append(resumen_alumno)


# 3. Mostrar el reporte estructurado
print("--- REPORTE FINAL DE DESEMPEÑO ---")
for reporte in reporte_desempeño:
    print(f"Estudiante: {reporte['estudiante']}")
    print(f"  > Promedio: {reporte['promedio_calificaciones']}")
    print(f"  > Estatus: {reporte['estatus']}")
    print(f"  > Materias Cursadas: {reporte['cantidad_materias']}")
    print("-" * 35)
