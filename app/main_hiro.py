import psycopg2
import os

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
    print("1. Insert a user")
    print("2. Query a user")
    print("3. Remove a user")
    print("4. Exit")

def insert_user():

    # Lembrar do tratamento de erros 
    # 
    name = input("Enter the name of the user: ")
    email = input("Enter the email of the user: ")
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    print("User inserted successfully.")

def query_user():
    name = input("Enter the name of the user to query: ")
    cur.execute("SELECT * FROM users WHERE name = %s", (name,))
    user = cur.fetchone()
    if user:
        print(f"User found: {user}")
    else:
        print("User not found.")

def remove_user():
    name = input("Enter the name of the user to remove: ")
    cur.execute("DELETE FROM users WHERE name = %s", (name,))
    conn.commit()
    print("User removed successfully.")

# Interactive loop
while True:
    print_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        insert_user()
    elif choice == "2":
        query_user()
    elif choice == "3":
        remove_user()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the cursor and connection
cur.close()
conn.close()
