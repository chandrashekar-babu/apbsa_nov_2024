from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN
#from concurrent.futures import ThreadPoolExecutor as Executor
from concurrent.futures import ProcessPoolExecutor as Executor

from threading import current_thread as current
#from multiprocessing import current_process as current

def create_server(addr, port, pool, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(SOMAXCONN)
    while True:
        print(f"Server: bound on {addr}:{port}. Waiting for incoming connection")
        (client, (chost, cport)) = sock.accept()
        print(f"Server: got connection from {chost}:{cport}")
        pool.submit(handler, client)

def handle_connection(client):
    c = current()

    out = client.makefile("w")
    inp = client.makefile("r")
    print("Hello from server.", flush=True, file=out)

    while True:
        line = inp.readline()
        if "bye" in line:
            break
        print(f"{c.name}: {line.upper()}", flush=True, file=out)
        out.flush()
    client.close()


if __name__ == '__main__':
    with Executor(max_workers=3) as workers:
        create_server("127.0.0.1", 7070, workers, handle_connection)
