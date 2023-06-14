# erros provenientes do sgbd ?
    # colocar try catch nos execute ?
# TODO: Tratamento de erros
# TODO: sql injection

# Usar o try except para inserção dos dados e ver os tipos de retorno de erro do psycopg2 para usar

import psycopg2
import os
import re

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

# Create a cursor object to interact with the database
cur = conn.cursor()

def print_menu():
    print("1. Inserir um indigena")
    print("2. Consultar todos os indigenas que tiveram aula com um dado Professor") # TODO
    print("3. Remover um indigena")
    print("4. Mostra todos os registros de indigenas na base de dados")
    print("5. Exit")


def read_cpf():
    cpf = input("Digite o CPF: ")
    while len(cpf) == 0 or len(cpf) > 11:
        print("CPF inválido. Max de caracteres = 11")
        cpf = input("Digite o CPF: ")

    return cpf

def read_data_nasc():
    data_nasc = input("Digite a data de nascimento no formato dd/mm/yyyy: ")
    validate = re.search(" ^(0[1-9]|[12][0-9]|3[01])[- /.] (0[1-9]|1[012])[- /.] (19|20)\d\d$", data_nasc)
    while validate == None:
        print("Data inválida. Digite a data no formato correto: ")
        data_nasc = input("Digite a data de nascimento no formato dd/mm/yyyy: ")
        validate = re.search(" ^(0[1-9]|[12][0-9]|3[01])[- /.] (0[1-9]|1[012])[- /.] (19|20)\d\d$", data_nasc)

    return data_nasc

def read_rani():
    rani = input("Digite o rani: ")
    while len(rani) == 0 or len(rani) > 15:
        print("rani inválido. Max de caracteres = 15")
        rani = input("Digite o rani: ")

    return rani

def read_nome():
    nome = input("Digite o nome: ")
    while len(nome) == 0 or len(nome) > 50:
        print("nome inválido. Max de caracteres = 50")
        nome = input("Digite o nome: ")
    
    return nome

def read_sexo():
    sexo = input("Digite o sexo: ")
    while len(sexo) == 0 or len(sexo) > 20:
        print("sexo inválido. Max de caracteres = 20")
        sexo = input("Digite o sexo: ")
    
    return sexo

def read_aldeia():
    print("Digite a localização da aldeia do indígena: ")
    latitude = input("Digite a latitude: ")
    longitude = input("Digite a longitude: ")
    aldeia = '(' + latitude + ',' + longitude + ')' # coordenadas da aldeia
    
    return aldeia

# Funcionalidade de cadasto de dados
def insert_indigena ():

    cpf = read_cpf()
    data_nasc = read_data_nasc()
    rani = read_rani()
    nome = read_nome()
    sexo = read_sexo()
    aldeia = read_aldeia()

    try: 
        # avoiding SQL injection
        cur.execute("INSERT INTO INDIGENA (cpf, data_nasc, rani, nome, sexo, aldeia)  VALUES (%s, %s, %s, %s, %s, %s);", (cpf, data_nasc, rani, nome, sexo, aldeia))
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
        print("Insercao falhou.")
        # conn.rollback()-> é necessário
    else:
        conn.commit() # tornando as mudanças persistentes na base -> podemos fazer aqui ?
                                                                # Salvamos a cada inserção ou remoção, não correndo o risco
                                                                # de perdermos o que foi feito. Está certo? ou a operação de commit é 
                                                                # muito cara pra ficar sendo feita após cada operação
        print("Indigena inserido com sucesso.")

# Funcionalidade de consulta ao banco ( Consulta número TODO de consultas.sql)
def query_indigena ():
    # cpf = input("Enter the cpf of the indigena  to query: ")
    # cur.execute("SELECT * FROM indigena s WHERE cpf = %s", (cpf,))
    # indigena  = cur.fetchone() -> usar fetchone() ou fetchall() dependendo da consulta
    # if indigena :
    #     print(f"indigena  found: {indigena }")
    # else:
    #     print("indigena  not found.")

    print("Digite o CPF do professor cuja lista de todos os alunos presentes em suas turmas vocẽ quer consultar.")
    prof = read_cpf()

    cur.execute(""" SELECT DISTINCT I.CPF, I.NOME 
                                FROM INDIGENA I JOIN TURMA T 
                                WHERE T.PROFESSOR = %s """,(prof,))

    try:
        indigenas = cur.fetchall()
    except(Exception, psycopg2.ProgrammingError) as error:
        print(error)
        print("Consulta falhou")
    else:
        for cpf,nome in indigenas:
            print(f"INDÍGENA - CPF: {cpf} NOME: {nome}")


# Funcionalidade extra: remoção de indigena por CPF
def remove_indigena ():
    cpf = read_cpf()

    try:
        cur.execute("DELETE FROM INDIGENA WHERE cpf = %s", (cpf,))
    except(Exception,psycopg2.DatabaseError) as error:
        print(error)
        print("Remocao falhou")
        # conn.rollback() -> é necessário ?
    else:
        conn.commit() # tornando as mudanças persistentes na base -> mesma dúvida mencionado acima
        print("Indigena removido com sucesso.")

def mostrar_indigenas():
    cur.execute("SELECT * FROM INDIGENA;")

    try:
        indigenas = cur.fetchall()
    except(Exception, psycopg2.ProgrammingError) as error:
        print(error)
        print("Consulta falhou")
    else:
        for ind in indigenas:
            print(ind)


# Interactive loop
while True:
    print_menu()
    choice = input("Digite o código da operação que deseje efetuar: ")
    if choice == "1":
        insert_indigena()
    elif choice == "2":
        query_indigena()
    elif choice == "3":
        remove_indigena()
    elif choice == "4":
        mostrar_indigenas()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")



# Close the cursor and connection
cur.close()
conn.close()
