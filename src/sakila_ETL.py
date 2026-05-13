from sqlalchemy import create_engine, text
from src.config import *
import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
QUERIES_FOLDER = PROJECT_ROOT / "queries"
OUTPUT_FOLDER = PROJECT_ROOT / "output"


def connection_bd():
    """Crear conexión a la base de datos"""
    # 1. Construir la URL de conexión completa
    url_db = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    # 2. Crear el objeto 'motor' (engine) usando la URL
    engine = create_engine(url_db)
    return engine.connect()


def test_connection():
    """Probar la conexión a la base de datos"""
    try:
        connection = connection_bd()
        with connection:
            print("Conexión exitosa a la base de datos.")
            result = connection.execute(text("SELECT COUNT() FROM customer;"))
            count = result.fetchone()[0]

            print(f"Clientes en la tabla customer: {count}")

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")


def run_query(query_path):
    try:
        connection = connection_bd()
        query_sql = Path(query_path).read_text(encoding="utf-8")

        with connection:
            df = pd.read_sql(text(query_sql), connection)

        return df

    except Exception as e:
        print(f"Error en query {query_path.name}: {e}")
        return pd.DataFrame()

def export_csv(df, output_path):
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    if df.empty:
        print(f"DataFrame vacío, no se exporta: {output_path.name}")
        return

    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"CSV generado: {output_path.name}")

def process_all_queries():
    sql_files = sorted(QUERIES_FOLDER.glob("*.sql"))

    successful_exports = []
    failed_queries = []

    if not sql_files:
        print(f"No se encontraron archivos SQL en: {QUERIES_FOLDER}")
        return

    print(f"Iniciando proceso ETL con {len(sql_files)} queries...\n")

    for sql_file in sql_files:
        print(f"Ejecutando: {sql_file.name}")

        try:
            df = run_query(sql_file)

            output_file = OUTPUT_FOLDER / f"{sql_file.stem}.csv"

<<<<<<< HEAD
        export_csv(df, output_file)
=======
            export_csv(df, output_file)
            successful_exports.append(sql_file.name)

        except Exception as e:
            print(f"Error procesando {sql_file.name}: {e}")
            failed_queries.append(sql_file.name)

    print("\nPROCESO FINALIZADO")
    print(f"CSVs generados: {len(successful_exports)}")
    print(f"Errores: {len(failed_queries)}")

    if failed_queries:
        print(f"Queries con error: {', '.join(failed_queries)}")
    
>>>>>>> feature/etl-powerpivot
