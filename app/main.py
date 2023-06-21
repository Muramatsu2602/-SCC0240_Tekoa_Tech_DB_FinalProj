# TODO Pesquisar erros mais específicos
    # subclasses precisam vir primeiro no try except
    # podemos ter vários except
# TODO SQL injection

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

try:
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

except (psycopg2.OperationalError) as error:
    print("Problemas na conexão com o base.")

except (Exception) as error:
    print(f"Unexpected {error=}, {type(error)=}")

def print_menu():
    print("1. Inserir um indigena")
    print("2. Consultar todos os indigenas que tiveram aula com um dado Professor")
    print("3. Remover um indigena")
    print("4. Mostra todos os registros de indigenas na base de dados")
    print("5. Aplicar modificações na base de dados.")
    print("6. Exit (Aplicar modificações e sair)")


def read_cpf():
    cpf = input("Digite o CPF: ")
    while len(cpf) == 0 or len(cpf) > 11:
        print("CPF inválido. Max de caracteres = 11")
        cpf = input("Digite o CPF: ")

    return cpf

def read_data_nasc():
    data_nasc = input("Digite a data de nascimento no formato dd/mm/yyyy: ")
    # validate = re.search('(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}', data_nasc)
    # while validate == None:
    #     print("Data inválida. Digite a data no formato correto: ")
    #     data_nasc = input("Digite a data de nascimento no formato dd/mm/yyyy: ")
    #     validate = re.search('(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}', data_nasc)

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
    aldeia = '(' + latitude + ', ' + longitude + ')' # coordenadas da aldeia
    
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
        # Passamos todos os valores dos atributos como parâmetros nomeados. Dessa forma nos prevenimos SQL Injection
        cur.execute("INSERT INTO INDIGENA (cpf, data_nasc, rani, nome, sexo, aldeia)  VALUES (%s, %s, %s, %s, %s, %s);", (cpf, data_nasc, rani, nome, sexo, aldeia))
    except psycopg2.IntegrityError as error:
        print("Insercao falhou.")
        print("Erro de integridade: ",error)
        print("Pode haver algum problema nas chaves.")
    except psycopg2.DataError as error:
        print("Insercao falhou.")
        print("Erro no formato dos dados inseridos: ", error)
    except Exception as error:
        print("Insercao falhou.")
        print(f"Unexpected {error=}, {type(error)=}")

    print("Indigena inserido com sucesso.")

# Funcionalidade de consulta ao banco
def query_indigena ():
    # cpf = input("Enter the cpf of the indigena  to query: ")
    # cur.execute("SELECT * FROM indigena s WHERE cpf = %s", (cpf,))
    # indigena  = cur.fetchone() -> usar fetchone() ou fetchall() dependendo da consulta
    # if indigena :
    #     print(f"indigena  found: {indigena }")
    # else:
    #     print("indigena  not found.")

    # CPF para testar a funcionalidade 87420936501

    print("Digite o CPF do professor cuja lista de todos os alunos presentes em suas turmas vocẽ quer consultar.")
    prof = read_cpf()

    try: 
        # Passamos o cpf do professor como um parâmetro nomeado. Dessa forma nos prevenimos SQL Injection
        query = 'SELECT DISTINCT I.CPF, I.NOME FROM TURMA T JOIN PROFESSOR P ON T.PROFESSOR = P.FUNCIONARIO JOIN ALUNO_TURMA AL ON T.ID = AL.TURMA JOIN INDIGENA I ON AL.ALUNO = I.CPF WHERE P.FUNCIONARIO = ' + "'" + prof + "'"
        cur.execute(query)
    
        indigenas = cur.fetchall()
        for cpf,nome in indigenas:
            print(f"INDÍGENA:\n\tCPF: {cpf}\n\tNOME: {nome}")
    except psycopg2.IntegrityError as error:
        print("Consulta falhou.")
        print("Erro de integridade: ",error)
        print("Pode haver algum problema nas chaves.")
    except Exception as error:
        print("Consulta falhou.")
        print(f"Unexpected {error=}, {type(error)=}")

# Funcionalidade extra: remoção de indigena por CPF
def remove_indigena ():
    cpf = read_cpf()

    try:
        # Passamos o cpf do indigena como um parâmetro nomeado. Dessa forma nos prevenimos SQL Injection
        cur.execute("DELETE FROM INDIGENA WHERE cpf = %s", (cpf,))
        print("Indigena removido com sucesso.")       
    except psycopg2.IntegrityError as error:
        print("Remocao falhou.")
        print("Erro de integridade: ",error)
        print("Pode haver algum problema nas chaves.")
    except Exception:
        print("Remocao falhou.")
        print(f"Unexpected {error=}, {type(error)=}")

# Extra: mostra todos os indígenas na base de dados
def mostrar_indigenas():
    try:
        cur.execute("SELECT * FROM INDIGENA;")
        indigenas = cur.fetchall()
        for ind in indigenas:
            print(ind)
    
    except psycopg2.IntegrityError as error:
        print("Consulta falhou.")
        print("Erro de integridade: ",error)
        print("Pode haver algum problema nas chaves.")
    except Exception as error:
        print("Consulta falhou.")
        print(f"Unexpected {error=}, {type(error)=}")

def program_loop():
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
            conn.commit()
            print("Commit efetuado.")
        elif choice == "6":
            conn.commit()
            break
        else:
            print("Invalid choice. Please try again.")


# Starting the execution of the program
program_loop()

# Close the cursor and connection
cur.close()
conn.close()
