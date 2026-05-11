from src.sakila_ETL import process_all_queries


def run_automation():
    print("Ejecutando automatización ETL...")
    process_all_queries()
    print("CSVs generados correctamente")

if __name__ == "__main__":
    run_automation()