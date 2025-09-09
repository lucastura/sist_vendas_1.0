from conexao import conectar

def inserir_produto(descricao,valor):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO produtos (descricao, valor) VALUES (%s, %s)"
        valores = (descricao, valor)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

def listar_produto():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT descricao, valor FROM produtos")
    resultado = cursor.fetchall() 
    cursor.close()
    con.close()
    return resultado

def excluir_produto(descricao):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM produtos WHERE descricao = %s", (descricao,))
    con.commit()
    cursor.close()
    con.close()