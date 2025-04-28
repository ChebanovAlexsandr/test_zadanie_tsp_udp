import socket
import sys


def server(file_path, host='127.0.0.1', port=8081):
    """Запускает UDP сервер."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))  # прослушивание сервера
        print(f"Serving {file_path}")
        _, addr = s.recvfrom(1024)  # Получаем данные из сокета в скобках указали количество данных для чтения.
        print(f"Request from {addr[0]}:{addr[1]}")
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(65507)  # Максимальный размер для UDP
                if not chunk:
                    break
                s.sendto(chunk, addr)
        s.sendto(b'', addr)  # передаём пустой пакет (завершение)
        print(f"Finished sending to {addr[0]}:{addr[1]}")


if __name__ == '__main__':
    server(sys.argv[1])
