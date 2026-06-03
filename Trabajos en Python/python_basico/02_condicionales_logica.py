# -*- coding: utf-8 -*-
"""
Script 02: Condicionales y Lógica de Decisiones
Profesor: Programación en Python para Ciencia de Datos

En este script aprenderás:
1. El uso de bloques de decisión jerárquica con if, elif y else.
2. Operadores de comparación (>, <, ==, !=, >=, <=).
3. Operadores lógicos (and, or, not) para evaluar múltiples condiciones a la vez.
"""

# =====================================================================
# CASO DE ESTUDIO: Calificación de Leads (Clientes Potenciales)
# =====================================================================
# En ciencia de datos, a menudo automatizamos la toma de decisiones.
# Evaluaremos si un usuario web califica como un "Lead Calificado para Ventas" (SQL)
# basándonos en tres variables:
# - score_interes: Puntuación de 0 a 100 basada en su actividad web.
# - descargas: Número de recursos (e-books, whitepapers) descargados.
# - correo_corporativo: Booleano que indica si el correo es corporativo o personal.

score_interes = 75
descargas = 3
correo_corporativo = True

print("--- EVALUACIÓN DE CLIENTE POTENCIAL (LEAD) ---")
print(f"Puntaje de interés: {score_interes}")
print(f"Descargas realizadas: {descargas}")
print(f"¿Tiene correo corporativo?: {correo_corporativo}\n")

# Toma de decisiones jerárquicas con operadores lógicos
# Condición 1: Muy alta prioridad (Score muy alto Y correo corporativo)
if score_interes >= 80 and correo_corporativo:
    prioridad = "ALTA"
    accion = "Enviar directamente al equipo de ventas (SQL)."

# Condición 2: Prioridad Media (Score medio-alto O múltiples descargas, pero con correo corporativo)
elif (score_interes >= 60 or descargas >= 4) and correo_corporativo:
    prioridad = "MEDIA"
    accion = "Asignar a campaña de correo automatizada (Nurturing)."

# Condición 3: Prioridad Baja (Cualquier cliente interesado pero sin correo corporativo)
elif score_interes >= 50 and not correo_corporativo:
    prioridad = "BAJA"
    accion = "Invitar a webinar gratuito para recopilar más datos."

# Condición 4: Caso por defecto (No cumple con los requisitos mínimos de interés)
else:
    prioridad = "NINGUNA"
    accion = "Mantener en base de datos general de suscriptores."

# Mostrar el resultado de la toma de decisiones
print(f"RESULTADO DEL ANÁLISIS:")
print(f"Prioridad del Lead: {prioridad}")
print(f"Acción a tomar: {accion}")

# =====================================================================
# EJEMPLO COMPLEMENTARIO: Verificación de calidad de datos
# =====================================================================
# Verificaremos si una variable que representa una tasa de conversión es válida.
tasa_conversion = 0.12  # 12%

# Una tasa de conversión lógica debe estar estrictamente entre 0 y 1 (o 0% y 100%)
if tasa_conversion < 0 or tasa_conversion > 1:
    print("\n[ALERTA] La tasa de conversión está fuera del rango lógico (0 a 1).")
else:
    print(f"\n[OK] Tasa de conversión de {tasa_conversion * 100}% validada correctamente.")
