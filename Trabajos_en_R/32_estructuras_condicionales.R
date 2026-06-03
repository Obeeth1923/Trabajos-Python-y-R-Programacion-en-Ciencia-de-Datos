# ==============================================================================
# 32_estructuras_condicionales.R: Estructuras Condicionales en R
# ==============================================================================

# 1. Condicionales Básicos (if, else if, else)
# Evaluación de un promedio académico individual
promedio <- 87.5

if (promedio >= 90) {
  print("Desempeño: Excelente (Aprobado con honores)")
} else if (promedio >= 70) {
  print("Desempeño: Satisfactorio (Aprobado)")
} else {
  print("Desempeño: No Aprobado (Repetir curso)")
}

# 2. Evaluación con condiciones lógicas compuestas
asistencia <- 0.85 # 85% de asistencia requerido

# Para aprobar se necesita calificación >= 70 Y asistencia >= 80%
if (promedio >= 70 && asistencia >= 0.80) {
  print("Resultado: Estudiante Acreditado")
} else {
  print("Resultado: Estudiante No Acreditado (Calificación insuficiente o faltas)")
}

# 3. Condicional Vectorizado (ifelse)
# ifelse() es eficiente para procesar vectores completos sin utilizar bucles.
calificaciones_grupo <- c(55, 90, 72, 88, 60, 95, 45, 80)

# Clasificar a cada alumno del vector en "Aprobado" o "Reprobado"
estado_alumnos <- ifelse(calificaciones_grupo >= 70, "Aprobado", "Reprobado")

# Crear un reporte legible
reporte <- data.frame(
  Calificacion = calificaciones_grupo,
  Estado = estado_alumnos
)
print("Reporte de Acreditación del Grupo:")
print(reporte)
