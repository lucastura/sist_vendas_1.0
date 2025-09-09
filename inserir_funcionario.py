from conexao import conectar

def inserir_funcionario(nome, idade, setor):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO funcionarios (nome, idade, setor) VALUES (%s, %s, %s)"
        valores = (nome, idade,setor)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()