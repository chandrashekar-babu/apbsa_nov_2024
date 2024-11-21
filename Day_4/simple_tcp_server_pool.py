from gevent import monkey; monkey.patch_all()

from threading import current_thread as current
from concurrent.futures import ThreadPoolExecutor as Executor

#from multiprocessing import current_process as current
#from concurrent.futures import ProcessPoolExecutor as Executor


def create_tcp_server(addr, port, handler_fn):
    from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN, SHUT_RD
    with socket(AF_INET, SOCK_STREAM) as listener:
        listener.bind((addr, port))
        listener.listen(SOMAXCONN)
        t = current()
        with Executor(max_workers=5) as workers:
            while True:
                print(f"Server[{t.name}]: waiting for new client connection...")
                client, (client_addr, client_port) = listener.accept()
                #handler_fn(client, client_addr, client_port)
                #Thread(target=handler_fn, args=(client, client_addr, client_port)).start()
                workers.submit(handler_fn, client, client_addr, client_port)

def create_tcp_connection(addr, port, handler_fn):
    from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN, SHUT_RDWR
    
    with socket(AF_INET, SOCK_STREAM) as conn:
        conn.connect((addr, port))
        handler_fn(conn, addr, port)


def echo_handler(conn, addr, port):
    t = current()
    print(f"Server-Handler[{t.name}]: Got incoming connection from {addr}:{port}")
    with conn.makefile("w") as outs, conn.makefile("r") as ins:
        print("Welcome to simple echo server.", file=outs, flush=True)

        while True:
            line = ins.readline().strip()
            print(f"Server-Handler[{t.name}]: {line.upper()}", file=outs, flush=True)
            if "exit" in line:
                break
        
if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    create_tcp_server(args.host, args.port, echo_handler)

