import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess  # Para abrir outro script Python

# Função para abrir a janela principal (principal.py)
def abrir_janela_principal():
    splash.destroy()  # Fecha a splash
    # Abre o script principal.py
    subprocess.Popen(["python", "principal.py"])

# Criando a tela splash
splash = tk.Tk()
splash.overrideredirect(True)  # Remove borda e barra de título
splash.geometry("400x300")
splash.config(bg="white")

# Centralizando a janela na tela
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x = (screen_width // 2) - (400 // 2)
y = (screen_height // 2) - (300 // 2)
splash.geometry(f"+{x}+{y}")

# Caminho da imagem
caminho_logo = "logo.jpg"

# Verificando se a imagem existe
if os.path.exists(caminho_logo):
    logo_image = Image.open(caminho_logo)
    logo_image = logo_image.resize((200, 180), Image.Resampling.LANCZOS)
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(splash, image=logo, bg="white")
    logo_label.pack(expand=True)
else:
    messagebox.showwarning("Aviso", f"Arquivo de logo não encontrado:\n{caminho_logo}")
    label_fallback = tk.Label(splash, text="Minha Empresa", font=("Arial", 24), bg="white")
    label_fallback.pack(expand=True)

# Exibindo splash por 5 segundos
splash.after(1000, abrir_janela_principal)

splash.mainloop()