import socket

host = 'localhost'
porta = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, porta))
s.listen()
print('Aguardando...')
con, endr = s.accept()
print(f'conectado em: {endr}')

try:
    while True:
        msm = con.recv(1024)
        print(f'\033[36mcliente:\33[m {msm.decode()}')
        s.close()
        con.sendall(input(str('mensagem: ')).encode())

except Exception as err:
    print(f'ocorreu um erro devido: {err}')
    s.close()
