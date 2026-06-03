# -*- coding: utf-8 -*-
"""
Script 33: Árbol de Decisión para Clasificación
Ingeniero de Machine Learning Senior

En este script aprenderás:
1. Construcción y entrenamiento de un árbol de decisión para clasificación.
2. Control de sobreajuste (overfitting) mediante poda (hiperparámetro `max_depth`).
3. Extracción de la importancia de características (feature importances).
4. Interpretación del modelo como "caja blanca" explicable.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# =====================================================================
# 1. CARGA Y DIVISIÓN DE DATOS
# =====================================================================
# Creamos un dataset simulado donde 2 características son informativas y las otras 2 son ruido (redundantes)
X, y = make_classification(
    n_samples=250, 
    n_features=4, 
    n_informative=2, 
    n_redundant=2, 
    random_state=42
)

# Nombres simulados para las columnas de características
nombres_columnas = ["Frecuencia_Uso", "Antiguedad_Meses", "Ingreso_Estimado", "Edad_Usuario"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("--- ÁRBOL DE DECISIÓN CLASIFICADOR ---")
print(f"Tamaño de entrenamiento: {X_train.shape}")
print(f"Tamaño de prueba       : {X_test.shape}\n")


# =====================================================================
# 2. CONFIGURACIÓN DEL ÁRBOL E HIPERPARÁMETROS
# =====================================================================
# Para evitar que el árbol crezca indefinidamente y se memorice los datos (overfitting),
# controlamos su profundidad máxima usando `max_depth`. Esto se conoce como pre-poda.
modelo_arbol = DecisionTreeClassifier(
    criterion="gini",       # Métrica para evaluar las divisiones en nodos
    max_depth=3,            # Limita el árbol a 3 niveles de ramificación
    min_samples_split=5,    # Mínimo de muestras para poder dividir un nodo interno
    random_state=42
)

# Ajuste del modelo
modelo_arbol.fit(X_train, y_train)


# =====================================================================
# 3. EVALUACIÓN Y EXTRACTO DE IMPORTANCIA DE CARACTERÍSTICAS
# =====================================================================
y_pred = modelo_arbol.predict(X_test)
exactitud = metrics.accuracy_score(y_test, y_pred)

print("--- Evaluación del Árbol de Decisión ---")
print(f"Exactitud Global (Accuracy): {exactitud * 100:.2f}%\n")

# Importancia de las Características (Feature Importances)
# Mide cuánto redujo cada variable la impureza Gini en las divisiones del árbol
importancias = modelo_arbol.feature_importances_

print("--- Importancia de las Características ---")
for nombre, importancia in zip(nombres_columnas, importancias):
    print(f"  * {nombre:<18}: {importancia * 100:6.2f}%")

print("\nInterpretación:")
print("Las variables con importancia del 0% no fueron utilizadas por el árbol")
print("en ninguna ramificación dentro del límite de profundidad de nivel 3.")
