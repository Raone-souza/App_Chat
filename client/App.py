import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.title("TalkMe")
janela.geometry("400x600")
janela.resizable(False, False)

# Tela de início com fundo aprimorado
fundo = ctk.CTkFrame(janela, width=400, height=600, corner_radius=0, fg_color="#1e1e1e")
fundo.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Logo com um novo estilo
logo = ctk.CTkLabel(fundo, text="TalkMe", font=ctk.CTkFont("Helvetica", 38, "bold"), text_color="#34C759")
logo.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

# Subtítulo ajustado para harmonizar com o design
subtitulo = ctk.CTkLabel(fundo, text="Conecte-se com o mundo", font=ctk.CTkFont("Helvetica", 15, slant="italic"), text_color="#a0a0a0")
subtitulo.place(relx=0.5, rely=0.17, anchor=ctk.CENTER)

# Mensagem acima do campo de entrada do nome de usuário
mensagem_usuario = ctk.CTkLabel(fundo, text="Digite seu nome de usuário para entrar", font=ctk.CTkFont("Helvetica", 12), text_color="#a0a0a0")
mensagem_usuario.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

# Entrada de nome de usuário com sombras e bordas mais suaves
nome_usuario = ctk.CTkEntry(
    fundo,
    width=250,
    height=40,
    corner_radius=10,
    placeholder_text="Nome de usuário",
    placeholder_text_color="#555555",
    fg_color="#2e2e2e",
    text_color="white"
)
nome_usuario.place(relx=0.5, rely=0.47, anchor=ctk.CENTER)

# Botão Entrar aprimorado com um gradiente e efeito hover
botao_entrar = ctk.CTkButton(
    fundo,
    text="Entrar",
    width=220,
    height=40,
    corner_radius=15,
    fg_color="#34C759",
    text_color="white",
    hover_color="#2dbb50",
    font=ctk.CTkFont(family="Helvetica", size=16, weight="bold")
)
botao_entrar.place(relx=0.5, rely=0.56, anchor=ctk.CENTER)

def entrar():
    nome = nome_usuario.get()
    if nome:
        nova_janela(nome)

botao_entrar.configure(command=entrar)

# Função para a nova janela de chat
def nova_janela(usuario):
    # Limpa todos os widgets da janela inicial
    for widget in janela.winfo_children():
        widget.place_forget()

    # Criação da área de chat
    chat_frame = ctk.CTkFrame(janela, width=400, height=600, corner_radius=0, fg_color="#1e1e1e")
    chat_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    # Frame para o cabeçalho com o texto "Bem-vindo"
    cabecalho_frame = ctk.CTkFrame(chat_frame, width=400, height=54, corner_radius=10, fg_color="#2f2f2f")
    cabecalho_frame.place(relx=0.5, rely=0.01, anchor=ctk.N)  # Cabeçalho fixo no topo

    # Cabeçalho fixo no topo da janela
    cabecalho = ctk.CTkLabel(cabecalho_frame, text=f"Bem-vindo, {usuario}", font=ctk.CTkFont("Helvetica", 20, "bold"), text_color="white")
    cabecalho.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    # Área de mensagens abaixo do cabeçalho
    message_area = ctk.CTkFrame(chat_frame, width=380, height=430, fg_color="#1e1e1e")
    message_area.place(relx=0.5, rely=0.1, anchor=ctk.N)

    # Janela de exibição das mensagens
    message_display = ctk.CTkTextbox(message_area, width=400, height=480, corner_radius=10, fg_color="#2f2f2f", text_color="white")
    message_display.pack(pady=2)
    message_display.insert("end", "Você entrou no chat...\n")
    message_display.configure(state="disabled")

    # Variável para controlar se é a primeira mensagem
    primeira_mensagem = True

    # Área de entrada de mensagem
    message_entry_frame = ctk.CTkFrame(chat_frame, width=400, height=50, fg_color="#2b2b2b", corner_radius=10)
    message_entry_frame.place(relx=0.5, rely=1, anchor=ctk.S)

    message_entry = ctk.CTkEntry(message_entry_frame, width=280, height=35, placeholder_text="Digite sua mensagem...", fg_color="#2f2f2f", text_color="white")
    message_entry.pack(side="left", padx=10, pady=10)

    # Função para enviar mensagens
    def enviar_mensagem():
        nonlocal primeira_mensagem
        mensagem = message_entry.get()
        if mensagem:
            message_display.configure(state="normal")
            if primeira_mensagem:
                # Limpa a mensagem inicial apenas na primeira vez
                message_display.delete("1.0", "end")
                primeira_mensagem = False
            message_display.insert("end", f"{usuario}: {mensagem}\n")
            message_display.configure(state="disabled")
            message_entry.delete(0, "end")

    # Botão de envio de mensagem
    send_button = ctk.CTkButton(message_entry_frame, text="Enviar", width=80, fg_color="#34C759", hover_color="#2dbb50", text_color="white", command=enviar_mensagem)
    send_button.pack(side="right", padx=10, pady=10)

janela.mainloop()
