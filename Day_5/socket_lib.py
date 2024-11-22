
class InvalidWorkerType(Exception): pass

class TCPServer:
    def __init__(self, host, port, handler, worker="thread", max_workers=10):
        self.host, self.port, self.handler = host, port, handler
        if worker == "thread":
            from concurrent.futures import ThreadPoolExecutor as Executor
        elif worker == "process":
            from concurrent.futures import ProcessPoolExecutor as Executor
        elif worker in ("greenlet", "coroutine", "gevent"):
            from gevent import monkey
            monkey.patch_all()
            from concurrent.futures import ThreadPoolExecutor as Executor
        else:
            raise InvalidWorkerType("worker must be either 'thread', 'process' or 'gevent'")

        self.executor = Executor       
        self.max_workers = max_workers
      

    def start(self):
        from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN
        self._listener = socket(AF_INET, SOCK_STREAM)
        self._listener.bind((self.host, self.port))
        self._listener.listen(SOMAXCONN)
        self.quit = False

    def run_forever(self):
        self.workers = self.executor(max_workers=self.max_workers)
        while not self.quit:
            client, client_info = self._listener.accept()
            self.workers.submit(self.handler, client, client_info)

    def shutdown(self):
        from socket import SHUT_RD
        self.workers.shutdown()
        self._listener.shutdown(SHUT_RD)

    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, et, ev, tb):
        self.shutdown()
