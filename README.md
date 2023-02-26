# ABANDONO DE CLIENTES EN TARJETAS DE CRÉDITO

<div align="center">
 <img alt ="logo-chrun" src="/img/logo.png" width="400" height="300"//>
</div>

**Integrante:**
- Alejandro Gutierrez 
- Lourdes Rojos
- Juan Pablo Manzano

Como podremos saber, una empresa vende un producto o presta un servicio a sus clientes y de esto obtiene dinero, cumpliendo su objetivo principal el cual es generar ganancias.

Por ello, este proyecto aputanara a uno de los componentes mas importantes de una empresa que son los clientes. Mas especificamente, analizaremos el abandono de los mismos, o mas conocido como customer chrun en ingles. 

Utilizaremos un dataset brindando por un banco anonimo, con datos de su cartera de clientes. Como podremos observar el customer churn rate o taza de abandono de clientes es bastante elevado 

<div align="center">
 <img alt ="pie-chart-chrun-rate" src="/img/chrun_rate.png" width="404" height="420"//>
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
 <img alt ="h1-image" src="/img/h1.png" width="949" height="604"//>
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

<div align="center">
 <img alt ="h2-image" src="/img/h2.png" width="949" height="604"//>
</div>

*Nota: Como la variable presenta una gran cantidad de Outliers, el valor mas representativo pasa a ser la mediana*

<div align="center">
 Mediana de cantidad total de transacciones

 |Attrition_Flag    | Mediana    |
 |------------------|------------|
 |Attrited Customer | 43     |
 |Existing Customer | 71     |
</div>

> **Insight:** Podemos validar la hipotesis H0 diciendo que *"La mediana de la cantidad total de transacciones es diferente según el target"*. Este analisis demostraria que el cliente que abandona el servicio hará una menor cantidad de transacciones que las que hace un cliente que seguira utilizandolo. 


### Hipótesis 3

H3 = La media de la variacion en cantidad de transacciones Q4 -Q1 (1) es **igual** para clientes activos y retirados 

H0 = La media de la variacion en cantidad de transacciones Q4 -Q1 (Total_Ct_Chng_Q4_Q1) es **diferente** para clientes activos y retirados

<div align="center">
 <img alt ="h3-image" src="/img/h3.png" width="949" height="604"//>
</div>

*Nota: Como la variable presenta una gran cantidad de Outliers, el valor mas representativo pasa a ser la mediana*

<div align="center">
 Mediana de variacion en cantidad de transacciones 

 |Attrition_Flag    | Mediana    |
 |------------------|------------|
 |Attrited Customer | 55.43 %    |
 |Existing Customer | 74.24 %    |
</div>

> **Insight:** Podemos validar la hipotesis H0 diciendo que *"La mediana de variacion en cantidad de transacciones es diferente según el target"*. Esto quiere decir que un cliente que abandona el servicio reduce casi en un 50% las transacciones que hace a final del periodo comparado con las que hace al inicio del periodo. El cliente que sigue utilizando el servicio tambien reduce esta cantida con respecto al inicio el perioo pero solo en un 25%

### Pregunta 1
 ¿Cúal es el género que más abandona la tarjeta de crédito?
 
<div align="center">
 <img alt ="p1-image" src="/img/p1.png" width="730" height="369"//>
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
 
<div align="center">
 <img alt ="p2-image" src="/img/p2.png" width="730" height="369"//>
</div>

<div align="center">
 Abandono del servicio segun estado civil 

 |Estado civil  |Attrited Customer|	Existing Customer	|% Abandono|
 |--------|------------|--------|--------|
 | Unknown	| 129	|620	 |17.22%
 | Single	 | 668	|3275	|16.94%
 | Divorced| 121	|627	 |16.17%
 | Married	| 709	|3978	|15.12%
</div>

> **Insight:** No se puede detectar ningun patrón de abandono en cuanto al estado civil de los clientes. Las variaciones son menores al 1%. El estado civil NO influye en la deserción. 

### Pregunta 3
 ¿Que edades promedio tienen las personas que abandonan las tarjetas de crédito?
 
<div align="center">
 <img alt ="p3-image" src="/img/p3.png" width="891" height="640"//>
</div>

<div align="center">
 Edad promedio de clientes según target 

 |Target  |Edad Promedio|
 |--------|------------|
 |Attrited Customer	|    46.65	| 
 |Existing Customer	|   46.26	| 
</div>

> **Insight:** Podemos decir que las edad de los clientes que abandonan el servicio no varia con la de los clientes que siguen utilizandolo. 

### Pregunta 4
¿Cuanto tiempo en promedio llevan las tarjetas sin utilizar de las personas que abandonan la tarjeta de crédito?

<div align="center">
 <img alt ="p4-image" src="/img/p4.png" width="891" height="640"//>
</div>

<div align="center">
 Meses inactivos segun target

 |Target  |Tiempo promedio|
 |--------|------------|
 |Attrited Customer	|    2.69	| 
 |Existing Customer	|   2.27| 
</div>

> **Insight:** Podemos decir que los clientes que abandonan el servicio tienden a estar mas inactivos en la utilizacion del mismo. Si bien la diferencia no es significativa a simple vista podria ser un factor a tener en cuenta que se analizara mas adelante.  

### Pregunta 5 
¿Que tipo de tarjeta usan los clientes que abandonan los servicios??

<div align="center">
 <img alt ="p5-image" src="/img/p5.png" width="730" height="369"//>
</div>

<div align="center">
 Tipo de tarjeta utilizadas por clientes segun target 
 
 |Card_Category|	Attrited Customer	|Existing Customer|	% Abandono |
 |-------------|-------------------|-----------------|------------|
 |Platinum|	5|	15|	25.00%|
 |Gold	|21	|95	|18.10%|
 |Blue	|1519	|7917|	16.09%|
 |Silver	|82	|473	|14.77%|
</div>
 
 > **Insight:** Podemos observar que los clientes con categoria *Platinum* son los que mas abandonan el servicio con un 25%. Esto debera ser analizado mas adelante, pero podria indicar que los clientes con tarjetas de mayor categoria no estan contentos por los beneficios brindados por las mismas. 

### Pregunta 6 
¿Que nivel de educacion tienen los clientes que abanonan los servicios?

<div align="center">
 <img alt ="p6-image" src="/img/p6.png" width="730" height="369"//>
</div>

<div align="center">
 Nivel educacional de los clientes según target

 |Education_Level|	Attrited Customer|	Existing Customer|	% Abandono|
 |---------------|------------------|------------------|-----------|			
 |Doctorate	|95|	356|	21.06%|
 |Post-Graduate	|92	|424	|17.82%|
 |Unknown	|256	|1263|	16.85%|
 |Uneducated	|237	|1250|	15.93%|
 |Graduate	|487	|2641|	15.56%|
 |College	|154	|859	|15.20%|
 |High School	|306	|1707	|15.20%|
 </div>
 
 > **Insight:** Dentro de los diferentes niveles, podemos observar que los clientes que poseen un nivel *Doctorate* tienen la mayor deserción, con un 21,06%. 

### Pregunta 7
¿Que nivel de ingresos tienen los clientes que abandonan los servicios?

<div align="center">
 <img alt ="p7-image" src="/img/p7.png" width="730" height="369"//>
</div>

<div align="center">
 Nivel educacional de los clientes según target

 |Income_Category|	Attrited Customer|	Existing Customer|	% Abandono|
 |---------------|------------------|------------------|-----------|			
 |$120K +	|126	|601	|17.33% |
 |Less than $40K	|612	|2949	|17.18%|
 |Unknown	|187	|925	|16.81%|
 |80𝐾 − 120K|242|	1293	|15.76%|
 |40𝐾 − 60K	|271	|1519	|15.13%|
 |60𝐾 − 80K	|189	|1213	|13.48%|
 </div>
 
 > **Insight:** Dentro de las diferentes categorias de ingreso, podemos ver que la que mayor deserción posee es la de mayor nivel de ingresos *$120K+*. Esto debera analizarse para ver si los beneficios que brinda el servicio para este tipo de clientes no es suficiente.  

## Análisis Multivariado

Con los gráficos anterior pudimos obtener algunos Insights que surgieron de hacer un análisis univariado y bivariado. A continuación profundizaremos en esto haciendo observaciones mas complejas de manera multivariada.

### Matríz de correlación
Indica la correlación que hay entre todas las variables numericas de los datos que estamos trabajando 

<div align="center">
 **Matriz de correlación segun coeficiente de Pearson**
 
 <img alt ="matriz_cor_pearson-image" src="/mat_corr_pearson.png" width="903" height="586"//>
 
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




