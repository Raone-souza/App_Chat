import customtkinter as ctk
from controllers.AuthLogin import logar_usuarios


def criar_tela_login(app):
    login_frame = ctk.CTkFrame(app)

    # Título e descrição
    ctk.CTkLabel(login_frame, text="Bem-vindo ao Chat", font=("Arial", 20)).pack(pady=55)

    # Campos de entrada
    ctk.CTkLabel(login_frame, text="Nome de Usuário").place(x=70, y=135)
    username_entry = ctk.CTkEntry(login_frame, placeholder_text="Digite seu nome de usuário", width=300, height=35)
    username_entry.place(x=60, y=160)

    ctk.CTkLabel(login_frame, text="Senha").place(x=70, y=225)
    password_entry = ctk.CTkEntry(login_frame, placeholder_text="Digite sua senha", width=300, height=35, show="*")
    password_entry.place(x=60, y=250)

    # Função de login
    def on_login_button_click():
        username = username_entry.get()
        password = password_entry.get()
        logar_usuarios(username, password, app)

    # Botão de login
    ctk.CTkButton(login_frame, text="Entrar", width=200, height=35, command=on_login_button_click).place(x=110, y=310)

    # Link para registro
    label_register = ctk.CTkLabel(login_frame, text="Ainda não tem cadastro?", font=("Arial", 10), fg_color="transparent", text_color="gray", cursor="hand2")
    label_register.place(x=150, y=350)

    login_frame.children["label_register"] = label_register  # Adiciona referência ao widget

    return login_frame
