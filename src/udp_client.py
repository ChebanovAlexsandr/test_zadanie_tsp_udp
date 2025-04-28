import socket
import sys


def client(save_path, host='127.0.0.1', port=8080):
    """Запускает TCP клиент"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))  # устанавливаем соединение с сервером
        print(f"Requesting from {host}:{port}")
        data = b''
        while True:
            chunk = s.recv(4096)  # считывание данных с сервера частями
            if not chunk:
                break
            data += chunk
        with open(save_path, 'wb') as f:  # сохранение полученных данных в файл
            f.write(data)  # запись данных
        print(f"Downloaded as {save_path}")


if __name__ == '__main__':
    client(sys.argv[1])
