import tkinter as tk
from tkinter import messagebox
from inserir_usuario import inserir_usuario  
from tela_listar_usuarios import exibir_usuarios  

def abrir_tela_usuario(master=None):
    def salvar_usuario():
        nome = entry_nome.get()
        senha = entry_senha.get()

        if not (nome and senha):
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return
    
        inserir_usuario(nome, senha)  

        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        limpar_campos()
        entry_nome.focus()

        def limpar_campos():
            entry_nome.delete(0, tk.END)
            entry_senha.delete(0, tk.END)
            entry_nome.focus()

        def foco_senha(event):
            entry_senha.focus()

        def salvar_enter(event):
            salvar_usuario()

    janela = tk.Toplevel()  
    janela.title("Cadastro de Usuários")
    janela.geometry("320x200")
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

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_nome = tk.Entry(janela, width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_senha = tk.Entry(janela, width=30, show="*")
    entry_senha.grid(row=1, column=1, padx=10, pady=10)


    btn_salvar = tk.Button(janela, text="Salvar", width=12, command=salvar_usuario)
    btn_salvar.grid(row=2, column=0, padx=10, pady=15)

    btn_listar = tk.Button(janela, text="Exibir Usuários", width=20, command=exibir_usuarios)
    btn_listar.grid(row=3, column=0, columnspan=2, pady=10)
 

    entry_nome.focus()
    janela.mainloop()