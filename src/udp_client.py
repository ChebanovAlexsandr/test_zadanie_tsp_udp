import socket
import sys


def client(save_path, host='127.0.0.1', port=8081):
    """Запускает UDP клиент."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # создание сокета и установка соединения
        s.sendto(b'request', (host, port))  # оправка запроса серверу
        print(f"Requesting from {host}:{port}")
        with open(save_path, 'wb') as f:
            while True:
                data, _ = s.recvfrom(65507)  # принимаем данные
                if not data:
                    break
                f.write(data)
        print(f"Downloaded as {save_path}")


if __name__ == '__main__':
    client(sys.argv[1])
