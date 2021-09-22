#!/usr/bin/env python3

import socket

HOST = 'localhost'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
print('Aguardando conexão de um cliente')
conn, ender = s.accept()
print('Conectado em', ender)
arquivo = conn.recv(1024).decode()
with open(arquivo, 'rb') as file:
  for data in file.readlines():
    conn.send(data)

  print('Arquivo enviado com sucesso')