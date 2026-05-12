# **Proyecto - Automatización MySQL → Python → Excel**

Este proyecto automatiza la extracción y análisis de datos de la base de datos SQL usando Python, generando varios archivos CSV que se conectan automáticamente a un libro de Excel. El objetivo final es generar archivos optimizados para alimentar un modelo de datos en Power Pivot y construir un Dashboard interactivo en Excel.

## **Fase 1: Configuración del Entorno y Extracción SQL**
En esta fase se prepara la infraestructura necesaria y se definen las consultas de extracción centradas en el núcleo del negocio: clientes, películas y alquileres.

Configuración inicial
•	**Instalación de Sakila**: Configuración del esquema y datos en el motor MySQL.
•	**Entorno de Python**: Creación de un entorno virtual (venv) para el aislamiento de dependencias.
•	**Seguridad**: Implementación de variables de entorno mediante un archivo .env para gestionar credenciales de conexión (Host, User, Password, Port).
### **.Generación de Dataframes (Vistas SQL)**

Se han diseñado tres consultas optimizadas para alimentar el modelo de datos:
1.	**Dataset  Rental** : Unifica rental y payment para obtener transacciones financieras con fechas de operación.
2.	**Dataset  Customers**: Vincula country y suma de amount
3.	**Dataset  Movies**: Relaciona title y suma de amount
________________________________________
## **Fase 2: Desarrollo del pipeline en Python**

Utilizando Python como motor de automatización, gestionamos el flujo de datos desde la base de datos hasta local.
## **Conexión y Extracción**
•	**Implementación de la conexión**: Uso de mysql-connector-python con gestión de errores para asegurar la disponibilidad del servidor.
•	**Generación del Dataset**: Ejecución de consultas SQL optimizadas y carga en estructuras de datos de Pandas para su limpieza inmediata.
## **Sistema de Exportación Automática**
•	**Gestión de rutas**: Creación dinámica de directorios de salida mediante la librería os.
•	**Generación de CSV estructurados**: Exportación de archivos con codificación  para garantizar la compatibilidad total con el motor de importación de Excel (Power Query).
________________________________________
## **Fase 3: Integración con Excel y Power Pivot**

El pipeline está diseñado específicamente para facilitar la creación de un modelo relacional dentro de Excel.
## **Estructura de Datos para Dashboard**
•	**Formateo compatible**: Los archivos generados incluyen encabezados estandarizados y tipos de datos, pre-procesados en Python.
•	**Documentación de conexión**:
1.	Importación de CSVs mediante Power Query.
2.	Carga directa al Modelo de Datos (Power Pivot).
3.	Establecimiento de relaciones entre customer, movie y rental
**Visualización**
•	Creación de medidas DAX 
•	Diseño de un Dashboard con segmentadores por categorías
________________________________________
**Automatización y Calidad**
Para garantizar la fiabilidad del flujo de datos, el proyecto incluye:
•	Script Principal (main.py): Un único punto de ejecución que dispara todo el proceso ETL.
•	Manejo de Errores: Implementación de bloques try-except para capturar fallos de conexión, errores en consultas SQL o permisos de escritura denegados al exportar archivos abiertos.
•	Validación de Datos: Verificación de que el stock de películas sea coherente antes de la exportación.
________________________________________
## **Estructura de archivos en el repositorio**
•	main.py: Script central que ejecuta el pipeline completo.
•	database_connection.py: Módulo encargado de la lógica de conexión y cierre de sesiones MySQL.
•	queries.py: Diccionario de consultas SQL optimizadas para customer, movie y rental.
•	requirements.txt: Dependencias necesarias (pandas, mysql-connector, python-dotenv).
•	.env_example: Plantilla para la configuración de accesos a la base de datos.
•	exports/: Carpeta (generada automáticamente) que contiene los CSV para Excel.
## **Fase 4: Análisis Estratégico y Business Intelligence**

A través del procesamiento de datos y la visualización en el Dashboard, el proyecto permite identificar patrones críticos para la toma de decisiones:
•	Comportamiento de clientes y patrones de consumo: Análisis de la frecuencia de alquiler y preferencias por categorías de películas o ratings de contenido.
•	Distribución geográfica de ingresos: Mapeo de la generación de dinero segmentada por países y ciudades, permitiendo identificar las regiones más rentables.
•	Tendencias temporales de alquileres y pagos: Visualización de picos de actividad por día de la semana y evolución mensual de los ingresos.
•	Identificación de clientes VIP y mercados clave: Aplicación de filtros para detectar a los usuarios con mayor gasto acumulado y las tiendas con mejor rendimiento de inventario.

________________________________________
Instrucciones de uso
1.	MySQL: Asegúrate de tener la base de datos Sakila instalada.
2.	Entorno: Crea y activa tu entorno virtual: python -m venv venv.
3.	Dependencias: Instala los requisitos: pip install -r requirements.txt.
4.	Configuración: Renombra .env_example a .env y completa tus datos.
5.	Ejecución: Corre el comando python main.py.
6.	Excel: Abre Excel, conecta los datos de la carpeta exports a Power Pivot y actualiza tu Dashboard.

## **Autores**

* Manuel Macarro de la Osa
* Félix González Álvarez
* Elena Suárez Serrano


