from gevent import monkey; monkey.patch_all()
import gevent

from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN

workers = []

def create_server(addr, port, pool, handler):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(SOMAXCONN)
    while True:
        print(f"Server: bound on {addr}:{port}. Waiting for incoming connection")
        (client, (chost, cport)) = sock.accept()
        print(f"Server: got connection from {chost}:{cport}")
        greenlet = gevent.spawn(handle_connection, client)
        workers.append(greenlet)

def handle_connection(client):

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
        create_server("127.0.0.1", 7070, workers, handle_connection)
        gevent.joinall(workers)
        