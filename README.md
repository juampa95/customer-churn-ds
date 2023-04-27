# ABANDONO DE CLIENTES EN TARJETAS DE CRÉDITO

<div align="center">
 <img alt ="logo-chrun" src="/img/logo.png" width=50% height: auto//>
</div>

**Integrante:**
- Alejandro Gutierrez 
- Lourdes Rojos
- Juan Pablo Manzano

Como podremos saber, una empresa vende un producto o presta un servicio a sus clientes y de esto obtiene dinero, cumpliendo su objetivo principal el cual es generar ganancias.

Por ello, este proyecto aputanara a uno de los componentes mas importantes de una empresa que son los clientes. Mas especificamente, analizaremos el abandono de los mismos, o mas conocido como customer chrun en ingles. 

Utilizaremos un dataset brindando por un banco anonimo, con datos de su cartera de clientes. Como podremos observar el customer churn rate o taza de abandono de clientes es bastante elevado 

<div align="center">
 <img alt ="pie-chart-chrun-rate" src="/img/chrun_rate.png" width=50% height=auto//>
</div>
  
 Esto quiere decir que desde el año anterior a dia de hoy el banco perdio un 16,07% de sus clientes. 
  
 # 1- OBJETIVOS

**Objetivos principales**

- Descubrir la causa por la cual hay deserción de clientes en las tarjetas de crédito
-Pronosticar cuales son los posibles clientes que abandonaran las tarjetas de crédito

**Objetivos secuendarios**

- Determinar que Modelo se adapta de mejor manera a las necesidades del problema
- Utilizar modelo para predecir grupos de clientes que abandonarian el banco
- Testear modelos generados
  
# 2-Contexto comercial

El Gerente comercial de un banco se encuentra frente a un listado de clientes que utilizan el servicio de tarjetas de crédito y detecta una alta taza de abandono de los mismos. Quieren analizar los datos para descubrir la razón detrás de esto y aprovechar lo mismo para predecir los clientes que probablemente abandonarán para poder tomar medidas sobre esto.
  
# 3-Problema comercial

El banco buscara reducir este abandono de clientes, pero para ello debera actuar sobre el grupo correcto de personas, ya sea a travez de campañas pubilicitarias o ofreciendo algun tipo de beneficio. Por ello es importante determinar de manera efectiva que clientes podrian llegar a dejar de usar los servicios. 

Tomar estas medidas con clientes que no tengan una predisposicion a abandonar el servicio podria incurrir en una reduccion de beneficios o en "molestar" mediante campañas publicitarias a clientes fidelizados. 

# 4-Glosario 

Para entender correctamente que quieren decirnos los datos es necesario saber que quieren decirnos las variables a analizar. Para ello, podemos ingresar al siguiente glosario haciendo click [`AQUI`](glosario.md)

# 5-Análisis Exploratorio de Datos (EDA)

Para comenzar se parte de un analisis exploratorio de los datos, el cual puede encontrarse en este [`notebook`](EDA.ipynb). En el mismo damos un primer vistazo a nuestros datos para intentar detectar patrones o estructuras en la informacion de manera visual. 

De ello podemos plantear diferentes Hipótesis o preguntas que se generen al hacer esta primera observacion.

## Hipótesis y preguntas

### Hipótesis 1

H1 = La media del monto total de transacciones (Total_Trans_Amt) es igual para clientes activos y retirados

H0 = La media del monto total de transacciones (Total_Trans_Amt) es diferente para clientes activos y retirados

<div align="center">
 <img alt ="h1-image" src="/img/h1.png"//>
</div>

*Nota: Como la variable presenta una gran cantidad de Outliers, el valor mas representativo pasa a ser la mediana*

<div align="center">
 Mediana de monto total de transacciones

 |Attrition_Flag    | Mediana    |
 |------------------|------------|
 |Attrited Customer | 2329     |
 |Existing Customer | 4100    |
</div>

> **Insight:** Podemos validar la hipotesis H0 diciendo que *"La mediana del monto total de transacciones es diferente según el target"*. Esto quiere decir que un cliente que abandonara el servicio realiza transacciones por montos menores que un cliente que seguira utilizandolo. 

### Hipótesis 2

H2 = La media de la cantidad total de transacciones (Total_Trans_Ct) es **igual** para clientes activos y retirados

H0 = La media de la cantidad total de transacciones (Total_Trans_Ct) es **diferente** para clientes activos y retirados

> **Insight:** Podemos validar la hipotesis H0 diciendo que *"La mediana de la cantidad total de transacciones es diferente según el target"*. Este analisis demostraria que el cliente que abandona el servicio hará una menor cantidad de transacciones que las que hace un cliente que seguira utilizandolo. 

[Respuesta Detallada](./hip_preg.md#Hipotesis-2)

### Hipótesis 3

H3 = La media de la variacion en cantidad de transacciones Q4 -Q1 (1) es **igual** para clientes activos y retirados 

H0 = La media de la variacion en cantidad de transacciones Q4 -Q1 (Total_Ct_Chng_Q4_Q1) es **diferente** para clientes activos y retirados

> **Insight:** Podemos validar la hipotesis H0 diciendo que *"La mediana de variacion en cantidad de transacciones es diferente según el target"*. Esto quiere decir que un cliente que abandona el servicio reduce casi en un 50% las transacciones que hace a final del periodo comparado con las que hace al inicio del periodo. El cliente que sigue utilizando el servicio tambien reduce esta cantida con respecto al inicio el perioo pero solo en un 25%

[Respuesta Detallada](./hip_preg.md#Hipotesis-3)

### Pregunta 1
 ¿Cúal es el género que más abandona la tarjeta de crédito?
 
<div align="center">
 <img alt ="p1-image" src="/img/p1.png"//>
</div>

<div align="center">
 Abandono del servicio segun genero 

 |Genero  |Attrited Customer|	Existing Customer	|% Abandono|
 |--------|------------|--------|--------|
 |F	|   930	|  4428	 |  17.35%  |
 |M	|   697	|  4072 	|  14.61%  |
</div>

> **Insight:** Podemos decir que las cantidades que abandonan segun genero no son tan diferentes. Pero hay un 3% mas de mujeres que abanbdonan el servicio.

### Pregunta 2
 Los que abandonan la tarjeta de crédito, ¿Cúal es su estado civil?
 
> **Insight:** No se puede detectar ningun patrón de abandono en cuanto al estado civil de los clientes. Las variaciones son menores al 1%. El estado civil NO influye en la deserción. 

 [Respuesta Detallada](./hip_preg.md#Pregunta-2)

### Pregunta 3
 ¿Que edades promedio tienen las personas que abandonan las tarjetas de crédito?
 
> **Insight:** Podemos decir que las edad de los clientes que abandonan el servicio no varia con la de los clientes que siguen utilizandolo. 

 [Respuesta Detallada](./hip_preg.md#Pregunta-3)

### Pregunta 4
¿Cuanto tiempo en promedio llevan las tarjetas sin utilizar de las personas que abandonan la tarjeta de crédito?

> **Insight:** Podemos decir que los clientes que abandonan el servicio tienden a estar mas inactivos en la utilizacion del mismo. Si bien la diferencia no es significativa a simple vista podria ser un factor a tener en cuenta que se analizara mas adelante.  

[Respuesta Detallada](./hip_preg.md#Pregunta-4)

### Pregunta 5 
¿Que tipo de tarjeta usan los clientes que abandonan los servicios??

 > **Insight:** Podemos señalar que los clientes con categoria *Platinum* son los que mas abandonan el servicio con un 25%. Esto debera ser analizado mas adelante, pero podria indicar que los clientes con tarjetas de mayor categoria no estan contentos por los beneficios brindados por las mismas. 

[Respuesta Detallada](./hip_preg.md#Pregunta-5)

### Pregunta 6 
¿Que nivel de educacion tienen los clientes que abanonan los servicios?

 > **Insight:** Dentro de los diferentes niveles, podemos detectar que los clientes que poseen un nivel *Doctorate* tienen la mayor deserción, con un 21,06%. 

[Respuesta Detallada](./hip_preg.md#Pregunta-6)

### Pregunta 7
¿Que nivel de ingresos tienen los clientes que abandonan los servicios?

 > **Insight:** Dentro de las diferentes categorias de ingreso, la que mayor deserción la posee el mayor nivel de ingresos *$120K+*. Esto debera analizarse para ver si los beneficios que brinda el servicio para este tipo de clientes no es suficiente.  

[Respuesta Detallada](./hip_preg.md#Pregunta-7)

## Análisis Multivariado

Con los gráficos anterior pudimos obtener algunos Insights que surgieron de hacer un análisis univariado y bivariado. A continuación profundizaremos en esto haciendo observaciones mas complejas de manera multivariada. Para acceder al notebook completo del análisis podemos hacer click [`AQUI`](multi.ipynb)

### Matríz de correlación
Indica la correlación que hay entre todas las variables numericas de los datos que estamos trabajando 


<div align="center">
 <b>Matriz de correlación segun coeficiente de Pearson</b>
 <img alt ="matriz_cor_pearson-image" src="/img/mat_corr_pearson.png" // title="Matriz de correlación segun coeficiente de Pearson">
</div>

<div align="center">

**TOP 5 VARIABLES CON MAYOR CORRELACIÓN**
 
 |Variable 1 | Variable 2 | Coef.Pearson | 
 |------------------|-----------------------|-----------|
 |Credit_Limit         |Avg_Open_To_Buy         | 0.995981
 |Total_Trans_Amt      |Total_Trans_Ct          | 0.807192
 |Customer_Age         |Months_on_book          | 0.788912
 |Total_Revolving_Bal  |Avg_Utilization_Ratio   | 0.624022
 |Avg_Open_To_Buy      |Avg_Utilization_Ratio   | 0.538808
</div>


>Nota: En ella podemos observar las variables de mayor correlacion en colores azul mas oscuro. Podemos detectar muy pocas variables que poseen una correlación. Tambien se hizo el análisis con correlaciones de kendall y spearman para ver si se observaba alguna diferencia. Pero las variables con mayor correlación son las mismas. Para ver las matrices de corrleación con otros coeficientes podemos verlas desde aquí [`Kendall`](img/mat_corr_kendall.png) Y [`Spearman`](img/mat_corr_spearman.png)

Se procede a realizar graficos detallados entre las variables que poseen un mayor coeficiente de correlación para ver si es posible obtener Insight visualmente.

Credit limit VS avg open to buy
-
<div align="center">
 <img alt ="Credit Limit VS Avg Open To Buy" src="/img/CL_vs_AOTB.png" // title="Credit Limit VS Avg Open To Buy">
</div>

Podemos observar que existe una correlacion casi perfecta entre estas dos variables. Y esto es de esperarse debido a la naturaleza de las mismas. 

El AVG Open to Buy representa cuanto puede comprar una persona sin tener problemas crediticios, por lo que mientras mayor sea el limite de credito que posea, mayor sera el AVG open to buy. 

>Nota: Se considerara la posibildiad de quitar una de estas columnas para no tener dos tipos de datos que indiquen lo mismo. 

total trans amt VS total trans ct
-
<div align="center">
 <img alt ="Total Trans Amt VS Total Trans Ct" src="/img/TTA_vs_TTC.png"// title="Total Trans Amt VS Total Trans Ct">
</div>

Si bien estas variables poseen una correlación de mas de un 0.8 ya no tienen un comportamiento tan marcado como el caso anterior. Pero es interesante ver que la mayoria de las transacciones se encuentran en montos menores a 6000 para ambos targets.

# 6-Prueba de modelos

Antes de comenzar a probar y analizar los resultados obtenidos con diferentes modelos, fue necesario hacer algunas transformaciones de los datos. Para lo que se utilizaron diferentes métodos por medio de pipelines con el fin de transformar los datos de diferentes formas y realizar pruebas para ver si esto meejoraba el rendimiento de los modelos. 

En el notebook de este [`LINK`](Modelos.ipynb) podemos encontrar el detalle de estos pipelines, pero a continuacion podran ver una tabla de que conjuntos se crearon y que se hizo en cada uno.

<div align="center">

| Pipeline |  Transformaciones | Conjunto train |  Conjunto test | conjunto |
|----------|-------------------|----------------|----------------| ---------|
| preprocess | OHE + Ordinalencoder(con MinMaxScaler) | X_train_enc | X_test_enc | enc | 
| preprocess1 | OHE (drop = 'first') | X_train_enc1 | X_test_enc2 | enc 1 | 
| preprocess2 | OHE, OrdinalEncoder y resto numerico MinMaXScaler | X_train_enc2 | X_test_enc2 | enc2 | 
| preprocess3 | OHE (sin drop = 'first') quitando columnas correlacionadas | X_train_enc3 | X_test_enc3| enc3 | 

</div>

Por ultimo transformamos los datos del conjunto "Y" para que las categorias esten representadas por 1 y 0 segun el target que nos interesa detectar

<div align="center">

| Target | Código | 
|--------|--------|
|Attrited Customer | 1 | 
| Existing Customer | 0 |

</div>

Una vez transformados los datos, comenzamos con el entrenamiento de modelos. En esta etapa se obtienen resultados de manera rapida y sencilla con distintos modelos, mediante la minima o nula modificacion de hiperparametros. A estos modelos les llamamos MODELOS BASE

Para poder evaluar los modelos se eligió una metrica especifica en fucnion del problema. Esta fue ROC_AUC. Mediante ella, se evalua y compara la performance de los distintos modelos. Logistic Regression, KNN y Random Forest Classifier.

## Modelos base

### Logistic Regression

Este modelo ofrecio resulados interesantes, considerando que el tuneo de hiperparametros fue nulo. Podemos ver una tabla con los resultados arrojados para los distintos tipos de datos transofrmados. 

<div align="center">

| Datos usados|	ROC_AUC|
|-------------|--------|
| enc2 |	0.706 | 
| enc	| 0.704 |
| enc1	| 0.681 | 
| enc3	| 0.654 |

</div>

<div align="center">
 <img alt ="Matriz de confusion Logistic Regression" src="/img/matriz_reg_log.png" // title="Matriz de confusion Logistic Regression">

</div>

### KNeighborsClassifier

A pesar de ser un modelo sencillo, arrojo resultados muy buenos considerando que no se realizo ningun tipo de optimizacion de hiperparametros. Podemos ver una tabla con los resultados arrojados para los distintos tipos de datos transofrmados. 

<div align="center">

| Datos usados|	ROC_AUC|
|-------------|--------|
| enc3 |	0.769 | 
| enc	| 0.768 |
| enc1	| 0.768 | 
| enc2	| 0.608 |

</div>

<div align="center">
 <img alt ="Matriz de confusion KNN" src="/img/matriz_KNN.png" // title="Matriz de confusion KNN">

</div>

### Random Forest Classifier

Este modelo tambien arrojo resultados muy buenos sin necesidad de tunear demasiado los hiperparametros. Podemos ver una tabla con los resultados arrojados para los distintos tipos de datos transofrmados. 

<div align="center">

| Datos usados|	ROC_AUC|     
|-------------|--------|   
| enc |		0.902 |   
| enc1	| 0.878 |
| enc2	| 0.863 |
| enc3	| 0.828 |

</div>

<div align="center">
 <img alt ="Matriz de confusion RFC" src="/img/matriz_RFC.png" // title="Matriz de confusion RFC">

</div>

## Estandarizacion de variables

Para seguir con el analisis se realizo una estandarizacion de las variables, en donde mediante un test de hipotesis se determino que variables tenian una distribucion normal y cuales no. Una vez definido esto, se realizó un StandardScaler para aquellas variables con distribucion normal y para el resto se utilizo un RobustScaler.

Luego se volvio a entrenar a nuestros modelos base con estos nuevos conjuntos de datos estandarizados. 

<div align="center">

| Modelo | ROC_AUC base | ROC_AUC estandarizado | 
|--------|--------------|-----------------------|
| LogisticRegression | 0.706 | 0.769 |
| KNeighborsClassifier | 0.768 | 0.790 | 
| RandomForestClassifier | 0.902 | 0.907 |
 
 </div>
 
 > Como podemos ver las metricas no mejoran demasiado usando los datos estandarizados, pero como era de esperarse, la regresion logistica es el modelo que mejor trabaja con estos datos estandarizados.
 

## Reducción de complejidad 

Se intenta reducir la dimensionalidad del modelo utilizando varias técnicas diferentes. Con cada una, se vuelven a evaluar los modelos base para ver si se logro alguna mejora en cuanto al rendimiento. 

### Reducción de dimensionalidad PCA

Se hizo un bucle en donde se intento determinar el mejor roc_auc en funcion de la cantidad de variables, probando con diferentes cantidades entre 1 y 15. Para los 3 modelos evaluados, la cantidad de variables optima era n_components = 3. Por lo que se procede a hacer un analisis del rendimiento de los modelos, aplicando un PCA con n_components = 3 en los datos de train y test. 

<div align="center">

| Modelo | ROC_AUC base | ROC_AUC PCA | 
|--------|--------------|-----------------------|
| LogisticRegression | 0.706 | 0.743 |
| KNeighborsClassifier | 0.768 | 0.761 | 
| RandomForestClassifier | 0.902 | 0.791 |
 
  </div>

> Como podemos ver, la metrica de evaluacion disminuye para todos los modelos entenados. Pero no debemos perder de vista, que se logro una reduccion de 21 variables a solo 3. Esto puede ser algo a evaluar cuando es necesario trabajar con conjuntos de datos livianos y faciles de procesar, sacrificando un poco el rendimiento del modelo pero ganando velocidad de procesamiento. 

### Feature selection VarianceThreshold

Se hizo un VarianceThreshold para identificar las variables que representaran el 90% de la varianza del conjunto. Esto logro reducir las 21 dimensiones que tenian nuestros datos orginiales y pasamos a tener solo 11. Podemos ver los resultados de los modelos en la tabal a continuación.

<div align="center">

| Modelo | ROC_AUC base | ROC_AUC VarianceThreshold | 
|--------|--------------|-----------------------|
| LogisticRegression | 0.706 | 0.672 |
| KNeighborsClassifier | 0.768 | 0.768 | 
| RandomForestClassifier | 0.902 | 0.890 |
 
  </div>

> Para el RandomForestClassifier la selección de caracteristicas fue bastante útil ya que aumento su metrica en casi un 5%, llevando el rendimiento del modelo a 0.792.

### Feature selection SelectKBest

Se hizo un SelectKBest para que mediante pruebas estadisticas detectara las 7 mejores variables que representaran el conjunto de datos. Este metodo para selección de caracteristicas fue el mas promeetedor, mejorando los resultados en los 3 modelos utilizados. 

<div align="center">

| Modelo | ROC_AUC base | ROC_AUC SelectKBest | 
|--------|--------------|-----------------------|
| LogisticRegression | 0.706 | 0.695 |
| KNeighborsClassifier | 0.768 | 0.803 | 
| RandomForestClassifier | 0.902 | 0.882 |
 
  </div>

> Se logro aumentar en gran medida el rendimiento del modelo KNeighborsClassifier (0.810). Superando el rendimiento logrado anteriormente por el RandomForestClassifier

## Tuneo de hiperparametros

Utilizando RandomizedSearchCV fue posible analizar el rendmiento de cada modelo cuando se modificaban sus hiperparametros y con la validacion cruzada realizada con un StratifiedKFold se busco la posibilidad de que el modelo estuviera teniendo overfiting. 

Para este punto, solo se siguio con los modelos KNeighborsClassifier y RandomForestClassifier que habian tenido los mejores resultados anteriormente. Adicionalmente, se hizo una prueba con un XGBOOSTClassifier para comparar resultados. 

<div align="center">

| Modelo            | Hiperparametros | ROC_AUC CV | ROC_AUC optimizado | 
|-------------------|-----------------|------------|--------------------|
|RandomForestClassifier|(max_depth=28, n_estimators=700,criterion = 'gini', random_state=0)|0.960|0.908|
|RandomForestClassifier + estandarizacion datos|(max_depth=28, n_estimators=500,criterion = 'gini', random_state=0)|0.959|0.914|
|KNeighborsClassifier|(algorithm='ball_tree', leaf_size=40, n_neighbors=44,weights='distance')|0.926|0.810|
|XGBClassifier|('subsample': 0.8,'min_child_weight': 5,'max_depth': 7,'gamma': 2,'colsample_bytree': 0.6)|0.982|0.901|
 
</div>

De esta tabla podemos determinar que todos los modelos estan tendiendo a tener un pequeño overfiting, ya que las metricas sobre los datos de entenamiento son un poco mejores que las obtenidas sobre los datos de test. Igualmente, la diferencia no es tan grande por lo que no habria que preocuparse por ello. 

# 7-Conclusión

En conclusión, el modelo a utilizar será un RandomForestClassifier ya que muestra un alto rendimiento para predecir el resultado binario de la variable objetivo en el conjunto de datos. El puntaje ROC AUC de `0.914` indica que el modelo tiene una gran capacidad para distinguir entre aquellos clientes que abandonaran el servicio y los que no lo haran. 

Para ello fue necesario lo siguiente:
- Usar los datos transformados mediante el pipeline `preprocess` que devuelve el conjunto de datos X_train_enc y X_test_enc.
- No reducir su dimensionalidad pero si estandarizar los datos mediante StandarScaler y RobustScaler
- Tunear sus hiperparametros con max_depth=28, n_estimators=500, criterion = 'gini', random_state=0

Podemos observar la matriz de confusión del modelo final para corroborar el buen desempeño del mismo. 

<div align="center">
 <img alt ="Matriz de confusion Final" src="/img/matriz_final.png" // title="Matriz de confusion Final">

</div>
