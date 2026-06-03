# -*- coding: utf-8 -*-
"""
Script 22: Similitud Coseno
Profesor: Programación en Ciencia de Datos

En este script aprenderás:
1. El concepto matemático de Similitud Coseno para evaluar orientación vectorial.
2. Cálculo de similitud en espacios de alta dimensionalidad (ej. bolsas de palabras o embeddings).
3. Aplicación en sistemas de filtrado colaborativo o recomendación.
"""

import numpy as np

# =====================================================================
# TEORÍA Y FÓRMULA MATEMÁTICA
# =====================================================================
# La similitud coseno mide el coseno del ángulo entre dos vectores.
# Similitud(A, B) = cos(theta) = (A · B) / (||A|| * ||B||)
#
# Características:
# - No depende de la magnitud de los vectores (solo de su dirección).
# - Rango: [-1, 1]. En Ciencia de Datos usualmente se aplica sobre vectores no negativos, limitando el rango a [0, 1].

def calcular_similitud_coseno(v1, v2):
    """
    Calcula la similitud de coseno entre dos vectores numéricos.
    """
    # Producto punto de los vectores
    producto_punto = np.dot(v1, v2)
    
    # Magnitudes (Norma L2)
    norma_v1 = np.linalg.norm(v1)
    norma_v2 = np.linalg.norm(v2)
    
    # Control de división por cero
    if norma_v1 == 0 or norma_v2 == 0:
        return 0.0
        
    return producto_punto / (norma_v1 * norma_v2)


# =====================================================================
# CASO PRÁCTICO: Recomendación de Contenido por Texto (TF-IDF Simple)
# =====================================================================
# Tres documentos representados por la frecuencia de 4 términos clave:
# ["python", "datos", "recetas", "cocina"]

# Documento 1: Introducción a la ciencia de datos con Python
doc_datos_python = np.array([4, 5, 0, 0])

# Documento 2: Programación avanzada en Python
doc_prog_python = np.array([5, 1, 0, 0])

# Documento 3: Recetario de repostería casera
doc_cocina_recetas = np.array([0, 0, 4, 6])

print("--- Vectores de Documentos (Frecuencias de palabras) ---")
print(f"Doc Datos Python : {doc_datos_python}")
print(f"Doc Prog Python  : {doc_prog_python}")
print(f"Doc Cocina       : {doc_cocina_recetas}\n")

# Calcular similitudes cruzadas
sim_1_2 = calcular_similitud_coseno(doc_datos_python, doc_prog_python)
sim_1_3 = calcular_similitud_coseno(doc_datos_python, doc_cocina_recetas)

print("--- RESULTADOS DE SIMILITUD COSENO ---")
print(f"Similitud(Doc Datos, Doc Prog) : {sim_1_2:.4f}")
print(f"Similitud(Doc Datos, Doc Cocina): {sim_1_3:.4f}")

print("\nInterpretación:")
print(f"El Doc 1 y Doc 2 tienen una similitud del {sim_1_2*100:.2f}% debido a que comparten vocabulario técnico (Python).")
print(f"El Doc 1 y Doc 3 tienen una similitud del {sim_1_3*100:.2f}% (ortogonales) al no compartir palabras clave.")
