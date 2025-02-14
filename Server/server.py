import socket  # Importa a biblioteca para comunicação em rede
import threading  # Importa threading para lidar com conexões simultâneas

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor (localhost)
PORT = 3133         # Porta na qual o servidor estará escutando

# Dicionário para armazenar os clientes conectados e seus respectivos nomes de usuário
clients = {}
# Lock para gerenciar o acesso seguro ao dicionário `clients` entre threads
lock = threading.Lock()

def handle_client(client_socket, username):
    with lock:
        clients[client_socket] = username

    # Notifica a todos os clientes que um novo usuário entrou no chat
    broadcast(f"{username} entrou no chat!", sender_username="")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(message, sender_socket=client_socket, sender_username=username)
            else:
                break
        except Exception as e:
            print(f"Erro ao comunicar com {username}: {e}")
            break
    
    # Remove o cliente da lista ao sair
    with lock:
        if client_socket in clients:
            del clients[client_socket]
    
    broadcast(f"{username} saiu do chat.", sender_username="")
    client_socket.close()

def broadcast(message, sender_socket=None, sender_username=""):
    """Envia a mensagem para todos os clientes, exceto o remetente."""
    with lock:
        for client in list(clients.keys()):  # Lista para evitar RuntimeError ao modificar o dicionário
            if client != sender_socket:
                try:
                    # Adiciona o nome do usuário apenas se for uma mensagem comum
                    formatted_message = f"{sender_username}: {message}" if sender_username else message
                    client.send(formatted_message.encode('utf-8'))
                except:
                    client.close()
                    del clients[client]

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reuso da porta
    
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Servidor rodando em {HOST}:{PORT}")

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                print(f"Conexão recebida de {client_address}")

                username = client_socket.recv(1024).decode('utf-8')
                if not username:
                    print(f"Nome de usuário não recebido de {client_address}")
                    client_socket.close()
                    continue

                print(f"{username} conectado de {client_address}")
                
                thread = threading.Thread(target=handle_client, args=(client_socket, username))
                thread.start()
            except Exception as e:
                print(f"Erro no servidor: {e}")
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")
    finally:
        server_socket.close()
        print("Servidor encerrado.")

if __name__ == "__main__":
    start_server()
