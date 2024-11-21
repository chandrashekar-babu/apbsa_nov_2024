from threading import Thread as Task, current_thread as current

class TCPServer:
    def __init__(self, host="localhost", port=7865, handler=None):
        self.host, self.port = host, port
        self.handler = handler
        
    def serve_forever(self):
       
        from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEADDR, SOMAXCONN, SHUT_RD

        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.bind((self.host, self.port))
            self.sock.listen(SOMAXCONN)

            while True:
                print("Waiting for incoming connection...")
                try:
                    conn, (addr, port) = self.sock.accept()
                    print(f"Got connection from {addr}:{port}")
                    #self.handler(conn.makefile("w"), conn.makefile("r"), addr, port)
                    t = Task(target=self.handler, 
                             args=(conn.makefile("w"), conn.makefile("r"), addr, port))
                    t.start()
                finally:
                    conn.close()

        finally:
            self.sock.shutdown(SHUT_RD)

class TCPClient:
    def __init__(self, host="localhost", port=7865, handler=None):
        self.host, self.port = host, port
        self.handler = handler

    def connect(self):
        try:
            from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEADDR, SOMAXCONN, SHUT_RDWR
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            self.handler(self.sock.makefile("w"), self.sock.makefile("r"), self.host, self.port)
        finally:
            self.sock.shutdown(SHUT_RDWR)       

def echo_client(outs, ins, addr, port):
    print(f"Connected to {addr}:{port}")
    print(f"Server: {ins.readline().strip()}")

    while True:
        line = input("Enter a line: ")
        print(line, file=outs, flush=True)
        if "exit" in line:
            break
        reply = ins.readline()
        print(f"Server: {reply.strip()}")

    outs.close()
    ins.close()


def echo_in_uppercase(outs, ins, addr, port):
    print(f"{current().name}: Handling connection for {addr}:{port}")
    print(f"Server says - 'Hello'", file=outs, flush=True)
    while True:
        line = ins.readline()
        if "exit" in line:
            break
        print(f"{current().name}: Got a message from {addr}:{port}: {line.strip()}")
        print(line.upper(), file=outs, flush=True)
    outs.close()
    ins.close()

if __name__ == '__main__':
    server = TCPServer(host="192.168.1.130", handler=echo_in_uppercase)
    server.serve_forever()
