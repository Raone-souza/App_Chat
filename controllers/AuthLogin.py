import pymysql
import customtkinter as ctk
import threading
import socket
from database.ConexaoDb import conexao_db

# Configuração do socket do cliente
HOST = "localhost" 
PORT = 3133 # Porta do servidor para a comunicação

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  # Conectar ao servidor

def abrir_chat(frame, nome_usuario):
    """Substitui a tela de login pelo chat e inicia a comunicação via socket."""
    for widget in frame.winfo_children():
        widget.destroy()

    frame.configure(bg="#1e1e1e")  # Fundo escuro

    # Caixa de mensagens com scroll
    message_box = ctk.CTkScrollableFrame(frame, height=440, width=400, fg_color="#2d2d2d")
    message_box.pack(fill="both", padx=5, pady=5)

    # Campo de entrada de mensagem
    entry_message = ctk.CTkEntry(frame, width=235, placeholder_text="Digite sua mensagem...", fg_color="#333", text_color="white")
    entry_message.place(x=10, y=465)

    send_button = ctk.CTkButton(frame, text="Enviar", command=lambda: enviar_mensagem(entry_message, message_box, nome_usuario))
    send_button.place(x=250, y=465)

    # Enviar o nome de usuário ao servidor ao conectar
    client_socket.send(nome_usuario.encode('utf-8'))

    # Iniciar thread para receber mensagens
    threading.Thread(target=receber_mensagens, args=(message_box, nome_usuario), daemon=True).start()

def enviar_mensagem(entry, box, nome_usuario):
    """Envia uma mensagem para o servidor."""
    msg = entry.get().strip()
    if msg:
        try:
            client_socket.send(msg.encode('utf-8'))  # Enviar apenas a mensagem (sem nome duplicado)
            adicionar_mensagem(box, f"Você: {msg}", direita=True)
            entry.delete(0, "end")
        except:
            adicionar_mensagem(box, "Erro ao enviar mensagem.", direita=True)

def receber_mensagens(box, nome_usuario):
    """Recebe mensagens do servidor."""
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                adicionar_mensagem(box, msg, direita=False)
        except:
            adicionar_mensagem(box, "Desconectado do servidor.", direita=False)
            client_socket.close()
            break

def adicionar_mensagem(box, msg, direita=False):
    """Adiciona uma mensagem na interface do chat."""
    msg_label = ctk.CTkLabel(
        box, text=msg, fg_color="#0078FF" if direita else "#444", 
        text_color="white", corner_radius=10, wraplength=280
    )
    msg_label.pack(anchor="e" if direita else "w", padx=10, pady=5)

def logar_usuarios(username, password, frame):
    """Verifica credenciais no banco de dados e abre o chat se forem válidas."""
    if not username or not password:
        ctk.CTkMessagebox(title="Erro", message="Usuário e senha não podem estar vazios.", icon="warning")
        return

    sql = "SELECT * FROM usuarios WHERE nome = %s AND senha = %s"
    valores = (username, password)

    try:
        conexao_db.conectar()

        if conexao_db.conexao is None:
            raise pymysql.MySQLError("Falha ao conectar ao banco de dados.")

        cursor = conexao_db.cursor
        cursor.execute(sql, valores)
        usuario = cursor.fetchone()

        if usuario:
            abrir_chat(frame, usuario["nome"])  # Carrega o chat
        else:
            ctk.CTkMessagebox(title="Erro", message="Usuário ou senha incorretos.", icon="warning")

    except pymysql.MySQLError as e:
        ctk.CTkMessagebox(title="Erro", message=f"Erro ao acessar o banco de dados: {e}", icon="error")

    finally:
        conexao_db.fechar()
