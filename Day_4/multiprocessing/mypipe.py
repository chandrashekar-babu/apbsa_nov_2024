class Pipe:
    def __init__(self):
        from collections import deque
        self.queue = deque()

    def send(self, v):
        self.queue.append(v)

    def recv(self):
        return self.queue.popleft()

