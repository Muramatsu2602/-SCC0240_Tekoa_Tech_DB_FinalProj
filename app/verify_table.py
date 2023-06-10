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

def verify_table():
    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM FUNCIONARIOS;")
    rows = cur.fetchall()

    # Print the records
    print("Current table contents:")
    for row in rows:
        print(row)

    # Close the cursor
    cur.close()


verify_table()

