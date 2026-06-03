# -*- coding: utf-8 -*-
"""
Script 09: Procesamiento de Archivos Línea por Línea
Profesor: Programación en Python para Ciencia de Datos

En este script aprenderás:
1. Lectura de un archivo simulado registro por registro (eficiente en memoria).
2. Parsing (análisis y separación) de cadenas con split.
3. Filtrado de registros basado en criterios específicos (Ciencia de Datos).
4. Guardado de los datos procesados y limpios en un nuevo archivo de salida.
"""

# Nombre de los archivos de entrada y salida
archivo_entrada = "logs_servidor.txt"
archivo_salida_limpio = "alertas_criticas.txt"

# =====================================================================
# 1. CREACIÓN DEL ARCHIVO SIMULADO DE LOGS (Solo para asegurar la existencia de datos)
# =====================================================================
logs_ejemplo = [
    "2026-06-02 10:00:05,INFO,Acceso al login por el usuario ana_g\n",
    "2026-06-02 10:01:20,WARNING,Consumo de memoria RAM superior al 85%\n",
    "2026-06-02 10:02:15,ERROR,Fallo de conexion con la base de datos\n",
    "2026-06-02 10:03:00,INFO,Cierre de sesión por el usuario ana_g\n",
    "2026-06-02 10:04:10,ERROR,Intento de acceso no autorizado al servidor admin\n",
    "2026-06-02 10:05:30,WARNING,Latencia de red inusual\n"
]

with open(archivo_entrada, "w", encoding="utf-8") as file:
    file.writelines(logs_ejemplo)


# =====================================================================
# 2. FILTRADO Y PROCESAMIENTO
# =====================================================================
# Procesaremos el archivo de logs línea por línea.
# Filtraremos únicamente los registros cuyo nivel de log sea "ERROR" y los guardaremos en un archivo nuevo de alertas.

contador_total = 0
contador_errores = 0

print(f"Iniciando el procesamiento de '{archivo_entrada}'...")

# Abrimos el archivo de lectura y el archivo de escritura al mismo tiempo
with open(archivo_entrada, "r", encoding="utf-8") as entrada, open(archivo_salida_limpio, "w", encoding="utf-8") as salida:
    
    # Iterar directamente sobre el objeto 'entrada' lee el archivo línea por línea de forma eficiente (sin cargar todo el archivo a RAM)
    for linea in entrada:
        contador_total += 1
        
        # Limpiar el carácter de salto de línea y separar por la coma
        linea_limpia = linea.strip()
        partes = linea_limpia.split(",")
        
        # Aseguramos que la línea tenga el formato esperado antes de acceder a sus índices
        if len(partes) == 3:
            timestamp = partes[0]
            nivel = partes[1]
            mensaje = partes[2]
            
            # Condición de filtrado: Solamente queremos los niveles de error crítico (ERROR)
            if nivel == "ERROR":
                contador_errores += 1
                # Escribimos el log formateado en el nuevo archivo limpio
                salida.write(f"ALERTAS CRÍTICAS - [{timestamp}] DETALLE: {mensaje}\n")

print("\n--- RESUMEN DEL PROCESAMIENTO ---")
print(f"Total de líneas procesadas: {contador_total}")
print(f"Errores encontrados y guardados: {contador_errores}")
print(f"El reporte de alertas limpias se ha guardado en: '{archivo_salida_limpio}'")
