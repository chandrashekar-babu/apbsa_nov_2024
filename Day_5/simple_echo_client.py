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
    PORT = 6789

    sock = socket(AF_INET, SOCK_STREAM)
    print(f"{sock=}")

    sock.connect((HOST, PORT))
    print(f"Connection established...")

    ins, outs = sock.makefile("r"), sock.makefile("w")

    while True:
        line = input("Enter message: ")
        print(line, file=outs, flush=True)
        reply = ins.readline()
        print(f"Server replied: {reply}")
        if "exit" in line:
            break
    
    ins.close()
    outs.close()
    sock.close()

