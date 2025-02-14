import customtkinter as ctk
from client.login import criar_tela_login
from client.registro import criar_tela_registro
import socket
import threading
import subprocess  # subprocess para iniciar o servidor automaticamente
import os

# Função para iniciar o servidor automaticamente
def iniciar_servidor():
    # Caminho para o arquivo server.py dentro da pasta 'server'
    server_path = os.path.join(os.path.dirname(__file__), "server", "server.py")
    subprocess.Popen(["python", server_path])

# Alternar entre login e registro
def ir_para_registro(event):
    login_frame.pack_forget()
    registro_frame.pack(fill="both", expand=True, padx=0.9, pady=0.9)

def ir_para_login(event):
    registro_frame.pack_forget()
    login_frame.pack(fill="both", expand=True, padx=0.9, pady=0.9)

# Configuração do cliente
HOST = '127.0.0.1'  # IP do servidor local (loopback)
PORT = 3133    # Porta do servidor para a comunicação

# Criação do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inicializa o aplicativo
app = ctk.CTk()
app.title("Chat")
app.geometry("400x500")
app.resizable(False, False)

# Criando telas
login_frame = criar_tela_login(app)  
registro_frame = criar_tela_registro(app, ir_para_login)

# Exibe a tela de login primeiro
login_frame.pack(fill="both", expand=True, padx=0.9, pady=0.9)

# Conectar evento de clique
login_frame.children["label_register"].bind("<Button-1>", ir_para_registro)
registro_frame.children["label_voltar"].bind("<Button-1>", ir_para_login)

# Inicia o servidor assim que o aplicativo cliente for iniciado
iniciar_servidor()

# Inicia o loop do App
app.mainloop()
