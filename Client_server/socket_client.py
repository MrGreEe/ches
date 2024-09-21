# import socket


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(('localhost', 3030))                  # Подключаемся к нашему серверу.
# s.sendall('Hello, Habr!'.encode('utf-8'))       # Отправляем фразу.
# data = s.recv(1024)                             # Получаем данные из сокета.
# s.close()



# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")