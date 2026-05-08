from src.sakila_ETL import test_connection, process_all_queries

def main():
    test_connection()
    process_all_queries()

if __name__ == "__main__":
    main()