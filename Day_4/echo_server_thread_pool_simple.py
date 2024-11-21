from argparse import ArgumentParser
from socket import socket, SOMAXCONN, AF_INET, SOCK_STREAM
from thread_pool import ThreadPool
# Implement the above thread_pool module

def handle_connection(client, addr, port):
    outs = client.makefile("w")
    ins = client.makefile("r")
    
    print("Server says 'Hello'", file=outs, flush=True)
    while True:
        line = ins.readline()
        if "exit" in line:
            break
        print(f"Client [{addr}:{port}] says -'{line}'")
        print(f"Reply: {line.upper()}", file=outs, flush=True)
    client.close()

if __name__ == '__main__':
    
    arg_parser = ArgumentParser(description="A simple echo server") 
    arg_parser.add_argument("host", help="Host name/ip address to bind")
    arg_parser.add_argument("port", type=int, help="Port number to bind this socket on")
    args = arg_parser.parse_args()

    echo_server = socket(AF_INET, SOCK_STREAM)

    print(f"Binding socket on {args.host}:{args.port}:")
    echo_server.bind((args.host, args.port))

    echo_server.listen(SOMAXCONN)

    workers = ThreadPool(max_workers=10)
    workers.start()

    try:
        while True:
            print(f"Waiting for client connection:")
            (client, (addr, port)) = echo_server.accept()
            print(f"Got connection from {addr}:{port}, socket = {client}")
            #Thread(target=handle_connection, args=(client, addr, port)).start()
            workers.submit(handle_connection, args=(client, addr, port))

            print(f"Client [{addr}:{port}] closed connection...")
    except:
        if client:
            client.close()
    finally:
        echo_server.close()
        workers.shutdown()
