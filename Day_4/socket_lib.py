from gevent import monkey; monkey.patch_all()
from threading import current_thread as current

def create_server(host, port, handler):
    from socket import socket, AF_INET, SOCK_STREAM, SO_REUSEADDR, SOMAXCONN
    #from threading import Thread
    #from concurrent.futures import ProcessPoolExecutor as Executor
    from concurrent.futures import ThreadPoolExecutor as Executor

    listener = socket(AF_INET, SOCK_STREAM)

    try:
        listener.bind((host, port))
        print(f"Server bound to {host}:{port}")
        #listener.setsockopt(SO_REUSEADDR, 1, 4)
        
        listener.listen(SOMAXCONN)
        
        print("Server waiting for incoming connections...")
        with Executor(max_workers=20) as workers:
            while True:
                conn, info = listener.accept()
                print(f"Got connection ({conn}) from {info}")
                #handler(conn, info)
                #Thread(target=handler, args=(conn, info)).start()
                workers.submit(handler, conn, info)

    except Exception as e:
        print("Caught an exception:", e)
    finally:
        listener.close()

def create_client(host, port, handler):
    from socket import socket, AF_INET, SOCK_STREAM

    conn = socket(AF_INET, SOCK_STREAM)

    try:
        conn.connect((host, port))
        print(f"Connection established to {host}:{port}")
        ins = conn.makefile("r")
        outs = conn.makefile("w")
        handler((host, port), ins, outs)

    except Exception as e:
        print("Caught an exception: ", e)
    
    finally:
        ins.close()
        outs.close()
        conn.close()
        
class RequestHandler:
    def __init__(self, conn, info):
        self._conn, self._info = conn, info
        self._cls_name = type(self).__name__
        self.start()
        
    def start(self):
        self.worker = current()
        print(f"{self._cls_name}[{self.worker}]: handling connection on {self._info}")
        ins = self._conn.makefile("r")
        outs = self._conn.makefile("w")
        self.shutdown = False
        
        try:
            while not self.shutdown:
                self.handle_request(ins, outs)
        except Exception as e:
            print(f"{self._cls_name}: caught an exception: {e}")
        finally:
            outs.close()
            ins.close()
            self._conn.close()      

    def handle_request(self, ins, outs):
        raise NotImplementedError("handle_request method needs to be implemented in the sub-class")
    

class EchoHandler(RequestHandler):
    def handle_request(self, ins, outs):
        line = ins.readline().strip()
        print(f"{self.worker.name}: {self._info}: incoming message = '{line}'")
        print(line.upper(), file=outs, flush=True)
        if "exit" in line:
            self.shutdown = True


def echo_server(conn, info):
    from threading import current_thread as current
    #from multiprocessing import current_process as current

    print(f"echo_server[{current()}]: handling connection on {info}")

    ins = conn.makefile("r")
    outs = conn.makefile("w")

    print("Welcome to echo server", file=outs, flush=True)
    try:
        while True:
            line = ins.readline().strip()
            print(f"{current().name}: {info}: incoming message = '{line}'")
            print(line.upper(), file=outs, flush=True)
            if "exit" in line:
                break
    except Exception as e:
        print(f"echo_server: caught an exception: {e}")
    finally:
        outs.close()
        ins.close()
        conn.close()

def echo_client(info, ins, outs):
    print(f"echo_client: sending messages to {info}")
    welcome_msg = ins.readline()
    print(f"Server message: {welcome_msg}")
    
    while True:
        line = input("Enter message: ")
        print(line, file=outs, flush=True)
        reply = ins.readline().strip()
        print(f"Server replied: {reply}")
        if "exit" in line:
            break

if __name__ == '__main__':
    #create_server("localhost", 8877, echo_server)
    #create_client("localhost", 8877, echo_client)
    pass