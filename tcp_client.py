'''
اتصال به یک آی پی و پورت مشخص

در صورتی که کانکشن اکسپت شود

رد و بدل کردن دیتا
'''

import socket

client = socket.socket()

client.connect(('127.0.0.1', 59999))

name = input("Enter name:")

client.send(name.encode())

data = client.recv(1024)

print(data.decode())