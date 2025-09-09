import tkinter as tk

from tkinter import messagebox
from inserir_vendas import inserir_venda

def cadastrar_venda():
    id_cliente = entry_cliente.get()
    id_funcionario = entry_funcionario.get()
    id_produto = entry_produto.get()
    quantidade = entry_quantidade.get()
    valor_unitario = entry_valor.get()

    if id_cliente == "" or id_funcionario == "" or id_produto == "" or quantidade == "" or valor_unitario == "":
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    try:
        inserir_venda(id_cliente,id_funcionario,id_produto,quantidade,valor_unitario)
        messagebox.showinfo("Sucesso", "venda cadastrada com sucesso!")
        entry_cliente.delete(0, tk.END)
        entry_funcionario.delete(0, tk.END)
        entry_produto.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

# Janela
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x350")
janela.resizable(False, False)

# Campos
tk.Label(janela, text="id_Cliente:").pack(pady=5)
entry_cliente = tk.Entry(janela, width=40)
entry_cliente.pack()

tk.Label(janela, text="id_Funcionario:").pack(pady=5)
entry_funcionario = tk.Entry(janela, width=40)
entry_funcionario.pack()

tk.Label(janela, text="id_Produto:").pack(pady=5)
entry_produto = tk.Entry(janela, width=40)
entry_produto.pack()

tk.Label(janela, text="quanidade:").pack(pady=5)
entry_quantidade = tk.Entry(janela, width=5)
entry_quantidade.pack()

tk.Label(janela, text="valor:").pack(pady=5)
entry_valor = tk.Entry(janela, width=5)
entry_valor.pack()

tk.Button(janela, text="Cadastrar", command=inserir_venda).pack(pady=15)

janela.mainloop()