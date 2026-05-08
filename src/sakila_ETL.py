from sqlalchemy import create_engine, text
from src.config import *
import pandas as pd
from pathlib import Path



def connection_bd():
    """Crear conexión a la base de datos"""
    # 1. Construir la URL de conexión completa
    url_db = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    # 2. Crear el objeto 'motor' (engine) usando la URL
    engine = create_engine(url_db)
    return engine.connect()


def test_connection():
    """Probar la conexión a la base de datos"""
    connection = connection_bd()
    try:
        with connection:
            print("Conexión exitosa a la base de datos.")
            result = connection.execute(text("SELECT COUNT() FROM customer;"))
            count = result.fetchone()[0]

            print(f"Clientes en la tabla customer: {count}")

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")


def run_query(query_path):
    """Ejecutar query desde archivo SQL y devolver DataFrame"""
    connection = connection_bd()

    query_sql = Path(query_path).read_text(encoding="utf-8")

    with connection:
        df = pd.read_sql(text(query_sql), connection)

    return df

def export_csv(df, output_path):
    """Guardar DataFrame en CSV"""
    Path("output").mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"CSV generado: {output_path}")

def process_all_queries():
    """Ejecuta todos los SQL de la carpeta queries y genera CSVs"""

    queries_folder = Path("queries")
    sql_files = list(queries_folder.glob(".sql"))

    for sql_file in sql_files:
        print(f"Ejecutando: {sql_file.name}")

        df = run_query(sql_file)

        output_file = Path("output") / f"{sql_file.stem}.csv"

        export_csv(df, output_file)
