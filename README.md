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
  
# 3- Problema comercial

### Hipótesis 1
H1 = La media del monto total de transacciones (Total_Trans_Amt) es igual para clientes activos y retirados

H0 = La media del monto total de transacciones (Total_Trans_Amt) es diferente para clientes activos y retirados

<div align="center">
 <img alt ="h1-image" src="/img/h1.png" width="949" height="604"//>
</div>

### Hipótesis 2


H2 = La media de la cantidad total de transacciones (Total_Trans_Ct) es **igual** para clientes activos y retirados

H0 = La media de la cantidad total de transacciones (Total_Trans_Ct) es **diferente** para clientes activos y retirados

<div align="center">
 <img alt ="h2-image" src="/img/h2.png" width="949" height="604"//>
</div>

## Hipótesis 3

H3 = La media de la variacion en cantidad de transacciones Q4 -Q1 (1) es **igual** para clientes activos y retirados 

H0 = La media de la variacion en cantidad de transacciones Q4 -Q1 (Total_Ct_Chng_Q4_Q1) es **diferente** para clientes activos y retirados

<div align="center">
 <img alt ="h3-image" src="/img/h3.png" width="949" height="604"//>
</div>

## Pregunta 1
 ¿Cúal es el género que más abandona la tarjeta de crédito?
 
<div align="center">
 <img alt ="p1-image" src="/img/p1.png" width="730" height="369"//>
</div>

## Pregunta 2
 Los que abandonan la tarjeta de crédito, ¿Cúal es su estado civil?
 
<div align="center">
 <img alt ="p2-image" src="/img/p2.png" width="730" height="369"//>
</div>

## Pregunta 3
 ¿Que edades promedio tienen las personas que abandonan las tarjetas de crédito?
 
<div align="center">
 <img alt ="p3-image" src="/img/p3.png" width="891" height="640"//>
</div>

## Pregunta 4
¿Cuanto tiempo en promedio llevan las tarjetas sin utilizar de las personas que abandonan la tarjeta de crédito?

<div align="center">
 <img alt ="p4-image" src="/img/p4.png" width="891" height="640"//>
</div>

## Pregunta 5 
¿Que tipo de tarjeta usan los clientes que abandonan los servicios??

<div align="center">
 <img alt ="p5-image" src="/img/p5.png" width="730" height="369"//>
</div>

## Pregunta 6 
¿Que nivel de educacion tienen los clientes que abanonan los servicios?

<div align="center">
 <img alt ="p6-image" src="/img/p6.png" width="730" height="369"//>
</div>

## Pregunta 7
¿Que nivel de ingresos tienen los clientes que abandonan los servicios?

<div align="center">
 <img alt ="p7-image" src="/img/p7.png" width="730" height="369"//>
</div>
