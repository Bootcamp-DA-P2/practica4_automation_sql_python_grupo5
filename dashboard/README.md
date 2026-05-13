# 📊 Sakila Dashboard (Excel)

## 🔄 Flujo de funcionamiento del dashboard

1. Ejecutar el proyecto desde Python:

```bash
python main.py
```

Este proceso ejecuta el pipeline ETL y genera automáticamente los archivos CSV en la carpeta `output/`.

---

## 🗂️ Consultas SQL utilizadas

El proyecto utiliza consultas SQL específicas para generar los conjuntos de datos principales del dashboard.

Las queries procesan información relacionada con:

- 👤 Clientes (`customer`)
- 🎬 Películas (`movie`)
- 📦 Alquileres y pagos (`rental` + `payment`)

---

## 📥 Carga de datos en Excel

Los archivos CSV se importan en Excel mediante **Power Query** utilizando:

```text
Datos → Obtener datos → Desde texto/CSV
```

Cada archivo se carga como:

- ✔ Solo conexión
- ✔ Añadir al modelo de datos

---


## 🧹 Limpieza de datos

No se realizan transformaciones adicionales en Power Query, ya que la limpieza y preparación de datos se realiza previamente en las consultas SQL del proyecto.

Las consultas incluyen:
- Normalización de texto (`LOWER`, `TRIM`)
- Gestión de valores nulos (`COALESCE`)
- Validaciones de datos
- Filtrado de registros inválidos

---

## 📊 Modelo analítico

Una vez cargados los datos en el modelo:

- Se crean relaciones entre tablas mediante Power Pivot
- Se generan medidas DAX para el cálculo de KPIs
- Se construyen tablas dinámicas y gráficos interactivos

La base analítica del proyecto se desarrolla en la **Hoja 1**, donde se organizan las tablas dinámicas, medidas y relaciones del modelo de datos.

El dashboard se divide en dos secciones principales:

### 💰 Importe Global

#### 🔝 KPIs principales

- Ingresos totales
- Total de alquileres
- Duración media del alquiler (días)

---

#### 📊 Visualizaciones

- Ranking de películas por ingresos
- Ranking de países por ingresos
- Ingresos por mes
- Categorías con menos alquileres
- Alquileres por categoría

---

#### 🎛️ Segmentadores (Slicers)

El dashboard incluye filtros interactivos para:
- Mes
- Categoría

---

### 👤 Gestión de Clientes

#### 📊 Visualizaciones

- Segmentación de cientes
- Estado de clientes
- Ranking de países por ingresos
- Ingresos por mes
- Alquileres por categoría

---

#### 🎛️ Segmentadores (Slicers)

El dashboard incluye filtros interactivos para:
- Tipo de cliente
- Estado

---

## 📈 Análisis del dashboard

### 💰 Importe Global

El análisis general muestra un volumen total de ingresos de **6.688.839**, con un total de **15.861 alquileres** registrados.

La duración media de los alquileres se sitúa en aproximadamente **5,03 días**, lo que refleja un comportamiento relativamente estable en los periodos de alquiler.

En relación con las categorías con menor actividad, destacan:
- Comedy
- Classics
- Horror
- Travel
- Music

Por otro lado, las categorías con mayor número de alquileres presentan una distribución bastante equilibrada, destacando:
- Sports
- Animation
- Action

Aunque existen diferencias entre categorías, la variación no es especialmente elevada, moviéndose aproximadamente entre los **800 y 1.200 alquileres**.

---

#### 📅 Evolución temporal de ingresos

Los ingresos muestran una evolución ascendente a lo largo de los meses analizados, manteniéndose relativamente estable en los dos últimos:

- Mayo: ~482.344
- Junio: ~962.989
- Julio: ~2.836.891
- Agosto: ~2.406.615

Julio representa el periodo con mayor volumen de ingresos dentro del conjunto analizado.

---

#### 🎬 Ranking de películas por ingresos

Entre las películas con mayor generación de ingresos destacan:
- Telegraph Voyage
- Wife Turn
- Zorro Ark

Los ingresos generados por las películas más destacadas se sitúan aproximadamente entre los **20.000 y 25.000**.

---

#### 🌍 Ranking de países por ingresos

Los países con mayor contribución de ingresos son:
- India
- China
- Estados Unidos

India presenta el mayor volumen de ingresos, situándose aproximadamente entre los **600.000 y 700.000**, seguida de China con cifras ligeramente inferiores.


---

### 👤 Gestión de clientes

En esta sección del dashboard se ha segmentado a los clientes en VIP y normales, utilizando como criterio un gasto superior a 15.000 o más de 35 alquileres. Bajo esta definición, los clientes VIP representan el 8%, mientras que los clientes normales suponen el 92%, lo que refleja que una minoría concentra el mayor valor del negocio.

En cuanto al estado de los clientes, el 97% se encuentra activo frente a un 3% inactivo, lo que indica una alta retención y uso del servicio.

Además, se han incluido el ranking de países por ingresos, los ingresos mensuales y los alquileres por categoría, con el objetivo de comparar estos datos globales con la segmentación de clientes y el estado de actividad, permitiendo así una visión más completa del comportamiento del negocio.

## 🔄 Actualización de datos

Para actualizar el dashboard:

### 1. Ejecutar nuevamente Python

```bash
python main.py
```

### 2. Abrir Excel y actualizar conexiones

- Presionar `F5`
- o `Ctrl + Alt + F5`
- o `Datos → Actualizar todo`

Esto actualiza automáticamente:
- tablas dinámicas
- gráficos
- KPIs
- segmentadores

sin necesidad de volver a importar los archivos CSV.

---

## 📌 Conclusión del análisis

El dashboard permite analizar el comportamiento de la base de datos Sakila desde diferentes perspectivas: ingresos, actividad de clientes, rendimiento de películas y distribución geográfica.

Gracias a Power Pivot, tablas dinámicas y segmentadores, los datos pueden explorarse de forma interactiva y dinámica.

El análisis facilita la identificación de patrones de comportamiento y tendencias temporales, transformando datos transaccionales en información útil para la toma de decisiones.
