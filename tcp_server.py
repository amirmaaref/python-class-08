'''

وظایف سرور:

گوش دادن روی یک پورت مشخص

اکسپت کردن کانکشن

رد و بدل کردن دیتا

SOCK_STREAM -> TCP
SOCK_DGRAM -> UDP
'''

import socket

server = socket.socket()

server.bind(('127.0.0.1', 59999))

server.listen()

print('Listening on 59999')

while True:
    print('Before accept')
    conn, addr = server.accept()
    print(f'Received connection from {addr}')
    name = conn.recv(1024).decode()
    conn.send(f"Hi, i'm Server, Welcome {name}".encode())
    conn.close()