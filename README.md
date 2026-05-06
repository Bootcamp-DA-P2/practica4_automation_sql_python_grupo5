# **Flujo de Datos: De SQL a Python (Base de Datos Sakila)**

Este proyecto documenta un flujo de trabajo de análisis de datos que integra el uso de bases de datos relacionales y procesamiento avanzado con Python. El objetivo principal es la extracción, limpieza y análisis del comportamiento de alquileres y pagos de la base de datos Sakila.

---

## **Fase 1: Extracción y Limpieza en SQL**

En esta fase inicial, se generan tres dataframes obligatorios mediante joins entre tablas específicas de la base de datos Sakila.

### Generación de Dataframes iniciales

**Dataframe 1: Actividad de clientes**

Tablas: customer, address, city, country, rental, payment.

Objetivo: Obtener un dataset que describa el comportamiento de alquileres y pagos.

---

**Dataframe 2: Catálogo de películas**

Tablas: film, film_category, category, language, inventory.

Objetivo: Generar una vista completa del catálogo con categorías, idiomas y disponibilidad física.

---

**Dataframe 3: Elenco y popularidad**

Tablas: film, actor, film_actor.

Objetivo: Analizar el elenco por película y frecuencia de aparición de actores.

---

### Limpieza preliminar SQL (Dataframe 1 seleccionado)

Se eligió el Dataframe 1 para aplicar las siguientes reglas de limpieza directamente en el motor de base de datos antes de su exportación:

* **Filtrado de nulos:** Eliminación de registros con `rental_id` o `payment_id` nulos.
* **Reglas de negocio:** Asegurar que `amount` sea mayor a 0 y que `return_date` no sea nula (alquileres completados).
* **Estandarización:** Uso de `LOWER()` para nombres, apellidos, emails y ciudades.
* **Consistencia temporal:** Verificación de que `rental_date` sea menor que `return_date`.
* **Columna derivada:** Creación de `rental_duration` calculada en días usando `DATEDIFF`.

---

## **Fase 2: Procesamiento y análisis en Python**

Utilizando Visual Studio Code, se realizó una limpieza profunda del dataset exportado de SQL.

---

### **Análisis exploratorio**

Uso de métodos `info()`, `isnull()` y `duplicated()` para validar la estructura.

---

### **Gestión de nulos**

Sustitución de valores faltantes en la columna `district` por el valor *"Sin datos"* y eliminación de registros con errores en fechas.

---

### **Normalización**

Conversión de tipos de datos a `datetime` para operaciones temporales y tratamiento del código postal como dato categórico.

---

### **Tratamiento de outliers**

Análisis de las variables `amount` y `rental_duration`. Se determinó que los valores altos en `amount` corresponden a transacciones reales del sistema y no a errores, por lo que se conservaron en el dataset.

---

### **Ingeniería de datos**

Creación de una columna para identificar el día de la operación.

---

## **Interpretación de las tablas**

A través de las visualizaciones generadas se identificaron los siguientes puntos clave:

* **Distribución de pagos:** La mayoría de las transacciones se concentran en un rango de 2.9 a 4.9.
* **Distribución de importes de pago:** Los importes no se distribuyen de forma uniforme, con picos repetidos en esos valores.
* **Temporalidad:** Los días se reparten de forma bastante homogénea, no existe una preferencia clara por un número concreto de días.
* **Relación de cobro:** Se validó que el importe total aumenta de manera proporcional a la cantidad de días de alquiler (`rental_duration`).

---

## **Estructura de archivos en el repositorio**

* `main.py`: script para la generación del CSV sobre el que se realiza la limpieza en Python.
* Carpeta `sql`: contiene las consultas SQL para la generación del dataframe limpio.
* `data_cleaning.ipynb`: notebook con el código de Python, limpieza final y visualizaciones.
* `requirements.txt`: dependencias del entorno del proyecto.
* `.gitignore`: archivos excluidos del repositorio.
* `.env_example`: plantilla del archivo `.env` para credenciales.

---

## **Instrucciones de uso**

* Descargar e importar la base de datos Sakila en MySQL.
* Configurar el archivo `.env` siguiendo `.env_example`.
* Activar el entorno virtual del proyecto.
* Instalar dependencias desde `requirements.txt`.
* Ejecutar `main.py` desde la raíz del proyecto.
* Verificar la creación de la carpeta `data` con `customer_activity.csv`.
* Abrir `data_cleaning.ipynb`.
* Conectar el notebook al kernel del entorno virtual.
* Ejecutar el notebook para reproducir el análisis en Python.

---

## **Autores**

* Manuel Macarro de la Osa
* Félix González Álvarez
* Elena Suárez Serrano


