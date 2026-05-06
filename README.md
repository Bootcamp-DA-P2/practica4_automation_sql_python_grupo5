# **Flujo de Datos: De SQL a Python (Base de Datos Sakila)**

Este proyecto documenta un flujo de trabajo de analisis de datos que integra el uso de bases de datos relacionales y procesamiento avanzado con Python. El objetivo principal es la extraccion, limpieza y analisis del comportamiento de alquileres y pagos de la base de datos Sakila.

Fase 1: Extraccion y Limpieza en SQL

En esta fase inicial, se generan tres dataframes obligatorios mediante joins entre tablas especificas de la base de datos Sakila.

Generacion de Dataframes iniciales
Dataframe 1: Actividad de clientes

Tablas: customer, address, city, country, rental, payment.

Objetivo: Obtener un dataset que describa el comportamiento de alquileres y pagos.

Dataframe 2: Catalogo de peliculas

Tablas: film, film_category, category, language, inventory.

Objetivo: Generar una vista completa del catalogo con categorias, idiomas y disponibilidad fisica.

Dataframe 3: Elenco y popularidad

Tablas: film, actor, film_actor.

Objetivo: Analizar el elenco por pelicula y frecuencia de aparicion de actores.

Limpieza Preliminar SQL (Dataframe 1 Seleccionado)
Se eligio el Dataframe 1 para aplicar las siguientes reglas de limpieza directamente en el motor de base de datos antes de su exportacion:

Filtrado de Nulos: Eliminacion de registros con rental_id o payment_id nulos.

Reglas de Negocio: Asegurar que amount sea mayor a 0 y que return_date no sea nula (alquileres completados).

Estandarizacion: Uso de LOWER() para nombres, apellidos, emails y ciudades.

Consistencia Temporal: Verificacion de que rental_date sea menor a return_date.

Columna Derivada: Creacion de rental_duration calculada en dias usando DATEDIFF.Creacion de columna derivada: Calculo de la duracion del alquiler en dias.

## **Fase 2: Procesamiento y Analisis en Python**

Utilizando Visual Studio, se realizo una limpieza profunda del dataset exportado de SQL:

### **Analisis Exploratorio**

Uso de metodos info(), isnull() y duplicated() para validar la estructura.

### **Gestion de nulos**

Sustitucion de valores faltantes en la columna district por el valor Sin Datos y eliminacion de registros con errores en fechas.

### **NormalizaciÃ³n**

Conversion de tipos de datos a datetime para operaciones temporales y tratamiento del codigo postal como dato categorico.

### **Tratamiento de Outliers**

Analisis de las variables amount y rental_duration. Se determino que los valores altos en amount corresponden a transacciones reales del sistema y no a errores, por lo que se conservaron en el dataset.

### **Ingenieria de datos**

Creacion de una columna para identificar el dias de la operacion.

## **Interpretación de las tablas**

A traves de las visualizaciones generadas se identificaron los siguientes puntos clave:

Distribucion de Pagos: La mayoria de las transacciones se concentran en un rango de 2.9 a 4.9.

Distribucion de importes de pago: Los importes de pago no se distribuyen de forma uniforme, con picos repetidos en esos importes.

Temporalidad: Los dias se reparten de forma bastante homogenea, no existe una prefrencia clara por un numero concreto de dias.

Relacion de Cobro: Se valido que el importe total aumenta de manera proporcional a la cantidad de dias de alquiler (rental_duration).

## **Estructura de Archivos en el Repositorio**

main.py: contiene el script para la generación del csv

Carpeta sql: Contiene las consultas de SQL para la generación del dataframe limpio.

data_cleaning.ipynb: Notebook con el código de Python, limpieza final y visualizaciones.

requirements.txt: Todos los requisitos para el entorno del proyecto.

.gitignore: Todo lo que queremos descartar del proyecto.

.evn_exmple: Modelo para el .evn que usaremos para poner nuestra contraseña

## **Instrucciones de Uso**

Ejecutar el script SQL en un entorno compatible con la base de datos Sakila.

Cargar el CSV en el Notebook de Python proporcionado para replicar el analisis y las visualizaciones.




