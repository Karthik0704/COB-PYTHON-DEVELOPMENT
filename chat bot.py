import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# Dictionary to store client connections
clients = {}

# Function to broadcast messages to all connected clients
def broadcast_message(message, client_socket):
    for client, address in clients.values():
        if client != client_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error broadcasting message to {address}: {e}")
                remove_client(client_socket)

# Function to handle individual client connections
def handle_client(client_socket, address):
    try:
        while True:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received message from {address}: {message.decode()}")
            broadcast_message(message, client_socket)
    except Exception as e:
        print(f"Error with client {address}: {e}")
    finally:
        remove_client(client_socket)

# Function to remove a client from the clients dictionary
def remove_client(client_socket):
    for key, value in clients.items():
        if value[0] == client_socket:
            clients.pop(key)
            break
    client_socket.close()

# Create a socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    clients[client_address] = (client_socket, client_address)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
