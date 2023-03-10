# Hipotesis-1

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

# Hipotesis-2


H2 = La media de la cantidad total de transacciones (Total_Trans_Ct) es **igual** para clientes activos y retirados

H0 = La media de la cantidad total de transacciones (Total_Trans_Ct) es **diferente** para clientes activos y retirados

<div align="center">
 <img alt ="h2-image" src="/img/h2.png"//>
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


# Hipotesis-3

H3 = La media de la variacion en cantidad de transacciones Q4 -Q1 (1) es **igual** para clientes activos y retirados 

H0 = La media de la variacion en cantidad de transacciones Q4 -Q1 (Total_Ct_Chng_Q4_Q1) es **diferente** para clientes activos y retirados

<div align="center">
 <img alt ="h3-image" src="/img/h3.png" //>
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

# Pregunta-1
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

# Pregunta-2
 Los que abandonan la tarjeta de crédito, ¿Cúal es su estado civil?
 
<div align="center">
 <img alt ="p2-image" src="/img/p2.png" //>
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

# Pregunta-3
 ¿Que edades promedio tienen las personas que abandonan las tarjetas de crédito?
 
<div align="center">
 <img alt ="p3-image" src="/img/p3.png" //>
</div>

<div align="center">
 Edad promedio de clientes según target 

 |Target  |Edad Promedio|
 |--------|------------|
 |Attrited Customer	|    46.65	| 
 |Existing Customer	|   46.26	| 
</div>

> **Insight:** Podemos decir que las edad de los clientes que abandonan el servicio no varia con la de los clientes que siguen utilizandolo. 

# Pregunta-4
¿Cuanto tiempo en promedio llevan las tarjetas sin utilizar de las personas que abandonan la tarjeta de crédito?

<div align="center">
 <img alt ="p4-image" src="/img/p4.png" //>
</div>

<div align="center">
 Meses inactivos segun target

 |Target  |Tiempo promedio|
 |--------|------------|
 |Attrited Customer	|    2.69	| 
 |Existing Customer	|   2.27| 
</div>

> **Insight:** Podemos decir que los clientes que abandonan el servicio tienden a estar mas inactivos en la utilizacion del mismo. Si bien la diferencia no es significativa a simple vista podria ser un factor a tener en cuenta que se analizara mas adelante.  

# Pregunta-5
¿Que tipo de tarjeta usan los clientes que abandonan los servicios??

<div align="center">
 <img alt ="p5-image" src="/img/p5.png"//>
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

# Pregunta-6
¿Que nivel de educacion tienen los clientes que abanonan los servicios?

<div align="center">
 <img alt ="p6-image" src="/img/p6.png"//>
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

# Pregunta-7
¿Que nivel de ingresos tienen los clientes que abandonan los servicios?

<div align="center">
 <img alt ="p7-image" src="/img/p7.png" //>
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
