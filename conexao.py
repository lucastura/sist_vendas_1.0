import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",        # seu usuário MySQL
            password="", # sua senha
            database="loja"     # seu banco de dados
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro na conexão: {erro}")
        return None