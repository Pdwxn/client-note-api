import time
import psycopg2
import os

DB_NAME = os.getenv("POSTGRES_DB", "client_notes")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "db")

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=5432,
            )
            conn.close()
            print("✅ Database ready!")
            break
        except psycopg2.OperationalError:
            print("⏳ Waiting for database...")
            time.sleep(2)

if __name__ == "__main__":
    wait_for_db()