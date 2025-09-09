import tkinter as tk
from tkinter import ttk, messagebox
from conexao import conectar 
from inserir_vendas import inserir_venda  

def abrir_tela_vendas(master=None):
    def carregar_clientes():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id_cliente, nome FROM cliente")
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return {nome: idc for idc, nome in dados} 

    def carregar_funcionarios():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id_funcionarios, nome FROM funcionarios")
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return {nome: idf for idf, nome in dados} 

    def carregar_produtos():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id_produtos, descricao, valor FROM produtos")
        dados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return {descricao: (idp, val) for idp, descricao, val in dados}


    def atualizar_valor(event):
        produto_selecionado = combo_produto.get()
        if produto_selecionado in produtos:
            entry_valor.delete(0, tk.END)
            valor = produtos[produto_selecionado][1]
            entry_valor.insert(0, f"{float(valor):.2f}")



    def cadastrar_venda():
        cliente = combo_cliente.get()
        funcionario = combo_funcionario.get()
        produto = combo_produto.get()
        quantidade = entry_quantidade.get()

        if not cliente or not funcionario or not produto or not quantidade:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro!")
            return

        id_cliente = clientes[cliente]
        id_funcionario = funcionarios[funcionario]
        id_produto, valor_unitario = produtos[produto]

        try:
            inserir_venda(id_cliente, id_funcionario, id_produto, quantidade, valor_unitario)
            valor_total = quantidade * valor_unitario
            messagebox.showinfo("Sucesso", f"Venda cadastrada!\nValor total: R$ {float(valor_total):.2f}")
            combo_cliente.set("")
            combo_funcionario.set("")
            combo_produto.set("")
            entry_valor.delete(0, tk.END)
            entry_quantidade.delete(0, tk.END)
            combo_cliente.focus_set()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")


    janela = tk.Toplevel() 
    janela.title("Cadastro de Vendas")
    janela.geometry("450x300")
    janela.resizable(False, False)

    janela.transient(master)
    janela.grab_set


    window_width = 400
    window_height = 300
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    janela.geometry(f"{window_width}x{window_height}+{x}+{y}")


    janela.transient(janela.master)  
    janela.grab_set()  


    clientes = carregar_clientes()
    funcionarios = carregar_funcionarios()
    produtos = carregar_produtos()


    tk.Label(janela, text="Cliente:").pack(pady=5)
    combo_cliente = ttk.Combobox(janela, values=list(clientes.keys()), width=50)
    combo_cliente.pack()

    tk.Label(janela, text="Funcionário:").pack(pady=5)
    combo_funcionario = ttk.Combobox(janela, values=list(funcionarios.keys()), width=50)
    combo_funcionario.pack()

    tk.Label(janela, text="Produto:").pack(pady=5)
    combo_produto = ttk.Combobox(janela, values=list(produtos.keys()), width=50)
    combo_produto.pack()
    combo_produto.bind("<<ComboboxSelected>>", atualizar_valor)

    tk.Label(janela, text="Valor Unitário:").pack(pady=5)
    entry_valor = tk.Entry(janela, width=15)
    entry_valor.pack()

    tk.Label(janela, text="Quantidade:").pack(pady=5)
    entry_quantidade = tk.Entry(janela, width=15)
    entry_quantidade.pack()

    tk.Button(janela, text="Cadastrar Venda", command=cadastrar_venda).pack(pady=15)

    janela.mainloop()