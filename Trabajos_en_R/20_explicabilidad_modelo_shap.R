# ==============================================================================
# 20_explicabilidad_modelo_shap.R: Interpretabilidad con DALEX (SHAP)
# ==============================================================================

# 1. Carga de librerías
library(tidyverse)
library(randomForest)
# Nota: Si no tiene instalado 'DALEX', ejecute: install.packages("dalex")
library(DALEX)

# 2. Carga y preprocesamiento de datos
data("iris")
datos <- as_tibble(iris)

# Para simplificar la interpretación, construiremos un modelo para predecir si es 'virginica' o no
datos_explicar <- datos %>%
  mutate(EsVirginica = factor(if_else(Species == "virginica", "Si", "No"))) %>%
  select(-Species)

# Entrenamiento del modelo de caja negra (Black-Box)
set.seed(654)
modelo_rf <- randomForest(EsVirginica ~ ., data = datos_explicar, ntree = 100)

# 3. Creación del Explicador (DALEX Engine)
explicador <- explain(
  model = modelo_rf,
  data = datos_explicar %>% select(-EsVirginica),
  y = as.numeric(datos_explicar$EsVirginica == "Si"),
  label = "Random Forest Virginica Classifier",
  verbose = FALSE
)

# 4. Evaluación de Explicabilidad
# Caso A: Importancia Global de las Variables (Feature Importance)
importancia_global <- model_parts(explicador, loss_function = loss_one_minus_auc)
print(importancia_global)

# Caso B: Explicación Local (SHAP/Breakdown para un registro específico)
# Tomamos una observación particular (por ejemplo, el primer registro de virginica)
observacion_individual <- datos_explicar %>%
  filter(EsVirginica == "Si") %>%
  slice(1) %>%
  select(-EsVirginica)

explicacion_local <- predict_parts(
  explainer = explicador,
  new_observation = observacion_individual,
  type = "shap"
)

print(explicacion_local)

# 5. Visualización
# Graficar la importancia global de características
plot_global <- plot(importancia_global) +
  labs(title = "Importancia de Variables (Modelo Global)",
       subtitle = "Basado en la pérdida de AUC tras permutación")

# Graficar explicabilidad local SHAP
plot_local <- plot(explicacion_local) +
  labs(title = "Contribuciones SHAP Locales (Observación Específica)",
       subtitle = "Descomposición del efecto de cada variable en la predicción")

print(plot_global)
print(plot_local)
