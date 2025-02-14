import customtkinter as ctk
from controllers.AuthCadastro import cadastrar_usuario

def criar_tela_registro(app, ir_para_login):
    registro_frame = ctk.CTkFrame(app)

    # Título e descrição
    ctk.CTkLabel(registro_frame, text="Cadastre seu usuário", font=("Arial", 20)).pack(pady=50)

    # Campos de entrada
    ctk.CTkLabel(registro_frame, text="Nome de Usuário").place(x=70, y=135)
    Username_entry = ctk.CTkEntry(registro_frame, placeholder_text="Crie seu nome de usuário", width=300, height=35)
    Username_entry.place(x=60, y=160)

    ctk.CTkLabel(registro_frame, text="Senha").place(x=70, y=225)
    Password_entry = ctk.CTkEntry(registro_frame, placeholder_text="Crie sua senha", width=300, height=35, show="*")
    Password_entry.place(x=60, y=250)

    # Botão de cadastro
    ctk.CTkButton(registro_frame, text="Cadastrar", width=200, height=35, command=lambda: cadastrar_usuario(Username_entry.get(), Password_entry.get())).place(x=110, y=310)

    # Botão para voltar ao login
    label_voltar = ctk.CTkLabel(registro_frame, text="Já tem uma conta? Faça login", font=("Arial", 10), fg_color="transparent", text_color="gray", cursor="hand2")
    label_voltar.place(x=135, y=350)
    
    # Conectar evento de clique para voltar à tela de login
    label_voltar.bind("<Button-1>", ir_para_login)

    # Adiciona a referência do label
    registro_frame.children["label_voltar"] = label_voltar

    return registro_frame
