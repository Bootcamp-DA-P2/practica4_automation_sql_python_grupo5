from sqlalchemy import create_engine, text
from config import *
import pandas as pd



# Create a database connection
def conection_bd():
    """Crear conexión a la base de datos"""
    # 1. Construir la URL de conexión completa
    url_db = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    # 2. Crear el objeto 'motor' (engine) usando la URL
    engine = create_engine(url_db)
    return engine.connect()


def test_connection():
    """Probar la conexión a la base de datos"""
    connection = conection_bd()
    try:
        with connection:
            print("Conexión exitosa a la base de datos.")
            result = connection.execute(text("SHOW TABLES;"))
            print(result.fetchone())

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        

def get_data_list_from_join():
    """Obtener dataframe 1: actividad de clientes (prelimpieza en SQL)"""

    connection = conection_bd()

    query_sql = """
    SELECT
        c.customer_id,
        LOWER(c.first_name) AS first_name,
        LOWER(c.last_name) AS last_name,
        LOWER(c.email) AS email,
        c.active,

        LOWER(a.address) AS address,
        LOWER(a.district) AS district,
        a.postal_code,

        LOWER(ci.city) AS city,
        LOWER(co.country) AS country,

        r.rental_id,
        r.rental_date,
        r.return_date,

        p.payment_id,
        p.payment_date,
        p.amount,

        DATEDIFF(r.return_date, r.rental_date) AS rental_duration

    FROM customer c
    JOIN address a ON c.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
    JOIN rental r ON c.customer_id = r.customer_id
    JOIN payment p ON r.rental_id = p.rental_id

    WHERE
        p.amount > 0
        AND r.return_date IS NOT NULL
        AND r.rental_date < r.return_date;
    """

    with connection:
        df = pd.read_sql(text(query_sql), connection)

    # Export opcional (mejor nombre acorde al proyecto)
    df.to_csv(
        "data/customer_activity.csv",
        index=False,
        encoding="utf-8"
    )

    print("✅ DataFrame creado correctamente y guardado en data/customer_activity.csv")

    return df
        
if __name__ == "__main__":
    test_connection()
    get_data_list_from_join()

    