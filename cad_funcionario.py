import tkinter as tk

from tkinter import messagebox
from inserir_funcionario import inserir_funcionario
def abrir_tela_funcionario(master=None):
    def cadastrar_cliente():
        nome = entry_nome.get()
        idade = entry_idade.get()
        setor = entry_setor.get()

        if nome == "" or idade == "" or setor == "":
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            inserir_funcionario(nome,idade, setor)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            entry_nome.delete(0, tk.END)
            entry_idade.delete(0, tk.END)
            entry_setor.delete(0, tk.END)
            entry_nome.focus_set()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

    # Janela
    janela = tk.Tk()
    janela.title("Cadastro de Funcionários")
    janela.geometry("350x250")
    janela.resizable(False, False)
    # centralizar
    window_width, window_height = 400, 300
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    janela.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Campos
    tk.Label(janela, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(janela, width=40)
    entry_nome.pack()

    tk.Label(janela, text="idade:").pack(pady=5)
    entry_idade = tk.Entry(janela, width=5)
    entry_idade.pack()

    tk.Label(janela, text="Setor:").pack(pady=5)
    entry_setor = tk.Entry(janela, width=40)
    entry_setor.pack()

    tk.Button(janela, text="Cadastrar", command=cadastrar_cliente).pack(pady=15)

    janela.mainloop()