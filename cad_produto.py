import tkinter as tk
from tkinter import messagebox
from inserir_produto import inserir_produto
from tela_listar_produtos import exibir_produtos
def abrir_tela_produto(master=None):
    def cadastrar_produto():
        descricao = entry_descricao.get()
        valor = entry_valor.get()
        
        
        if descricao == "" or valor == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

        try:
            inserir_produto(descricao, valor)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            entry_descricao.delete(0, tk.END)
            entry_valor.delete(0, tk.END)
            entry_descricao.focus_set()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")


    janela = tk.Toplevel(master)
    janela.title("Cadastro de Produtos")
    janela.geometry("350x250")
    janela.resizable(False, False)
    # centralizar
    window_width, window_height = 400, 300
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    janela.geometry(f"{window_width}x{window_height}+{x}+{y}")


    janela.transient(master)
    janela.grab_set

    tk.Label(janela, text="Descrição:").pack(pady=5)
    entry_descricao = tk.Entry(janela, width=40)
    entry_descricao.pack()

    tk.Label(janela, text="Valor:").pack(pady=5)
    entry_valor = tk.Entry(janela, width=5)
    entry_valor.pack()

    tk.Button(janela, text="Cadastrar", command=cadastrar_produto).pack(pady=15)

    btn_listar = tk.Button(janela, text="Exibir produtos", width=20, command=exibir_produtos)
    btn_listar.pack(pady=10)

    #janela.mainloop()
    return janela