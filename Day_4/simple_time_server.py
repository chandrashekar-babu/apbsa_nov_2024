from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN
from threading import Thread

def time_handler(conn):
    from time import ctime
    outs = conn.makefile("w")
    print(ctime(), file=outs, flush=True)
    outs.close()

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 6677

    sock = socket(AF_INET, SOCK_STREAM)
    print(f"{sock=}")

    sock.bind((HOST, PORT))
    sock.listen(SOMAXCONN)
    print(f"Server socket is setup, waiting for client connections...")

    while True:
        client, address = sock.accept()
        print(f"Accepted connection from {address}, {client=}")
        worker = Thread(target=time_handler, args=(client,))
        worker.start()
       
        