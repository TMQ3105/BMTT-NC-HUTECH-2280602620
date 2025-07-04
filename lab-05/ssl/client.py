import socket
import ssl
import threading

server_address = ('localhost', 2620)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhan:", data.decode('utf-8'))
    except:
        pass
    finally:
        ssl_socket.close()
        print("Ket noi da dong.")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False

ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

ssl_socket.connect(server_address)

receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

try:
    while True:
        message= input("Nhap tin nhan: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    ssl_socket.close()
        