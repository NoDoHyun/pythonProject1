import socket

host = "127.0.0.1"  # 로컬호스트

port = 2002  # 포트번호는 겹치지않는선에서 정하자

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((host, port))

serverSocket.listen()
# 받은 데이터를 해석함.