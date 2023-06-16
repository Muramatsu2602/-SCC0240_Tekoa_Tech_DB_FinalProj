<<<<<<< HEAD
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
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

def verify_table():
    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    # Print the records
    print("Current table contents:")
    for row in rows:
        print(row)

    # Close the cursor
    cur.close()


verify_table()

=======
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
    print("FUNCIONARIOS contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM ADMINISTRADOR;")
    rows = cur.fetchall()

    # Print the records
    print("ADMINISTRADOR contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM PROFESSOR;")
    rows = cur.fetchall()

    # Print the records
    print("PROFESSOR contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM IDIOMAS_PROF;")
    rows = cur.fetchall()

    # Print the records
    print("IDIOMAS_PROF contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM PATROCINADOR;")
    rows = cur.fetchall()

    # Print the records
    print("PATROCINADOR contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM CONTATO;")
    rows = cur.fetchall()

    # Print the records
    print("CONTATO contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM REPRESENTANTES;")
    rows = cur.fetchall()

    # Print the records
    print("REPRESENTANTES contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM ALDEIA;")
    rows = cur.fetchall()

    # Print the records
    print("ALDEIA contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM INDIGENA;")
    rows = cur.fetchall()

    # Print the records
    print("INDIGENA contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM IDIOMAS_INDIGENA;")
    rows = cur.fetchall()

    # Print the records
    print("IDIOMAS_INDIGENA contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM PATROCINIO;")
    rows = cur.fetchall()

    # Print the records
    print("PATROCINIO contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM FORNECIMENTO;")
    rows = cur.fetchall()

    # Print the records
    print("FORNECIMENTO contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM MATERIAL;")
    rows = cur.fetchall()

    # Print the records
    print("MATERIAL contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM MATERIAL_FORNECIMENTO;")
    rows = cur.fetchall()

    # Print the records
    print("MATERIAL_FORNECIMENTO contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM CURSO;")
    rows = cur.fetchall()

    # Print the records
    print("CURSO contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM PRE_REQUISITOS;")
    rows = cur.fetchall()

    # Print the records
    print("PRE_REQUISITOS contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM FORNECIMENTO_CURSO;")
    rows = cur.fetchall()

    # Print the records
    print("FORNECIMENTO_CURSO contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM PROJETO;")
    rows = cur.fetchall()

    # Print the records
    print("PROJETO contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM PALAVRAS_CHAVE;")
    rows = cur.fetchall()

    # Print the records
    print("PALAVRAS_CHAVE contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM FORNECIMENTO_PROJETO;")
    rows = cur.fetchall()

    # Print the records
    print("FORNECIMENTO_PROJETO contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM TURMA;")
    rows = cur.fetchall()

    # Print the records
    print("TURMA contents:")
    for row in rows:
        print(row)

    print()

    # Query the table and fetch all records
    cur.execute("SELECT * FROM ALUNO_TURMA;")
    rows = cur.fetchall()

    # Print the records
    print("ALUNO_TURMA contents:")
    for row in rows:
        print(row)

    print()


    # Close the cursor
    cur.close()


verify_table()

>>>>>>> Dio
