from conexao import conectar

def inserir_venda(id_cliente,id_funcionario,id_produto,quantidade,valor_unitario):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO vendas (id_cliente,id_funcionario,id_produto,quantidade,valor_unitario) VALUES (%s, %s,%s,%s,%s)"
        valores = (id_cliente,id_funcionario,id_produto,quantidade,valor_unitario)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()