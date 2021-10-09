import socket

host = 'localhost'
porta = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, porta))

try:
    while True:
        s.sendall(input(str('mensagem: ')).encode())
        msm = s.recv(1024)
        print(f'\033[31mserve:\033[m {msm.decode()}')
except Exception as err:
    print(f'conexão falhou devido ao erro: {err}')
    s.close()
