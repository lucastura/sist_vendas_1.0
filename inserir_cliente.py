from conexao import conectar

def inserir_cliente(nome, email, cidade, estado):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO cliente (nome, email, cidade, estado) VALUES (%s, %s, %s, %s)"
        valores = (nome, email, cidade, estado)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()