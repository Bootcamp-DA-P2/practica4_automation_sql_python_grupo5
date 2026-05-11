from sakila_automation import run_automation
from pathlib import Path
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()


def main():
    print("Iniciando proyecto Sakila...")

    # 1. Ejecutar ETL
    run_automation()

    print("CSVs generados")

    # 2. Leer configuración desde .env
    auto_open = os.getenv("AUTO_OPEN_EXCEL", "false").lower() == "true"
    excel_file = os.getenv("EXCEL_FILE")

    if not excel_file:
        print("No hay ruta de Excel configurada")
        return

    # 3. Construir ruta absoluta
    PROJECT_ROOT = Path(__file__).resolve().parent
    excel_path = PROJECT_ROOT / excel_file

    # 4. Abrir Excel si está activado en .env
    if auto_open:
        try:
            os.startfile(excel_path)
            print("Excel abierto correctamente")
        except Exception as e:
            print(f"No se pudo abrir Excel: {e}")
    else:
        print("Apertura automática de Excel desactivada")

    print("Proceso finalizado")


if __name__ == "__main__":
    main()