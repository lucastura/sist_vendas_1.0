from conexao import conectar

# Função para inserir usuário
def inserir_usuario(nome, senha):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (%s, %s)", (nome, senha))
    con.commit()
    cursor.close()
    con.close()

# Função para listar usuários
def listar_usuarios():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT nome, senha FROM usuarios")
    resultado = cursor.fetchall()  # retorna lista de tuplas
    cursor.close()
    con.close()
    return resultado

def excluir_usuario(nome):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM usuarios WHERE nome = %s", (nome,))
    con.commit()
    cursor.close()
    con.close()