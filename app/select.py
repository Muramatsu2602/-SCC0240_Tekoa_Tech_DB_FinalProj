import psycopg2
import os
import time

# Get PostgreSQL connection details from environment variables
host = os.environ.get('POSTGRES_HOST')
port = os.environ.get('POSTGRES_PORT')
user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
database = os.environ.get('POSTGRES_DB')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host = host,
    port = port,
    user = user,
    password = password,
    database = database
)

def select_db():
    # Create a cursor object to interact with the database
    cur = conn.cursor()

    select_str = input('Esreva o seu input:\n')

    # Query the table and fetch all records
    cur.execute(select_str)
    rows = cur.fetchall()

    # Print the records
    print("RESPOSTA DA CONSULTA:")
    for row in rows:
        print(row)

    print()

    # Close the cursor
    cur.close()

select_db()