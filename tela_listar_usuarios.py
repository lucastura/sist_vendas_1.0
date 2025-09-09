import tkinter as tk
from tkinter import messagebox
from inserir_usuario import listar_usuarios, excluir_usuario  # criar excluir_usuario no inserir_usuario.py

def exibir_usuarios():
    usuarios = listar_usuarios()  # pega os usuários do banco

    if not usuarios:
        messagebox.showinfo("Usuários", "Nenhum usuário cadastrado.")
        return

    # Cria janela filha
    janela_lista = tk.Toplevel()
    janela_lista.title("Usuários Cadastrados")
    janela_lista.resizable(False, False)  # não permite redimensionar

    # Centraliza
    window_width = 450
    window_height = 350
    screen_width = janela_lista.winfo_screenwidth()
    screen_height = janela_lista.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    janela_lista.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Janela modal
    janela_lista.transient(janela_lista.master)
    janela_lista.grab_set()

    tk.Label(janela_lista, text="Usuários cadastrados:", font=("Arial", 12, "bold")).pack(pady=10)

    # Listbox
    listbox = tk.Listbox(janela_lista, width=60, height=10)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    for nome, senha in usuarios:
        listbox.insert(tk.END, f"{nome} | {senha}")

    # Função para atualizar listbox
    def atualizar_lista():
        listbox.delete(0, tk.END)
        for n, s in listar_usuarios():
            listbox.insert(tk.END, f"{n} | {s}")

    # Função para excluir usuário
    def excluir():
        selecionado = listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um usuário para excluir.")
            return

        usuario_texto = listbox.get(selecionado[0])
        nome = usuario_texto.split(" | ")[0]  # pega o nome do usuário

        confirmar = messagebox.askyesno("Confirmação", f"Deseja realmente excluir o usuário '{nome}'?")
        if confirmar:
            excluir_usuario(nome)  # função no banco de dados
            messagebox.showinfo("Sucesso", f"Usuário '{nome}' excluído com sucesso.")
            atualizar_lista()

    # Botões
    btn_excluir = tk.Button(janela_lista, text="Excluir Usuário", width=20, command=excluir)
    btn_excluir.pack(pady=5)

    def fechar():
        janela_lista.grab_release()
        janela_lista.destroy()

    tk.Button(janela_lista, text="Fechar", width=12, command=fechar).pack(pady=5)

    # Bloqueia fechar pelo X
    janela_lista.protocol("WM_DELETE_WINDOW", lambda: None)