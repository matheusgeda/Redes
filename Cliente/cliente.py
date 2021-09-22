#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 50000

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))
print('Conectado com sucesso!\n')
arquivo = str(input('Arquivo: '))
c.send(arquivo.encode())
with open(arquivo, 'wb') as file:
    while 1:
        data = c.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{arquivo} Recebido!\n')