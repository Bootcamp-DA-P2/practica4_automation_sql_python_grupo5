# 📊 Proyecto - Automatización MySQL → Python → Excel (ETL + BI)

Este proyecto automatiza la extracción y análisis de datos de la base de datos SQL usando Python, generando varios archivos CSV que se conectan automáticamente a un libro de Excel. El objetivo final es generar archivos optimizados para alimentar un modelo de datos en Power Pivot y construir un Dashboard interactivo en Excel.

---

## 🎯 Objetivo del proyecto

El proyecto se centra en el análisis de:

- Comportamiento de clientes y patrones de consumo
- Distribución geográfica de ingresos (países y ciudades)
- Tendencias temporales de alquileres y pagos
- Identificación de clientes VIP y mercados clave

---

## 🏗️ Arquitectura del flujo de datos

```
MySQL (Sakila)
      ↓
SQLAlchemy (engine)
      ↓
Queries SQL (.sql files)
      ↓
Pandas DataFrames
      ↓
CSV (output/)
      ↓
Excel (Power Query + Power Pivot)
      ↓
Dashboard BI
```

---

## ⚙️ Fase 1: Configuración del entorno y extracción SQL

En esta fase se prepara la infraestructura necesaria y se definen las consultas de extracción centradas en el núcleo del negocio: clientes, películas y alquileres.

### 🔧 Configuración inicial

- **Instalación de Sakila**: Configuración del esquema y datos en el motor MySQL.
- **Entorno de Python**: Creación de un entorno virtual (`venv`) para el aislamiento de dependencias.
- **Seguridad**: Uso de variables de entorno mediante un archivo `.env` para gestionar credenciales de conexión (Host, User, Password, Port).

---

### 🧾 Generación de datasets (consultas SQL)

Se han diseñado consultas SQL modulares almacenadas en la carpeta `/queries`, que generan los siguientes datasets:

1. **Dataset Rental**: Unifica `rental` y `payment` para obtener transacciones con fechas e importes.
2. **Dataset Customer**: Incluye clientes junto con `city` y `country`, permitiendo análisis geográfico.
3. **Dataset Movie**: Relaciona películas con categorías y métricas de consumo.

---

## 🐍 Fase 2: Desarrollo del pipeline en Python

El objetivo es automatizar el flujo de datos desde MySQL hasta archivos locales mediante un ETL modular.

### 🔌 Conexión y extracción

- Implementación de conexión con SQLAlchemy (`engine`) y control de errores.
- Ejecución dinámica de consultas SQL desde archivos `.sql`.
- Carga de resultados en Pandas para procesamiento inmediato.

### 📤 Sistema de exportación automática

- Recorrido automático de la carpeta `/queries`.
- Generación de CSV estructurados compatibles con Excel (Power Query).
- Exportación dinámica al directorio `/output`.
- Logging de éxito y errores por query.

---

## 📊 Fase 3: Integración con Excel y Power Pivot

El pipeline está diseñado para construir un modelo relacional en Excel.

### 📂 Estructura de datos para dashboard

- Formato estandarizado de columnas y tipos de datos.
- Preparación de datasets para Power Pivot.
- Relaciones entre tablas: `customer`, `movie`, `rental`.

### 📈 Visualización

- Creación de medidas DAX.
- Segmentadores por categorías, países y clientes.
- Dashboard interactivo en Excel.

### ⚙️ Automatización y calidad

- Script principal `main.py` como punto único de ejecución.
- Módulo `src/sakila_ETL.py` como motor principal del pipeline ETL.
- Manejo de errores con `try-except`.
- Validación básica de datos antes de exportación.

---

## 📁 Estructura del repositorio

- `main.py`: Punto de entrada del proyecto.
- `src/sakila_ETL.py`: Motor ETL (SQLAlchemy + ejecución de queries).
- `src/config.py`: Configuración de credenciales y entorno.
- `queries/`: Consultas SQL del proyecto.
- `output/`: Datasets generados automáticamente en CSV.
- `dashboard/`: Contiene el archivo `sakila_dashboard.xlsx` y su README de documentación.
- `requirements.txt`: Dependencias del proyecto.
- `.env_example`: Plantilla de configuración de entorno.

---

## 📈 Fase 4: Análisis estratégico y Business Intelligence

El sistema permite identificar patrones clave de negocio:

- **Clientes y consumo**: frecuencia de alquiler y comportamiento de compra.
- **Geografía**: ingresos por país y ciudad.
- **Tendencias temporales**: evolución mensual de alquileres y pagos.
- **Clientes VIP**: usuarios con mayor gasto acumulado.

---

## 🚀 Instrucciones de uso

### 1. Base de datos
Asegúrate de tener instalada la base de datos **Sakila** en MySQL.

### 2. Entorno
Crear y activar entorno virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 3. Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configuración
Renombra `.env_example` a `.env` y completa credenciales.

### 5. Ejecución del pipeline

```bash
python main.py
```

Cada vez que se ejecute `main.py`, se regenerarán los datasets automáticamente.

---

### 6. Actualización en Excel

- Abrir el archivo `dashboard/sakila_dashboard.xlsx`.
- Ir a **Datos → Actualizar todo** o pulsar **F5**.
- El dashboard se sincroniza automáticamente con los datos en `output/`.

---

## 👥 Autores

- Manuel Macarro de la Osa
- Félix González Álvarez
- Elena Suárez Serrano

