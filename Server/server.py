import socket  # Importa a biblioteca para comunicação em rede
import threading  # Importa threading para lidar com conexões simultâneas

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor (localhost)
PORT = 12345        # Porta na qual o servidor estará escutando

# Dicionário para armazenar os clientes conectados e seus respectivos nomes de usuário
clients = {}
# Lock para gerenciar o acesso seguro ao dicionário `clients` entre threads
lock = threading.Lock()

# Função que lida com um cliente específico
def handle_client(client_socket, username):
    # Adiciona o cliente ao dicionário de clientes conectados
    with lock:
        clients[client_socket] = username
    
    # Notifica a todos os clientes que um novo usuário entrou no chat
    broadcast(f"{username} entrou no chat!", client_socket)

    while True:
        try:
            # Recebe a mensagem enviada pelo cliente
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                # Repassa a mensagem para os outros clientes
                broadcast(f"{username}: {message}", client_socket)
        except:
            # Remove o cliente do dicionário em caso de erro ou desconexão
            with lock:
                del clients[client_socket]
            # Notifica a todos que o cliente saiu do chat
            broadcast(f"{username} saiu do chat.", client_socket)
            # Fecha a conexão com o cliente
            client_socket.close()
            break

# Função que envia uma mensagem para todos os clientes conectados, exceto o remetente
def broadcast(message, sender_socket=None):
    with lock:
        for client in clients.keys():
            if client != sender_socket:  # Evita enviar a mensagem de volta ao remetente
                try:
                    client.send(message.encode('utf-8'))  # Envia a mensagem codificada
                except:
                    # Remove o cliente em caso de erro ao enviar a mensagem
                    client.close()
                    del clients[client]

# Função principal que inicia o servidor
def start_server():
    # Cria o socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))  # Associa o socket ao endereço e porta especificados
    server_socket.listen()  # Coloca o socket em modo de escuta
    print(f"Servidor rodando em {HOST}:{PORT}")

    while True:
        # Aguarda uma nova conexão
        client_socket, client_address = server_socket.accept()
        # Recebe o nome de usuário do cliente
        username = client_socket.recv(1024).decode('utf-8')
        print(f"{username} conectado de {client_address}")
        # Cria uma nova thread para lidar com o cliente
        thread = threading.Thread(target=handle_client, args=(client_socket, username))
        thread.start()

# Ponto de entrada do script
if __name__ == "__main__":
    start_server()
