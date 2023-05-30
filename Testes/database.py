import pyodbc

# Definir a string de conexão com o banco de dados do Access
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\t4iga\OneDrive\Projetos\Programação\Assistente_Pessoal\jar.accdb;'

# Conectar ao banco de dados
conn = pyodbc.connect(conn_str)

# Criar um cursor para executar consultas
cursor = conn.cursor()

# Executar uma consulta
funcao = "teste"
cursor.execute('SELECT perg FROM perguntas WHERE func = '+"'"+funcao+"';")

# Recuperar os resultados da consulta
rows = cursor.fetchall()

# Imprimir os resultados
for row in rows:
    print(row)

# Fechar a conexão com o banco de dados
conn.close()
