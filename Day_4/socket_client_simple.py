from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

addr, port = "192.168.1.130", 7070


if __name__ == '__main__':

    conn = socket(AF_INET, SOCK_STREAM)
    conn.connect((addr, port))
    print(f"Connection established to {addr}:{port}")

    inp = conn.makefile("r")
    out = conn.makefile("w")

    line = inp.readline()
    print("Server: ", line)

    print("hello world", file=out, flush=True)
    line = inp.readline()
    print(f"Got reply from connection: {line}")

    print("bye", file=out, flush=True)

    inp.close()
    out.close()
    conn.close()
