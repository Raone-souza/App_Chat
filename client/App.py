import customtkinter as ctk  # Importa a biblioteca CustomTkinter para criar interfaces modernas
import socket  # Importa a biblioteca socket para comunicação em rede
import threading  # Importa threading para lidar com threads paralelas

# Configuração do cliente
HOST = '127.0.0.1'  # IP do servidor local (loopback)
PORT = 12345        # Porta do servidor para a comunicação

# Criação do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Configura o socket para conexão TCP/IP

# Inicialização do Tkinter
app = ctk.CTk()  # Inicializa o aplicativo com CustomTkinter
app.title("Login - Chat Local")  # Define o título da janela
app.geometry("400x300")  # Define o tamanho inicial da janela

# Tela de Login
login_frame = ctk.CTkFrame(app)  # Frame principal para a tela de login
login_frame.pack(fill="both", expand=True, padx=20, pady=20)

label_title = ctk.CTkLabel(login_frame, text="Bem-vindo ao Chat!", font=("Arial", 20))  # Título da tela
label_title.pack(pady=20)

username_label = ctk.CTkLabel(login_frame, text="Digite seu nome de usuário:")  # Rótulo para o campo de nome
username_label.pack()

username_entry = ctk.CTkEntry(login_frame, placeholder_text="Seu nome...")  # Campo de entrada para o nome do usuário
username_entry.pack(pady=10, padx=20, fill="x")

error_label = ctk.CTkLabel(login_frame, text="", text_color="red")  # Rótulo para exibir erros de conexão
error_label.pack()

# Função para conectar ao servidor
def conectar():
    username = username_entry.get()  # Obtém o nome do usuário
    if username:  # Verifica se o nome não está vazio
        try:
            client_socket.connect((HOST, PORT))  # Conecta ao servidor
            client_socket.send(username.encode('utf-8'))  # Envia o nome do usuário ao servidor
            login_frame.pack_forget()  # Remove a tela de login
            chat_screen(username)     # Chama a função para abrir a tela de chat
        except Exception as e:
            error_label.configure(text="Erro ao conectar! Verifique o servidor.")  # Exibe erro de conexão

connect_button = ctk.CTkButton(login_frame, text="Entrar", command=conectar)  # Botão para entrar no chat
connect_button.pack(pady=20)

# Tela de Chat
def chat_screen(username):
    chat_frame = ctk.CTkFrame(app)  # Frame principal para a tela de chat
    chat_frame.pack(fill="both", expand=True)

    message_box = ctk.CTkTextbox(chat_frame, wrap="word")  # Caixa de texto para exibir mensagens
    message_box.pack(fill="both", expand=True, padx=10, pady=10)
    message_box.configure(state="disabled")  # Caixa desabilitada para impedir edição manual

    message_entry = ctk.CTkEntry(chat_frame, placeholder_text="Digite sua mensagem...")  # Campo de entrada para mensagens
    message_entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

    # Função para enviar mensagens
    def enviar_mensagem():
        message = message_entry.get()  # Obtém o texto da mensagem
        if message:
            try:
                client_socket.send(message.encode('utf-8'))  # Envia a mensagem ao servidor
                message_box.configure(state="normal")
                message_box.insert("end", f"Você: {message}\n")  # Exibe a mensagem na tela
                message_box.configure(state="disabled")
                message_entry.delete(0, "end")  # Limpa o campo de entrada
            except:
                message_box.configure(state="normal")
                message_box.insert("end", "Erro ao enviar mensagem.\n")
                message_box.configure(state="disabled")

    send_button = ctk.CTkButton(chat_frame, text="Enviar", command=enviar_mensagem)  # Botão para enviar mensagem
    send_button.pack(side="right", padx=10, pady=10)

    # Função para receber mensagens do servidor
    def receber_mensagens():
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')  # Recebe mensagens do servidor
                if message:
                    message_box.configure(state="normal")
                    message_box.insert("end", f"{message}\n")  # Exibe a mensagem recebida na tela
                    message_box.configure(state="disabled")
            except:
                message_box.configure(state="normal")
                message_box.insert("end", "Desconectado do servidor.\n")  # Notifica o cliente sobre a desconexão
                message_box.configure(state="disabled")
                client_socket.close()  # Fecha a conexão do socket
                break

    # Thread para receber mensagens continuamente sem travar a interface
    threading.Thread(target=receber_mensagens, daemon=True).start()

# Inicializa o loop principal da interface
app.mainloop()
