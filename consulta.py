#!/usr/bin/python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org", 43))

query = sys.argv[1] + "\r\n"
s.send(query.encode())

resposta = s.recv(4096)

print(resposta.decode())
