import socket

client = '127.0.0.1'

port = 2001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((client, port))

sock.send('TEST DATA'.encode()) # 인코딩