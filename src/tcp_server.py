import socket
import sys

def server(file_path, host='127.0.0.1', port=8080):
    """Запускает TCP сервера"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port)) # обозначили как сервер
        s.listen()           # слушаем наш сервер
        print(f"Serving {file_path}")
        client, addr = s.accept() # принимает отправленные запросы и разделяет на клиента и адрес
        with client:
            print(f"Request from {addr[0]}:{addr[1]}")
            with open(file_path, 'rb') as f:
                data = f.read()
                client.sendall(data) # продолжает отправлять данные до тех пор, пока они не будут переданы.
            print(f"Finished sending to {addr[0]}:{addr[1]}")

if __name__ == '__main__':
    server(sys.argv[1])


