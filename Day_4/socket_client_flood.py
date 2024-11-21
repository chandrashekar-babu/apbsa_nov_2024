from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

addr, port = "192.168.1.130", 7090


if __name__ == '__main__':
    connections = []

    for i in range(3000):
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((addr, port))
        print(f"Connection {i} established...")

        inp = conn.makefile("r")
        out = conn.makefile("w")

        print(f"Connection {i}: hello world", file=out, flush=True)
        line = inp.readline()
        print(f"Got reply from connection {i}: {line}")

        connections.append((conn, inp, out))

    sleep(60)

    for c, inp, out in connections:
        inp.close()
        out.close()
        c.close()
