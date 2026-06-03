# ==============================================================================
# 14_gradient_boosting_xgboost.R: Gradient Boosting con XGBoost
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
# Nota: Si no tiene instalado 'xgboost', ejecute: install.packages("xgboost")
library(xgboost)

# 2. Carga y preprocesamiento de datos
data("mtcars")
# Predecir la variable binaria 'am' (Tipo de transmisión: 0/1)
datos <- as_tibble(mtcars)

# XGBoost requiere matrices numéricas nativas como entrada y etiquetas base-0
X_datos <- datos %>% select(-am) %>% as.matrix()
y_datos <- datos$am

# División en entrenamiento (75%) y prueba (25%)
set.seed(777)
indices <- sample(1:nrow(datos), size = 0.75 * nrow(datos))
X_entrenamiento <- X_datos[indices, ]
y_entrenamiento <- y_datos[indices]
X_prueba <- X_datos[-indices, ]
y_prueba <- y_datos[-indices]

# Crear estructuras de datos nativas de XGBoost (DMatrix)
dtrain <- xgb.DMatrix(data = X_entrenamiento, label = y_entrenamiento)
dtest <- xgb.DMatrix(data = X_prueba, label = y_prueba)

# 3. Entrenamiento con optimización de hiperparámetros (Bucle de cuadrícula simple)
# Definimos algunos parámetros a evaluar
mejores_parametros <- list()
mejor_error <- Inf

tasas_aprendizaje <- c(0.1, 0.3)
profundidades_arbol <- c(3, 6)

for (eta_val in tasas_aprendizaje) {
  for (max_depth_val in profundidades_arbol) {
    # Validación cruzada interna para evaluar combinaciones
    cv_resultado <- xgb.cv(
      params = list(objective = "binary:logistic", eta = eta_val, max_depth = max_depth_val),
      data = dtrain,
      nrounds = 50,
      nfold = 3,
      verbose = FALSE,
      early_stopping_rounds = 10
    )
    
    error_iteracion <- min(cv_resultado$evaluation_log$test_logloss_mean)
    
    if (error_iteracion < mejor_error) {
      mejor_error <- error_iteracion
      mejores_parametros <- list(objective = "binary:logistic", eta = eta_val, max_depth = max_depth_val)
    }
  }
}

print("Mejores parámetros encontrados:")
print(mejores_parametros)

# Entrenar el modelo final
modelo_xgb <- xgb.train(
  params = mejores_parametros,
  data = dtrain,
  nrounds = 100,
  watchlist = list(val = dtest, train = dtrain),
  verbose = FALSE
)

# 4. Evaluación y Visualización
# Predicciones probabilísticas
probabilidades <- predict(modelo_xgb, newdata = dtest)
predicciones <- ifelse(probabilidades > 0.5, 1, 0)

# Exactitud (Accuracy)
accuracy <- mean(predicciones == y_prueba)
print(paste("Exactitud en prueba:", round(accuracy, 4)))

# Importancia de características
importancia <- xgb.importance(feature_names = colnames(X_datos), model = modelo_xgb)
print(importancia)

# Graficar importancia de variables
xgb.plot.importance(importance_matrix = importancia, col = "#2980b9", main = "Importancia de Variables (XGBoost)")
