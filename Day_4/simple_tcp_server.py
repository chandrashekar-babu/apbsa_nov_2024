def create_tcp_server(addr, port, handler_fn):
    from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN, SHUT_RD
    with socket(AF_INET, SOCK_STREAM) as listener:
        listener.bind((addr, port))
        listener.listen(SOMAXCONN)

        while True:
            client, (client_addr, client_port) = listener.accept()
            handler_fn(client, client_addr, client_port)


def create_tcp_connection(addr, port, handler_fn):
    from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN, SHUT_RDWR
    
    with socket(AF_INET, SOCK_STREAM) as conn:
        conn.connect((addr, port))
        handler_fn(conn, addr, port)


def echo_handler(conn, addr, port):
    print(f"Got incoming connection from {addr}:{port}")
    with conn.makefile("w") as outs, conn.makefile("r") as ins:
        print("Welcome to simple echo server.", file=outs, flush=True)

        while True:
            line = ins.readline().strip()
            print(line.upper(), file=outs, flush=True)
            if "exit" in line:
                break
        
if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    create_tcp_server(args.host, args.port, echo_handler)

