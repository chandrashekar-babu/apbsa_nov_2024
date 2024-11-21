from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN

def echo_handler(conn):
    ins, outs = conn.makefile("r"), conn.makefile("w")
    for line in ins:
        print(f"Client sent: {line}")
        print(line.upper(), file=outs, flush=True)
        if "exit" in line:
            break
    ins.close()
    outs.close()

if __name__ == '__main__':
    HOST = "localhost"
    PORT = 6677

    sock = socket(AF_INET, SOCK_STREAM)
    print(f"{sock=}")

    sock.connect((HOST, PORT))
    print(f"Connection established...")

    ins = sock.makefile("r")
    line = ins.readline()
    print("Server time:", line)
    
    ins.close()
    sock.close()

