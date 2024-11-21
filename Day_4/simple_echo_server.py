from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN

def echo_handler(conn):
    ins, outs = conn.makefile("r"), conn.makefile("w")
    try:
        for line in ins:
            print(f"Client sent: {line}")
            print(line.upper(), file=outs, flush=True)
            if "exit" in line:
                break
    except ConnectionResetError:
        print("Client closed the connection...")
    finally:
        ins.close()
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
        echo_handler(client)
        client.close()
        