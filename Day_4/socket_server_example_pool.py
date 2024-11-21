from gevent import monkey; monkey.patch_all()

from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN, SHUT_RDWR
from threading import Thread, current_thread as current
from concurrent.futures import ThreadPoolExecutor as Executor

from signal import signal, SIGINT

def create_server(addr, port, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(SOMAXCONN)

    def cleanup(sig, tb):
        sock.shutdown(SHUT_RDWR)
        sock.close()

    signal(SIGINT, cleanup)

    with Executor(max_workers=5) as workers:
        while True:
            print(f"Server: bound on {addr}:{port}. Waiting for incoming connection")
            (client, (chost, cport)) = sock.accept()
            print(f"Server: got connection from {chost}:{cport}")
            #handler(client)
            #Thread(target=handler, args=(client,)).start()
            workers.submit(handler, client)
  
def handle_connection(client):
    c = current()

    out = client.makefile("w")
    inp = client.makefile("r")
    print("Hello from server.", flush=True, file=out)

    while True:
        line = inp.readline().strip()
        if "bye" in line:
            break
        print(f"{c.name}: {line.upper()}", flush=True, file=out)
        out.flush()
    client.close()


if __name__ == '__main__':
    create_server("192.168.1.130", 7070, handle_connection)
